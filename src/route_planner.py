# route_planner.py

class RoutePlanner:
    """
    Handles route planning & distance estimation.
    """

    AVERAGE_SPEEDS = {
        "car": 60,
        "bike": 40,
        "bus": 50,
        "train": 80,
        "flight": 600
    }

    def __init__(self, origin, destination, mode):
        self.origin = origin
        self.destination = destination
        self.mode = mode.lower()

    def get_distance(self):
        """
        Placeholder logic — replace with API if needed.
        """
        # Fake distance calculation until API integration
        return (len(self.origin) + len(self.destination)) * 5

    def estimate_travel_time(self, distance):
        if self.mode not in self.AVERAGE_SPEEDS:
            raise ValueError("Invalid mode of transport.")
        speed = self.AVERAGE_SPEEDS[self.mode]
        hours = distance / speed
        return round(hours, 2)
