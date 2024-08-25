from selenium.webdriver.common.by import By

from PageObject.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver
    cardTitle=(By.XPATH, "//div[@class='card h-100']")
    cardFooter=(By.XPATH, "div/button")
    productName=(By.XPATH, "div/h4/a")
    cart=(By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut=(By.XPATH, "//button[@class='btn btn-success']")
    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self,product):
        return product.find_element(*CheckoutPage.cardFooter)

    def getProductName(self,product):
        return product.find_element(*CheckoutPage.productName)

    def Cart(self):
        return self.driver.find_element(*CheckoutPage.cart)

    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmpage=ConfirmPage(self.driver)
        return confirmpage
