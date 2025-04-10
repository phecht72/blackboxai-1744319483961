"""
Main application file for the Retro Clock.
Implements a multi-page clock application with settings and alarm functionality.
"""

import tkinter as tk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import config
from ui_elements import (
    RetroButton, RetroLabel, RetroFrame,
    RetroEntry, create_separator, create_navigation_button
)

class ClockFrame(RetroFrame):
    """Frame displaying the clock."""
    def __init__(self, master):
        super().__init__(master)
        self.setup_clock()

    def setup_clock(self):
        """Setup clock display elements."""
        self.time_label = RetroLabel(
            self,
            font=("Courier New", 48),
            relief="ridge"
        )
        self.time_label.pack(pady=20)

        self.date_label = RetroLabel(
            self,
            font=("Courier New", 24)
        )
        self.date_label.pack(pady=10)

        self.update_time()

    def update_time(self):
        """Update the time display."""
        try:
            current_config = config.load_config()
            time_format = current_config["clock"]["time_format"]
            
            if time_format == "24h":
                time_str = strftime('%H:%M:%S')
            else:
                time_str = strftime('%I:%M:%S %p')

            self.time_label.config(text=time_str)

            if current_config["clock"]["show_date"]:
                date_format = current_config["clock"]["date_format"]
                date_str = datetime.now().strftime(date_format)
                self.date_label.config(text=date_str)
            else:
                self.date_label.config(text="")
            
            # Update every 1000ms (1 second)
            self.after(1000, self.update_time)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update time: {str(e)}")

class SettingsFrame(RetroFrame):
    """Frame for application settings."""
    def __init__(self, master):
        super().__init__(master)
        self.setup_settings()

    def setup_settings(self):
        """Setup settings controls."""
        title = RetroLabel(
            self,
            text="Settings",
            font=("Courier New", 24)
        )
        title.pack(pady=20)

        # Time format setting
        format_frame = RetroFrame(self)
        format_frame.pack(pady=10, fill="x", padx=20)
        
        RetroLabel(format_frame, text="Time Format:").pack(side="left", padx=10)
        self.format_var = tk.StringVar(value=config.current_config["clock"]["time_format"])
        
        format_24h = RetroButton(
            format_frame,
            text="24h",
            command=lambda: self.update_time_format("24h")
        )
        format_24h.pack(side="left", padx=5)
        
        format_12h = RetroButton(
            format_frame,
            text="12h",
            command=lambda: self.update_time_format("12h")
        )
        format_12h.pack(side="left", padx=5)

        # Date display setting
        date_frame = RetroFrame(self)
        date_frame.pack(pady=10, fill="x", padx=20)
        
        RetroLabel(date_frame, text="Show Date:").pack(side="left", padx=10)
        self.show_date_var = tk.BooleanVar(value=config.current_config["clock"]["show_date"])
        date_toggle = RetroButton(
            date_frame,
            text="Toggle Date",
            command=self.toggle_date
        )
        date_toggle.pack(side="left", padx=5)

    def update_time_format(self, format_type):
        """Update the time format setting."""
        try:
            config.update_config("clock", "time_format", format_type)
            self.format_var.set(format_type)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update time format: {str(e)}")

    def toggle_date(self):
        """Toggle date display setting."""
        try:
            current = self.show_date_var.get()
            new_value = not current
            config.update_config("clock", "show_date", new_value)
            self.show_date_var.set(new_value)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to toggle date display: {str(e)}")

class AlarmFrame(RetroFrame):
    """Frame for alarm functionality."""
    def __init__(self, master):
        super().__init__(master)
        self.setup_alarm()

    def setup_alarm(self):
        """Setup alarm controls."""
        title = RetroLabel(
            self,
            text="Alarm",
            font=("Courier New", 24)
        )
        title.pack(pady=20)

        # Alarm time entry
        time_frame = RetroFrame(self)
        time_frame.pack(pady=10, fill="x", padx=20)
        
        RetroLabel(time_frame, text="Set Alarm (HH:MM):").pack(side="left", padx=10)
        self.alarm_entry = RetroEntry(time_frame, width=5)
        self.alarm_entry.pack(side="left", padx=5)
        
        set_button = RetroButton(
            time_frame,
            text="Set Alarm",
            command=self.set_alarm
        )
        set_button.pack(side="left", padx=5)

    def set_alarm(self):
        """Set the alarm time."""
        try:
            alarm_time = self.alarm_entry.get()
            # Here you would add actual alarm functionality
            messagebox.showinfo("Alarm", f"Alarm set for {alarm_time}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to set alarm: {str(e)}")

class RetroClock(tk.Tk):
    """Main application window."""
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_frames()
        self.setup_navigation()

    def setup_window(self):
        """Configure the main window."""
        current_config = config.load_config()
        window_config = current_config["window"]
        
        self.title(window_config["title"])
        self.geometry(f"{window_config['width']}x{window_config['height']}")
        self.configure(bg="black")
        self.resizable(window_config["resizable"], window_config["resizable"])

    def setup_frames(self):
        """Setup application frames."""
        # Container for all frames
        container = RetroFrame(self)
        container.pack(side="top", fill="both", expand=True)

        # Initialize frames
        self.frames = {}
        for F in (ClockFrame, SettingsFrame, AlarmFrame):
            frame = F(container)
            self.frames[F] = frame
            frame.pack(fill="both", expand=True)
            frame.pack_forget()  # Hide all frames initially

        # Show clock frame by default
        self.show_frame(ClockFrame)

    def setup_navigation(self):
        """Setup navigation buttons."""
        nav_frame = RetroFrame(self)
        nav_frame.pack(side="bottom", fill="x", pady=10)

        buttons = [
            ("Clock", ClockFrame),
            ("Settings", SettingsFrame),
            ("Alarm", AlarmFrame)
        ]

        for text, frame_class in buttons:
            btn = create_navigation_button(
                nav_frame,
                text=text,
                command=lambda f=frame_class: self.show_frame(f)
            )
            btn.pack(side="left", padx=10)

    def show_frame(self, frame_class):
        """Show the specified frame."""
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        
        # Show selected frame
        frame = self.frames[frame_class]
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    try:
        app = RetroClock()
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Application error: {str(e)}")
