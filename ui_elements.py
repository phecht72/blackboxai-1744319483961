"""
Common UI elements and styling for the Retro Clock application.
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Optional

class RetroButton(tk.Button):
    """Custom button with retro styling."""
    def __init__(self, master: Any, **kwargs):
        super().__init__(
            master,
            bg="black",
            fg="lime",
            activebackground="lime",
            activeforeground="black",
            font=("Courier New", 12),
            relief="ridge",
            **kwargs
        )
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)

    def _on_enter(self, e):
        """Mouse enter event handler."""
        self.config(bg='lime', fg='black')

    def _on_leave(self, e):
        """Mouse leave event handler."""
        self.config(bg='black', fg='lime')

class RetroLabel(tk.Label):
    """Custom label with retro styling."""
    def __init__(self, master: Any, **kwargs):
        super().__init__(
            master,
            bg="black",
            fg="lime",
            font=("Courier New", 14),
            **kwargs
        )

class RetroFrame(tk.Frame):
    """Custom frame with retro styling."""
    def __init__(self, master: Any, **kwargs):
        super().__init__(
            master,
            bg="black",
            **kwargs
        )

class RetroEntry(tk.Entry):
    """Custom entry with retro styling."""
    def __init__(self, master: Any, **kwargs):
        super().__init__(
            master,
            bg="black",
            fg="lime",
            insertbackground="lime",
            font=("Courier New", 12),
            relief="ridge",
            **kwargs
        )

def create_separator(master: Any, orient: str = "horizontal") -> ttk.Separator:
    """Create a themed separator."""
    style = ttk.Style()
    style.configure("Retro.TSeparator", background="lime")
    return ttk.Separator(master, orient=orient, style="Retro.TSeparator")

def create_navigation_button(master: Any, text: str, command: Optional[callable] = None) -> RetroButton:
    """Create a navigation button with consistent styling."""
    return RetroButton(
        master,
        text=text,
        command=command,
        width=10,
        padx=10,
        pady=5,
        border=2
    )
