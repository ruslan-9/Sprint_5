from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import AutorisationLocators
from data import BASE_URL, LOGIN_URL, EMAIL, PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserLogin:
    def test_user_login_success(self, driver: WebDriver):
        driver.get(BASE_URL)

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AutorisationLocators.EMAIL_INPUT))
    ).send_keys(EMAIL)

        driver.find_element(*AutorisationLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AutorisationLocators.ENTER_BUTTON).click()

        assert driver.current_url == LOGIN_URL
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(AutorisationLocators.USER_AVATAR)
    )
        assert driver.find_element(*AutorisationLocators.USER_AVATAR).is_displayed()
        assert driver.find_element(*AutorisationLocators.USER_NAME).text == "User."


    def test_user_logout_success(self, driver: WebDriver):
        driver.get(BASE_URL)

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AutorisationLocators.EMAIL_INPUT))
    ).send_keys(EMAIL)
        
        driver.find_element(*AutorisationLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AutorisationLocators.ENTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AutorisationLocators.LOGOUT_BUTTON))
    ).click()
        
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(AutorisationLocators.USER_AVATAR)
        )
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(AutorisationLocators.USER_NAME)
        )
        assert driver.find_element(*AutorisationLocators.LOGIN_BUTTON).text == "Вход и регистрация"  
