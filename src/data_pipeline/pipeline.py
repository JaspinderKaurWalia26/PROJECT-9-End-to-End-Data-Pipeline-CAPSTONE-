import asyncio
import os
from .extractor import fetch_api
from .transformer import transform_users,transform_posts
from .loader import save_csv
from .logger_config import get_logger
from dotenv import load_dotenv

load_dotenv()
logger = get_logger(__name__)

# function implementing pipeline
async def run_pipeline():
    users_api = os.getenv("USERS_API")
    posts_api = os.getenv("POSTS_API")
    
    users_data, posts_data = await asyncio.gather(
        fetch_api(users_api, "Users API"),
        fetch_api(posts_api, "Posts API")
    )
    # cleaning/ transforming data
    users_clean = transform_users(users_data)
    posts_clean = transform_posts(posts_data)
    # saving data
    save_csv(users_clean, "data/users.csv", ["id", "name"])
    save_csv(posts_clean, "data/posts.csv", ["id", "title"])

    logger.info("Pipeline executed successfully")
