from retry_handler import calculate_backoff

for attempt in range(1, 5):
    print(attempt, calculate_backoff(attempt))