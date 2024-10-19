# import tkinter as tk
# from tkinter import messagebox, filedialog
# import threading
# import time
# import random
# import pyautogui
# from pynput import mouse, keyboard
# import json
# import utils  # Import the utility functions
#
#
# class MacroRecorder:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Macro Recorder")
#         self.recording = False
#         self.recorded_events = []
#
#         self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
#         self.start_button.pack(pady=10)
#
#         self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
#         self.stop_button.pack(pady=10)
#
#         self.save_button = tk.Button(master, text="Save Macro", command=self.save_macro, state=tk.DISABLED)
#         self.save_button.pack(pady=10)
#
#         self.load_button = tk.Button(master, text="Load Macro", command=self.load_macro)
#         self.load_button.pack(pady=10)
#
#         self.replay_button = tk.Button(master, text="Replay Macro", command=self.replay_macro, state=tk.DISABLED)
#         self.replay_button.pack(pady=10)
#
#     def start_recording(self):
#         self.recorded_events = []
#         self.recording = True
#         self.start_button.config(state=tk.DISABLED)
#         self.stop_button.config(state=tk.NORMAL)
#         self.save_button.config(state=tk.DISABLED)
#         self.replay_button.config(state=tk.DISABLED)
#
#         self.mouse_listener = mouse.Listener(on_click=self.on_click)
#         self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
#
#         self.mouse_listener.start()
#         self.keyboard_listener.start()
#
#     def stop_recording(self):
#         self.recording = False
#         self.mouse_listener.stop()
#         self.keyboard_listener.stop()
#         self.start_button.config(state=tk.NORMAL)
#         self.stop_button.config(state=tk.DISABLED)
#         self.save_button.config(state=tk.NORMAL)
#         self.replay_button.config(state=tk.NORMAL)
#
#     def on_click(self, x, y, button, pressed):
#         if pressed and self.recording:
#             event = ('mouse_click', x, y, button.name)
#             self.recorded_events.append(event)
#
#     def on_key_press(self, key):
#         if self.recording:
#             try:
#                 print(f"Key pressed: {key.char}")  # This will print standard characters
#                 event = ('key_press', key.char)
#             except AttributeError:
#                 print(f"Special key pressed: {key}")  # This will print special keys
#                 event = ('key_press', key.name)
#             self.recorded_events.append(event)
#
#     def save_macro(self):
#         if not self.recorded_events:
#             messagebox.showwarning("No Data", "No recorded events to save.")
#             return
#
#         file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
#         if file_path:
#             utils.save_macro(file_path, self.recorded_events)
#             messagebox.showinfo("Success", "Macro saved successfully!")
#
#     def load_macro(self):
#         file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
#         if file_path:
#             self.recorded_events = utils.load_macro(file_path)
#             messagebox.showinfo("Success", "Macro loaded successfully!")
#             self.replay_button.config(state=tk.NORMAL)
#
#     def replay_macro(self):
#         if not self.recorded_events:
#             messagebox.showwarning("No Data", "No macro loaded to replay.")
#             return
#
#         def replay_events(events):
#             for event in events:
#                 # Introduce random delay to simulate human reaction time
#                 time.sleep(random.uniform(0.1, 0.5))
#
#                 if event[0] == 'mouse_click':
#                     x, y, button = event[1], event[2], event[3]
#                     self.human_like_mouse_move(x, y)
#                     pyautogui.click(button=button)
#
#                 elif event[0] == 'key_press':
#                     key = event[1]
#                     pyautogui.press(key)
#
#         replay_thread = threading.Thread(target=replay_events, args=(self.recorded_events,))
#         replay_thread.start()
#
#     def human_like_mouse_move(self, x, y):
#         current_x, current_y = pyautogui.position()
#         steps = random.randint(10, 30)
#
#         for i in range(steps):
#             intermediate_x = current_x + (x - current_x) * (i + 1) / steps + random.randint(-2, 2)
#             intermediate_y = current_y + (y - current_y) * (i + 1) / steps + random.randint(-2, 2)
#             pyautogui.moveTo(intermediate_x, intermediate_y, duration=0.01)
#             time.sleep(random.uniform(0.01, 0.03))
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MacroRecorder(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import messagebox, filedialog
# import json
# import threading
# import time
# import random
# import pyautogui
# import keyboard  # Import the keyboard library
# from pynput import mouse, keyboard as pynput_keyboard
# import utils  # Import utility functions
#
#
# class MacroRecorder:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Macro Recorder")
#         self.recording = False
#         self.recorded_events = []
#
#         self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
#         self.start_button.pack(pady=10)
#
#         self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
#         self.stop_button.pack(pady=10)
#
#         self.save_button = tk.Button(master, text="Save Macro", command=self.save_macro, state=tk.DISABLED)
#         self.save_button.pack(pady=10)
#
#         self.load_button = tk.Button(master, text="Load Macro", command=self.load_macro)
#         self.load_button.pack(pady=10)
#
#         self.replay_button = tk.Button(master, text="Replay Macro", command=self.replay_macro, state=tk.DISABLED)
#         self.replay_button.pack(pady=10)
#
#     def start_recording(self):
#         self.recorded_events = []
#         self.recording = True
#         self.start_button.config(state=tk.DISABLED)
#         self.stop_button.config(state=tk.NORMAL)
#         self.save_button.config(state=tk.DISABLED)
#         self.replay_button.config(state=tk.DISABLED)
#
#         self.mouse_listener = mouse.Listener(on_click=self.on_click)
#         self.mouse_listener.start()
#
#         # Start the keyboard listener
#         keyboard.hook(self.on_key_press)
#
#     def stop_recording(self):
#         self.recording = False
#         self.mouse_listener.stop()
#         keyboard.unhook_all()  # Unhook the keyboard listener
#         self.start_button.config(state=tk.NORMAL)
#         self.stop_button.config(state=tk.DISABLED)
#         self.save_button.config(state=tk.NORMAL)
#         self.replay_button.config(state=tk.NORMAL)
#
#     def on_click(self, x, y, button, pressed):
#         if pressed and self.recording:
#             event = ('mouse_click', x, y, button.name)
#             self.recorded_events.append(event)
#
#     def on_key_press(self, event):
#         if self.recording:
#             key = event.name
#             if key == 'print screen':  # Handle Print Screen key
#                 key = 'PrtSc'
#                 # Append the event to take a screenshot
#                 self.recorded_events.append(('take_screenshot',))
#             else:
#                 self.recorded_events.append(('key_press', key))
#
#     def save_macro(self):
#         if not self.recorded_events:
#             messagebox.showwarning("No Data", "No recorded events to save.")
#             return
#
#         file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
#         if file_path:
#             utils.save_macro(file_path, self.recorded_events)
#             messagebox.showinfo("Success", "Macro saved successfully!")
#
#     def load_macro(self):
#         file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
#         if file_path:
#             self.recorded_events = utils.load_macro(file_path)
#             messagebox.showinfo("Success", "Macro loaded successfully!")
#             self.replay_button.config(state=tk.NORMAL)
#
#     def replay_macro(self):
#         if not self.recorded_events:
#             messagebox.showwarning("No Data", "No macro loaded to replay.")
#             return
#
#         def replay_events(events):
#             for event in events:
#                 # Introduce random delay to simulate human reaction time
#                 time.sleep(random.uniform(0.1, 0.5))
#
#                 if event[0] == 'mouse_click':
#                     x, y, button = event[1], event[2], event[3]
#                     self.human_like_mouse_move(x, y)
#                     pyautogui.click(button=button)
#
#                 elif event[0] == 'key_press':
#                     key = event[1]
#                     pyautogui.press(key)
#
#                 elif event[0] == 'take_screenshot':  # Handle screenshot event
#                     self.take_screenshot()
#
#         replay_thread = threading.Thread(target=replay_events, args=(self.recorded_events,))
#         replay_thread.start()
#
#     def take_screenshot(self):
#         """Take a screenshot and save it with a timestamp."""
#         timestamp = time.strftime("%Y%m%d-%H%M%S")
#         screenshot_name = f"screenshot_{timestamp}.png"
#         pyautogui.screenshot(screenshot_name, region = (480, 300, 1370, 1380))
#         print(f"Screenshot taken and saved as {screenshot_name}")
#
#     def human_like_mouse_move(self, x, y):
#         current_x, current_y = pyautogui.position()
#         steps = random.randint(10, 30)
#
#         for i in range(steps):
#             intermediate_x = current_x + (x - current_x) * (i + 1) / steps + random.randint(-2, 2)
#             intermediate_y = current_y + (y - current_y) * (i + 1) / steps + random.randint(-2, 2)
#             pyautogui.moveTo(intermediate_x, intermediate_y, duration=0.01)
#             time.sleep(random.uniform(0.01, 0.03))
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MacroRecorder(root)
#     root.mainloop()

import tkinter as tk
from tkinter import messagebox, filedialog
import json
import threading
import time
import random
import pyautogui
import keyboard
from pynput import mouse
import os
import pytesseract
from PIL import Image

class MacroRecorder:
    def __init__(self, master):
        self.master = master
        self.master.title("Macro Recorder")
        self.recording = False
        self.recorded_events = []

        self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.save_button = tk.Button(master, text="Save Macro", command=self.save_macro, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.load_button = tk.Button(master, text="Load Macro", command=self.load_macro)
        self.load_button.pack(pady=10)

        self.replay_button = tk.Button(master, text="Replay Macro", command=self.replay_macro, state=tk.DISABLED)
        self.replay_button.pack(pady=10)

        # Set default screenshot region (adjust as needed)
        self.screenshot_region = (480, 300, 1370, 1380)  # (left, top, width, height)

    def start_recording(self):
        self.recorded_events = []
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.DISABLED)
        self.replay_button.config(state=tk.DISABLED)

        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.mouse_listener.start()

        # Start the keyboard listener
        keyboard.hook(self.on_key_press)

    def stop_recording(self):
        self.recording = False
        self.mouse_listener.stop()
        keyboard.unhook_all()  # Unhook the keyboard listener
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)
        self.replay_button.config(state=tk.NORMAL)

    def on_click(self, x, y, button, pressed):
        if pressed and self.recording:
            event = ('mouse_click', x, y, button.name)
            self.recorded_events.append(event)

    def on_key_press(self, event):
        if self.recording:
            key = event.name
            if key == 'print screen':  # Handle Print Screen key
                key = 'PrtSc'
                # Append the event to take a screenshot
                self.recorded_events.append(('take_screenshot',))
            else:
                self.recorded_events.append(('key_press', key))

    def save_macro(self):
        if not self.recorded_events:
            messagebox.showwarning("No Data", "No recorded events to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(self.recorded_events, f)
            messagebox.showinfo("Success", "Macro saved successfully!")

    def load_macro(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                self.recorded_events = json.load(f)
            messagebox.showinfo("Success", "Macro loaded successfully!")
            self.replay_button.config(state=tk.NORMAL)

    def replay_macro(self):
        if not self.recorded_events:
            messagebox.showwarning("No Data", "No macro loaded to replay.")
            return

        def replay_events(events):
            for event in events:
                # Introduce random delay to simulate human reaction time
                time.sleep(random.uniform(0.1, 0.5))

                if event[0] == 'mouse_click':
                    x, y, button = event[1], event[2], event[3]
                    self.human_like_mouse_move(x, y)
                    pyautogui.click(button=button)

                elif event[0] == 'key_press':
                    key = event[1]
                    pyautogui.press(key)

                elif event[0] == 'take_screenshot':
                    self.scroll_and_capture()

        replay_thread = threading.Thread(target=replay_events, args=(self.recorded_events,))
        replay_thread.start()

    def scroll_and_capture(self):
        """Scroll through the page and take screenshots until the end is detected."""
        scroll_pause_time = 1  # Adjust as needed

        while True:
            self.take_screenshot()
            time.sleep(scroll_pause_time)  # Wait for the page to render after scrolling

            if self.is_end_of_page():
                print("Reached the end of the page.")
                break
            else:
                pyautogui.scroll(-500)  # Scroll down; adjust the value as needed
                time.sleep(0.5)

    def is_end_of_page(self):
        """Check if the end of the page is reached."""
        # Take a small screenshot of the bottom area
        # Adjust the region to the area where the end indicator appears
        region = (self.screenshot_region[0], self.screenshot_region[1] + self.screenshot_region[3] - 100, self.screenshot_region[2], 100)
        screenshot = pyautogui.screenshot(region=region)
        text = pytesseract.image_to_string(screenshot)

        # Check for specific text that indicates the end
        end_indicators = ['End of Content', 'No more results', 'You\'re all caught up']
        for indicator in end_indicators:
            if indicator.lower() in text.lower():
                return True
        return False

    def take_screenshot(self):
        """Take a screenshot and save it with a timestamp."""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"screenshot_{timestamp}.png"
        pyautogui.screenshot(screenshot_name, region=self.screenshot_region)
        print(f"Screenshot taken and saved as {screenshot_name}")
        # Optionally process the screenshot here

    def human_like_mouse_move(self, x, y):
        current_x, current_y = pyautogui.position()
        steps = random.randint(10, 30)

        for i in range(steps):
            intermediate_x = current_x + (x - current_x) * (i + 1) / steps + random.randint(-2, 2)
            intermediate_y = current_y + (y - current_y) * (i + 1) / steps + random.randint(-2, 2)
            pyautogui.moveTo(intermediate_x, intermediate_y, duration=0.01)
            time.sleep(random.uniform(0.01, 0.03))

if __name__ == "__main__":
    root = tk.Tk()
    app = MacroRecorder(root)
    root.mainloop()
