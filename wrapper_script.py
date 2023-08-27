import subprocess
import re
import requests
import webbrowser
import json
def auto_search_stack_overflow(type,message):
    api_url = "https://api.stackexchange.com/2.3/questions"
    params={
        "order": "desc",
        "sort": "activity",
        "tagged": type,
        "intitle": message,  # Add intitle parameter
        "site": "stackoverflow",
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    for item in data["items"]:
        print("Question Title:", item["title"])
        print("Question Link:", item["link"])
        webbrowser.open(item["link"])
def main():
    try:
        result=subprocess.run(["python","test_program.py"],capture_output=True,text=True,check=True)
        output=result.stdout
    except subprocess.CalledProcessError as e:
        output=e.stderr
    if "Traceback (most recent call last):" in output:
        error_pattern = re.compile(r"(\w+Error): (.+)")
        errors = error_pattern.findall(output)
        for error_type, error_msg in errors:
            auto_search_stack_overflow(error_type, error_msg)
    else:
        print("no errors found")
if __name__=="__main__":
    main()
