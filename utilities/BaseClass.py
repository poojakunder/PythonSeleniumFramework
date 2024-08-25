import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#all the reusable code here in baseclass

@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_link_presence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def setOptionByText(self,locator,text):
         dropdown = Select(locator)
         dropdown.select_by_visible_text(text)

    def get_logger(self):
        loggername=inspect.stack()[1][3] #gets testcase name
        # create object
        # we need info from which testcase or file we are getting logs so use __name__
        logger = logging.getLogger(loggername)
        # where to print the log
        fileHandler = logging.FileHandler("logFile.log")
        # for the format
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        # add filehandler object here
        logger.addHandler(fileHandler)

        # we can set the level -> log levels are debug,info,warning,error,crtical
        logger.setLevel(logging.INFO) #level starts from INFO now so debug will get skipped
        # logger.debug("A Debug statement is executed")
        # logger.info("Information")
        # logger.warning("Warning : balance is in negative")
        # logger.error("Error found assertion error")
        # logger.critical("Critical error : Hacked ")
        return logger
