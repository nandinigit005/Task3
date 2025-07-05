import re

def check_password_strength(password):
    strength = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    # Count how many criteria are met
    strength = sum(criteria.values())

    print("\nPassword Analysis:")
    for key, value in criteria.items():
        print(f"{key.capitalize()} requirement: {'✔️' if value else '❌'}")

    # Feedback based on strength
    if strength == 5:
        return "Strength: 🔐 Very Strong"
    elif strength >= 4:
        return "Strength: ✅ Strong"
    elif strength >= 3:
        return "Strength: ⚠️ Medium"
    else:
        return "Strength: ❌ Weak"

# Example usage
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
