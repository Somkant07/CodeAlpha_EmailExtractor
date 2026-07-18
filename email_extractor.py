import re

# Read the input file
with open("input.txt", "r") as file:
    text = file.read()

# Extract email addresses using Regular Expression
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save extracted emails to a new file
with open("extracted_emails.txt", "w") as file:
    if emails:
        for email in emails:
            file.write(email + "\n")
    else:
        file.write("No email addresses found.")

# Display results
print("=" * 40)
print("Extracted Email Addresses")
print("=" * 40)

if emails:
    for email in emails:
        print(email)
else:
    print("No email addresses found.")

print("\nEmails have been saved to extracted_emails.txt")