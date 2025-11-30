from flask import Flask, request, render_template_string
from src.model import HousePrice

app = Flask(__name__)
hp = HousePrice()
hp.model()   # train model once when server starts

# Simple HTML UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>House Price Prediction</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h2>House Price Prediction</h2>
    <form method="post">
        <label>Square Feet:</label><br>
        <input name="sqft" type="number" required><br><br>

        <label>Bedrooms:</label><br>
        <input name="bed" type="number" required><br><br>

        <label>Bathrooms:</label><br>
        <input name="bath" type="number" required><br><br>

        <label>Age of House:</label><br>
        <input name="age" type="number" required><br><br>

        <button type="submit">Predict Price</button>
    </form>

    {% if price %}
        <h3>Predicted Price: {{ price }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    price = None
    if request.method == "POST":
        sqft = float(request.form["sqft"])
        bed = int(request.form["bed"])
        bath = int(request.form["bath"])
        age = int(request.form["age"])

        price = round(hp.predict(sqft, bed, bath, age), 2)

    return render_template_string(HTML_PAGE, price=price)


if __name__ == "__main__":
    app.run(debug=True)
