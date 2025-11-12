# part2_task2_testing/run_test.py
# This is the new, more reliable test script.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# We are adding these new libraries for "Explicit Waits"
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_login_test():
    print("Starting test...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Set a maximum wait time of 10 seconds
    wait = WebDriverWait(driver, 10)
    
    try:
        # 1. Open the login page
        driver.get("https://the-internet.herokuapp.com/login")
        
        # 2. Wait for the username field to be visible, then type
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username_field.send_keys("tomsmith")
        
        # 3. Find the password field and type
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        
        # 4. Find the login button using a more specific selector and click
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # 5. Wait until an element with ID "flash" is visible
        success_message_element = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        
        # 6. Check the message text
        success_message_text = success_message_element.text
        
        # --- THIS IS THE FIXED LINE ---
        if "You logged into a secure area!" in success_message_text:
            print("\n----------------------------------")
            print("   TEST PASSED: Login was successful.")
            print("----------------------------------")
        else:
            # This will catch if it finds the RED error banner
            print(f"\nTEST FAILED: Found a banner, but it wasn't the success message. Message was: {success_message_text}")
            
    except Exception as e:
        # This will catch if it times out (can't find the 'flash' element at all)
        print(f"\nTEST FAILED: An error occurred (e.g., element not found or timed out): {e}")
        
    finally:
        # 7. Close the browser window
        driver.quit()
        print("Test finished and browser closed.")

if __name__ == "__main__":
    run_login_test()