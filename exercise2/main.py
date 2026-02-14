import asyncio
import time
from request import async_requests_all, sync_requests

api_url = "https://698fefe4dcc9a4df204b958f.mockapi.io/api/Overwatch/"
hero_key = ["ana", "anran", "ashe", "baptiste", "domina", "doomfist", "dva", "echo", "emre", "freja"]

print("Async requests:")
request_start = time.time()
req_result = asyncio.run(async_requests_all([api_url + herok for herok in hero_key]))
request_end = time.time()
print(f"Time: {request_end - request_start}") # 1.128697156906128
print("===========")

print("Sync requests:")
req_start = time.time()
for hk in hero_key:
    url = api_url + hk
    sync_requests(url)
req_end = time.time()
print(f"Time: {req_end - req_start}") # Time: 5.461224555969238
