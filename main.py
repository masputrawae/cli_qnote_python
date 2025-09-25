from datetime import datetime as dt, timezone as tz, timedelta as td
from pathlib import Path
import subprocess
import sys
import re

menus = f'''
=====
[1]. Create Note
[2]. Show List
[3]. Backup
[4]. Backup Status
[5]. Restore
[6]. Clear
[7]. Exit
=====
>>>> '''

def get_date(format_type="simple"):
    time_zone = tz(td(hours=7))
    now = dt.now(time_zone)
    
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    iso_format = now.isoformat(timespec="seconds")
    simple_format = now.strftime("%Y-%m-%d")
    commit_date = now.strftime("%Y-%m-%d %H:%M:%S")

    if format_type == "simple":
        return simple_format
    elif format_type == "iso":
        return iso_format
    elif format_type == "timestamp":
        return timestamp
    elif format_type == "commit_date":
        return commit_date
    else:
        return "format not found, only: simple, iso, timestamp"

def make_dir(path):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def slugfy(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '_', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text

def save_note(file, content):
    try:
        with open(file, "w") as f:
            f.write(content)
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        subprocess.run(["vim", str(file)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"!Failed to Open File With Vim: Error {e}")

def create_note():
    timestamp = get_date("timestamp")
    create_date = get_date("iso")

    input_title = input("Enter Title (default: untitled) >>> ") or "untitled"
    input_path = input("Enter Path (default: ./notes/inbox )>>> ") or "./notes/inbox"
    input_tags = input("Enter Tags. (separate with commas, or skip) >>> ") or "unorganized" 
    
    tags = input_tags.split(",")
    path = ""

    if not input_path.startswith("./"):    
        path = "./" + input_path
    else:
        path = input_path

    make_dir(path)
    save_file = f"{path}/{timestamp}_{slugfy(input_title)}.md"
    content = f"---\ntitle: {input_title.title()}\ntags: {tags}\ncreated: {create_date}\n---\n"
    
    save_note(save_file, content)

def backup():
    try:
        now = get_date("commit_date")
        message = f"Backup On: {now}"

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("Backup Complated")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def backup_status():
    try:
        hr = "\n" + "=" * 40 + "\n"
        status_output = hr
        status_output += "STATUS REPOSITORY".center(40)
        status_output += hr

        status_output += subprocess.run(["git", "status"], text=True, capture_output=True).stdout

        log_output = hr
        log_output += "HISTORY LAST BACKUP".center(40)
        log_output += hr

        log_output += subprocess.run(["git", "log", "--oneline", "-n", "10"], text=True, capture_output=True).stdout

        final_output = status_output + log_output + hr
        print(final_output)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def clear():
    print("\033c", end="")

def main():
    try:
        print("===== MD NOTE =====\n")
        while True:
            try:
                user_menu = int(input(menus))
                if user_menu == 1:
                    create_note()
                elif user_menu == 2:
                    subprocess.run(["tree"])
                elif user_menu == 3:
                    backup()
                elif user_menu == 4:
                    backup_status()
                elif user_menu == 5:
                    subprocess.run(["git", "pull"])
                elif user_menu == 6:
                    clear()
                elif user_menu == 7:
                    print("Goodbye")
                    break
                else:
                    print("Invalid Choice, Only 1 - 7")
                    continue

            except ValueError:
                print("Invalid Option, Only Accepts Numbers 1 - 7!")
                continue

    except KeyboardInterrupt:
        print("=====!Safely Force Terminate Program!=====")
        
if __name__ == "__main__":
    main()
