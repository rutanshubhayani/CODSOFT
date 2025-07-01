import random
import string
import sys

class PasswordGenerator:
    def __init__(self):

        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate_password(self, length=12, use_uppercase=True, use_digits=True, use_special=True):
        """
        Generate a password with specified criteria
        
        Args:
            length (int): Length of the password
            use_uppercase (bool): Include uppercase letters
            use_digits (bool): Include digits
            use_special (bool): Include special characters
        
        Returns:
            str: Generated password
        """
        chars = self.lowercase
        
        if use_uppercase:
            chars += self.uppercase
        if use_digits:
            chars += self.digits
        if use_special:
            chars += self.special_chars
        
        password = []
        
        password.append(random.choice(self.lowercase))
        
        if use_uppercase:
            password.append(random.choice(self.uppercase))
        if use_digits:
            password.append(random.choice(self.digits))
        if use_special:
            password.append(random.choice(self.special_chars))
        
        remaining_length = length - len(password)
        for _ in range(remaining_length):
            password.append(random.choice(chars))
        
        random.shuffle(password)
        
        return ''.join(password)
    
    def generate_multiple_passwords(self, count=5, length=12, use_uppercase=True, use_digits=True, use_special=True):
        """
        Generate multiple passwords
        
        Args:
            count (int): Number of passwords to generate
            length (int): Length of each password
            use_uppercase (bool): Include uppercase letters
            use_digits (bool): Include digits
            use_special (bool): Include special characters
        
        Returns:
            list: List of generated passwords
        """
        passwords = []
        for _ in range(count):
            password = self.generate_password(length, use_uppercase, use_digits, use_special)
            passwords.append(password)
        return passwords

def get_user_input():
    """Get password generation preferences from user"""
    print("=" * 50)
    print("           PASSWORD GENERATOR")
    print("=" * 50)
    
    while True:
        try:
            length = int(input("Enter password length (8-50): "))
            if 8 <= length <= 50:
                break
            else:
                print("Length must be between 8 and 50 characters.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nPassword complexity options:")
    use_uppercase = input("Include uppercase letters? (y/n) [default: y]: ").lower() != 'n'
    use_digits = input("Include digits? (y/n) [default: y]: ").lower() != 'n'
    use_special = input("Include special characters? (y/n) [default: y]: ").lower() != 'n'
    
    while True:
        try:
            count = int(input("\nHow many passwords to generate? (1-10): "))
            if 1 <= count <= 10:
                break
            else:
                print("Count must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")
    
    return length, use_uppercase, use_digits, use_special, count

def display_password_strength(password):
    """Display password strength analysis"""
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
        feedback.append("✓ Good length (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("✓ Acceptable length (8+ characters)")
    else:
        feedback.append("✗ Too short")

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    if has_lower:
        score += 1
        feedback.append("✓ Contains lowercase letters")
    if has_upper:
        score += 1
        feedback.append("✓ Contains uppercase letters")
    if has_digit:
        score += 1
        feedback.append("✓ Contains digits")
    if has_special:
        score += 1
        feedback.append("✓ Contains special characters")
    
    if score >= 5:
        strength = "Strong"
        color = "\033[92m"  
    elif score >= 3:
        strength = "Medium"
        color = "\033[93m"  
    else:
        strength = "Weak"
        color = "\033[91m" 
    
    print(f"\n{color}Password Strength: {strength}\033[0m")
    for item in feedback:
        print(f"  {item}")

def main():
    generator = PasswordGenerator()
    
    while True:
        try:
            length, use_uppercase, use_digits, use_special, count = get_user_input()
            
            print(f"\nGenerating {count} password(s)...")
            passwords = generator.generate_multiple_passwords(count, length, use_uppercase, use_digits, use_special)
            
            print("\n" + "=" * 50)
            print("           GENERATED PASSWORDS")
            print("=" * 50)
            
            for i, password in enumerate(passwords, 1):
                print(f"\nPassword {i}:")
                print(f"  {password}")
                display_password_strength(password)
            
            print("\n" + "=" * 50)
            choice = input("Generate more passwords? (y/n): ").lower()
            if choice != 'y':
                print("Thank you for using the Password Generator!")
                break
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()