from aiohttp import ClientSession


async def search():
    async with ClientSession(base_url='https://nominatim.openstreetmap.org') as session:
        response = await session.get(url='/search', params={'city': 'минск', 'street': '143 богдановича', 'format': 'json'})
        print(await response.json())


async def reverse():
    async with ClientSession(base_url='https://nominatim.openstreetmap.org') as session:
        response = await session.get(url='/reverse', params={'lat': 53.925440449999996, 'lon': 27.57040906747597, 'format': 'json'})
        print(await response.json())



async def wss():
    async with ClientSession() as session:
        async with session.ws_connect('ws://localhost:8000/ws') as ws:
            async for msg in ws:
                print(msg)


import asyncio
asyncio.run(wss())
