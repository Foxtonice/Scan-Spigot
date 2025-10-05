import json
import os
from datetime import datetime

class AccountManager:
    def __init__(self, accounts_file="accounts/accounts.txt"):
        self.accounts_file = accounts_file
        self.ensure_accounts_file()
    
    def ensure_accounts_file(self):
        """Ensure accounts file exists"""
        os.makedirs(os.path.dirname(self.accounts_file), exist_ok=True)
        if not os.path.exists(self.accounts_file):
            with open(self.accounts_file, 'w', encoding='utf-8') as f:
                f.write("# Add SpigotMC usernames here (one per line)\n")
                f.write("# Example:\n")
                f.write("# Notch\n")
                f.write("# Jeb\n")
                f.write("# Dinnerbone\n")
    
    def add_account(self, username):
        """Add account to list"""
        with open(self.accounts_file, 'r+', encoding='utf-8') as f:
            accounts = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            if username in accounts:
                print(f"⚠️ Account '{username}' already exists")
                return False
            
            f.write(f"{username}\n")
            print(f"✅ Added account: {username}")
            return True
    
    def remove_account(self, username):
        """Remove account from list"""
        with open(self.accounts_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(self.accounts_file, 'w', encoding='utf-8') as f:
            removed = False
            for line in lines:
                if line.strip() != username:
                    f.write(line)
                else:
                    removed = True
            
            if removed:
                print(f"✅ Removed account: {username}")
            else:
                print(f"⚠️ Account '{username}' not found")
            
            return removed
    
    def list_accounts(self):
        """List all accounts"""
        try:
            with open(self.accounts_file, 'r', encoding='utf-8') as f:
                accounts = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            print(f"\n📋 Accounts ({len(accounts)}):")
            for i, account in enumerate(accounts, 1):
                print(f"  {i}. {account}")
            
            return accounts
        except Exception as e:
            print(f"❌ Error listing accounts: {e}")
            return []