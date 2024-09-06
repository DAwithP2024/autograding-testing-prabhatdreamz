while True:
    username = input("Enter a username: ")
    
    # Check if the username is made up of only alphabets and numbers
    if not username.isalnum():
        print("Invalid username. Only alphabets and numbers are allowed.")
        continue
    
    # If the username is valid, enter a loop to prompt for the password
    while True:
        password = input("Enter a password: ")

        # Initialize flags for password validation
        has_letter = False
        has_digit = False
        has_special = False
        has_uppercase = False

        # Check each character in the password
        for char in password:
            if char.isalpha():
                has_letter = True
                if char.isupper():
                    has_uppercase = True
            elif char.isdigit():
                has_digit = True
            #elif not char.isalnum():
                #has_special = True

        # Validate the password
        if not (has_letter and has_digit and has_special and has_uppercase):
            print("Invalid password. Password must contain letters, numbers, at least one special character, and at least one uppercase letter.")
            continue
        
        # If the password is valid, break out of the password loop
        print("Both username and password are valid!")
        break
    
    # Break out of the main loop since both username and password are valid
    break
# Write your code in this file
