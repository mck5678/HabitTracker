The Social Kindness Habit Tracker is a simple habit tracking application built in Python. The program runs in the terminal and allows users to add habits, list existing habits, and mark habits as completed. All data is saved in a JSON file so habits and completion dates persist between sessions.

The app was created for a university portfolio project focusing on clean backend logic, object-oriented programming, and a functional command-line interface.

The main features include:
- Creating new habits with a name and periodicity
- Displaying all habits in the program
- Marking habits as completed
- Automatic saving and loading of habit data
- Storing all data in a habits.json file

How to run the project:
1. Make sure Python 3 is installed on the system.
2. Download or clone this repository.
3. Open a terminal inside the project folder.
4. Run: python3 main.py

The project consists of the following files:

main.py – This file starts the program and handles the terminal interface.  
habit.py – Contains the Habit class that represents a single habit.  
habit_tracker.py – Contains the HabitTracker class that manages all habits together.  
habits.json – A data file that stores all habits and their completion dates.

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

Future improvements:
Adding validation to prevent invalid input  
Adding statistics or streak tracking  
Creating a graphical interface in the future

This project is free to use, extend, or modify.
