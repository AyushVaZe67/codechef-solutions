import requests
import os
import json
from datetime import datetime

USERNAME = "<YOUR_CODECHEF_USERNAME>"

# Folder to save problems
BASE_DIR = "CodeChef"

def fetch_submissions():
    url = f"https://www.codechef.com/api/list/user/{USERNAME}"
    r = requests.get(url)
    data = r.json()

    # All solved problems
    solved = data["solved"]

    all_problems = []

    for diff in solved:
        for prob in solved[diff]:
            all_problems.append((prob["problem_code"], diff))

    return all_problems


def fetch_solution(problem_code):
    url = f"https://www.codechef.com/api/submission/{USERNAME}/{problem_code}"
    r = requests.get(url)
    data = r.json()

    # Get the latest Accepted submission
    for sub in data["content"]:
        if sub["status"] == "accepted":
            return sub["solution"], sub["language"]

    return None, None


def sanitize_lang(lang):
    if "C++" in lang:
        return ".cpp"
    if "Python" in lang:
        return ".py"
    if "C" == lang:
        return ".c"
    return ".txt"


def save_to_file(problem_code, diff, code, lang):
    ext = sanitize_lang(lang)
    folder = os.path.join(BASE_DIR, diff)
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{problem_code}{ext}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Saved: {filepath}")


if __name__ == "__main__":
    problems = fetch_submissions()
    for (problem_code, diff) in problems:
        code, lang = fetch_solution(problem_code)
        if code:
            save_to_file(problem_code, diff, code, lang)
