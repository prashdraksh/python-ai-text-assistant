
import time
import random
import logging

logger = logging.getLogger(__name__)

def calculate_backoff(attempt):
    if attempt <= 0:
        raise ValueError("Attempt must be positive.")

    base_delay = 2 ** (attempt - 1)
    jitter = random.uniform(0, 1)

    return base_delay + jitter


def retry_operation(operation, max_attempts=3):
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    for attempt in range(1, max_attempts + 1):

        try:
            return operation()

        except (ConnectionError, TimeoutError) as exc:
            logger.warning("Attempt %s failed: %s", attempt, exc)

            if attempt == max_attempts:
                raise

            wait_time = calculate_backoff(attempt)

            logger.info("Retrying in %.2f seconds", wait_time)
            time.sleep(wait_time)
