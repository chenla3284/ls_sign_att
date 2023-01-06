# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.common.exceptions import NoSuchElementException
from Member import Member
import random


class vote:
    MAIN_PAGE = 'https://docs.google.com/forms/d/e/1FAIpQLSfdF6I3lAL9uyy1Q24QollKrCmbblJO-UOO_bv5EC29_dhVlg/viewform'  # SihRong 6122
    # MAIN_PAGE = 'https://txp.rs/v/A28tDbHhvr8/EDENREDLANDING?desktop=true'  # Allen 7825

    def __init__(self, member: Member):
        # 人員物件
        self.member = member

    def runSign(self):

        # 初始化新瀏覽器
        self.__reInit()
        # 打開蛋糕網頁
        self.__openMainPage()

        list = ['NO.2 佳樺','NO.3 May','NO.1 玟樺']

        while True:
            random_num = random.choice(list)
            a = self.driver.find_element_by_xpath("//div[@data-value='%s']"%(random_num)) # NO.3 May # NO.2 佳樺 # NO.1 玟樺
            a.click()
            a = self.driver.find_element_by_xpath("//div[@jsname='M2UYVd']")
            a.click()
            a = self.driver.find_element_by_xpath("//a[@href='https://docs.google.com/forms/d/e/1FAIpQLSfdF6I3lAL9uyy1Q24QollKrCmbblJO-UOO_bv5EC29_dhVlg/viewform?usp=form_confirm']")
            a.click()      

    def __reInit(self):
        # 瀏覽器參數
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        # 開啟瀏覽器視窗(Chrome)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        # 等待網頁回應
        self.wait = ui.WebDriverWait(self.driver, 10)

    def __openMainPage(self):
        # 前往蛋糕系統
        self.driver.get(self.MAIN_PAGE)

    def __checkPasswordCorrect(self, password):
        # 輸入密碼
        elementPassword = self.driver.find_element_by_id('Authcodepwd')
        elementPassword.send_keys(password)
        try:
            self.driver.find_element_by_id(
                'Authcodepwd'
            )
        except NoSuchElementException:
            return True

        return False

    def __closeBrowser(self):
        # 關閉瀏覽器視窗
        self.driver.close()
