from .logger_config import get_logger

logger = get_logger(__name__)

# tranforming data from url fetching only users id and name
def transform_users(users):
    data = [{"id": user["id"], "name": user["name"]} for user in users]
    logger.info("Users data transformed")
    return data
# tranforming data from url fetching only posts id and post title
def transform_posts(posts):
    data = [{"id": post["id"], "title": post["title"]} for post in posts]
    logger.info("Posts data transformed")
    return data
