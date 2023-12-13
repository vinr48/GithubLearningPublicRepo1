import requests

def get_data():
    # Replace 'your_dummy_api_key' with your actual API key
    api_key = '5e118ae6-pdup-3796-qlxu-888bdcf1cc2d'
    api_url = f'https://api.example.com/data?key={5e118ae6-pdup-3796-qlxu-888bdcf1cc2d}'

    try:
        # Make a request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            print("Received data:", data)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to test
get_data()
