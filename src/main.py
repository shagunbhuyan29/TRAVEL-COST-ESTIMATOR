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

