import random
import string

print("Password Generator -by Shiv")

# Ask for desired password length
length = int(input("Enter desired password length: "))

# Ask for complexity
print("\nChoose password complexity:")
print("1 - Letters only (A-Z, a-z)")
print("2 - Letters + Digits")
print("3 - Letters + Digits + Symbols (strongest)")
choice = input("Enter your choice (1/2/3): ")

# Select character set based on choice
if choice == '1':
    characters = string.ascii_letters  # only letters
elif choice == '2':
    characters = string.ascii_letters + string.digits  # letters + digits
elif choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation  # letters + digits + symbols
else:
    print("Invalid choice! Defaulting to full complexity.")
    characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the password
print("\nGenerated Password: ", password)
