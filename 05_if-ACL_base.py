'''
The standard ACL numbers are between 1 and 99 (inclusive)
The extended ACL numbers are between 100 199 (inclusive)
Other ACL numbers are nor standard nor extended.
Input an ACL number and categorize it!
'''
def category(acl_number):
    if 1 <= acl_number <= 99:
        return "Standard ACL"
    elif 100 <= acl_number <= 199:
        return "Extended ACL"
    else:
        return "Neither Standard nor Extended ACL"
def main():
    while True:
        user_input = input("Enter an ACL number (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        try:
            acl_number = int(user_input)
            category =category(acl_number)
            print(f"ACL number {acl_number} is categorized as: {category}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
main()