import requests
from bs4 import BeautifulSoup
from getpass import getpass
import json
import csv


BASE_URL = "https://hello.iitk.ac.in/"
LOGIN_ACTION = "index.php/user/login"
course = "esc201a21"

# Login
def login(url):
    sss = requests.Session()

    # Get Crendentials
    username = input("Username: ")
    password = getpass(prompt="Password: ")

    # Create the payload
    payload = {
        'name': username,
        'pass': password,
        'form_id': 'user_login_form',
        'op': 'SIGN IN'
    }

    # Get BUILD ID
    r = sss.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    build_ID = soup.find(attrs={"name": "form_build_id"}).get("value")
    payload["form_build_id"] = build_ID

    # Post Login
    _ = sss.post(url, data=payload)

    return sss


def main():
    # Start the session
    session = requests.Session()

    #login
    session = login(BASE_URL+LOGIN_ACTION)
    try:
        session.headers.update({
            "uid": session.cookies['uid'], 
            "token": session.cookies['token']
        })
    except:
        print("Try again")
        return

    # request data
    url = "https://hello.iitk.ac.in/api/" + \
        course + "/lectures/summary"

    r = session.get(url)
    r = r.json()

    # store entries
    entries = []

    # itterate over data
    for entry in r:
        data = {
            'week': entry['week'],
            'topic': entry['topic'],
            'title': entry['title'],
            'vidURL': entry['videosUploaded'],
            'resources': entry['resources']
        }
        entries.append(data)
    
    # print in json file
    with open('out.json', 'w') as f:
        json.dump(entries, f)
    
    # print in csv File
    with open('out.csv', 'w') as f:
        headers = ['week', 'topic', 'title', 'vidURL', 'resources']
        writer = csv.DictWriter(f, fieldnames=headers)
        
        writer.writeheader()
        writer.writerows(entries)

if __name__ == '__main__':
    main()