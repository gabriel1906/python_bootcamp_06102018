import sys


def validate_email(line):
    line = line.strip().lower()
    if line.count('@') == 1:
        return line


if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    emails = set()
    with open(input_file) as f:
        for line in f:
            email = validate_email(line)
            if email:
                emails.add(email)

    with open(output_file, 'w') as f:
        for email in sorted(emails):
            f.write(email + "\n")


else:
    print("Nieprawidłowa ilość parametrów")
