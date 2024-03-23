from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '1bf6c1ee848648d83f06b212e000b0d6'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_info = {
            'city': city,
            'description': data['weather'][0]['description'],
            'temperature': round(data['main']['temp'], 1),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind'].get('speed', None)
        }
        return render_template('weather.html', weather=weather_info)
    else:
        error_msg = "City not found. Please enter a valid city name."
        return render_template('error.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)