# cost_calculator.py

class CostCalculator:
    """
    Handles cost calculations for the Travel Cost Estimator.
    """

    def __init__(self, distance_km, fuel_price, mileage, toll_cost=0, misc_cost=0):
        self.distance_km = distance_km
        self.fuel_price = fuel_price
        self.mileage = mileage
        self.toll_cost = toll_cost
        self.misc_cost = misc_cost

    def calculate_fuel_cost(self):
        if self.mileage <= 0:
            raise ValueError("Mileage must be greater than zero.")
        fuel_needed = self.distance_km / self.mileage
        return round(fuel_needed * self.fuel_price, 2)

    def calculate_total_cost(self):
        fuel_cost = self.calculate_fuel_cost()
        total = fuel_cost + self.toll_cost + self.misc_cost
        return round(total, 2)
