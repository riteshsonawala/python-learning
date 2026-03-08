import asyncio

async def fetch_data() -> str:
    await asyncio.sleep(1)
    return "Hello world!"

async def fetch_metadata() -> str:
    await asyncio.sleep(1)
    return "World of many worlds but this one is called Earth and is inhibited by humans !"

async def run_async() -> tuple:
    list_of_responses = await asyncio.gather(fetch_data(), fetch_metadata())
    print("Running async")
    return list_of_responses


if __name__ == "__main__":
    results=asyncio.run(run_async())
    print(results)