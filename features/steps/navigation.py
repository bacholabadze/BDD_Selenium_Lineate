import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from features.locators.base_page import BasePageLocators
from features.locators.chat_bot import ChatBotLocators
from features.page_model.base_page import BasePage
from features.page_model.chat_bot import ChatBot
from features.page_model.home_page import HomePage

use_step_matcher('re')

DRIVER_PATH = "/features/chromedriver.exe"


@given("I am on the homepage")
def homepage(context):
    context.browser = webdriver.Chrome(DRIVER_PATH)
    context.browser.maximize_window()
    page = HomePage(context.browser)
    context.browser.get(page.url)
    # page.driver.get(page.url)


@then('I am on the "(.*)" page')
def redirected_page(context, pagename):
    pagename = pagename.lower().replace(" ", "-")
    current_url = context.browser.current_url
    assert pagename in current_url


@step('Title contains "(.*)"')
def correct_title(context, title):
    current_title = context.browser.title.lower()
    title = title.lower()
    assert title in current_title

# @then('I am on the "{pagename}" page')
# def step_impl(context, pagename):
#     pagename = pagename.lower().replace(" ", "-")
#     current_url = context.browser.current_url
#     assert pagename in current_url


@step('I see greetings messages')
def chat_messages(context):
    time.sleep(2)

    greeting_element = context.browser.find_element(*ChatBotLocators.CHAT_GREETING)
    greeting_text = "Hi there! I’m Lineate Bot and would like to assist you. What brings you here today?"
    assert greeting_text in greeting_element.text

    sales_text = "I want to talk to Sales"
    talk_to_sales_button = context.browser.find_element(*ChatBotLocators.CHAT_TALK_SALE)
    assert sales_text in talk_to_sales_button.text


@step('The chat is ended')
def end_of_the_chat(context):
    chat_cl = ChatBot(context.browser)
    WebDriverWait(chat_cl.driver, 15).until(expected_conditions.visibility_of_element_located(ChatBotLocators.CHAT_END))
    chat_footer = chat_cl.element_finder(ChatBotLocators.CHAT_END)
    footer_text = "Your chat has ended."
    assert footer_text in chat_footer.text