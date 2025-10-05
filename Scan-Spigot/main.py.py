#!/usr/bin/env python3
"""
SpigotMC Account Scanner
Tool để quét các account SpigotMC và kiểm tra plugins đã mua
"""

import sys
import os
from src.scanner import SpigotAccountScanner
from src.account_manager import AccountManager
from src.utils import load_config, display_help

def main():
    print("🎯 SpigotMC Account Scanner")
    print("=" * 40)
    
    # Load configuration
    config = load_config()
    scanner = SpigotAccountScanner(config)
    account_manager = AccountManager()
    
    if len(sys.argv) > 1:
        # Command line mode
        command = sys.argv[1]
        
        if command == "scan":
            results = scanner.scan_multiple_accounts("accounts/accounts.txt")
            scanner.generate_report(results)
        
        elif command == "add" and len(sys.argv) > 2:
            account_manager.add_account(sys.argv[2])
        
        elif command == "remove" and len(sys.argv) > 2:
            account_manager.remove_account(sys.argv[2])
        
        elif command == "list":
            account_manager.list_accounts()
        
        elif command == "help":
            display_help()
        
        else:
            print("❌ Unknown command. Use 'help' for usage information.")
    
    else:
        # Interactive mode
        while True:
            print("\nOptions: scan, add, remove, list, config, help, exit")
            choice = input("\nEnter command: ").strip().lower()
            
            if choice == 'scan':
                results = scanner.scan_multiple_accounts("accounts/accounts.txt")
                scanner.generate_report(results)
            
            elif choice.startswith('add '):
                username = choice[4:].strip()
                if username:
                    account_manager.add_account(username)
                else:
                    print("❌ Please provide a username")
            
            elif choice.startswith('remove '):
                username = choice[7:].strip()
                if username:
                    account_manager.remove_account(username)
                else:
                    print("❌ Please provide a username")
            
            elif choice == 'list':
                account_manager.list_accounts()
            
            elif choice == 'config':
                print("\nCurrent configuration:")
                for key, value in config.items():
                    print(f"  {key}: {value}")
            
            elif choice == 'help':
                display_help()
            
            elif choice == 'exit':
                print("👋 Goodbye!")
                break
            
            else:
                print("❌ Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()