class Validator:

    def get_float(self, message):
        while True:
            try:
                value = float(input(message))
                if value < 0:
                    print("Value cannot be negative. Try again.")
                    continue
                return value
            except ValueError:
                print("Invalid number. Please try again.")
