import pytest
from retry_handler import calculate_backoff
from retry_handler import retry_operation
from test_retry import api_call, successful_operation

def test_first_attempt_backoff():
    result = calculate_backoff(1)
    assert 2 >= result >= 1

def test_second_attempt_backoff():
    result = calculate_backoff(2)
    assert 3 >= result >= 2

def test_invalid_attempt_raises_value_error():
    with pytest.raises(ValueError):
        calculate_backoff(0)

def test_retry_succeeds_after_two_failures(monkeypatch):
    attempts = 0

    monkeypatch.setattr("retry_handler.time.sleep", lambda _: None)

    def unstable_operation():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ConnectionError("Simulated connection error.")
        return "Success!"

    result = retry_operation(unstable_operation, max_attempts=3)

    assert result == "Success!"
    assert attempts == 3

def test_retry_raises_error_after_max_attempts(monkeypatch):
    attempts = 0
    
    monkeypatch.setattr("retry_handler.time.sleep", lambda _: None)
    
    def unstable_operation():
        nonlocal attempts
        attempts += 1
        raise ConnectionError("Simulated connection error.")
    with pytest.raises(ConnectionError):
        retry_operation(unstable_operation, max_attempts=3)
        
    assert attempts == 3       