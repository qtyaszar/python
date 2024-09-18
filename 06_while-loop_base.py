'''
Write Python program :
    get an input for a number to count to
    if input is "q" or "quit", the program exits
    else write numbers from 1 to the number in one line, separated by space and goes back to the input
'''


def numbers(n):
    return " ".join(map(str, range(1, n + 1)))

def main():
    while True:
        user_input = input("Enter a number to count to (or 'q' / 'quit' to exit): ")

        if user_input.lower() in ["q", "quit"]:
            print("Exiting the program.")
            break
        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                print(numbers(number))
            else:
                print("Please enter a positive integer.")
        else:
            print("Invalid input. Please enter a valid number or 'q' / 'quit'.")
main()