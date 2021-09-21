class Member:
    def __init__(self, account, password):
        self.account = account  # 帳號
        self.password = password  # 密碼

    def getAccount(self):
        return self.account

    def getPassword(self):
        return self.password
