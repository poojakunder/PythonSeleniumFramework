import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckoutPage import CheckoutPage
from PageObject.ConfirmPage import ConfirmPage
from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        logger=self.get_logger()
        homepage=HomePage(self.driver)
        logger.info("clicked on shop icon")
        checkoutpage=homepage.shopItems()#operations is click here
        products = checkoutpage.getCardTitles()
        for product in products:
            productName=checkoutpage.getProductName(product).text
            if productName == "Blackberry":
                checkoutpage.getCardFooter(product).click()
        checkoutpage.Cart().click()
        confirmpage=checkoutpage.checkoutItems()
        confirmpage.getCountry().send_keys("ind")
        self.verify_link_presence("India")  #explicit wait
        confirmpage.getCountryIndia().click()
        confirmpage.getPrivacyPolicy().click()
        confirmpage.Submit().click()
        successText=confirmpage.Alert().text
        logger.info("text recieved is "+successText)
        assert "Success! Thank you!" in successText
