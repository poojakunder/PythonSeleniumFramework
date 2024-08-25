from selenium.webdriver.common.by import By

from PageObject.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.CSS_SELECTOR, " a[href*='shop']")
    name=(By.CSS_SELECTOR,"input[name='name']")
    email=(By.NAME,"email")
    checkBox=(By.ID,"exampleCheck1")
    GenderDropdown=(By.ID,"exampleFormControlSelect1")
    submitForm=(By.XPATH,"//input[@type='submit']")
    successPage=(By.CLASS_NAME,"alert-success")

    # constructor
    def __init__(self, driver):
        self.driver = driver  # self.driver is instance variable here

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        # self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.GenderDropdown)

    def SubmitForm(self):
        return self.driver.find_element(*HomePage.submitForm)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successPage)
