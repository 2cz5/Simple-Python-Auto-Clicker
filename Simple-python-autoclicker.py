# | Made by 2cz5 | https://github.com/2cz5 | Discord:2cz5 (for questions etc..)

import pyautogui
import time
import keyboard
import win32gui
import win32con

# Example coordinates (replace with desired coordinates)
x_coord = 244
y_coord = 422

# Function to minimize the command prompt window
def minimize_cmd_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

# Function to click on specified coordinates with error handling
def click_on_coordinates(x, y):
    try:
        pyautogui.click(x, y)
    except pyautogui.FailSafeException:
        print("FailSafeException: Mouse moved to upper-left corner. Exiting the loop.")
        raise KeyboardInterrupt  # Trigger manual termination of the program

# Main function to control clicking loop
def main():
    minimize_cmd_window()  # Minimize the command prompt window
    running = True
    try:
        while running:
            click_on_coordinates(x_coord, y_coord)
            time.sleep(0.5)  # Adjust the delay between clicks as needed

            # Check if the killswitch key ('q') is pressed
            if keyboard.is_pressed('q'):
                running = False
                print("Killswitch activated. Exiting the loop.")
    except KeyboardInterrupt:
        print("\nProgram manually terminated.")
    finally:
        print("Program exited.")

if __name__ == "__main__":
    main()
