from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Pobieramy dane z formularza
            km = float(request.form.get("km", 0))
            energy = float(request.form.get("energy", 0))
            
            # Obliczanie emisji CO2
            co2_km = km * 0.2  # Emisja CO2 na km (200 g/km)
            co2_energy = energy * 0.5  # Emisja CO2 na kWh (500 g/kWh)
            result = co2_km + co2_energy
        except ValueError:
            result = "Proszę wprowadzić poprawne wartości liczbowe."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
