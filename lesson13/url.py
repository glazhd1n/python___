import requests

api_key = 'B1CmKcutpNFpQlVisGnaSACUCblDfs8p'
start_location = '37.773972,-122.431297'  # San Francisco
end_location = '37.774929,-122.419416'  # Golden Gate Bridge

url = f'https://api.tomtom.com/routing/1/calculateRoute/{start_location}:{end_location}/json?key={api_key}'
response = requests.get(url)

if response.status_code == 200:
    # Success! The response content is in JSON format.
    json_response = response.json()
    print(json_response)
else:
    # Something went wrong.
    print(f'Request failed with status code {response.status_code}.')
