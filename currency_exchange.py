import requests

def get_usd_to_uah_ratio():
    url = "https://api.minfin.com.ua/mb/latest/53fca59fbb52062d53fb18ba9a6af95f325e0433/?currency=usd"
    try:
        response = requests.get(url)
        data = response.json()
        ratio = data['usd']
        return ratio
    except Exception as e:
        print("Error fetching data:", e)
        return None

def send_to_google_analytics(ratio):
    # Replace 'your_measurement_id' with your actual Google Analytics Measurement ID
    measurement_id = 'G-ZKWYKME4ZD'
    url = f"https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}"
    payload = {
        "client_id": "currency exchange tracker",
        "events": [
            {
                "name": "currency_conversion",
                "params": {
                    "currency_to": "UAH",
                    "currency_from": "USD",
                    "ratio": ratio
                }
            }
        ]
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Data sent to Google Analytics successfully")
        else:
            print("Failed to send data to Google Analytics. Status code:", response.status_code)
    except Exception as e:
        print("Error sending data to Google Analytics:", e)

if __name__ == "__main__":
    ratio = get_usd_to_uah_ratio()
    if ratio is not None:
        send_to_google_analytics(ratio)
