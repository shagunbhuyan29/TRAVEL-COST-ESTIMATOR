class TravelCostService:
    def calculate_cost(self, distance, mileage, fuel_price, vehicle_type):
        vehicle_factor = {
            "car": 1.0,
            "bike": 0.7,
            "bus": 1.3
        }
        
        multiplier = vehicle_factor.get(vehicle_type.lower(), 1.0)
        
        fuel_needed = distance / mileage
        base_cost = fuel_needed * fuel_price
        
        return base_cost * multiplier

