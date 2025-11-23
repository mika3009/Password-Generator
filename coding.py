import random
import string
import time
import sys
import pyperclip
from colorama import Fore, Style, init
import os

init(autoreset=True)


#ui

def slow_print(text, delay=0.01):
    for c in text:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def progress_bar(duration=1.5):
    bar_length = 30
    start = time.time()
    while time.time() - start < duration:
        elapsed = time.time() - start
        filled = int((elapsed / duration) * bar_length)
        bar = "█" * filled + "-" * (bar_length - filled)
        print(Fore.MAGENTA + f"\r[{bar}] {int((filled/bar_length)*100)}%", end="")
        time.sleep(0.03)
    print(Fore.MAGENTA + f"\r[{'█'*bar_length}] 100%")
    print()


def header():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "╔══════════════════════════════════╗")
    print(Fore.CYAN + "║      PASSWORD GENERATOR 6767     ║")
    print(Fore.CYAN + "║        by Mika and Cheryl        ║")
    print(Fore.CYAN + "╚══════════════════════════════════╝")


def menu():
    header()
    print(Fore.MAGENTA + " Choose a mode:\n")
    print(Fore.CYAN + " 1. Normal Password (with symbols)")
    print(Fore.CYAN + " 2. No-Symbol Password")
    print(Fore.CYAN + " 3. Multiple Passwords")
    print(Fore.CYAN + " 4. Advanced (choose character types)")
    print(Fore.RED + " 5. Exit")
    print()
    return input(Fore.YELLOW + " Select mode (1/2/3/4/5): ")


#generator

def generate(length=12, characters=""):
    return "".join(random.choice(characters) for _ in range(length))


def mode_normal():
    length = int(input(Fore.YELLOW + "Password length: "))
    header()
    print(Fore.CYAN + "Generating your password...\n")
    progress_bar()

    characters = string.ascii_letters + string.digits + string.punctuation
    pw = generate(length, characters)

    print(Fore.GREEN + "Your password:")
    print(Fore.WHITE + pw)
    pyperclip.copy(pw)
    print(Fore.MAGENTA + "(Copied to clipboard!)")


def mode_no_symbol():
    length = int(input(Fore.YELLOW + "Password length: "))
    header()
    print(Fore.CYAN + "Generating...\n")
    progress_bar()

    characters = string.ascii_letters + string.digits
    pw = generate(length, characters)

    print(Fore.GREEN + "Your password:")
    print(Fore.WHITE + pw)
    pyperclip.copy(pw)
    print(Fore.MAGENTA + "(Copied to clipboard!)")


def mode_multiple():
    length = int(input(Fore.YELLOW + "Password length: "))
    count = int(input(Fore.YELLOW + "How many passwords: "))
    header()
    print(Fore.CYAN + "Generating multiple passwords...\n")
    progress_bar()

    characters = string.ascii_letters + string.digits + string.punctuation
    all_pw = []

    for i in range(count):
        pw = generate(length, characters)
        all_pw.append(pw)
        print(Fore.GREEN + f"{i+1}. " + Fore.WHITE + pw)

    pyperclip.copy("\n".join(all_pw))
    print(Fore.MAGENTA + "\n(All passwords copied to clipboard!)")


def mode_advanced():
    header()
    print(Fore.CYAN + "Advanced Generator — choose character types:\n")

    length = int(input(Fore.YELLOW + "Password length: "))
    count = int(input(Fore.YELLOW + "How many passwords: "))
    use_lower = input(Fore.YELLOW + "Include lowercase? (y/n): ").lower() == "y"
    use_upper = input(Fore.YELLOW + "Include uppercase? (y/n): ").lower() == "y"
    use_digits = input(Fore.YELLOW + "Include digits? (y/n): ").lower() == "y"
    use_symbols = input(Fore.YELLOW + "Include symbols? (y/n): ").lower() == "y"

    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        print(Fore.RED + "ERROR: You must select at least one character type!")
        return

    header()
    print(Fore.CYAN + "Generating advanced passwords...\n")
    progress_bar(2.0)

    all_pw = []
    for i in range(count):
        pw = generate(length, characters)
        all_pw.append(pw)
        print(Fore.GREEN + f"{i+1}. " + Fore.WHITE + pw)

    pyperclip.copy("\n".join(all_pw))
    print(Fore.MAGENTA + "\n(All copied to clipboard!)")

#mainloop
while True:
    choice = menu()

    if choice == "1":
        mode_normal()
    elif choice == "2":
        mode_no_symbol()
    elif choice == "3":
        mode_multiple()
    elif choice == "4":
        mode_advanced()
    elif choice == "5":
        print(Fore.RED + "\nGoodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice!")

    input(Fore.YELLOW + "\nPress ENTER to return to menu...")

input("\nPress ENTER to close program...")
