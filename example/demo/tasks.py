from datetime import datetime

from .core import celery, logger, redis_store


@celery.task
def test(value):
    msg = f'celery test({value}) on {datetime.now().isoformat(" ")}'
    logger.error(f"logger error {msg}")
    redis_store.set("test:celery", value, ex=10)
    return msg
