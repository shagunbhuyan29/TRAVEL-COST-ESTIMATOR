class TravelModel:
    def __init__(self, distance, mileage, fuel_price, tolls):
        self.distance = distance
        self.mileage = mileage
        self.fuel_price = fuel_price
        self.tolls = tolls

    def to_dict(self):
        return {
            "distance": self.distance,
            "mileage": self.mileage,
            "fuel_price": self.fuel_price,
            "tolls": self.tolls
        }
