import time

max_retries = 4

for attempt in range(1, max_retries + 1):

    wait_time = 2 ** (attempt - 1)

    print(f"Attempt {attempt}")
    print(f"Waiting {wait_time} seconds before retry")

    time.sleep(wait_time)