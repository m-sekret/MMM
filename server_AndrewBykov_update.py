from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

weather_data = {"hryvnia&dollar": 0.0,
		"dollar&euro": 0.0,
		"dollar&pound": 0.0,
		"Gold": 0.0,
		"Platinum": 0.0,
		"Silver": 0.0,
		"Mercury": 0.0,
		"Palladium": 0.0,
		"Copper": 0.0,
		"Intel": 0.0,
		"AMD": 0.0,
                "Nvidia": 0.0,
                "Cocacola": 0.0,
                "Pepsi": 0.0,
                "McDonalds": 0.0,
                "Dollar&Zloty": 0.0,
                "Dollar&YEN": 0.0,
                "Hryvnia&Zloty": 0.0,
                "IBM": 0.0,
                "bayractar": 0.0,
                "cisco": 0.0,
                "Palladium": 0.0,
                "Silber": 0.0,
                "Iridium": 0.0,}
update_sensor = ["hryvnia&dollar", "dollar&euro", "dollar&pound",
                "Gold", "Platinum", "Silver",
                "Mercury", "Palladium", "Copper",
                "Intel", "AMD", "Nvidia",
                "Cocacola", "Pepsi", "McDonalds",
                "Dollar&Zloty", "Dollar&YEN", "Hryvnia&Zloty",
                "IBM", "bayractar", "cisco",
                "Palladium", "Silber", "Iridium"]

@app.route('/update', methods=['POST'])
def update_weather():
	global weather_data
	data = request.json
	for key in update_sensor:
		weather_data[key] = data.get(key, weather_data[key])
	return jsonify({"status": "success"}), 200

@app.route('/current_weather', methods=['GET'])
def get_weather():
	return jsonify(weather_data), 200

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',  port=5000)
