# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.support import ui
from Member import Member


class SignAttendance:
    MAIN_PAGE = 'https://auth.mayohr.com/HRM/Account/Login'
    ATTENDANCE_TAB = 'https://apolloxe.mayohr.com/ta'

    def __init__(self, member: Member):
        # 人員物件
        self.member = member

        # 開啟瀏覽器視窗(Chrome)
        self.driver = webdriver.Chrome()

        # 等待網頁回應
        self.wait = ui.WebDriverWait(self.driver, 10)

    def runSign(self):
        # 開啟主畫面
        self.__openMainPage()

        # 登入
        self.__login()

        # 切換打卡分頁
        self.__goToAttendanceTab()

        # 點擊打卡
        self.__pressCheckAttendance()

        # 關閉瀏覽器
        # self.__closeBrowser()

    def __openMainPage(self):
        # 前往打卡系統
        self.driver.get(self.MAIN_PAGE)

    def __login(self):
        self.wait.until(lambda driver: driver.find_element_by_name('userName'))
        elementUserName = self.driver.find_element_by_name('userName')
        elementUserName.send_keys(self.member.getAccount())

        # 輸入密碼
        elementPassword = self.driver.find_element_by_name('password')
        elementPassword.send_keys(self.member.getPassword())

        # 按下登入
        elementSubmit = self.driver.find_element_by_css_selector(
            'button.submit-btn')
        elementSubmit.click()

    def __goToAttendanceTab(self):
        # 等待登入完成
        self.wait.until(lambda driver: driver.find_element_by_css_selector(
            'a.ta__confirmation'))
        # 切換到簽到頁面
        self.driver.get(self.ATTENDANCE_TAB)

    def __pressCheckAttendance(self):
        # 等待我要打卡按鈕
        self.wait.until(lambda driver: driver.find_element_by_css_selector(
            'div.ta-link-btn[data-reactid=".0.0.1.2.0.1.1.1.0.1.2.0"]'))
        # 我要打卡
        elementAttendancePage = self.driver.find_element_by_css_selector(
            'div.ta-link-btn[data-reactid=".0.0.1.2.0.1.1.1.0.1.2.0"]')
        elementAttendancePage.click()

        # 等待上班按鈕
        self.wait.until(lambda driver: driver.find_element_by_css_selector(
            'button.ta_btn_cancel[data-reactid=".0.0.1.2.0.1.1.1.5.0.1.0.1.0.0"]'))
        # 按下上班
        elementCheckAttendance = self.driver.find_element_by_css_selector(
            'button.ta_btn_cancel[data-reactid=".0.0.1.2.0.1.1.1.5.0.1.0.1.0.0"]')
        elementCheckAttendance.click()

    def __closeBrowser(self):
        # 關閉瀏覽器視窗
        self.driver.close()
