from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import requests
import io
import cv2
import numpy as np
import re

# Set Tesseract path (required on Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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

def preprocess_image(image):
    """
    Advanced preprocessing for CAPTCHA images with multiple techniques
    """
    # Convert to grayscale
    gray_image = image.convert('L')
    
    # Convert PIL Image to numpy array for OpenCV processing
    img_array = np.array(gray_image)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(img_array, (3, 3), 0)
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                  cv2.THRESH_BINARY, 11, 2)
    
    # Apply morphological operations to remove noise
    kernel = np.ones((2, 2), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel)
    
    # Convert back to PIL Image
    processed_img = Image.fromarray(cleaned)
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(processed_img)
    enhanced_image = enhancer.enhance(3.0)
    
    # Sharpen the image
    sharpener = ImageEnhance.Sharpness(enhanced_image)
    sharpened_image = sharpener.enhance(2.0)
    
    return sharpened_image

def solve_captcha_advanced(driver, img_url, max_attempts=3):
    """
    Advanced CAPTCHA solving with multiple techniques and validation
    """
    response = requests.get(img_url)
    img = Image.open(io.BytesIO(response.content))
    
    best_result = ""
    best_confidence = 0
    
    # Try multiple preprocessing and OCR configurations
    for attempt in range(max_attempts):
        try:
            # Preprocess with different parameters
            if attempt == 0:
                processed_img = preprocess_image(img)
                config = '--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789'
            elif attempt == 1:
                # Different preprocessing for second attempt
                gray_img = img.convert('L')
                processed_img = gray_img.point(lambda p: 255 if p > 180 else 0)
                config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789'
            else:
                # Third attempt with different approach
                processed_img = img.convert('L')
                enhancer = ImageEnhance.Contrast(processed_img)
                processed_img = enhancer.enhance(4.0)
                config = '--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789'
            
            # Use Tesseract with detailed output for confidence scoring
            data = pytesseract.image_to_data(processed_img, config=config, output_type=pytesseract.Output.DICT)
            
            # Extract text with confidence scores
            captcha_digits = []
            confidences = []
            
            for i in range(len(data['text'])):
                if int(data['conf'][i]) > 30:  # Minimum confidence threshold
                    text = data['text'][i].strip()
                    if text.isdigit() and len(text) == 1:
                        captcha_digits.append(text)
                        confidences.append(int(data['conf'][i]))
            
            if captcha_digits:
                current_text = ''.join(captcha_digits)
                current_confidence = sum(confidences) / len(confidences) if confidences else 0
                
                # Keep the result with highest average confidence
                if current_confidence > best_confidence:
                    best_result = current_text
                    best_confidence = current_confidence
                    
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            continue
    
    # Validate the result
    if best_result and 4 <= len(best_result) <= 6:  # Typical CAPTCHA length
        print(f"CAPTCHA solved with confidence: {best_confidence:.1f}%")
        return best_result
    else:
        # Fallback to basic method
        return solve_captcha_basic(img)

def solve_captcha_basic(image):
    """Basic fallback method"""
    processed_img = image.convert('L')
    text = pytesseract.image_to_string(processed_img, config='--psm 6 --oem 3').strip()
    digits = re.findall(r'\d+', text)
    return ''.join(digits) if digits else ""

def solve_captcha_with_retry(driver, img_url, max_retries=5):
    """
    Solve CAPTCHA with automatic retry and validation
    """
    for retry in range(max_retries):
        try:
            captcha_text = solve_captcha_advanced(driver, img_url)
            
            if captcha_text and 4 <= len(captcha_text) <= 6:
                print(f"Attempt {retry + 1}: Detected CAPTCHA: {captcha_text}")
                return captcha_text
            else:
                print(f"Attempt {retry + 1}: Invalid CAPTCHA format, retrying...")
                time.sleep(1)
                
        except Exception as e:
            print(f"Attempt {retry + 1} failed with error: {e}")
            time.sleep(1)
    
    return ""

def save_captcha_image_for_analysis(img, filename_prefix):
    """Save CAPTCHA images for manual analysis and improvement"""
    timestamp = int(time.time())
    img.save(f"{filename_prefix}_{timestamp}.png")
    print(f"CAPTCHA image saved for analysis: {filename_prefix}_{timestamp}.png")

driver = webdriver.Chrome()

try:
    driver.get("https://digitalsatbara.mahabhumi.gov.in/aaplichawdi")
    wait = WebDriverWait(driver, 20)

    # Select the radio button
    radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'सातबारा (फेरफार)')]/preceding-sibling::input")))
    radio_button.click()

    # Fill dropdowns
    wait_for_options(driver, 'ddlDist1')
    select_dropdown_js(driver, 'ddlDist1', '26')

    wait_for_options(driver, 'ddlTahsil')
    select_dropdown_js(driver, 'ddlTahsil', '11')

    wait_for_options(driver, 'ddlVillage')
    select_dropdown_js(driver, 'ddlVillage', '272600110331040000')

    print("Dropdowns filled successfully!")
    time.sleep(2)

    # Get CAPTCHA image URL
    captcha_img = wait.until(EC.presence_of_element_located((By.ID, "myimg")))
    img_url = captcha_img.get_attribute("src")

    if img_url.startswith("/"):
        img_url = "https://digitalsatbara.mahabhumi.gov.in" + img_url

    print(f"CAPTCHA image URL: {img_url}")

    # Download and save CAPTCHA for analysis
    response = requests.get(img_url)
    original_img = Image.open(io.BytesIO(response.content))
    save_captcha_image_for_analysis(original_img, "original_captcha")

    captcha_text = solve_captcha_with_retry(driver, img_url)

    if captcha_text and len(captcha_text) >= 4:
        print(f"Final CAPTCHA result: {captcha_text}")

        captcha_input = wait.until(EC.element_to_be_clickable((By.ID, "CaptchaText")))
        captcha_input.clear()
        
        # Type slowly to mimic human behavior
        for char in captcha_text:
            captcha_input.send_keys(char)
            time.sleep(0.1)
        
        print("CAPTCHA filled successfully!")
        
        # Optional: Add verification step here
        # You can add code to verify if CAPTCHA was accepted
        
    else:
        print("Failed to detect valid CAPTCHA after multiple attempts.")
        print("Consider manual intervention or using a CAPTCHA solving service")

    time.sleep(10)

finally:
    driver.quit()