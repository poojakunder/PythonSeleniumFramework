from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    CountryIndia = (By.LINK_TEXT, "India")
    PrivacyPolicy = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    alertSuccess = (By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountryIndia(self):
        return self.driver.find_element(*ConfirmPage.CountryIndia)

    def getPrivacyPolicy(self):
        return self.driver.find_element(*ConfirmPage.PrivacyPolicy)

    def Submit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def Alert(self):
        return self.driver.find_element(*ConfirmPage.alertSuccess)
