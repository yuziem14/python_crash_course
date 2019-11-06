# Example of a custom module to be imported


def validate_email(email):
    if len(email) < 8:
        return False
    return True
