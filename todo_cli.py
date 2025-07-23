import json
import os
from colorama import Fore, Style, init

#  Initialize colorama 
init(autoreset=True)

TASKS_FILE = "tasks.json"

#  Pastel vibe palette
PASTEL_PINK = Fore.LIGHTMAGENTA_EX
PASTEL_YELLOW = Fore.LIGHTYELLOW_EX
PASTEL_GREEN = Fore.LIGHTGREEN_EX
PASTEL_CYAN = Fore.CYAN
NEUTRAL_GRAY = Fore.LIGHTBLACK_EX

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def get_priority_color(priority):
    if priority == "high":
        return PASTEL_PINK
    elif priority == "medium":
        return PASTEL_YELLOW
    elif priority == "low":
        return PASTEL_GREEN
    return NEUTRAL_GRAY

def list_tasks(tasks):
    if not tasks:
        print("😶‍🌫️ No tasks yet, you lil’ productivity ghost.")
        return
    print("\n🌈 Your ✨ aesthetic ✨ To-Dos:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⏳"
        color = get_priority_color(task.get("priority", "low"))
        priority = task.get("priority", "low").capitalize()
        print(f"{i}. {color}{task['title']} {Style.RESET_ALL}[{priority} Priority] [{status}]")

def add_task(tasks):
    title = input("🎯 What’s the task, bestie? → ")
    print("🚦 Set a priority level:")
    print("1️⃣ High 🔥\n2️⃣ Medium 😌\n3️⃣ Low 🧊")
    level = input("Pick 1/2/3 → ")
    
    if level == "1":
        priority = "high"
    elif level == "2":
        priority = "medium"
    else:
        priority = "low"
    
    tasks.append({"title": title, "done": False, "priority": priority})
    print(f"💅 Task added with {priority.upper()} priority! You're literally glowing.")

def mark_done(tasks):
    list_tasks(tasks)
    try:
        i = int(input("✨ Which task did you slay? (task no.) → ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
            print("🔥 Yasss! Task marked as done. Time to reward yourself 🍫.")
        else:
            print("❌ Uhm, that number's not in the chat.")
    except ValueError:
        print("🫠 That wasn't even a number, boo.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        i = int(input("🚮 Which task we canceling today? (task no.) → ")) - 1
        if 0 <= i < len(tasks):
            removed = tasks.pop(i)
            print(f"💔 '{removed['title']}' got ghosted.")
        else:
            print("🤷‍♀️ Babe, that ain't even on the list.")
    except ValueError:
        print("🫠 Uhh that’s not a number either, try again.")

def main():
    tasks = load_tasks()
    print(PASTEL_CYAN + "\n🌟 Welcome to your ✨ Gen Z To-Do CLI ✨")
    print("💖 Slay your day, one pastel task at a time 💖")

    while True:
        print("\n🛍️ MENU")
        print("1️⃣  See the vibe (view tasks)")
        print("2️⃣  Add a new slay")
        print("3️⃣  I did the thing (mark done)")
        print("4️⃣  Yeet a task (delete)")
        print("5️⃣  GTFO (save & exit)")

        choice = input("🎀 Pick ur option → ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print(NEUTRAL_GRAY + "📂 Your pastel dreams are saved. Peace out ✌️✨")
            break
        else:
            print("😵‍💫 That ain't it. Try a valid number, bestie.")

if __name__ == "__main__":
    main()
