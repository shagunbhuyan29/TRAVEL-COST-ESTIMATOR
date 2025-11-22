from estimator.travel_estimator import TravelEstimator
from services.validation_service import Validator

class TravelCostCLI:
    def __init__(self):
        self.estimator = TravelEstimator()
        self.validator = Validator()

    def start(self):
        print("\nWelcome to the Travel Cost Estimator CLI\n")

        distance = self.validator.get_float("Enter travel distance (km): ")
        fuel_efficiency = self.validator.get_float("Enter vehicle mileage (km/l): ")
        fuel_price = self.validator.get_float("Enter fuel price per litre: ")
        tolls = self.validator.get_float("Enter total toll charges (optional, press 0 if none): ")

        result = self.estimator.estimate_total_cost(
            distance=distance,
            fuel_efficiency=fuel_efficiency,
            fuel_price=fuel_price,
            tolls=tolls
        )

        print("\n===== Estimated Travel Cost =====")
        print(f"Fuel Needed: {result['fuel_needed']} litres")
        print(f"Fuel Cost: ₹{result['fuel_cost']}")
        print(f"Toll Charges: ₹{result['tolls']}")
        print(f"Total Cost: ₹{result['total_cost']}")
        print("=================================\n")
