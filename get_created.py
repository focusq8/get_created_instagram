from requests import get , post
from os import system
from uuid import uuid4
from datetime import datetime

def all_info():
    put_sessions = input("Enter your session: ")
    system('cls||clear')
    print("\n==========(Created Account)==========\n")
    url_Created ="https://www.instagram.com/accounts/access_tool/?__a=1"
    get_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        "cookie": f"mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; csrftoken=3MaMIQfeCBoThizTBlIMvUZ9fmmSUFyq; sessionid={put_sessions}"
        }   
    req_Created = get(url=url_Created, headers=get_headers)
    if "date_joined" in req_Created.text:
        print(f'Created Account is: {datetime.fromtimestamp(req_Created.json()["date_joined"]["data"]["timestamp"])}')      
    else:
        print(f'Created Account Wrong: {req_Created.text}')
    
    if 'date_of_birth' in req_Created.text:
        print(f'\nBirth Day is: {datetime.fromtimestamp(req_Created.json()["date_of_birth"]["data"]["timestamp"])}')      
    else:
        print(f'No date of birth: {req_Created.text}')

    print("\n==========(All Usernames)==========\n")
    url_username ="https://www.instagram.com/accounts/access_tool/former_usernames?__a=1"
    req_usernames = get(url=url_username, headers=get_headers)
    usernames_list = []
    if '"data":[]' in req_usernames.text:
        print("Username Not Changed")
    else:
        for loop_username in req_usernames.json()["data"]["data"]:
            usernames_list.append(loop_username["text"])
        print(usernames_list)

    print("\n==========(All Emails)==========\n")

    url_former_emails ="https://www.instagram.com/accounts/access_tool/former_emails?__a=1"
    req_emails = get(url=url_former_emails, headers=get_headers)    
    Emails_list = []
    if '"data":[]' in req_usernames.text:
        print("No Email Linked")
    else:
        for loop_email in req_emails.json()["data"]["data"]:
            Emails_list.append(loop_email["text"])
        print(Emails_list)
    
    print("\n==========(Email is linking now)==========\n")

    url__email_active = 'https://www.instagram.com/download/request/?__a=1'
    req_email_active = get(url=url__email_active, headers=get_headers)
    Active_email = req_email_active.json()
    print(Active_email["email_hint"])

    print("\n==========(All phones)==========\n")
    url_former_phone = 'https://www.instagram.com/accounts/access_tool/former_phones?__a=1'
    req_phones = get(url=url_former_phone, headers=get_headers)
    phone_list = []
    if '"data":[]' in req_phones.text:
        print("No phone linked")
    else:
        for loop_phone in req_phones.json()["data"]["data"]:
            phone_list.append(loop_phone["text"])
        print(phone_list)
          
    print("\n==========(Usernames You Blocked)==========\n")
    url_blocked= 'https://www.instagram.com/accounts/access_tool/accounts_you_blocked?__a=1'
    req_blocked = get(url=url_blocked, headers=get_headers)
    blocked_list = []
    if '"data":[]' in req_blocked.text:
        print("No one blocked")
    else:
        for loop_blocked in req_blocked.json()["data"]["data"]:
            blocked_list.append(loop_blocked["text"])
        print(blocked_list)
        

def login_one_session():
    global req_login_one_session , headers_one_session , username_one_session

    system('cls||clear')

    username_one_session = input("[+] username: ")
    password = input("[+] password: ") 

    url_one_session = 'https://i.instagram.com/api/v1/accounts/login/'

    headers_one_session = {

        'X-Pigeon-Session-Id': str(uuid4()),
        'X-IG-Device-ID': str(uuid4()),
        'User-Agent': 'Instagram 159.0.0.40.122 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 245196089)',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvx8=',
        "Connection" : 'keep-alive',
        "Accept-Language": "en-US",
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        "Accept-Encoding": "gzip, deflate",
        'Host': 'i.instagram.com',
        'Cookie': 'mid=YqejMwABAAExc4QmMCMsnq5YVuEw; csrftoken=BE0qlaD88tnB3vjkLhGksva9WFE2LPYB'
        }
        
    data = {
        'username': username_one_session,
        'enc_password': f"#PWD_INSTAGRAM:0:&:{password}",
        "adid": uuid4(),
        "guid": uuid4(),
        "device_id": uuid4(),
        "phone_id": uuid4(),
        "google_tokens": "[]",
        'login_attempt_count': '0'
        }

    req_login_one_session = post(url=url_one_session, headers=headers_one_session, data=data)
    system('cls||clear')

    if 'logged_in_user' in req_login_one_session.text:
        print(f"[+] Logged in with {username_one_session}")
        sessionid = req_login_one_session.cookies.get("sessionid")
        print(sessionid)
        with open(f'{username_one_session}.txt', 'w') as file:
            file.write(f'{sessionid}')
            print(f"[$] Saved as {username_one_session}.txt")

    elif "The password you entered is incorrect. Please try again." in req_login_one_session.text:
            print(f"{username_one_session} ===> password is wrong\n")
            login_one_session()

    elif "challenge_required" in req_login_one_session.text:
        print(f"{username_one_session} is secured")
        send_code_one_session()

    elif "Please wait a few minutes" in req_login_one_session.text:
        input(f"Blocked login Try Again Later\n\n")
        login_one_session()

    else:
        input(req_login_one_session.text)

def send_code_one_session():
    global api_path_url
    api_path_url = req_login_one_session.json()['challenge']['api_path']
   
    url_send_code = f"https://i.instagram.com/api/v1{api_path_url}"
    req_send_code = get(url=url_send_code,headers=headers_one_session).json()

    if "phone_number" in req_send_code["step_data"] and "email" in req_send_code["step_data"]:
        print(f'[0] Phone_Number: {req_send_code["step_data"]["phone_number"]} \n[1] Email: {req_send_code["step_data"]["email"]}')
        get_code_one_session()
    
    elif 'contact_point' in req_send_code["step_data"]:
        print(f'[1] Email: {req_send_code["step_data"]["contact_point"]}')
        get_code_one_session()
    
    elif 'email' in req_send_code["step_data"]:
        print(f'[1] Email: {req_send_code["step_data"]["email"]}')
        get_code_one_session()
            
    elif "phone_number" in req_send_code["step_data"]:
        print(f'[0] Phone_Number: {req_send_code["step_data"]["phone_number"]}')
        get_code_one_session()

    elif  "phone_number" not in req_send_code["step_data"] and "email" not in req_send_code["step_data"]:
        print("Account needs to confirm it's you ")
    
    else:
        input(req_send_code)
      

def get_code_one_session():

    choice = input('choose a number: ')
    url_get_code = f"https://i.instagram.com/api/v1{api_path_url}"
    get_code_data = {
        'choice': str(choice),
        'device_id': uuid4(),
        'guid': uuid4(),
        '_csrftoken': "BE0qlaD88tnB3vjkLhGksva9WFE2LPYB"
        }
    req_get_code = post(url= url_get_code,headers=headers_one_session,data=get_code_data)
  
    if "step_data" in req_get_code.text:
        print( f'code sent to: {req_get_code.json()["step_data"]["contact_point"]}')
    else:
        input(req_get_code.text)
    security_code = input('\nEnter the security code: ')
    send_code_data = {
            'security_code': str(security_code),
            'device_id': uuid4(),
            'guid': uuid4(),
            '_csrftoken': "BE0qlaD88tnB3vjkLhGksva9WFE2LPYB"
            }
    url_send_code = f"https://i.instagram.com/api/v1{api_path_url}"
    req_send_code = post(url=url_send_code,headers=headers_one_session, data=send_code_data)

    if "logged_in_user" in req_send_code.text:
        print(f'logged in with {username_one_session}')
        get_session = req_send_code.cookies["sessionid"]
        with open(f'{username_one_session}.txt', 'w') as file:
            file.write(f'{get_session}')
            print(get_session)
            input(f"[$] Saved as {username_one_session}.txt")
        
    elif "Please check the code we sent you and try again." in req_send_code.text:
        print('you entered wrong code , try again')
        get_code_one_session()

    elif "This field is required." in req_send_code.text:
        print("Enter the code!")
        get_code_one_session()

    elif '"lock":true'  in req_send_code.text:
        input("you need to active code and change password") 

    else:
        input(req_send_code.text)
        get_code_one_session()


if __name__ == "__main__":
    choose = input("""
1. get session username api Android

2. get All info created account


choose please the number: """)

    system('cls||clear')
    if choose == "1":
        login_one_session()   

    elif choose == "2":
        all_info()
