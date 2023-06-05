import re
mistakes_messages = {
    'length': 'Password must have 8 characters length or more',
    'substring': "Password must don't have same substring of login",
    'digits': 'Password must have 1 digit or more',
    'special': 'Password must have 1 symbol of !@#$ or more',
    'uppercase': 'Password must have 1 uppercase letter or more',
    'lowercase': 'Password must have 1 lowercase letter or more'
}


def password_verification(login, password):
    """
    Verify the strength of 'password'
    Returns message about first meeting mistake and stop verification
    A password is considered strong if:
        8 characters length or more
        don't have the same substring of login (forbidden: login - "johndoe@gmail.com", and password "1#johndoe123H")
        1 digit or more
        1 symbol of !@#$ or more
        1 uppercase letter or more
        1 lowercase letter or more
    """
    # calculating the length
    if len(password) < 8:
        return mistakes_messages['length']

    substring = (re.split('@', login)[0])
    if substring in password:
        return mistakes_messages['substring']

    # searching for digits
    if not re.search(r"\d", password):
        return mistakes_messages['digits']

    # searching for uppercase
    if not re.search(r"[A-Z]", password):
        return mistakes_messages['uppercase']

    # searching for lowercase
    if not re.search(r"[a-z]", password):
        return mistakes_messages['lowercase']

    # searching for symbols
    if not re.search(r"[!@#$]", password):
        return mistakes_messages['special']

    if True:
        return True
