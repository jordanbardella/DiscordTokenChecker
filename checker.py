import requests
from requests.structures import CaseInsensitiveDict

def ch(token):
    url = "https://discord.com/api/v9/users/@me/billing/payment-sources"
    headers = CaseInsensitiveDict()
    headers["authorization"] = token

    resp = requests.get(url, headers=headers)
    return resp.status_code == 200

def main():
    input_file = "tokens.txt"
    output_file = "valid_tokens.txt"

    with open(input_file, "r") as f:
        tokens = f.readlines()

    valid_tokens = []

    for token in tokens:
        token = token.strip()
        if ch(token):
            print(f"Token valid: {token}")
            valid_tokens.append(token)
        else:
            print(f"Token invalid: {token}")

    with open(output_file, "w") as f:
        for token in valid_tokens:
            f.write(token + "\n")

if __name__ == "__main__":
    main()
