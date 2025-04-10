
Built by https://www.blackbox.ai

---

```markdown
# Retro Clock 1980's

## Project Overview
The Retro Clock application is a nostalgic timekeeping application that resembles the style of clocks from the 1980s. It features a user-friendly interface built with Tkinter, allowing users to view the time in either a 12-hour or 24-hour format, toggle the display of the date, and set alarms. It draws inspiration from retro aesthetics with its distinctive color palette and styling.

## Installation
To get started with the Retro Clock application, you need to have Python installed. It is recommended to use a virtual environment for this project. Follow the steps below to set it up:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/retro-clock.git
   cd retro-clock
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages. Make sure to adjust for any additional libraries not noted in the provided content:
   ```bash
   pip install tkinter
   ```

4. Run the application:
   ```bash
   python retro_clock.py
   ```

## Usage
Once the application is running, you can switch between the three main functionalities using the navigation buttons at the bottom:
- **Clock**: Displays the current time and date.
- **Settings**: Allows you to change the time format and toggle the date display.
- **Alarm**: Set alarms based on the specified time.

## Features
- **Time Display**: View time in both 12-hour and 24-hour formats.
- **Date Display**: Option to toggle the display of the current date.
- **Alarm Functionality**: Set alarms for reminders.
- **Customizable Appearance**: Retro design with configurable window dimensions, colors, and fonts.

## Dependencies
The application uses the following dependencies:
- `tkinter`: For the GUI components.
- `json`: For configuration file handling (comes with Python).
- `os`: For file operations (comes with Python).
- `datetime` and `time`: For time management (comes with Python).

No additional external packages are detailed in the provided files, but you may require other libraries depending on your environment.

## Project Structure
Here is the structure of the project directory:

```
retro-clock/
│
├── config.py            # Handles configuration settings.
├── ui_elements.py       # Contains UI elements and styling.
├── retro_clock.py       # Main application file that runs the clock.
├── index.html           # HTML template for a web interface (optional).
└── clock_settings.json   # User configuration file for app settings.
```

## Conclusion
The Retro Clock application combines nostalgia with modern utility, serving not only as a timekeeper but also as a customizable alarm system. Contribute to the project by creating issues or pull requests in the repository. Enjoy your journey back to the '80s with this retro clock!
```