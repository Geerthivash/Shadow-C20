import os
import shutil
import time

import pyfiglet
from termcolor import colored

def center_text(text):
    """Centers text dynamically based on terminal width."""
    terminal_width = shutil.get_terminal_size().columns
    return text.center(terminal_width)

# ASCII Banner
ascii_banner = pyfiglet.figlet_format("Shadow-C20")
ascii_banner = colored(ascii_banner, 'cyan')  # Make it look cool

# Welcome Message
welcome_msg = """
[+] Steganographic Encryption Tool
[+] Powered by ChaCha20 & Binary Encoding
[+] Developed for Cybersecurity Professionals

[*] Hide. Encrypt. Secure. Stay in Control.
"""

# Instructions
instructions = colored("\n[!] Load an image and embed your secret text securely!", 'yellow')

# Clear Screen
os.system("cls" if os.name == "nt" else "clear")

def art() :

    # Display Output
    print(center_text(ascii_banner))
    print(center_text(colored("Version 1.0", 'green')))
    print(center_text(colored("By JD", 'red')))
    print(center_text(colored("*" * 50, 'magenta')))
    print(center_text(colored(welcome_msg, 'light_blue')))
    time.sleep(0.99)
    print(center_text(instructions))
    time.sleep(2)
    print(colored("\n[?] Choose an operation:", 'cyan'))

    print(colored("\n[1] Encrypt a message", 'green'))
    print(colored("[2] Decrypt a message", 'green'))
    print(colored("[3] Exit", 'green'))

    choice = input(colored("\n[+] Enter your choice (1/2/3) : ", 'light_blue'))

    return choice