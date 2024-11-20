import obspython as obs
import json

# Global variable initialization
G = lambda: ...
G.settings = None
G.countdown_time = 0
G.last_tick_time = 0
G.timer_active = False
G.source_name = "Countdown Timer"

# Script description
def script_description():
    return "Countdown Timer"

# Script properties (user interface for settings in OBS)
def script_properties():
    props = obs.obs_properties_create()
    
    obs.obs_properties_add_button(props, "create_text", "Create Text", create_text_source)
    obs.obs_properties_add_int(props, "minutes_input", "Minutes", 0, 59, 1)
    obs.obs_properties_add_int(props, "seconds_input", "Seconds", 0, 59, 1)
    obs.obs_properties_add_button(props, "set_button", "Set Timer", set_timer)
    obs.obs_properties_add_button(props, "start_button", "Start", start_timer)
    obs.obs_properties_add_button(props, "stop_button", "Stop", stop_timer)

    return props

# Script load function to initialize settings
def script_load(settings):
    G.settings = settings
    G.timer_active = False
    print("Script loaded successfully!")

# Function to create the countdown text source
def create_text_source(props, pressed):
    countdown_source = obs.obs_get_source_by_name(G.source_name)

    if countdown_source is None:
        # Create the text source with initial settings
        font = {"face": "Arial", "size": 72, "style": "bold"}
        color = 0xFFFFFFFF
        text_settings_json = {"text": convert_seconds_to_minute_mix_second(G.countdown_time), "font": font, "color": color}
        countdown_source = obs.obs_source_create("text_gdiplus", G.source_name, obs.obs_data_create_from_json(json.dumps(text_settings_json)), None)
        
        # Create and add the text source to the current active scene
        current_scene_source  = obs.obs_frontend_get_current_scene()
        scene = obs.obs_scene_from_source(current_scene_source)
        obs.obs_scene_add(scene, countdown_source)
        print(f"[LOG] Countdown source created and added to scene.")

    else:
        print(f"[LOG] Source '{G.source_name}' already exists.")

    obs.obs_source_release(countdown_source)

# Function to set the timer based on user input
def set_timer(props, pressed):
    minutes = get_minutes_input()
    seconds = get_seconds_input()
    G.countdown_time = minutes * 60 + seconds
    update_text_source()
    print(f"[LOG] Timer set to {minutes} minutes and {seconds} seconds.")

# Function to start the timer
def start_timer(props, pressed):
    if not G.timer_active:
        G.timer_active = True
        obs.timer_add(secound_tick, 1000) # Update every second
        print("[LOG] Timer started.")

# Function to stop the timer
def stop_timer(props, pressed):
    if G.timer_active:
        G.timer_active = False
        obs.timer_remove(secound_tick) # Stop the timer update
        print("[LOG] Timer stopped.")


def script_tick(seconds):
    pass

# The function that is triggered every second to update the countdown
def secound_tick():
    if G.timer_active:
        if G.countdown_time > 0:
            G.countdown_time -= 1
            update_text_source()
        elif G.countdown_time <= 0:
            G.timer_active = False
            obs.timer_remove(secound_tick) # Stop the timer when it reaches 0
            print("[LOG] Timer stopped.")

# =======================================================
# Utility functions

# Convert seconds into "minutes:seconds" format
def convert_seconds_to_minute_mix_second(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02d}"

# Update the text source with the current countdown time
def update_text_source():
    if G.countdown_time < 0:
        return

    time_str = convert_seconds_to_minute_mix_second(G.countdown_time)
    countdown_source = obs.obs_get_source_by_name(G.source_name)

    if countdown_source is not None:
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", time_str)
        obs.obs_source_update(countdown_source, settings)
        obs.obs_data_release(settings)

    obs.obs_source_release(countdown_source)

# Get the minute input from the script properties
def get_minutes_input():
    return obs.obs_data_get_int(G.settings, "minutes_input")

# Get the second input from the script properties
def get_seconds_input():
    return obs.obs_data_get_int(G.settings, "seconds_input")