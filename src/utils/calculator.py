class Calculator:

    def calculate_fuel_needed(self, distance, fuel_efficiency):
        return distance / fuel_efficiency

    def calculate_fuel_cost(self, fuel_needed, price_per_litre):
        return fuel_needed * price_per_litre
