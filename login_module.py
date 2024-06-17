import instaloader

def login(username, password):
    l = instaloader.Instaloader()
    try:
        l.login(username, password)
        print("Login successful")
        return l
    except Exception as e:
        print(f"An error occurred during login: {e}")
        return None
