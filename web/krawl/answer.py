import requests


def retrieve_letters(base_url, num_files):

    for i in range(1, num_files + 1):
        file_url = f"{base_url}/file{i}"
        response = requests.get(file_url).text
        print(response)
        if len(response) > 0 and "CTF" in response:
            return response

    return None

base_url = "puturlhere"
num_files = 600

message = retrieve_letters(base_url, num_files)
print(message)
