"""
Multi-Utility Toolkit - GUI Version (Tkinter)

Run:  python gui_main.py

Is file me aapke console project ke saare features ka UI version hai:
Date/Time, Math, Random Data, UUID, File Operations, Explore Module.
Koi extra library install karne ki zarurat nahi (sirf Python + tkinter).
"""

import importlib
import math
import os
import random
import string
import time
import tkinter as tk
import uuid
from datetime import datetime
from tkinter import messagebox, ttk

# Files isi folder ke andar create / read / write hongi
BASE_FOLDER = "moduler & packager"

# explore_module me allowed modules (same as original helper.py)
ALLOWED_MODULES = ["math", "random", "datetime", "time", "uuid"]


# ======================================================================
# Helper functions (safe input for GUI)
# ======================================================================

def get_int(value, name="Value", minimum=None, maximum=None):
    """String ko int me convert karta hai, error par messagebox dikhata hai."""
    try:
        number = int(value.strip())
    except ValueError:
        messagebox.showerror("Invalid input", f"{name} must be a whole number.")
        return None
    if minimum is not None and number < minimum:
        messagebox.showerror("Invalid input", f"{name} must be at least {minimum}.")
        return None
    if maximum is not None and number > maximum:
        messagebox.showerror("Invalid input", f"{name} must be at most {maximum}.")
        return None
    return number


def get_float(value, name="Value"):
    try:
        number = float(value.strip())
    except ValueError:
        messagebox.showerror("Invalid input", f"{name} must be a number.")
        return None
    if number < 0:
        messagebox.showerror("Invalid input", f"{name} cannot be negative.")
        return None
    return number


def get_text(value, name="Field"):
    text = value.strip()
    if text == "":
        messagebox.showerror("Invalid input", f"{name} cannot be empty.")
        return None
    return text


def make_output(parent, height=8):
    """Read-only jaisa output box banata hai."""
    box = tk.Text(parent, height=height, wrap="word", state="disabled",
                  font=("Consolas", 10), bg="#f7f7f7", relief="solid", bd=1)
    return box


def set_output(box, text):
    box.config(state="normal")
    box.delete("1.0", "end")
    box.insert("end", text)
    box.config(state="disabled")


def labeled_entry(parent, label, row, width=24):
    ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=4)
    entry = ttk.Entry(parent, width=width)
    entry.grid(row=row, column=1, sticky="w", padx=5, pady=4)
    return entry


# ======================================================================
# Tab 1 : Date & Time
# ======================================================================

class DateTimeTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)

        # --- stopwatch state ---
        self.start_time = None
        self.elapsed = 0.0
        self.sw_job = None
        self.cd_job = None

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        notebook.add(self.build_current(notebook), text="Current Date/Time")
        notebook.add(self.build_date_diff(notebook), text="Date Difference")
        notebook.add(self.build_time_diff(notebook), text="Time Difference")
        notebook.add(self.build_format(notebook), text="Format Date")
        notebook.add(self.build_stopwatch(notebook), text="Stopwatch")
        notebook.add(self.build_countdown(notebook), text="Countdown")

    # ---- current date time ----
    def build_current(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.now_label = ttk.Label(frame, text="", font=("Segoe UI", 20, "bold"))
        self.now_label.pack(pady=20)
        ttk.Button(frame, text="Refresh", command=self.show_now).pack()
        self.show_now()
        return frame

    def show_now(self):
        self.now_label.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # ---- date difference ----
    def build_date_diff(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.d1 = labeled_entry(frame, "First date (YYYY-MM-DD):", 0)
        self.d2 = labeled_entry(frame, "Second date (YYYY-MM-DD):", 1)
        ttk.Button(frame, text="Calculate", command=self.calc_date_diff).grid(
            row=2, column=0, columnspan=2, pady=8)
        self.date_diff_out = make_output(frame, 3)
        self.date_diff_out.grid(row=3, column=0, columnspan=2, sticky="ew")
        return frame

    def calc_date_diff(self):
        try:
            first = datetime.strptime(self.d1.get().strip(), "%Y-%m-%d")
            second = datetime.strptime(self.d2.get().strip(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid format", "Use date format YYYY-MM-DD.")
            return
        days = abs(first - second).days
        set_output(self.date_diff_out, f"Difference between two dates : {days} days")

    # ---- time difference ----
    def build_time_diff(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.t1 = labeled_entry(frame, "Start time (H:M:S):", 0)
        self.t2 = labeled_entry(frame, "End time (H:M:S):", 1)
        ttk.Button(frame, text="Calculate", command=self.calc_time_diff).grid(
            row=2, column=0, columnspan=2, pady=8)
        self.time_diff_out = make_output(frame, 3)
        self.time_diff_out.grid(row=3, column=0, columnspan=2, sticky="ew")
        return frame

    def calc_time_diff(self):
        try:
            start = datetime.strptime(self.t1.get().strip(), "%H:%M:%S")
            end = datetime.strptime(self.t2.get().strip(), "%H:%M:%S")
        except ValueError:
            messagebox.showerror("Invalid format", "Use time format H:M:S (e.g. 14:30:00).")
            return
        set_output(self.time_diff_out, f"Duration between given time : {abs(start - end)}")

    # ---- format date ----
    def build_format(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.f_date = labeled_entry(frame, "Enter date (YYYY-MM-DD):", 0)
        ttk.Button(frame, text="Format", command=self.format_date).grid(
            row=1, column=0, columnspan=2, pady=8)
        self.format_out = make_output(frame, 6)
        self.format_out.grid(row=2, column=0, columnspan=2, sticky="ew")
        return frame

    def format_date(self):
        try:
            d = datetime.strptime(self.f_date.get().strip(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid format", "Use date format YYYY-MM-DD.")
            return
        text = (
            f"Original date : {d.strftime('%Y-%m-%d')}\n"
            f"DD-MM-YYYY    : {d.strftime('%d-%m-%Y')}\n"
            f"MM-DD-YYYY    : {d.strftime('%m-%d-%Y')}\n"
            f"Month         : {d.strftime('%B')}\n"
            f"Day           : {d.strftime('%A')}"
        )
        set_output(self.format_out, text)

    # ---- stopwatch ----
    def build_stopwatch(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.sw_label = ttk.Label(frame, text="0.00 s", font=("Consolas", 28, "bold"))
        self.sw_label.pack(pady=15)
        btns = ttk.Frame(frame)
        btns.pack()
        ttk.Button(btns, text="Start", command=self.sw_start).grid(row=0, column=0, padx=5)
        ttk.Button(btns, text="Stop", command=self.sw_stop).grid(row=0, column=1, padx=5)
        ttk.Button(btns, text="Reset", command=self.sw_reset).grid(row=0, column=2, padx=5)
        self.sw_status = ttk.Label(frame, text="")
        self.sw_status.pack(pady=8)
        return frame

    def sw_tick(self):
        if self.start_time is not None:
            total = self.elapsed + (time.time() - self.start_time)
            self.sw_label.config(text=f"{total:.2f} s")
            self.sw_job = self.after(50, self.sw_tick)

    def sw_start(self):
        if self.start_time is None:
            self.start_time = time.time()
            self.sw_status.config(text="Stopwatch started...")
            self.sw_tick()
        else:
            self.sw_status.config(text="Stopwatch is already running!")

    def sw_stop(self):
        if self.start_time is not None:
            self.elapsed += time.time() - self.start_time
            self.start_time = None
            if self.sw_job:
                self.after_cancel(self.sw_job)
            self.sw_label.config(text=f"{self.elapsed:.2f} s")
            self.sw_status.config(text="Stopwatch stopped.")
        else:
            self.sw_status.config(text="First start the stopwatch.")

    def sw_reset(self):
        if self.sw_job:
            self.after_cancel(self.sw_job)
        self.start_time = None
        self.elapsed = 0.0
        self.sw_label.config(text="0.00 s")
        self.sw_status.config(text="Stopwatch reset!")

    # ---- countdown ----
    def build_countdown(self, parent):
        frame = ttk.Frame(parent, padding=15)
        row = ttk.Frame(frame)
        row.pack()
        ttk.Label(row, text="Seconds (1-30):").grid(row=0, column=0, padx=5)
        self.cd_entry = ttk.Entry(row, width=8)
        self.cd_entry.grid(row=0, column=1, padx=5)
        ttk.Button(row, text="Start", command=self.cd_start).grid(row=0, column=2, padx=5)
        self.cd_label = ttk.Label(frame, text="--", font=("Consolas", 40, "bold"))
        self.cd_label.pack(pady=20)
        return frame

    def cd_start(self):
        seconds = get_int(self.cd_entry.get(), "Seconds", 1, 30)
        if seconds is None:
            return
        if self.cd_job:
            self.after_cancel(self.cd_job)
        self.cd_run(seconds)

    def cd_run(self, remaining):
        if remaining > 0:
            self.cd_label.config(text=str(remaining))
            self.cd_job = self.after(1000, self.cd_run, remaining - 1)
        else:
            self.cd_label.config(text="Time's up!")
            self.bell()


# ======================================================================
# Tab 2 : Math
# ======================================================================

class MathTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        notebook.add(self.build_factorial(notebook), text="Factorial")
        notebook.add(self.build_interest(notebook), text="Compound Interest")
        notebook.add(self.build_trig(notebook), text="Trigonometry")
        notebook.add(self.build_area(notebook), text="Area of Shapes")

    def build_factorial(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.fact_entry = labeled_entry(frame, "Enter a number (1-30):", 0)
        ttk.Button(frame, text="Calculate", command=self.calc_factorial).grid(
            row=1, column=0, columnspan=2, pady=8)
        self.fact_out = make_output(frame, 4)
        self.fact_out.grid(row=2, column=0, columnspan=2, sticky="ew")
        return frame

    def calc_factorial(self):
        n = get_int(self.fact_entry.get(), "Number", 1, 30)
        if n is None:
            return
        set_output(self.fact_out, f"Factorial of {n} is : {math.factorial(n)}")

    def build_interest(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.ci_p = labeled_entry(frame, "Principal amount:", 0)
        self.ci_r = labeled_entry(frame, "Interest rate (%):", 1)
        self.ci_t = labeled_entry(frame, "Time (years):", 2)
        ttk.Button(frame, text="Calculate", command=self.calc_interest).grid(
            row=3, column=0, columnspan=2, pady=8)
        self.ci_out = make_output(frame, 4)
        self.ci_out.grid(row=4, column=0, columnspan=2, sticky="ew")
        return frame

    def calc_interest(self):
        p = get_float(self.ci_p.get(), "Principal amount")
        r = get_float(self.ci_r.get(), "Interest rate")
        t = get_float(self.ci_t.get(), "Time")
        if None in (p, r, t):
            return
        amount = p * (1 + r / 100) ** t
        interest = amount - p
        set_output(self.ci_out,
                   f"Compound interest : {interest:.2f}\nFinal amount      : {amount:.2f}")

    def build_trig(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.trig_entry = labeled_entry(frame, "Angle (degrees):", 0)
        ttk.Button(frame, text="Calculate", command=self.calc_trig).grid(
            row=1, column=0, columnspan=2, pady=8)
        self.trig_out = make_output(frame, 4)
        self.trig_out.grid(row=2, column=0, columnspan=2, sticky="ew")
        return frame

    def calc_trig(self):
        angle = get_float(self.trig_entry.get(), "Angle")
        if angle is None:
            return
        rad = math.radians(angle)
        set_output(self.trig_out,
                   f"Sine    : {round(math.sin(rad), 4)}\n"
                   f"Cosine  : {round(math.cos(rad), 4)}\n"
                   f"Tangent : {round(math.tan(rad), 4)}")

    def build_area(self, parent):
        frame = ttk.Frame(parent, padding=15)

        circle = ttk.LabelFrame(frame, text="Circle", padding=10)
        circle.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.radius = labeled_entry(circle, "Radius:", 0, 12)
        ttk.Button(circle, text="Area", command=self.calc_circle).grid(
            row=1, column=0, columnspan=2, pady=5)

        tri = ttk.LabelFrame(frame, text="Triangle", padding=10)
        tri.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.base = labeled_entry(tri, "Base:", 0, 12)
        self.height = labeled_entry(tri, "Height:", 1, 12)
        ttk.Button(tri, text="Area", command=self.calc_triangle).grid(
            row=2, column=0, columnspan=2, pady=5)

        self.area_out = make_output(frame, 3)
        self.area_out.grid(row=1, column=0, columnspan=2, sticky="ew", pady=8)
        return frame

    def calc_circle(self):
        r = get_float(self.radius.get(), "Radius")
        if r is None:
            return
        set_output(self.area_out, f"Area of circle is : {math.pi * math.pow(r, 2)}")

    def calc_triangle(self):
        b = get_float(self.base.get(), "Base")
        h = get_float(self.height.get(), "Height")
        if None in (b, h):
            return
        set_output(self.area_out, f"Area of triangle is : {0.5 * b * h}")


# ======================================================================
# Tab 3 : Random Data
# ======================================================================

class RandomTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        notebook.add(self.build_number(notebook), text="Random Number")
        notebook.add(self.build_list(notebook), text="Random List")
        notebook.add(self.build_password(notebook), text="Random Password")
        notebook.add(self.build_otp(notebook), text="Random OTP")

    @staticmethod
    def check_range(minimum, maximum):
        if minimum is None or maximum is None:
            return False
        if minimum < 0 or maximum < 0:
            messagebox.showerror("Invalid range", "Negative number is not allowed!")
            return False
        if maximum < minimum:
            messagebox.showerror("Invalid range", "Minimum cannot be greater than maximum!")
            return False
        return True

    def build_number(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.rn_min = labeled_entry(frame, "Minimum number:", 0)
        self.rn_max = labeled_entry(frame, "Maximum number:", 1)
        ttk.Button(frame, text="Generate", command=self.gen_number).grid(
            row=2, column=0, columnspan=2, pady=8)
        self.rn_out = make_output(frame, 3)
        self.rn_out.grid(row=3, column=0, columnspan=2, sticky="ew")
        return frame

    def gen_number(self):
        lo = get_int(self.rn_min.get(), "Minimum")
        hi = get_int(self.rn_max.get(), "Maximum")
        if not self.check_range(lo, hi):
            return
        set_output(self.rn_out, f"Random number is : {random.randint(lo, hi)}")

    def build_list(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.rl_len = labeled_entry(frame, "List length (1-20):", 0)
        self.rl_min = labeled_entry(frame, "Minimum number:", 1)
        self.rl_max = labeled_entry(frame, "Maximum number:", 2)
        ttk.Button(frame, text="Generate", command=self.gen_list).grid(
            row=3, column=0, columnspan=2, pady=8)
        self.rl_out = make_output(frame, 4)
        self.rl_out.grid(row=4, column=0, columnspan=2, sticky="ew")
        return frame

    def gen_list(self):
        length = get_int(self.rl_len.get(), "List length", 1, 20)
        lo = get_int(self.rl_min.get(), "Minimum")
        hi = get_int(self.rl_max.get(), "Maximum")
        if length is None or not self.check_range(lo, hi):
            return
        data = [random.randint(lo, hi) for _ in range(length)]
        set_output(self.rl_out, f"Random list is : {data}")

    def build_password(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.pw_len = labeled_entry(frame, "Password length (1-32):", 0)
        ttk.Button(frame, text="Generate", command=self.gen_password).grid(
            row=1, column=0, columnspan=2, pady=8)
        self.pw_out = make_output(frame, 3)
        self.pw_out.grid(row=2, column=0, columnspan=2, sticky="ew")
        ttk.Button(frame, text="Copy to clipboard",
                   command=lambda: self.copy(self.pw_out)).grid(row=3, column=0, columnspan=2, pady=5)
        return frame

    def gen_password(self):
        length = get_int(self.pw_len.get(), "Password length", 1, 32)
        if length is None:
            return
        values = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(values, k=length))
        set_output(self.pw_out, password)

    def build_otp(self, parent):
        frame = ttk.Frame(parent, padding=15)
        self.otp_len = labeled_entry(frame, "OTP length (1-8):", 0)
        ttk.Button(frame, text="Generate", command=self.gen_otp).grid(
            row=1, column=0, columnspan=2, pady=8)
        self.otp_out = make_output(frame, 3)
        self.otp_out.grid(row=2, column=0, columnspan=2, sticky="ew")
        return frame

    def gen_otp(self):
        length = get_int(self.otp_len.get(), "OTP length", 1, 8)
        if length is None:
            return
        set_output(self.otp_out, "".join(random.choices("0123456789", k=length)))

    def copy(self, box):
        text = box.get("1.0", "end").strip()
        if text:
            self.clipboard_clear()
            self.clipboard_append(text)
            messagebox.showinfo("Copied", "Copied to clipboard!")


# ======================================================================
# Tab 4 : UUID
# ======================================================================

class UUIDTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)
        ttk.Label(self, text="Generate Unique Identifier (UUID4)",
                  font=("Segoe UI", 12, "bold")).pack(pady=5)
        ttk.Button(self, text="Generate UUID", command=self.generate).pack(pady=10)
        self.out = make_output(self, 3)
        self.out.pack(fill="x")
        ttk.Button(self, text="Copy to clipboard", command=self.copy).pack(pady=8)

    def generate(self):
        set_output(self.out, f"Generated uuid : {uuid.uuid4()}")

    def copy(self):
        text = self.out.get("1.0", "end").strip()
        if text:
            self.clipboard_clear()
            self.clipboard_append(text.replace("Generated uuid : ", ""))
            messagebox.showinfo("Copied", "UUID copied to clipboard!")


# ======================================================================
# Tab 5 : File Operations
# ======================================================================

class FileTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=15)
        os.makedirs(BASE_FOLDER, exist_ok=True)

        ttk.Label(self, text=f"Files folder : {BASE_FOLDER}/",
                  foreground="#555").pack(anchor="w")

        top = ttk.Frame(self)
        top.pack(fill="x", pady=8)
        ttk.Label(top, text="File name:").grid(row=0, column=0, padx=5)
        self.name_entry = ttk.Entry(top, width=30)
        self.name_entry.grid(row=0, column=1, padx=5)

        ttk.Label(self, text="Content:").pack(anchor="w")
        self.content = tk.Text(self, height=8, font=("Consolas", 10), relief="solid", bd=1)
        self.content.pack(fill="x", pady=4)

        btns = ttk.Frame(self)
        btns.pack(pady=6)
        ttk.Button(btns, text="Create", command=self.create_file).grid(row=0, column=0, padx=4)
        ttk.Button(btns, text="Write", command=self.write_file).grid(row=0, column=1, padx=4)
        ttk.Button(btns, text="Read", command=self.read_file).grid(row=0, column=2, padx=4)
        ttk.Button(btns, text="Append", command=self.append_file).grid(row=0, column=3, padx=4)

        self.status = ttk.Label(self, text="", foreground="#0a6b2b")
        self.status.pack(anchor="w", pady=4)

    def path(self):
        name = get_text(self.name_entry.get(), "File name")
        if name is None:
            return None
        # sirf file name allow karo, folder traversal se bachne ke liye
        return os.path.join(BASE_FOLDER, os.path.basename(name))

    def get_content(self):
        return self.content.get("1.0", "end-1c")

    def say(self, message, error=False):
        self.status.config(text=message, foreground="#b00020" if error else "#0a6b2b")

    def create_file(self):
        path = self.path()
        if path is None:
            return
        try:
            with open(path, "x", encoding="utf-8") as f:
                f.write("File created with x mode.")
            self.say("File created successfully!")
        except FileExistsError:
            self.say(f"{os.path.basename(path)} already exists!", True)
        except OSError as error:
            self.say(f"File operation failed : {error}", True)

    def write_file(self):
        path = self.path()
        text = get_text(self.get_content(), "Content") if path else None
        if path is None or text is None:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.get_content())
            self.say("Content written successfully!")
        except OSError as error:
            self.say(f"File operation failed : {error}", True)

    def read_file(self):
        path = self.path()
        if path is None:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = f.read()
            self.content.delete("1.0", "end")
            if data == "":
                self.say("File is empty.")
            else:
                self.content.insert("end", data)
                self.say("File read successfully!")
        except FileNotFoundError:
            self.say(f"{os.path.basename(path)} not found!", True)
        except OSError as error:
            self.say(f"File operation failed : {error}", True)

    def append_file(self):
        path = self.path()
        text = get_text(self.get_content(), "Content") if path else None
        if path is None or text is None:
            return
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(self.get_content() + "\n")
            self.say("Content appended successfully!")
        except OSError as error:
            self.say(f"File operation failed : {error}", True)


# ======================================================================
# Tab 6 : Explore Module (dir())
# ======================================================================

class ExploreTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=15)
        row = ttk.Frame(self)
        row.pack(fill="x")
        ttk.Label(row, text="Module:").grid(row=0, column=0, padx=5)
        self.combo = ttk.Combobox(row, values=ALLOWED_MODULES, width=20)
        self.combo.grid(row=0, column=1, padx=5)
        self.combo.set(ALLOWED_MODULES[0])
        ttk.Button(row, text="Explore", command=self.explore).grid(row=0, column=2, padx=5)

        self.out = make_output(self, 18)
        self.out.pack(fill="both", expand=True, pady=10)

    def explore(self):
        name = get_text(self.combo.get(), "Module name")
        if name is None:
            return
        if name not in ALLOWED_MODULES:
            set_output(self.out, "Module not found!")
            return
        module = importlib.import_module(name)
        set_output(self.out, "\n".join(dir(module)))


# ======================================================================
# Main Window
# ======================================================================

class MultiUtilityToolkitApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Utility Toolkit")
        self.geometry("760x560")
        self.minsize(680, 500)

        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        header = ttk.Label(self, text="Welcome to Multi-Utility Toolkit",
                           font=("Segoe UI", 16, "bold"), padding=10)
        header.pack()

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=5)

        notebook.add(DateTimeTab(notebook), text="Datetime & Time")
        notebook.add(MathTab(notebook), text="Math")
        notebook.add(RandomTab(notebook), text="Random Data")
        notebook.add(UUIDTab(notebook), text="UUID")
        notebook.add(FileTab(notebook), text="File Operations")
        notebook.add(ExploreTab(notebook), text="Explore Module")

        footer = ttk.Frame(self, padding=8)
        footer.pack(fill="x")
        ttk.Button(footer, text="Exit", command=self.on_exit).pack(side="right")

    def on_exit(self):
        if messagebox.askyesno("Exit", "Thank you for using the Multi-Utility Toolkit!\n\nClose the app?"):
            self.destroy()


if __name__ == "__main__":
    app = MultiUtilityToolkitApp()
    app.mainloop()