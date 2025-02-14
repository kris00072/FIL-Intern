import requests


API_URL = "http://127.0.0.1:8000/black/blackholes/"

try:
   
    response = requests.get(API_URL)

   
    if response.status_code == 200:
        blackholes = response.json()  

        blackhole_dict = {bh["Bid"]: bh for bh in blackholes}

    
        print("Black Holes Data (Dictionary Format):")
        print(blackhole_dict)

    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
