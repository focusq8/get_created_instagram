import requests
import os

def former_username():
    put_sessions = input("enter your session: ")
    os.system('cls||clear')
    
    url_username ="https://www.instagram.com/accounts/access_tool/former_usernames?__a=1"
    get_headers = {
        'dnt': '1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'accept': '*/*',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        "cookie": f"mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; csrftoken=3MaMIQfeCBoThizTBlIMvUZ9fmmSUFyq; sessionid={put_sessions}"
        }
  
    req_cursor = requests.get(url=url_username, headers=get_headers).json()
    get_cursor= req_cursor["data"]["cursor"]

    url_info = f"https://www.instagram.com/accounts/access_tool/former_usernames?__a=1&cursor={get_cursor}"
    req_info = requests.get(url=url_info, headers=get_headers).json()

    print("all usernames have been changed\n\n")
    get_usernames= req_info["data"]["data"]
    for loop in get_usernames:
        print(loop["text"])
    
    # print("\n\nall trusted usernames have been changed\n\n")
    # get_trusted= req_cursor["data"]["data"]
    # for loop in get_trusted:
    #     print(loop["text"])


def former_emails():
    put_sessions = input("enter your session: ")
    os.system('cls||clear')
    
    url_former_emails ="https://www.instagram.com/accounts/access_tool/former_emails?__a=1"
    get_headers = {
        'dnt': '1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'accept': '*/*',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        "cookie": f"mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; csrftoken=3MaMIQfeCBoThizTBlIMvUZ9fmmSUFyq; sessionid={put_sessions}"
        }
  

    req_emails = requests.get(url=url_former_emails, headers=get_headers)

    emails= req_emails.json()["data"]["data"]
    for loop in emails:
        print(loop["text"])
    if '"data":[]' in req_emails.text:
        print("No email linked")

def email_active():
    put_sessions = input("enter your session: ")
    os.system('cls||clear')

    url_create_email = 'https://www.instagram.com/download/request/?__a=1'
    get_headers = {
        'dnt': '1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'accept': '*/*',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        "cookie": f"mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; csrftoken=3MaMIQfeCBoThizTBlIMvUZ9fmmSUFyq; sessionid={put_sessions}"
        }


    req_url_create_email = requests.get(url=url_create_email, headers=get_headers)
    first_email = req_url_create_email.json()
    print("Email is linking: "+first_email["email_hint"])

def former_phones():
    put_sessions = input("enter your session: ")
    os.system('cls||clear')

    url_former_phone = 'https://www.instagram.com/accounts/access_tool/former_phones?__a=1'
    get_headers = {
        'dnt': '1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'accept': '*/*',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        "cookie": f"mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; csrftoken=3MaMIQfeCBoThizTBlIMvUZ9fmmSUFyq; sessionid={put_sessions}"
        }
    req_phones = requests.get(url=url_former_phone, headers=get_headers)
    get_phones = req_phones.json()["data"]["data"]
    for loop in get_phones:
        print(loop["text"])
    if '"data":[]' in req_phones.text:
        print("No phone linked")

def accounts_you_blocked():
    put_sessions = input("enter your session: ")
    os.system('cls||clear')
    
    url_blocked= 'https://www.instagram.com/accounts/access_tool/accounts_you_blocked?__a=1'

    get_headers = {
        'dnt': '1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'accept': '*/*',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        "cookie": f"mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; csrftoken=3MaMIQfeCBoThizTBlIMvUZ9fmmSUFyq; sessionid={put_sessions}"
        }
  
    req_blocked = requests.get(url=url_blocked, headers=get_headers)

    get_blocked= req_blocked.json()["data"]["data"]
    for loop in get_blocked:
        print(loop["text"])
    if '"data":[]' in req_blocked.text:
        print("No one blocked")

def all_info():
    put_sessions = input("enter your session: ")
    os.system('cls||clear')
    print("\n==========(former usernames)==========\n")
    url_username ="https://www.instagram.com/accounts/access_tool/former_usernames?__a=1"
    get_headers = {
        'dnt': '1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'accept': '*/*',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        "cookie": f"mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; csrftoken=3MaMIQfeCBoThizTBlIMvUZ9fmmSUFyq; sessionid={put_sessions}"
        } 
    req_cursor = requests.get(url=url_username, headers=get_headers).json()
    get_cursor= req_cursor["data"]["cursor"]
    url_info = f"https://www.instagram.com/accounts/access_tool/former_usernames?__a=1&cursor={get_cursor}"
    req_info = requests.get(url=url_info, headers=get_headers).json()
    get_usernames= req_info["data"]["data"]
    for loop in get_usernames:
        print(loop["text"])

    print("\n==========(former emails)==========\n")

    url_former_emails ="https://www.instagram.com/accounts/access_tool/former_emails?__a=1"
    req_emails = requests.get(url=url_former_emails, headers=get_headers)
    emails= req_emails.json()["data"]["data"]
    for loop in emails:
        print(loop["text"])
    if '"data":[]' in req_emails.text:
        print("No email linked")
    
    print("\n==========(email active in account)==========\n")

    url_create_email = 'https://www.instagram.com/download/request/?__a=1'
    req_url_create_email = requests.get(url=url_create_email, headers=get_headers)
    first_email = req_url_create_email.json()
    print("Email is linking: "+first_email["email_hint"])

    print("\n==========(former phones)==========\n")
    url_former_phone = 'https://www.instagram.com/accounts/access_tool/former_phones?__a=1'
    req_phones = requests.get(url=url_former_phone, headers=get_headers)
    get_phones = req_phones.json()["data"]["data"]
    for loop in get_phones:
        print(loop["text"])
    if '"data":[]' in req_phones.text:
        print("No phone linked")
    
    print("\n==========(accounts you blocked)==========\n")
    url_blocked= 'https://www.instagram.com/accounts/access_tool/accounts_you_blocked?__a=1'
    req_blocked = requests.get(url=url_blocked, headers=get_headers)
    get_blocked= req_blocked.json()["data"]["data"]
    for loop in get_blocked:
        print(loop["text"])
    if '"data":[]' in req_blocked.text:
        print("No one blocked")

if __name__ == "__main__":
    choose = input("""
1. Show all usernames
2. Show all emails
3. Show all phones
4. Show first email
5. Show all accounts you blocked
6. All info

choose please the number: """)

    os.system('cls||clear')

    if choose == "1":
        former_username()

    elif choose == "2":
        former_emails()

    elif choose == "3":
        former_phones()

    elif choose == "4":
        email_active()

    elif choose == "5":
        accounts_you_blocked()    

    elif choose == "6":
        all_info()