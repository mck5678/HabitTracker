from tracker import HabitTracker
from habit import Habit

def show_menu():
    print("\nHabit Tracker")
    print("1. Show Habits")
    print("2. Mark a habit as completed")
    print("3. View Streaks")
    print("4. Exit")

def main():
    tracker = HabitTracker("habits.json")   # ← THIS is the missing argument

    print("Welcome to the Social Kindness Tracker!")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            tracker.show_habits()
        elif choice == "2":
            tracker.show_habits()
            index = int(input("Which habit number did you complete? "))
            tracker.mark_completed(index)
        elif choice == "3":
            tracker.show_habits()
            index = int(input("Which habit number do you want to view streaks for? "))
            tracker.view_streak(index)
        elif choice == "4":
            print("Goodbye! Keep spreading kindness 🫶🏻")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
