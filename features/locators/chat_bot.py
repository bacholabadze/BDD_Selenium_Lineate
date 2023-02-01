from selenium.webdriver.common.by import By


class ChatBotLocators:
    CHAT_BOT_IFRAME = (By.ID, "hubspot-conversations-iframe")
    CHAT_ICON = (By.CSS_SELECTOR, 'p[data-test-id="initial-message-text"].initial-message-text.m-top-1.m-bottom-0')
    CHAT_GREETING = (By.XPATH, '//*[@id="live-chat-widget"]/div/div/div[1]/div/section/div/div[1]/div/div/div[2]/div/div/div/div/div')
    CHAT_TALK_SALE = (By.XPATH, '//*[@id="live-chat-widget"]/div/div/div[1]/div/section/div/div[2]/div/div/div[2]/div/button[1]')
    CHAT_FRONT_END = (By.XPATH, '//*[@id="live-chat-widget"]/div/div/div[1]/div/section/div/div[5]/div/div/div[2]/div/button[1]/div')
    CHAT_B2B = (By.XPATH, '//*[@id="live-chat-widget"]/div/div/div[1]/div/section/div/div[8]/div/div/div[2]/div/button[1]/div')
    CHAT_DIRECTOR = (By.XPATH, '//*[@id="live-chat-widget"]/div/div/div[1]/div/section/div/div[17]/div/div/div[2]/div/button[3]/div')
    CHAT_INPUT = (By.CSS_SELECTOR, '#live-chat-widget > div > div > div.input-container.m-bottom-2.no-branding > div > div.VizExFormControl__FormControlWrapper-p2q08x-0.cJJItb > div')
    CHAT_END = (By.XPATH, '//*[@id="live-chat-widget"]/div/div/div[1]/div/div/p/i18n-string')
