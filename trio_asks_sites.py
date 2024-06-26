import time
import asks
import trio


asks.init('trio')

urls = [
    'http://www.badtaxidermy.com/',
    'https://www.google.com/',
    'https://www.ranker.com/list/bad-taxidermy-pictures/ashley-reign',
]

async def get_one(url, t1):
    r = await asks.get(url)
    t2 = time.time()
    print(f"{(t2-t1):.04}\t{len(r.content)}\t{url}")

async def get_sites(sites):
    t1 = time.time()
    async with trio.open_nursery() as nursery:
        for url in sites:
            nursery.start_soon(get_one, url, t1)

if __name__ == '__main__':
    print('seconds\tbytes\turl')
    trio.run(get_sites, urls)