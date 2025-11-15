The Social Kindness Habit Tracker is a simple habit tracking application built in Python. The program runs in the terminal and allows users to show habits, mark them as completed and view existing streaks. All data is saved in a JSON file so habits and completion dates persist between sessions.

The app was created for a university portfolio project focusing on clean backend logic, object-oriented programming, and a functional command-line interface.

The main features are:
- Showing all predefined habits with name and periodicity
- Marking a habit as completed with date and time
- Viewing the current streak for each habit
- Saving all habit data and completion timestamps into a habits.json file to keep progress between sessions

How to run the project:
1. Make sure Python 3 is installed on the system.
2. Download or clone this repository.
3. Open a terminal inside the project folder.
4. Run: python3 main.py

The project consists of the following files:

main.py – runs the program and shows the menu in the terminal.  
habit.py – defines the Habit class (one single habit with its data).  
tracker.py – defines the HabitTracker class, which loads, saves, lists habits and tracks streaks.  
habits.json – stores all habits and their completion dates.

Example terminal output looks like this:

Welcome to the Social Kindness Tracker!

Habit Tracker
1. Show Habits
2. Mark a habit as completed
3. View Streaks
4. Exit

The purpose of this project was to learn practical Python skills, work with JSON storage, and structure an application in a clear and maintainable way. The app is intentionally simple but can be extended with more features later, like an input validation, analytics, streak calculations, or a graphical interface.

Technologies used:
Python 3  
JSON for data storage

This project is free to use, extend, or modify.
