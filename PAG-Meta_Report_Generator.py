import pyautogui
import subprocess
import time

# STEP 1: Open Chrome
subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
time.sleep(5)  # Wait for Chrome to launch

# STEP 2: Auto-click on the desired Chrome Profile
pyautogui.click(871, 660)  # Example: Profile icon coordinates (adjust manually)
time.sleep(5)  # Wait for Chrome to open with selected profile

# STEP 3: Open Ads Manager URL
pyautogui.write("https://adsmanager.facebook.com/adsmanager/manage/", interval=0.1)
pyautogui.press("enter")
time.sleep(10)  # Wait for Ads Manager to fully load

# STEP 4: Click Ad Account Drop-down (Next to Campaigns)
pyautogui.click(454, 152)  # Example: Drop-down button position (adjust manually)
time.sleep(3)  # Wait for dropdown to open

# STEP 5: Scroll down to find "sandy.physio" (adjust scroll as needed)
pyautogui.moveTo(406, 383)  # Adjust inside dropdown
time.sleep(1)
pyautogui.scroll(-370)  # Negative scrolls down
time.sleep(2)

# STEP 6: Click "sandy.physio" (after scrolling, adjust position carefully)
pyautogui.click(324, 700)  # Example: sandy.physio position after scroll (adjust manually)
time.sleep(2)

# STEP 7: Click "Telephysio" under sandy.physio
pyautogui.click(609, 369)  # Example: Telephysio account position (adjust manually)
time.sleep(5)  # Wait for the account to load

# STEP 2: Auto-click on report 
pyautogui.click(1233, 341)  # Example: Profile icon coordinates (adjust manually)
time.sleep(5)  # Wait for report to be clicked

# STEP 4: Click on create new report
pyautogui.click(1095, 436)  # Example:  button position (adjust manually)
time.sleep(7)  # Wait report page to open

# STEP 4: Click on export button
pyautogui.click(1749, 156)  # Example:  button position (adjust manually)
time.sleep(3)  # Wait to export dialog box opens

# STEP 4: Click on export 
pyautogui.click(1212, 654)  # Example:  button position (adjust manually)
time.sleep(3)  # report got downloaded

print("✅ Task Completed Successfully!")

