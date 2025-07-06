from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Setup Chrome options: No password popup, fresh session
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Use incognito (No saved passwords or popups)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

# ✅ Launch browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# ✅ Step 1: Visit SauceDemo
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# ✅ Step 2: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# ✅ Step 3: Wait for sorting dropdown and select "Price (low to high)"
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
)
sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
sort_dropdown.select_by_visible_text("Price (low to high)")
time.sleep(2)

# ✅ Step 4: Add first product to cart
driver.find_element(By.CLASS_NAME, "btn_inventory").click()
time.sleep(2)

# ✅ Step 5: Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# ✅ Step 6: Wait for and click checkout
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "checkout"))
).click()
time.sleep(2)

# ✅ Step 7: Enter checkout info
driver.find_element(By.ID, "first-name").send_keys("Rizwana")
driver.find_element(By.ID, "last-name").send_keys("Hussain")
driver.find_element(By.ID, "postal-code").send_keys("600001")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# ✅ Step 8: Finish purchase
driver.find_element(By.ID, "finish").click()
time.sleep(2)

print("✅ Automation Completed Successfully (Full Order Flow)")

# ✅ Quit browser
time.sleep(2)
driver.quit()
