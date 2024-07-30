import tkinter as tk
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x150")

        # Create input fields for duration or target date/time
        self.duration_label = tk.Label(self.root, text="Enter duration (HH:MM:SS) or target date/time (YYYY-MM-DD HH:MM:SS):")
        self.duration_label.pack(padx=10, pady=10)

        self.duration_entry = tk.Entry(self.root, width=30)
        self.duration_entry.pack(padx=10, pady=10)

        # Create start button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(padx=10, pady=10)

        # Create timer display label
        self.timer_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.timer_label.pack(padx=10, pady=10)

        # Create alert label
        self.alert_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.alert_label.pack(padx=10, pady=10)

    def start_timer(self):
        duration = self.duration_entry.get()
        try:
            if ":" in duration:
                # Parse duration in HH:MM:SS format
                hours, minutes, seconds = map(int, duration.split(":"))
                delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            else:
                # Parse target date/time in YYYY-MM-DD HH:MM:SS format
                target_date = datetime.strptime(duration, "%Y-%m-%d %H:%M:%S")
                delta = target_date - datetime.now()
            self.countdown(delta)
        except ValueError:
            self.alert_label.config(text="Invalid input. Please enter a valid duration or target date/time.")

    def countdown(self, delta):
        while delta.total_seconds() > 0:
            self.timer_label.config(text=str(delta))
            delta -= timedelta(seconds=1)
            self.root.update()
            self.root.after(1000)  # Update every 1 second
        self.alert_label.config(text="Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()