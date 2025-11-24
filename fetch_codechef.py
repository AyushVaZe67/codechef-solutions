import requests
from bs4 import BeautifulSoup
import os
import time

USERNAME = "ayush_vaze"
BASE_DIR = "CodeChef"

# -------- Step 1: Fetch solved problem codes --------
def get_solved_problems():
    url = f"https://www.codechef.com/users/{USERNAME}"
    r = requests.get(url)
    if r.status_code != 200:
        print("Error fetching profile page")
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    solved_section = soup.find("section", {"class": "rating-data-section problems-solved"})

    if not solved_section:
        print("Could not locate solved problems section")
        return []

    codes = set()

    for tag in solved_section.find_all("a"):
        href = tag.get("href", "")
        if "/problems/" in href:
            code = href.split("/")[-1]
            codes.add(code)

    return list(codes)


# -------- Step 2: Fetch latest accepted submission using problem page --------
def get_latest_accepted_code(problem):
    url = f"https://www.codechef.com/status/{problem},{USERNAME}"
    r = requests.get(url)
    if r.status_code != 200:
        return None, None

    soup = BeautifulSoup(r.text, "html.parser")

    # Find solution links
    rows = soup.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 7 and "accepted" in cols[3].text.lower():
            lang = cols[6].text.strip()
            sol_link = cols[7].find("a")
            if sol_link:
                sol_url = "https://www.codechef.com" + sol_link["href"]
                return fetch_code(sol_url), lang
    return None, None


# -------- Step 3: Extract code from solution page --------
def fetch_code(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    code_area = soup.find("div", {"class": "program-source-code"})
    if not code_area:
        return None
    return code_area.text


def lang_ext(lang):
    if "C++" in lang:
        return ".cpp"
    if "Python" in lang:
        return ".py"
    if lang == "C":
        return ".c"
    return ".txt"


# -------- Step 4: Save file --------
def save(problem, code, lang):
    os.makedirs(BASE_DIR, exist_ok=True)
    ext = lang_ext(lang)
    path = os.path.join(BASE_DIR, f"{problem}{ext}")
    with open(path, "w", encoding="utf8") as f:
        f.write(code)
    print("Saved:", path)


# -------- Main --------
if __name__ == "__main__":
    problems = get_solved_problems()
    print("Solved problems:", problems)

    for p in problems:
        code, lang = get_latest_accepted_code(p)
        if code:
            save(p, code, lang)
        time.sleep(1)
