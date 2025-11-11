#!/usr/bin/env python3
"""
Crash.py - ملف اختباري بسيط للتأكد من عمل Python.
لن يقوم بأي شيء ضار — فقط يعرض معلومات وجملة ترحيبية.
"""
import sys
import platform

def main():
    print("Crash.py is working! ✅")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")

if __name__ == "__main__":
    main()
