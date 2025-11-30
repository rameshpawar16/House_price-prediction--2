import json
from src.model import HousePrice

THRESHOLD = 0.90  

def monitor():
    hp = HousePrice()
    hp.model()

    metrics = hp._evaluate_on_file("data/test.csv")
    accuracy = metrics["r2"]
    
    print("Current accuracy:", accuracy)

    if accuracy < THRESHOLD:
        print("⚠ ALERT: Model accuracy dropped!")

        hp.model()
        print("New model trained and ready to deploy")

        with open("alert.json", "w") as f:
            json.dump({"alert": True}, f)

    else:
        print("Accuracy OK")
        with open("alert.json", "w") as f:
            json.dump({"alert": False}, f)

if __name__ == "__main__":
    monitor()
