from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://siima.in/Voting/"

# Number of iterations for the loop
num_iterations = 10

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the URL
driver.get(url)

# Wait for the page to be fully loaded
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
element = driver.find_element(By.XPATH, "//*[@id='frm_radio_28-0']/label/input[@value='67']")
driver.execute_script("arguments[0].scrollIntoView();", element)

# Validate that a specific element is present
try:
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='frm_radio_28-0']/label/input[@value='67']")))
    print("Page loaded successfully.")
except:
    print("Page did not load successfully.")

for _ in range(num_iterations):
    try:
        # Find and select the radio button
        radio_button = driver.find_element(By.XPATH, "//*[@id='frm_radio_28-0']/label/input[@value='67']")
        radio_button.click()
        
        time.sleep(5)

        # Find and click the button
        button = driver.find_element(By.XPATH, "(//*[@id='frm_form_3_container']/form/input)[13]")
        button.click()

        # Wait for the alert to appear
        time.sleep(5)
        
        # Switch to the alert and accept it
        alert = Alert(driver)
        alert_text = alert.text
        print("Alert Text:", alert_text)
        alert.accept()
        
        print("Iteration completed.")
    
    except Exception as e:
        print("Error:", e)

# Close the browser
    #driver.quit()
