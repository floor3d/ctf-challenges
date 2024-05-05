import random
import signal

def generate_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    problem = f"{num1} {operator} {num2}"
    solution = eval(problem)
    return problem, solution

def get_user_input():
    try:
        return float(input("Your answer: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def timeout_handler(signum, frame):
    print("\nTime's up! You didn't solve the problem in 1 second.")
    raise SystemExit

def main():
    print("Welcome to the Math Challenge!")
    print("You have 1 second to solve each problem.")

    times_right = 0
    while True:
        problem, solution = generate_math_problem()
        print("Solve the following problem:")
        print(problem)

        # Set a timer for 1 second
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(1)

        try:
            user_input = get_user_input()
        finally:
            # Cancel the timer
            signal.alarm(0)

        if user_input is not None and user_input == solution:
            times_right += 1
            if times_right >= 10:
                print("CTF{KW1K_M4FS_P0G}")
                break
            print("Correct! Next problem.")
        elif user_input is not None:
            print(f"Wrong answer. The correct answer is {solution}.")
            break

if __name__ == "__main__":
    main()

