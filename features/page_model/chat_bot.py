from selenium.webdriver import Keys

from features.locators.chat_bot import ChatBotLocators
from features.page_model.base_page import BasePage


class ChatBot(BasePage):

    @property
    def chat_buttons(self):
        return {"I_want_to_talk_to_Sales": ChatBotLocators.CHAT_TALK_SALE,
                "front-end_development": ChatBotLocators.CHAT_FRONT_END,
                "B2B": ChatBotLocators.CHAT_B2B,
                "Director": ChatBotLocators.CHAT_DIRECTOR
        }

    def type_in_chat(self, txt):
        chat_input = super().element_finder(ChatBotLocators.CHAT_INPUT)
        chat_input.send_keys(txt)
        chat_input.send_keys(Keys.RETURN)
        return True