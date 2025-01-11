is_logged_in = False

def require_login(fn):
    def inner(*args, **kwargs):
        if is_logged_in:
            fn(*args, **kwargs)
        else:
            raise ValueError("is_logged_in varable is False")
    return inner

@require_login
def view_profile():
    print("Finished execution!")

view_profile()