from flask import Flask, render_template
import weather_api  # weather_api.py 모듈 임포트
app = Flask(__name__)
@app.route("/")
def index():
    all_weather = weather_api.get_all_cities_weather()
    return render_template("index.html", weathers=all_weather)
if __name__ == "__main__":
    app.run(debug=True)