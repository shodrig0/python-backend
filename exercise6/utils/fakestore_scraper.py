import httpx

# Exercise 8

client = httpx.Client(
    headers = {
        "User-Agent": "PriceUpdaterBot/1.0",
        "Accept": "application/json"
    },
    cookies = {
        "session_id": "shodrig0-fake-session"
    }
)

def fakestore_scraper(url: str):
    response = client.get(url)
    response.raise_for_status()
    return response.json()

print("qqqqqqqqqqqqqqqqqqqqqqqq")
print(client.headers)
print("qqqqqqqqqqqqqqqqqqqqqqqq")
print(client.cookies)

# import requests

# def fakestore_scraper(url: str):
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json()