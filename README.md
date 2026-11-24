# Password
# Password Policy Validation Engine

## 1. Project Overview

The **Password Policy Validation Engine** is a Python-based application designed to evaluate password strings according to predefined security rules.

The system checks minimum password length, uppercase letters, lowercase letters, digits, special characters, repeated characters, and prohibited substrings.

It identifies valid and invalid passwords and provides clear explanations for every failed condition.

## 2. Objectives

- To validate passwords based on predefined security policies.
- To check minimum password length.
- To verify uppercase and lowercase characters.
- To check the presence of digits and special characters.
- To identify consecutive repeated characters.
- To detect prohibited words and sequences.
- To explain why a password fails validation.
- To display whether a password is valid or invalid.

## 3. Assumptions

1. The minimum password length is 8 characters.
2. Every password must contain at least one uppercase letter.
3. Every password must contain at least one lowercase letter.
4. Every password must contain at least one digit.
5. Every password must contain at least one special character.
6. Three or more consecutive identical characters are not allowed.
7. Passwords must not contain prohibited substrings.
8. Prohibited substring checking is case-insensitive.

## 4. Password Validation Rules

| Rule | Description |
|---|---|
| Minimum Length | At least 8 characters |
| Uppercase | At least one uppercase letter (A–Z) |
| Lowercase | At least one lowercase letter (a–z) |
| Digit | At least one number (0–9) |
| Special Character | At least one symbol |
| Repetition | No three consecutive identical characters |
| Prohibited Words | password, admin, qwerty, 1234 |

## 5. Algorithm

1. Start the program.
2. Display the password validation rules.
3. Enter the number of sample passwords.
4. Read a password from the user.
5. Check whether its length is at least 8 characters.
6. Check for an uppercase letter.
7. Check for a lowercase letter.
8. Check for a digit.
9. Check for a special character.
10. Check for three consecutive identical characters.
11. Check for prohibited substrings.
12. Store all failed conditions in a list.
13. If no conditions fail, display VALID PASSWORD.
14. Otherwise, display INVALID PASSWORD and all failure reasons.
15. Repeat for the remaining passwords.
16. Display the completion message.
17. Stop the program.

## 6. Pseudocode

```text
START

DEFINE minimum length = 8

DEFINE prohibited words:
    password, admin, qwerty, 1234

INPUT number of passwords

FOR each password:

    INPUT password

    CREATE empty failed conditions list

    IF length < 8:
        ADD minimum length error

    IF uppercase letter is missing:
        ADD uppercase error

    IF lowercase letter is missing:
        ADD lowercase error

    IF digit is missing:
        ADD digit error

    IF special character is missing:
        ADD special character error

    IF three consecutive identical characters exist:
        ADD repetition error

    IF prohibited substring exists:
        ADD prohibited substring error

    IF failed conditions list is empty:
        DISPLAY VALID PASSWORD

    ELSE:
        DISPLAY INVALID PASSWORD
        DISPLAY all failed conditions

DISPLAY completion message

STOP
```

## 7. Test Cases

| Test Case | Password | Expected Result |
|---|---|---|
| 1 | Hello@123 | Valid |
| 2 | hello123 | Invalid |
| 3 | Admin@123 | Invalid |
| 4 | AAAhello@1 | Invalid |
| 5 | Ab1@ | Invalid |
| 6 | Welcome#2026 | Valid |

### Test Case Explanation

**Test Case 1: Hello@123**

- Length is greater than 8.
- Contains uppercase and lowercase letters.
- Contains digits.
- Contains a special character.
- No prohibited substring.
- Result: Valid password.

**Test Case 2: hello123**

- Does not contain an uppercase letter.
- Does not contain a special character.
- Result: Invalid password.

**Test Case 3: Admin@123**

- Contains the prohibited substring "admin".
- Result: Invalid password.

**Test Case 4: AAAhello@1**

- Contains three consecutive identical characters.
- Result: Invalid password.

**Test Case 5: Ab1@**

- Does not satisfy the minimum length requirement.
- Result: Invalid password.

**Test Case 6: Welcome#2026**

- Satisfies all password validation rules.
- Result: Valid password.

## 8. Sample Output

```text
==========================================
      PASSWORD POLICY VALIDATION
==========================================

Password 1
Result: VALID PASSWORD
All password rules are satisfied.

Password 2
Result: INVALID PASSWORD
Failed Conditions:
- Password must contain at least one uppercase letter.
- Password must contain at least one special character.

Password 3
Result: INVALID PASSWORD
Failed Conditions:
- Password contains a prohibited word or sequence.

Password 4
Result: INVALID PASSWORD
Failed Conditions:
- Password must not contain three consecutive identical characters.

==========================================
Password validation completed.
==========================================
```

## 9. Python Concepts Used

- Variables and data types
- Input and output statements
- Conditional statements (if, else)
- For loops
- Lists
- Functions
- String operations
- String methods such as `isupper()`, `islower()`, `isdigit()`, and `isalnum()`
- Logical operators
- Return statements

## 10. Conclusion

The Password Policy Validation Engine successfully evaluates sample passwords using predefined security conditions.

It checks password length, character categories, repeated characters, and prohibited substrings. It also explains the reasons for password rejection.

This project demonstrates the practical application of Python programming concepts in developing a simple password validation system. It helps users understand password requirements and encourages the creation of stronger passwords.

## 11. Project Structure

```text
Password-Policy-Validation/
│
├── password_validation.py
├── README.md
│
└── screenshots/
    └── output.png
```

## 12. Execution Instructions

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open `password_validation.py`.
4. Run the program using:

```bash
python password_validation.py
```

5. Enter the number of sample passwords.
6. Enter fictional passwords for testing.
7. View the validation results and failure explanations.
8. Capture the actual program output screenshot.
9. Upload the Python file, README, and screenshot to GitHub.

## 13. Author Details

- **Name:** v.v.s.s.gayathri
- **Roll Number:** N26V01A0388
- **Branch:** CSE
- **Section:** Section-5
- **Subject:** Python Programming
- **Project:** Password policy
