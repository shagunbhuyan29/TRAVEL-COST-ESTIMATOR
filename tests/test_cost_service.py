import unittest
from services.cost_service import TravelCostService

class TestTravelCost(unittest.TestCase):

    def test_calculate_cost(self):
        service = TravelCostService()
        result = service.calculate_cost(100, 10, 100, "car")
        self.assertEqual(result, 1000)

if __name__ == "__main__":
    unittest.main()
