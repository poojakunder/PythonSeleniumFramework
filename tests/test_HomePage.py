import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log=self.get_logger()
        homepage = HomePage(self.driver)
        log.info("name"+getData["name"])
        homepage.getName().send_keys(getData["name"])
        log.info("email"+getData["email"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckbox().click()
        log.info("email"+getData["gender"])
        self.setOptionByText(homepage.getGender(), getData["gender"])
        # dropdown = Select(homepage.getGender())
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)
        homepage.SubmitForm().click()
        message = homepage.getSuccessMessage().text
        log.info("Success message "+message)
        assert "success" in message
        self.driver.refresh()
        time.sleep(2)

    #parameterizing
    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param



    # @pytest.fixture(params=[{"name": "Pooja", "email": "pooja@gmail.com", "gender": "Female"},
    #                         {"name": "Kumar", "email": "kumar@gmail.com", "gender": "Male"}])
    # def getData(self, request):
    #     return request.param

    # we can use tuple,dictionary as well to store data to send
    # @pytest.fixture(params=[("Pooja", "pooja@gmail.com", "Female"), ("Kumar", "kumar@gmail.com", "Male")])
    # def getData(self, request):
    #     return request.param
