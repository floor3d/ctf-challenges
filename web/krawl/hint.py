import requests

def retrieve_letters(base_url, num_files):

    for i in range(1, num_files + 1):
        # fix the file URL! what should it look like?
        file_url = f"{base_url}/idk?????"
        response = requests.get(file_url).text
        # what now? the flag definitely has "CTF" in it ...

    return None

#put the base url here
base_url = "put the base url here"
# guess... how many files? to be safe, put a decently large number. hint: it's more than 100
num_files = 0

message = retrieve_letters(base_url, num_files)
print(message)
