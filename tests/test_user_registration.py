from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import RegistrationLocators
from helpers import random_email, random_email_not_mask, random_password
from data import BASE_URL, REGISTRATION_URL, EMAIL, PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserRegistration:
    def test_user_registration_success(self, driver: WebDriver):
        new_email = random_email()
        new_password = random_password()
        driver.get(BASE_URL)

        driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((RegistrationLocators.REGISTER_BUTTON))
    ).click()

        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(new_email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(new_password)
        driver.find_element(*RegistrationLocators.SUBMIT_PASSWORD_INPUT).send_keys(new_password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        assert driver.current_url == REGISTRATION_URL
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(RegistrationLocators.USER_AVATAR)
    )
        assert driver.find_element(*RegistrationLocators.USER_AVATAR).is_displayed()
        assert driver.find_element(*RegistrationLocators.USER_NAME).text == "User."

    
    def test_user_registration_email_not_mask(self, driver: WebDriver):
        email_not_mask = random_email_not_mask()
        driver.get(BASE_URL)

        driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((RegistrationLocators.REGISTER_BUTTON))).click()

        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email_not_mask)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(RegistrationLocators.EMAIL_ERROR)
    )
        assert driver.find_element(*RegistrationLocators.EMAIL_ERROR).text == "Ошибка"
        
        color_rgb = "rgb(255, 105, 114)"

        email_frame = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationLocators.EMAIL_BORDER)
        )
        assert email_frame.value_of_css_property("border-color") == color_rgb

        password_frame = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationLocators.PASSWORD_BORDER)
        )
        assert password_frame.value_of_css_property("border-color") == color_rgb

        submit_password_frame = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationLocators.SUBMIT_PASSWORD_BORDER)
        )
        assert submit_password_frame.value_of_css_property("border-color") == color_rgb


    def test_existing_user_registration(self, driver: WebDriver):
        driver.get(BASE_URL)

        driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((RegistrationLocators.REGISTER_BUTTON))
    ).click()

        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*RegistrationLocators.SUBMIT_PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(RegistrationLocators.EMAIL_ERROR)
    )
        assert driver.find_element(*RegistrationLocators.EMAIL_ERROR).text == "Ошибка"
        
        color_rgb = "rgb(255, 105, 114)"

        email_frame = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationLocators.EMAIL_BORDER)
        )
        assert email_frame.value_of_css_property("border-color") == color_rgb

        password_frame = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationLocators.PASSWORD_BORDER)
        )
        assert password_frame.value_of_css_property("border-color") == color_rgb

        submit_password_frame = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationLocators.SUBMIT_PASSWORD_BORDER)
        )
        assert submit_password_frame.value_of_css_property("border-color") == color_rgb
