import webbrowser
import time
import datetime
import pyautogui
import pyperclip

# --- 1. Configure ---
# WhatsApp number
phone_number = "+919999999999" #Replace with your number

# Message to send
message = "🎉🎂 Happy Birthday! 🎂🎉\nWishing you an amazing year ahead! 🥳"

# Target date and time (24-hour format)
target_date = datetime.date(2025, 6, 26)
target_hour = 16
target_minute = 30

# --- 2. Wait until target time ---
now = datetime.datetime.now()
target_datetime = datetime.datetime.combine(target_date, datetime.time(target_hour, target_minute))
seconds_to_wait = (target_datetime - now).total_seconds()

if seconds_to_wait <= 0:
    print("❌ The target time is in the past.")
    exit()

print(f"⏳ Waiting until {target_datetime} to send message...")
time.sleep(seconds_to_wait)

# --- 3. Open WhatsApp Web ---
wa_url = f"https://web.whatsapp.com/send?phone={phone_number}"
webbrowser.open(wa_url)
print("🌐 Opening WhatsApp Web...")
time.sleep(15)  # Adjust this if your internet is slow

# --- 4. Copy message to clipboard ---
pyperclip.copy(message)

# --- 5. Send message 5 times ---
for i in range(5):
    pyautogui.hotkey("ctrl", "v")  # Paste
    pyautogui.press("enter")       # Send
    time.sleep(1)                  # Delay between messages

print("✅ Birthday message sent 5 times!")
