import aiohttp
import asyncio
import os
from dotenv import load_dotenv
from .logger_config import get_logger


load_dotenv()
logger = get_logger(__name__)

RETRIES = int(os.getenv("RETRIES"))
# fetching data from url
async def fetch_api(url, name):
    for attempt in range(1, RETRIES + 1):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()
                    logger.info(f"{name} fetched successfully")
                    return await response.json()
        except Exception as e:
            logger.error(f"{name} failed (Attempt {attempt}): {e}")
            await asyncio.sleep(2)

    raise Exception(f"{name} API failed after retries")
