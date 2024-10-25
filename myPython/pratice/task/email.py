
import re


def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z-.]+$'
    if  re.fullmatch(regex, email):
        return True
    else:
        raise  ValueError("invalid email")

    #if (r'\email' in os.listdir()):
        #return True