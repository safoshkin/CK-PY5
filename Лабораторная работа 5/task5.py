def get_random_password() -> str:
    import string
    import random
    str_ = string.digits + string.ascii_uppercase + string.ascii_lowercase
    password = ''.join(random.sample(str_, 8))

    return password


print(get_random_password())
