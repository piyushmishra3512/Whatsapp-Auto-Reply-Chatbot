import pyautogui
import time
import pyperclip
import google.generativeai as genai
import sys
API_KEY="AIzaSyC-_4G97Nfw_5ZKSH8ru1ezYVcToBqye8Y"
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel('gemini-2.0-flash')

chat = model.start_chat(history=[])

def is_last_message_from_sender(chat_log, sender_name="Ritik AIML "):
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Coordinates
click_x, click_y = 1258, 1059 
drag_start_x, drag_start_y = 681, 222  
drag_end_x, drag_end_y = 1916, 1072  

# Step 1: Small delay to give you time to switch window
time.sleep(2)

# Step 2: Click at (a, b)
pyautogui.click(click_x, click_y)
time.sleep(0.5)
while True:
# Step 3: Drag to select text
    pyautogui.moveTo(drag_start_x, drag_start_y)
    pyautogui.dragTo(drag_end_x, drag_end_y, duration=0.5, button='left')
    time.sleep(0.5)

    # Step 4: Press Ctrl+C to copy
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(681, 222 )
    time.sleep(0.5)

    # Step 5: Get text from clipboard
    chat_history = pyperclip.paste()

    print("Copied Text:")
    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
        # Prepare the prompt
        prompt = (
            "You are a person named Piyush who speaks Hindi .\n"
            "He is from  India and a btech first year undergradyuate, who loves coding , talking with friends, cricket and always enjoying with friends.\n"
            "You analyze chat history and roast people in a funny way.\n"
            "Rules: Output should be the next chat response (text message only).\n"
            "Do not start like this: [21:02, 12/6/2024] Rohan Das:\n\n"
            f"Chat history:\n{chat_history}\n"
        )

        # Send to Gemini
        response = chat.send_message(prompt)
        generated_text = response.text

        # Copy response to clipboard
        pyperclip.copy(generated_text)

        # Click on the input box
        pyautogui.click(838, 554)
        time.sleep(1)

        # Paste and send
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
    else:
        no_message_counter += 1
        print(f"No message from {30*no_message_counter} seconds.")

    if no_message_counter >= 2:  # After two checks (30 sec each), exit
        print("No new messages detected. Exiting program in 5 seconds...")
        time.sleep(5)
        sys.exit()
        