import subprocess

def execute_command(user_input):
    # Insecure use of user input in a shell command
    result = subprocess.check_output("echo " + user_input, shell=True)
    return result.decode("utf-8")

if __name__ == "__main__":
    print("Enter a string, and it will be echoed back to you.")

    user_input = input("Enter your input: ")

    # Displaying the result of the insecure command execution
    result = execute_command(user_input)
    print("Result: ", result)

