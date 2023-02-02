import time

from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from features.locators.chat_bot import ChatBotLocators
from features.page_model.base_page import BasePage
from features.page_model.chat_bot import ChatBot
from features.page_model.home_page import HomePage

use_step_matcher('re')

# @when('I click on the "{page}" button')
# def step_impl(context, page):
#     page = page.replace(" ", "_")
#     menu_cl = BasePage(context.browser)
#     element_tuple = menu_cl.menu_items[page]
#     element = menu_cl.clickable_menu_item(element_tuple)
#     element.click()


@when('I click on the "(.*)" button')
def click_menu(context, button_name):
    button_name = button_name.replace(" ", "_")
    menu_cl = BasePage(context.browser)
    element_tuple = menu_cl.menu_items[button_name]
    element = menu_cl.element_finder(element_tuple)
    element.click()


@step('I click on the "(.*)" chat button')
def step_impl(context, button_name):
    chat_cl = ChatBot(context.browser)

    time.sleep(3)

    button_name = button_name.replace(" ", "_")
    element_tuple = chat_cl.chat_buttons[button_name]
    WebDriverWait(chat_cl.driver, 15).until(
        expected_conditions.element_to_be_clickable(element_tuple)
    )
    element = chat_cl.element_finder(element_tuple)
    element.click()


@step('I type "(.*)" in the chat')
def step_impl(context, type_text):
    time.sleep(4)
    chat_cl = ChatBot(context.browser)
    WebDriverWait(chat_cl.driver, 10).until(expected_conditions.visibility_of_element_located(ChatBotLocators.CHAT_INPUT))
    chat_cl.type_in_chat(type_text)


