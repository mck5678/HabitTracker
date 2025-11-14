import json
from habit import Habit


class HabitTracker:
    def __init__(self, data_file):
        self.data_file = data_file
        self.habits = []
        self.load()

    def load(self):
        """Load habits from a JSON file."""
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
            self.habits = [Habit.from_dict(item) for item in data]
        except FileNotFoundError:
            self.habits = []

    def save(self):
        """Save habits to a JSON file."""
        data = [habit.to_dict() for habit in self.habits]
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def show_habits(self):
        """Print all habits with an index."""
        if len(self.habits) == 0:
            print("No habits found.")
            return

        for index, habit in enumerate(self.habits):
            print(f"{index}. {habit.name} ({habit.periodicity})")

    def mark_completed(self, index):
        """Mark a habit as completed."""
        if index < 0 or index >= len(self.habits):
            print("Invalid habit number.")
            return

        habit = self.habits[index]
        timestamp = habit.complete()
        self.save()
        print(f"Marked '{habit.name}' as completed at {timestamp}")

    def view_streak(self, index):
        """View the streak of a habit."""
        if index < 0 or index >= len(self.habits):
            print("Invalid habit number.")
            return

        habit = self.habits[index]
        s = habit.streak()
        print(f"Current streak for '{habit.name}': {s}")
