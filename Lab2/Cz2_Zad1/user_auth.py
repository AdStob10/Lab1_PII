class UserAuth:
    def __init__(self, users: dict):
        self.users = users

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError(username)
        if password != self.users[username]:
            raise WrongPasswordError(username)

        print("Success !")


class UserNotFoundError(Exception):

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User {self.username} not found"


class WrongPasswordError(Exception):

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"Wrong password for username {self.username}"
