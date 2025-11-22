from utils.calculator import Calculator

class TravelEstimator:
    def __init__(self):
        self.calc = Calculator()

    def estimate_total_cost(self, distance, fuel_efficiency, fuel_price, tolls):
        fuel_needed = self.calc.calculate_fuel_needed(distance, fuel_efficiency)
        fuel_cost = self.calc.calculate_fuel_cost(fuel_needed, fuel_price)
        total_cost = fuel_cost + tolls

        return {
            "fuel_needed": round(fuel_needed, 2),
            "fuel_cost": round(fuel_cost, 2),
            "tolls": round(tolls, 2),
            "total_cost": round(total_cost, 2)
        }
