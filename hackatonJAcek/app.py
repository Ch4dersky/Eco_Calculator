from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Pobieramy dane z formularza
            km = float(request.form.get("km", 0))
            fuel_efficiency = float(request.form.get("fuel_efficiency", 0))
            passengers = int(request.form.get("passengers", 1))
            energy = float(request.form.get("energy", 0))
            home_energy = float(request.form.get("home_energy", 0))

            # Obliczanie emisji CO2
            co2_km = (km * fuel_efficiency * 2.31) / passengers  # 2.31 kg CO2 na litr paliwa
            co2_energy = energy * 0.5  # 500 g CO2 na kWh
            co2_home_energy = home_energy * 0.4  # 400 g CO2 na kWh energii domowej
            result = co2_km + co2_energy + co2_home_energy
        except ValueError:
            result = "Proszę wprowadzić poprawne wartości liczbowe."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
