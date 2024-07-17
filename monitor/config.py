import os
import json

CONFIG_FILE = os.path.expanduser("~/.downloads_monitor_config.json")

DEFAULT_CONFIG = {
    "download_folder": os.path.expanduser("~/Downloads")
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return DEFAULT_CONFIG

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def get_config():
    config = load_config()
    save_config(config)     # Ensure the config file exists and is updated with default values
    return config
