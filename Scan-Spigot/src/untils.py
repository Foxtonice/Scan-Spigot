import json
import os
from datetime import datetime

def load_config(config_file="config.json"):
    """Load configuration from file"""
    default_config = {
        "delay": 1,
        "delay_between_accounts": 2,
        "max_pages": 10,
        "timeout": 30
    }
    
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as f:
                user_config = json.load(f)
            default_config.update(user_config)
            print("✅ Configuration loaded")
        except Exception as e:
            print(f"⚠️ Error loading config, using defaults: {e}")
    
    return default_config

def save_config(config, config_file="config.json"):
    """Save configuration to file"""
    try:
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        print("✅ Configuration saved")
    except Exception as e:
        print(f"❌ Error saving config: {e}")

def display_help():
    """Display help information"""
    print("""
🎯 SpigotMC Account Scanner - Help

Commands:
  scan          - Scan all accounts in accounts.txt
  add <user>    - Add account to scan list
  remove <user> - Remove account from scan list
  list          - List all accounts
  config        - Show current configuration
  help          - Show this help message
  exit          - Exit the program

Usage:
  1. Add SpigotMC usernames to accounts/accounts.txt
  2. Run 'scan' to start scanning
  3. Check results in results/ folder

Note: This tool only scans publicly available information.
""")