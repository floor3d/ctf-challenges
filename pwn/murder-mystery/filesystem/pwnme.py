import os, time

def create_and_list_files():
    print("Welcome to the file store! We guarantee that you can find any information you need!")
    _ = input("Please enter your name: ")
    print("What would you like to read today?")
    print("Choices:")
    print("1. Bruh book")
    print("2. One Fish Two Fish")
    print("3. Playboi Carti Biography")
    to_read = input("Choice: ")

    read_file(to_read)

    resp = input("Would you like to add a new file? Y/n: ")
    if "y" in resp.lower():
        file_name = input("Enter the name of the new file: ")

        time.sleep(1)
        print(".", end= "", flush=True)
        time.sleep(1)
        print(".", end= "", flush=True)
        time.sleep(1)
        print(".", flush=True)
        time.sleep(2)
        print("Error code: 400-4-6413 FILESYSTEM FULL")

        # List files after creating the new file
        list_files()

    print("Thanks! Bye now!")

def list_files():
    current_files = os.listdir('.')
    
    if not current_files:
        print("No files in the current directory.")
    else:
        print("Current files in the directory:")
        for file in current_files:
            print(file, end=" ")
        print("")
        time.sleep(1)

def read_file(to_read):
    if(to_read == "1"):
        to_read = "bruh.txt"
    if(to_read == "2"):
        to_read = "hello.txt"
    if(to_read == "3"):
        to_read = "slime.txt"
    try:
        with open(to_read, 'r') as read_file:
            content = read_file.read()
            print(f"{content}")
    except FileNotFoundError:
        print(f"File '{to_read}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    # Ask user for a filename, create the file, and then list the files
    create_and_list_files()
