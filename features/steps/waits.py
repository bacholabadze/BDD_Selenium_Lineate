import time

import selenium
from behave import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from features.locators.base_page import BasePageLocators
from features.locators.chat_bot import ChatBotLocators
from features.page_model.base_page import BasePage


@when('Chat icon is displayed and I click on the chat icon')
def step_impl(context):
    time.sleep(2)
    basepage_cl = BasePage(context.browser)
    WebDriverWait(basepage_cl.driver, 20).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(ChatBotLocators.CHAT_BOT_IFRAME)
            )
    element = basepage_cl.driver.find_element(*ChatBotLocators.CHAT_ICON)
    element.click()


