import os

def open_program(text)->str:
    if "код" in text:
        os.system("code")
        return "code"
    elif "браузер" in text:
        os.system("brave")
        return "brave"
    elif "telegram" in text:
        os.system("telegram-desktop")
        return "telegram" 
    
    return False

def shut_down():
    os.system("shutdown")

