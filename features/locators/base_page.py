from selenium.webdriver.common.by import By


class BasePageLocators:
    MENU_WHO_WE_ARE = (By.XPATH, "/html/body/div/div[1]/nav/div/div/div[3]/ul/li[1]/a")
    MENU_WHAT_WE_DO = (By.XPATH, "/html/body/div/div[1]/nav/div/div/div[3]/ul/li[2]/a")
    MENU_OUR_WORK = (By.XPATH,   "/html/body/div/div[1]/nav/div/div/div[3]/ul/li[3]/a")
    MENU_BID_IDEAS = (By.XPATH,  "/html/body/div/div[1]/nav/div/div/div[3]/ul/li[4]/a")
    MENU_CAREERS = (By.XPATH,    "/html/body/div/div[1]/nav/div/div/div[3]/ul/li[5]/a")
    MENU_BLOG = (By.XPATH,       "/html/body/div/div[1]/nav/div/div/div[3]/ul/li[6]/a")
    MENU_CONTACT = (By.XPATH,    "/html/body/div/div[1]/nav/div/div/div[3]/ul/li[7]/a")
