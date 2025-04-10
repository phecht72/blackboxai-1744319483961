"""
Configuration module for the Retro Clock application.
Handles default settings and user preferences.
"""

import json
import os
from typing import Dict, Any

# Default configuration
DEFAULT_CONFIG = {
    "appearance": {
        "background_color": "black",
        "text_color": "lime",
        "font_family": "Courier New",
        "font_size": 48,
        "relief_style": "ridge"
    },
    "clock": {
        "time_format": "24h",  # '24h' or '12h'
        "show_date": True,
        "date_format": "%Y-%m-%d"
    },
    "window": {
        "title": "Reloj Retro 1980's",
        "width": 800,
        "height": 400,
        "resizable": True
    }
}

CONFIG_FILE = "clock_settings.json"

def load_config() -> Dict[str, Any]:
    """Load configuration from file or create with defaults if not exists."""
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        return DEFAULT_CONFIG
    except Exception as e:
        print(f"Error loading config: {e}")
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any]) -> bool:
    """Save configuration to file."""
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False

def update_config(section: str, key: str, value: Any) -> bool:
    """Update a specific configuration value."""
    try:
        config = load_config()
        if section in config and key in config[section]:
            config[section][key] = value
            return save_config(config)
        return False
    except Exception as e:
        print(f"Error updating config: {e}")
        return False

# Initialize configuration on module import
current_config = load_config()
