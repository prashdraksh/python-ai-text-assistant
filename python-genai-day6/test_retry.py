from retry_handler import retry_operation
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

attempts = 0

def api_call():
    raise ConnectionError("API request timed out")

def successful_operation():
    global attempts

    attempts += 1
    if attempts < 3:
        raise ConnectionError("Simulated connection error.")
    return "Success!"
if __name__ == "__main__":
    try:
        result = retry_operation(api_call, max_attempts=3)
    except TimeoutError as exc:
        print("Caught:", exc)
