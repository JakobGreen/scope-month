"""
Do all the web stuff
"""
import socket
import time

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support import select


class ScopeMonthWebDriver(object):
    """ Class used to enter scope month drawing """

    input_fields = [
        ('input[name="field_0"]', 'first_name'),
        ('input[name="field_1"]', 'last_name'),
        ('input[name="field_2"]', 'email'),
        ('input[name="field_6"]', 'country'),
        ('input[name="field_7"]', 'preferred_distributor'),
    ]

    select_fields = [
        ('select[name="field_4"]', 'oscope_need'),
    ]

    def __init__(self, config, browser='firefox', headless=False):
        if headless:
            self.display = Display(visible=0, size=(1920, 1080))
            self.display.start()

        self.driver = self._get_driver(browser)

        self.driver.set_window_size(1920, 1080)
        self.config = config

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

    def _fill_input_boxes(self):
        """ Fill all the input boxes with the data from config """
        for css_selector, field in self.input_fields:
            self.driver.find_element_by_css_selector(css_selector).send_keys(self.config[field])

    def _fill_select_boxes(self):
        """ Fill all the select boxes with data from config """
        for css_selector, field in self.select_fields:
            select_box = select.Select(self.driver.find_element_by_css_selector(css_selector))
            select_box.select_by_value(self.config[field])

    def validate_config(self):
        """ Check the config given to make sure it has all necessary fields """
        for _, field in self.input_fields:
            if field not in self.config:
                raise Exception('Config missing field: {}'.format(field))

        for _, field in self.select_fields:
            if field not in self.config:
                raise Exception('Config missing field: {}'.format(field))

    def run(self):
        """ Register for the giveaway """

        self.driver.get(
            'http://www.keysight.com/main/editorial.jspx'
            '?cc=US&lc=eng&ckey=2678002&nid=-32546.0.00&id=2678002')
        time.sleep(3)

        new_url = self.driver.find_element_by_css_selector('#intro iframe').get_attribute('src')
        self.driver.get(new_url)
        time.sleep(3)

        english_button = self.driver.find_element_by_css_selector(
            '#absolute_canvas_object_abs_element_3 a')
        english_button.click()

        time.sleep(3)

        self._fill_input_boxes()
        self._fill_select_boxes()

        submit_button = self.driver.find_element_by_css_selector('input[name="submit"]')
        submit_button.click()

        # TODO: Need to check for success here
