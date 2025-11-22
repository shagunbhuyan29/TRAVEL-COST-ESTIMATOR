from services.cost_service import TravelCostService
from utils.input_validator import validate_float, validate_vehicle_type

def main():
    print("=== Travel Cost Estimator ===")

    distance = validate_float("Enter distance (km): ")
    mileage = validate_float("Enter mileage (km per litre): ")
    fuel_price = validate_float("Enter fuel price per litre: ")

    vehicle_type = validate_vehicle_type()

    cost_service = TravelCostService()
    total_cost = cost_service.calculate_cost(
        distance, mileage, fuel_price, vehicle_type
    )

    print(f"\nEstimated Travel Cost: ₹{total_cost:.2f}")

if __name__ == "__main__":
    main()
    # main.py

from cost_calculator import CostCalculator
from route_planner import RoutePlanner
from data_validator import DataValidator
from utils import print_divider, format_currency

def main():
    print("\n🚗 Travel Cost Estimator")
    print_divider()

    origin = DataValidator.validate_string(input("Enter starting location: "), "Origin")
    destination = DataValidator.validate_string(input("Enter destination: "), "Destination")
    mode = DataValidator.validate_string(input("Enter mode (car/bike/bus/train/flight): "), "Mode")

    route = RoutePlanner(origin, destination, mode)
    distance = route.get_distance()
    travel_time = route.estimate_travel_time(distance)

    print_divider()
    print(f"Estimated distance: {distance} km")
    print(f"Estimated travel time: {travel_time} hours")
    print_divider()

    fuel_price = DataValidator.validate_positive_number(input("Fuel price per liter (₹): "), "Fuel price")
    mileage = DataValidator.validate_positive_number(input("Vehicle mileage (km/l): "), "Mileage")
    toll = DataValidator.validate_positive_number(input("Toll charges (₹): "), "Toll")
    misc = DataValidator.validate_positive_number(input("Miscellaneous costs (₹): "), "Misc cost")

    cost_calc = CostCalculator(distance, fuel_price, mileage, toll, misc)

    total = cost_calc.calculate_total_cost()

    print_divider()
    print("FINAL TRAVEL ESTIMATE")
    print_divider()
    print(f"Fuel Cost: {format_currency(cost_calc.calculate_fuel_cost())}")
    print(f"Total Cost: {format_currency(total)}")
    print_divider()

if __name__ == "__main__":
    main()


