# Countdown Timer Script for OBS ⏰

This script creates a countdown timer in OBS using the Text (GDI+) source. It allows you to set a timer, start, and stop it during your stream or recording. The timer is displayed as text in the current scene, and you can customize it via script properties.

## Requirements ⚙️

- **OBS Studio** (v27.0 or higher)
- **Python** (v3.8 or higher) with `obspython` support

## Installation 📥

1. **Download the Script**  
   Download the script file (`countdown_timer.py`) and save it to your local system.

2. **Add the Script to OBS**  
   - Open **OBS Studio**.
   - Go to the **Tools** menu and select **Scripts**.
   - Click the **+** button in the "Script Manager" window.
   - Navigate to the location where you saved the script and select it.

3. **Configure the Timer**  
   Once the script is loaded, you can configure the countdown timer:

   - **Create Text Source**: Creates a new text source to display the countdown timer.
   - **Minutes**: Set the number of minutes for the countdown.
   - **Seconds**: Set the number of seconds for the countdown.
   - **Set Timer**: Updates the countdown timer.
   - **Start**: Starts the countdown timer.
   - **Stop**: Stops the countdown timer.

## How to Use the Script 🖥️

### 1. Setting Up the Timer

- In the **Script Properties** panel, set the desired **Minutes** and **Seconds** for your countdown timer.
- Click the **Set Timer** button to save your settings.

### 2. Starting the Timer

- Click the **Start** button to begin the countdown. The timer will display the time remaining in **"MM:SS"** format.
- The countdown will decrease by one second every second.

### 3. Stopping the Timer

- If you wish to stop the timer at any time, click the **Stop** button. The countdown will freeze at the current time.

### 4. Text Source Customization

- The script automatically creates a text source named **"Countdown Timer"** to display the countdown. You can modify the text properties (font, size, color) using OBS's built-in text settings.

## Script Features

- **Live Countdown**: The timer updates in real-time.
- **Customizable Time**: Set the countdown time dynamically.
- **Simple Controls**: Start, stop, and set the timer with the press of a button.
- **Automatic Source Creation**: The script automatically creates the text source if it doesn't exist.

## Troubleshooting

- If the countdown source is not appearing in the scene, make sure the **Create Text** button is pressed.
- If the timer is not updating, check the script settings to ensure the correct timer is set.

---

For more information and support, visit the [OBS Forum](https://obsproject.com/forum/) or the [OBS Discord](https://discord.gg/obsproject).
