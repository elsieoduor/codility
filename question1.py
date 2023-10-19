def generate_email(name, company, email_dict):
    parts = name.split()
    first_name = parts[0]
    middle_name = parts[1][0] if len(parts) == 3 else ""
    last_name = parts[-1].replace("-", "").replace(" ", "")[:8]
    base_email = f"{first_name.lower()}{middle_name.lower()}{last_name.lower()}@{company.lower()}.com"
    
    if base_email in email_dict:
        email_dict[base_email] += 1
        return f"{name} <{base_email}{email_dict[base_email]}@{company.lower()}.com>"
    else:
        email_dict[base_email] = 1
        return f"{name} <{base_email}@{company.lower()}.com>"

def solution(S, C):
    names = S.split(", ")
    email_dict = {}
    result = []

    for name in names:
        formatted_email = generate_email(name, C, email_dict)
        result.append(formatted_email)

    return ", ".join(result)

# Example usage:
C = "Example"
S = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"
result = solution(S, C)
print(result)
