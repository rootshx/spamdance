# Dance Macro Script for League of Legends

This Python script automates the dance mechanism in League of Legends by pressing **Ctrl + 3** (which triggers the dance action) when the `X2` mouse button is pressed. The script keeps running until you manually stop it, and you can stop the macro by pressing the `.` key.

## Installation

1. **Clone or Download the Repository**:
   - You can clone the repository using Git:
     ```bash
     git clone https://github.com/rootshx/spamdance.git
     ```

   - Or you can download the ZIP file from GitHub and extract it.

2. **Install Python**:
   - Make sure you have Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/).

3. **Install Required Dependencies**:
   The script uses the following Python libraries:
   - `keyboard` for detecting key presses and controlling keyboard input
   - `mouse` for detecting mouse button presses

   To install the dependencies, run:
   ```bash
   pip install keyboard mouse
   ```

## Usage

### Running the Script:
Navigate to the directory where the script is located and run the script using Python:

```bash
python dance.py
```

### How It Works

- When you press the X2 mouse button (usually the side button on a mouse), the script simulates pressing `Ctrl + 3` to trigger the dance action in League of Legends.
- The dance action will repeat as long as you keep pressing the X2 button, and it will stop if you release the button.
- To stop the script, press the `.` key on your keyboard.

## Notes

- Ensure you have the necessary permissions to control the keyboard and mouse input.
- The `X2` button refers to the side mouse button (commonly used for back/forward navigation) on most mice. If the button doesn't work, you may need to configure your mouse's settings or remap the button.
- The script relies on the `keyboard` and `mouse` libraries to simulate key presses and detect mouse events. If you encounter any issues with these libraries, please ensure they are installed and up to date.
