# data_validator.py

class DataValidator:
    """
    Validates all user input.
    """

    @staticmethod
    def validate_positive_number(value, label):
        try:
            value = float(value)
        except ValueError:
            raise ValueError(f"{label} must be a number.")
        if value < 0:
            raise ValueError(f"{label} must be positive.")
        return value

    @staticmethod
    def validate_string(value, label):
        if not value or not value.strip():
            raise ValueError(f"{label} cannot be empty.")
        return value.strip()
