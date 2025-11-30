from flask import Flask, request, render_template_string
from src.model import HousePrice

app = Flask(__name__)
hp = HousePrice()
hp.model()   


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>House Price Prediction</title>
    <style>
        body {
            font-family: Arial;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #f2f2f2;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.15);
            width: 380px;
            text-align: center;
        }

        .logo {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            background: linear-gradient(135deg, #007BFF, #00C6FF);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 22px;
            margin: 0 auto 15px auto;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
        }

        input {
            width: 90%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            margin-top: 15px;
            background-color: #007BFF;
            color: white;
            padding: 12px 20px;
            border: none;
            width: 100%;
            font-size: 16px;
            border-radius: 10px;
            cursor: pointer;
            position: relative;
        }

        button::after {
            content: "✔";
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 18px;
            color: white;
        }

        button:hover {
            background-color: #005FCC;
        }

        h2 {
            margin-top: 5px;
            margin-bottom: 20px;
        }

        h3 {
            margin-top: 20px;
            color: #333;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Text-based logo -->
        <div class="logo">RP</div>

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
    </div>

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
