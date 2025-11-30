import math
from src.model import HousePrice


def test_model_training_creates_fitted_model():
    """Model() should fit LinearRegression on train.csv."""
    hp = HousePrice()
    hp.model()

    # LinearRegression is fitted -> has coef_ and intercept_
    assert hasattr(hp.lr, "coef_"), "Model is not fitted - coef_ missing"
    assert hasattr(hp.lr, "intercept_"), "Model is not fitted - intercept_ missing"


def test_evaluate_on_valid_and_test_files():
    """_evaluate_on_file should return r2 and mae within valid ranges."""
    hp = HousePrice()
    hp.model()

    valid_metrics = hp._evaluate_on_file("data/valid.csv")
    test_metrics = hp._evaluate_on_file("data/test.csv")

    for name, metrics in [("valid", valid_metrics), ("test", test_metrics)]:

        assert "r2" in metrics and "mae" in metrics, f"{name}: keys missing"

        r2 = metrics["r2"]
        mae = metrics["mae"]

        assert 0.0 <= r2 <= 1.0, f"{name}: r2 out of range: {r2}"

        assert mae >= 0.0 and math.isfinite(mae), f"{name}: mae invalid: {mae}"


def test_predict_returns_positive_price():
    """predict() should return a positive numeric price."""
    hp = HousePrice()
    hp.model()

    price = hp.predict(1800, 3, 2, 10)

    assert isinstance(price, (float, int)), "Prediction is not a number"
    assert price > 0, f"Prediction should be positive, got {price}"
