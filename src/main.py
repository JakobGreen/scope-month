"""
Do all the web stuff
"""
import socket
import time

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.common.exceptions import NoSuchElementException, WebDriverException


class ScopeMonthWebDriver(object):
    """ Class used to enter scope month drawing """

    def __init__(self, browser='firefox', headless=False):
        if headless:
            self.display = Display(visible=0, size=(1920, 1080))
            self.display.start()

        self.driver = self._get_driver(browser)

        self.driver.set_window_size(1920, 1080)

    def __del__(self):
        """ Try to stop the selenium webdriver """
        if self.driver is None:
            return

        try:
            self.driver.quit()
        except socket.error:
            pass

    @staticmethod
    def _get_driver(browser):
        """ Return the correct browser driver """
        if browser.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser.lower() == 'chrome':
            return  webdriver.Chrome()
        else:
            raise StandardError('Must specify a valid browser type: [firefox, chrome]')

    def run(self):
        """ Register for the giveaway """

        self.driver.get('http://www.keysight.com/main/editorial.jspx?cc=US&lc=eng&ckey=2678002&nid=-32546.0.00&id=2678002')
        time.sleep(3)

        english = self.driver.find_element_by_css_selector('#absolute_canvas_object_abs_element_4 > div > a')
        english.click()

        time.sleep(3)

        el = self.driver.find_element_by_css_selector('.field_0_identity .form-element input')
        el.send_keys('Jakob')

        time.sleep(.5)

        el = self.driver.find_element_by_css_selector('.field_1_identity .form-element input')
        el.send_keys('Green')

        time.sleep(.5)

if __name__ == '__main__':
    driver = ScopeMonthWebDriver()
    driver.run()
