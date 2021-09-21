# 載入需要的套件
from Member import Member
from SignAttendance import SignAttendance
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

_ACCOUNTS = list(filter(None, os.getenv('ACCOUNTS').split(',', -1)))
_PASSWORDS = list(filter(None, os.getenv('PASSWORDS').split(',', -1)))

_membersInfo = dict(zip(_ACCOUNTS, _PASSWORDS))

for acc, pwd in _membersInfo.items():
    singleMember = Member(acc, pwd)
    signAction = SignAttendance(singleMember)
    signAction.runSign()
