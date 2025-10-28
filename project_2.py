




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_options(driver, name, minimum=2, timeout=15):
    WebDriverWait(driver, timeout).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, f"select[name='{name}'] option")) >= minimum
    )

def select_dropdown_js(driver, name, value):
    driver.execute_script(f"""
        let select = document.getElementsByName('{name}')[0];
        select.value = '{value}';
        select.dispatchEvent(new Event('change'));
    """)

driver = webdriver.Chrome()

try:
    driver.get("https://digitalsatbara.mahabhumi.gov.in/aaplichawdi")
    wait = WebDriverWait(driver, 20)

    radio_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//label[contains(text(),'सातबारा (फेरफार)')]/preceding-sibling::input"
    )))
    radio_button.click()

    wait_for_options(driver, 'ddlDist1')
    select_dropdown_js(driver, 'ddlDist1', '26')

    wait_for_options(driver, 'ddlTahsil')
    select_dropdown_js(driver, 'ddlTahsil', '11')

    wait_for_options(driver, 'ddlVillage')
    select_dropdown_js(driver, 'ddlVillage', '272600110331040000')

    print("Dropdowns filled successfully!")

    time.sleep(5)

finally:
    driver.quit()
