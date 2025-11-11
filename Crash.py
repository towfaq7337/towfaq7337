#!/usr/bin/env python3
"""
Crash.py - ملف اختباري آمن يطبع معلومات بيئة Python
"""
import sys
import platform

def main():
    print("Crash.py is working! ✅")
    print(f"Current directory: {__import__('os').getcwd()}")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")

if __name__ == "__main__":
    main()
