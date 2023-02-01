from features.locators.base_page import BasePageLocators
from features.locators.chat_bot import ChatBotLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return "https://www.lineate.com"

    @property
    def menu_items(self):
        return {"Who_we_are": BasePageLocators.MENU_WHO_WE_ARE,
                "What_we_do": BasePageLocators.MENU_WHAT_WE_DO,
                "Our_work": BasePageLocators.MENU_OUR_WORK,
                "Big_ideas": BasePageLocators.MENU_BID_IDEAS,
                "Careers": BasePageLocators.MENU_CAREERS,
                "Blog": BasePageLocators.MENU_BLOG,
                "Contact": BasePageLocators.MENU_CONTACT}

    def element_finder(self, name):
        return self.driver.find_element(*name)

    def chat_iframe(self):
        return self.driver.find_element(*ChatBotLocators.CHAT_BOT_IFRAME)


