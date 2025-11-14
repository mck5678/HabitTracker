import datetime

class Habit:
    """
    Represents a single habit with a name, periodicity, creation date,
    and a list of completion timestamps.
    """

    def __init__(self, name, periodicity, created_at=None, completions=None):
        self.name = name                        # e.g. "Give one honest compliment"
        self.periodicity = periodicity          # "daily" or "weekly"
        self.created_at = created_at or datetime.datetime.now().isoformat()
        self.completions = completions or []    # list of timestamps

    def complete(self):
        """Mark the habit as completed RIGHT NOW."""
        timestamp = datetime.datetime.now().isoformat()
        self.completions.append(timestamp)
        return timestamp

    def streak(self):
        """
        Calculates the current streak length.

        Daily habits → must be completed once per day  
        Weekly habits → must be completed once per week
        """
        if not self.completions:
            return 0

        # Convert timestamps into datetime objects
        dates = [datetime.datetime.fromisoformat(t).date() for t in self.completions]
        dates = sorted(dates, reverse=True)

        streak = 1
        last = dates[0]

        for d in dates[1:]:
            if self.periodicity == "daily":
                expected = last - datetime.timedelta(days=1)
            else:  # weekly
                expected = last - datetime.timedelta(weeks=1)

            if d == expected:
                streak += 1
                last = d
            else:
                break

        return streak

    def to_dict(self):
        """Convert to dictionary for saving into JSON."""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at,
            "completions": self.completions
        }

    @staticmethod
    def from_dict(data):
        """Create a Habit object from a dictionary."""
        return Habit(
            name=data["name"],
            periodicity=data["periodicity"],
            created_at=data.get("created_at"),
            completions=data.get("completions", [])
        )
