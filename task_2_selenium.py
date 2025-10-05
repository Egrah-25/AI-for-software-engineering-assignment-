from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup (Replace with your ChromeDriver path)
driver = webdriver.Chrome()
driver.get("https://example.com/login") # Replace with a test login page

def test_login(username, password, expected_result):
    """Tests a login attempt and checks the result."""
    try:
        # Find elements
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")) # Update selectors
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-btn")

        # Perform login
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

        # Wait for result and check
        time.sleep(2) # Simple wait; better to use WebDriverWait for a specific element
        if expected_result == "success":
            # Check for a logout button or dashboard element
            assert "dashboard" in driver.current_url or driver.find_element(By.ID, "logout")
            print(f"Login Success Test with {username}: PASSED")
        else:
            # Check for an error message
            error_message = driver.find_element(By.CLASS_NAME, "error").text
            assert "invalid" in error_message.lower()
            print(f"Login Failure Test with {username}: PASSED")

    except Exception as e:
        print(f"Test FAILED for {username}: {e}")
    finally:
        # Go back to login page for next test, or clear fields
        driver.get("https://example.com/login")

# Execute test cases
test_login("valid_user", "valid_pass", "success")
test_login("invalid_user", "wrong_pass", "failure")
test_login("", "", "failure")

# Close the browser
driver.quit()
