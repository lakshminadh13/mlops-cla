def predict(value):
    if value >= 50:
        return "High"
    return "Low"


if __name__ == "__main__":
    print("Prediction:", predict(75))
