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

@app.route('/update', methods=['POST'])
def update_weather():
	global weather_data
	data = request.json
	weather_data['hryvnia&dollar'] = data.get('hryvnia&dollar', weather_data['hryvnia&dollar'])
	weather_data['dollar&euro'] = data.get('dollar&euro', weather_data['dollar&euro'])
	weather_data['dollar&pound'] = data.get('dollar&pound', weather_data['dollar&pound'])
        weather_data['Gold'] = data.get('Gold', weather_data['Gold'])
        weather_data['Platinum'] = data.get('Platinum', weather_data['Platinum'])
        weather_data['Silver'] = data.get('Silver', weather_data['Silver'])
        weather_data['Mercury'] = data.get('Mercury', weather_data['Mercury'])
        weather_data['Palladium'] = data.get('Palladium', weather_data['Palladium'])
        weather_data['Copper'] = data.get('Copper', weather_data['Copper'])
        weather_data['Intel'] = data.get('Intel', weather_data['Intel'])
        weather_data['AMD'] = data.get('AMD', weather_data['AMD'])
        weather_data['Nvidia'] = data.get('Nvidia', weather_data['Nvidia'])
        weather_data['Cocacola'] = data.get('Cocacola', weather_data['Cocacola'])
        weather_data['Pepsi'] = data.get('Pepsi', weather_data['Pepsi'])
        weather_data['McDonalds'] = data.get('McDonalds', weather_data['McDonalds'])
        weather_data['Dollar&Zloty'] = data.get('Dollar&Zloty', weather_data['Dollar&Zloty'])
        weather_data['Dollar&YEN'] = data.get('Dollar&YEN', weather_data['Dollar&YEN'])
        weather_data['Hryvnia&Zloty'] = data.get('Hryvnia&Zloty', weather_data['Hryvnia&Zloty'])
        weather_data['IBM'] = data.get('IBM', weather_data['IBM'])
        weather_data['bayractar'] = data.get('bayractar', weather_data['bayractar'])
        weather_data['cisco'] = data.get('cisco', weather_data['cisco'])
        weather_data['Palladium'] = data.get('Palladium', weather_data['Palladium'])
        weather_data['Silber'] = data.get('Silber', weather_data['Silber'])
        weather_data['Iridium'] = data.get('Iridium', weather_data['Iridium'])
	return jsonify({"status": "success"}), 200

@app.route('/current_weather', methods=['GET'])
def get_weather():
	return jsonify(weather_data), 200

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',  port=5000)
