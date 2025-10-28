from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def wait_for_element(driver, by, value, timeout=15):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

driver = webdriver.Chrome()

try:
    driver.get("https://digitalsatbara.mahabhumi.gov.in/aaplichawdi")
    wait = WebDriverWait(driver, 20)

    # Wait for and interact with radio buttons and dropdowns (same as before)
    radio_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//label[contains(text(),'सातबारा (फेरफार)')]/preceding-sibling::input"
    )))
    radio_button.click()

    # Wait for dropdowns and select options (values to be set based on actual options)
    wait_for_element(driver, By.NAME, 'ddlDist1')
    driver.execute_script("document.getElementsByName('ddlDist1')[0].value = '26';")

    wait_for_element(driver, By.NAME, 'ddlTahsil')
    driver.execute_script("document.getElementsByName('ddlTahsil')[0].value = '11';")

    wait_for_element(driver, By.NAME, 'ddlVillage')
    driver.execute_script("document.getElementsByName('ddlVillage')[0].value = '272600110331040000';")

    # ---- New: Locate captcha image and save it to a local file ----
    try:
        captcha_img = wait.until(EC.presence_of_element_located((By.ID, "myimg")))
        
        # Save the captcha image to the current working directory
        captcha_path = os.path.join(os.getcwd(), "captcha.png")
        captcha_img.screenshot(captcha_path)
        print(f"Captcha image saved to: {captcha_path}")
    except Exception as e:
        print("Error while finding CAPTCHA image:", e)

    # ---- Prompt the user to manually enter the CAPTCHA ----
    captcha_text = input("Please type the CAPTCHA from the saved image and press Enter: ").strip()

    # ---- Enter CAPTCHA solution into the input field ----
    captcha_input = driver.find_element(By.ID, "CaptchaText")  # ID from HTML provided
    captcha_input.clear()  # Clear any existing value
    captcha_input.send_keys(captcha_text)  # Enter the CAPTCHA text

    # ---- Submit the form ----
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Assuming submit button uses this XPath
    submit_button.click()

    print("Form submitted with the CAPTCHA.")

    time.sleep(5)

finally:
    driver.quit()
