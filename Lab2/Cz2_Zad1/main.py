import user_auth

if __name__ == '__main__':
    auth = user_auth.UserAuth({"admin":"1234", "user":"abcd"})
    try:
        auth.login("admin","1234")
        auth.login("unknown", "pass")
        auth.login("user", "wrongpass")
    except user_auth.UserNotFoundError as e:
        print(f"Błąd: {e}")
    except user_auth.WrongPasswordError as e:
        print(f"Błąd: {e}")
