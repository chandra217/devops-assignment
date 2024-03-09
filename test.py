import pytest
from calculator import CalculatorApp

@pytest.fixture
def app():
    # Setup
    yield CalculatorApp()
    # Teardown (if needed)

def test_initial_result_value(app):
    assert app.result.value == "0"

def test_button_clicked_reset(app):
    app.result.value = "Error"
    app.button_clicked("AC")
    assert app.result.value == "0"

# Add more test cases as needed
