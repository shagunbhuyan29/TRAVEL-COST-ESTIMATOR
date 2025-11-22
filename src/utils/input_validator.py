def validate_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive!")
                continue
            return value
        except ValueError:
            print("Please enter a valid number!")

def validate_vehicle_type():
    while True:
        v = input("Enter vehicle type (car/bike/truck): ").lower()
        if v in ["car", "bike", "truck"]:
            return v
        print("Invalid vehicle type.")

