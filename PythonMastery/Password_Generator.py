# Password Generator (random, secure).
import secrets
import string

def generate_password(length=12, exclude_ambiguous=True):
    #Define character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ambiguous characters (often excluded in security policies)
    ambiguous = "Il1O0|`'\"~"

    # character set: letters (upper/lower), digits, punctuation
    characters = upper + lower + digits + symbols

    if exclude_ambiguous:
        characters = ''.join(c for c in characters if c not in ambiguous)

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

def main():
    print(f"Password = {generate_password(16)}")

if __name__ == "__main__":
    main()