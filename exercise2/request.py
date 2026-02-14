import httpx
import asyncio

async def async_requests(req):
    async with httpx.AsyncClient() as client:
        res = await client.get(req)
        print(res.status_code)


async def async_requests_all(urls):
    return await asyncio.gather(*[async_requests(url) for url in urls])

def sync_requests(req):
    res = httpx.get(req)
    print(res.status_code)