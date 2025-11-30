from src.model import HousePrice

def main():
    hp = HousePrice()

    hp.model()
    print("\nTraining complete!")

    val_metrics = hp.evaluate_on_validation()
    print("\nValidation Metrics:", val_metrics)

    test_metrics = hp.evaluate_on_test()
    print("\nTest Metrics:", test_metrics)

    price = hp.predict(1800, 3, 2, 10)
    print("\nPredicted Price:", price)


if __name__ == "__main__":
    main()
