from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl


class InstaBot:
    def __init__(self, usr_name, password, url):
        self.usr_name = usr_name
        self.password = password
        self.url = url
        self.bot = webdriver.Chrome("C:/Users/ko/Desktop/Emmett/Programming/Scripts/Python Scripts/Insta_Bot/chromedriver.exe")

    def login(self):
        bot = self.bot
        url = self.url
        bot.get(url)
        print(f"Connected to {url}")
        sl(1)
        print("Loging in...")
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.usr_name)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        sl(2)
        print("Login complete!")
        sl(1)
        self.main()
    
    def main(self):
        bot = self.bot
        button = bot.find_element_by_class_name('aOOlW.HoLwm')
        button.click()

