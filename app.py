from flask import Flask, request
import requests

app = Flask(__name__)

# Set the API endpoint and API key
API_ENDPOINT = 'http://api.ipstack.com/'
API_KEY = '9b4575a107a8e9105b3f4c1a09b95d6e'

@app.route('/get_country_name')
def get_country_name():
    # Get the IP address from the 'ip_address' parameter in the request
    ip_address = request.args.get('ip_address', '8.8.8.8')

    # Make a request to the ipstack API to get the country name
    response = requests.get(f'{API_ENDPOINT}{ip_address}?access_key={API_KEY}')
    if response.status_code == 200:
        country_name = response.json().get('country_name')
    else:
        country_name = 'Unknown'

    return country_name

if __name__ == '__main__':
    app.run()