#from flask import Flask, request, jsonify, render_template
import requests
import random
import time

#app = Flask(__name__)
url = 'http://localhost:5000/update'
while True:
    weather_data = {
        "Gold": round(random.uniform(2400, 2500), 2),
        "Platinum": round(random.uniform(857, 957), 2),
        "Silver": round(random.uniform(22, 28), 2),
    }

    response = requests.post(url, json=weather_data)
    print(f"Sent data: {weather_data}, Response: {response.status_code}")
    time.sleep(5)

#@app.route('/update', methods=['POST'])
#def update_weather():
 #   global weather_data
  #  data = request.json
   # weather_data['Gold'] = data.get('Gold', weather_data['Gold'])
#    weather_data['Platinum'] = data.get('Platinum', weather_data['Platinum'])
 #   weather_data['Silver'] = data.get('Silver', weather_data['Silver'])
  #  return jsonify({"status": "success"}), 200

#@app.route('/current_weather', methods=['GET'])
#def get_weather():
 #   return jsonify(weather_data), 200

#@app.route('/')
#def index():
 #   return render_template('index.html')

#if __name__ == '__main__':
 #   app.run(debug=True, host='0.0.0.0', port=5001)
