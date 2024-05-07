# AutoClicker

### Description:
This Python script automates mouse clicks at specified coordinates on the screen. It's particularly useful for repetitive tasks or automation purposes.

### Features:
- **Customizable Coordinates:** You can specify the exact coordinates where you want the clicks to occur by modifying the `x_coord` and `y_coord` variables in the script.
- **Error Handling:** The script includes error handling to deal with scenarios where the mouse cursor moves to the upper-left corner of the screen, triggering a `FailSafeException`.
- **Killswitch:** You can terminate the script at any time by pressing the 'q' key on your keyboard.

### Requirements:
- Python 3.x
- pyautogui
- keyboard
- win32gui
- win32con

### Installation:
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install the required libraries using pip: pip install pyautogui keyboard pywin32

### Usage:
1. Clone the repository:git clone https://github.com/2cz5/AutoClicker.git
2. Navigate to the directory
3. Edit the `x_coord` and `y_coord` variables in the `autoclicker.py` script to set the desired click coordinates.
4. Run the script:python autoclicker.py (Or double click)

### Contributing:
Contributions are welcome! Feel free to open an issue or submit a pull request.

### Author:
Made by [2cz5](https://github.com/2cz5). For any questions or suggestions, you can reach out to me on Discord:2cz5




