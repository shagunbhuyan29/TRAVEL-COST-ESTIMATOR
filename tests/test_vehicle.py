import unittest
from models.vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    def test_vehicle_creation(self):
        v = Vehicle("car", 15)
        self.assertEqual(v.vehicle_type, "car")
        self.assertEqual(v.mileage, 15)

if __name__ == "__main__":
    unittest.main()
