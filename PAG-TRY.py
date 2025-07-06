import pyautogui
import time
import subprocess

# Step 1: Open browser (Example: Chrome)
subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])

# Step 2: Wait for browser to load
time.sleep(5)

# Step 3: Move to the search bar (Adjust your coordinates carefully!)
pyautogui.click(300, 50)  # Example coordinates for search bar

# Step 4: Type search query
pyautogui.write("South Africa vs Australia score", interval=0.1)
pyautogui.press("enter")

# Step 5: Wait for results to load
time.sleep(5)

# Step 6: Click first search result (Adjust these coordinates)
pyautogui.click(400, 300)
