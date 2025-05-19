from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import CreateAdvert
from locators.locators import AutorisationLocators
from data import BASE_URL, PROFILE_URL, EMAIL, PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCreateAdvert:
    def test_create_advert_unauthorized_user(self, driver: WebDriver):
        driver.get(BASE_URL)

        driver.find_element(*CreateAdvert.NEW_ADVERT).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(CreateAdvert.MODAL_WINDOW)
        )
        assert driver.find_element(*CreateAdvert.MODAL_WINDOW).is_displayed()
        assert driver.find_element(*CreateAdvert.MODAL_WINDOW_TITLE).text == "Чтобы разместить объявление, авторизуйтесь"
        

    def test_create_advert_authorized_user_success(self, driver: WebDriver):
        driver.get(BASE_URL)

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AutorisationLocators.EMAIL_INPUT))
    ).send_keys(EMAIL)
        driver.find_element(*AutorisationLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AutorisationLocators.ENTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(CreateAdvert.MODAL_WINDOW)
    )

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(CreateAdvert.NEW_ADVERT)
    ).click()

        driver.find_element(*CreateAdvert.NAME_INPUT).send_keys('Iphone 15')
        driver.find_element(*CreateAdvert.PRODUCT_DESCRIPTION).send_keys('iPhone 15 128 ГБ Серый')
        driver.find_element(*CreateAdvert.PRICE_INPUT).send_keys('50000')

        driver.find_element(*CreateAdvert.CATEGORY_INPUT).click()
        driver.find_element(*CreateAdvert.TECHNOLOGY_BUTTON).click()

        driver.find_element(*CreateAdvert.CITY_INPUT).click()
        driver.find_element(*CreateAdvert.SPB_BUTTON).click()

        driver.find_element(*CreateAdvert.RABIO_BUTTON_BU).click()
        driver.find_element(*CreateAdvert.TO_PUBLISH).click()

        driver.get(PROFILE_URL)

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(CreateAdvert.CARD_SEARCH)
    )
        assert driver.find_element(*CreateAdvert.CARD_SEARCH).text == "Iphone 15"
