"""Store tests related to start page"""
# from time import sleep
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\Malini\PycharmProjects\QaComplex\drivers\chromedriver.exe")
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        driver.find_element_by_xpath(".//button[contains(text(), 'Sign Out')]").click()
        sleep(1)

    @pytest.fixture(scope="function")
    def register(self, driver):
        registered_user = self.register_user(driver)
        driver.find_element_by_xpath(".//button[contains(text(), 'Sign Out')]").click()
        sleep(1)
        return registered_user

    def register_user(self, driver):
        """Fill required fields and press button"""
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.debug("Open page")

        # fill email, login and password fields

        username_value = f"Name{self.variety}"
        username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        username.clear()
        username.send_keys(username_value)
        self.log.info("Valid login is entered")
        sleep(1)

        email_value = f"user{self.variety}@com.ua"
        email = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        email.clear()
        email.send_keys(email_value)
        self.log.info("Valid email is entered")
        sleep(1)

        password_value = f"PassWord{self.variety}"
        password = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Invalid pass entered")
        sleep(1)

        # Click on Sign up button
        driver.find_element_by_xpath(".//button[@type='submit']").click()
        sleep(1)
        self.log.info("User was registered")

        return username_value, email_value, password_value

    def test_empty_fields_login(self, driver):
        """
        - Open start page
        - Clear password and login fields
        - Click on Sign In button
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear required fields
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        self.log.info("Fields were cleared")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        sign_in_button.click()
        self.log.info("Clicked on 'Sign In'")

        # Verify error message
        error_message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")
        assert error_message.text == 'Invalid username / password'
        self.log.info("Error message match to expected")

    def test_invalid_login(self, driver: object):
        """
        - Open start page
        - Clear password and login fields
        - Enter invalid login and password
        - Click on Sign In button
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear required fields and enter invalid login and password
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("anna")
        # password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("Sho")
        sleep(1)
        self.log.info("Fields were cleared and invalid login entered")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        sign_in_button.click()
        self.log.info("Clicked on 'Sign In'")

        # Verify error message
        error_message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")
        assert error_message.text == 'Invalid username / password'
        self.log.info("Error message match to expected")

        # Sign up tests

    def test_short_login_sign_up(self, driver: object):
        """
        - Open start page
        - Clear login field
        - Enter login with 2 characters
        - Clear email field
        - Enter valid email
        - Clear password field
        - Enter valid password
        - Click on "Sign up for OurApp" button
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear login field and enter invalid login
        username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        username.clear()
        username.send_keys("a1")
        self.log.info("Short login entered")
        sleep(1)

        # Verify error message
        error_message = driver.find_element_by_xpath(
            ".//div[contains(text(),  'Username must be at least 3 characters.')]")
        assert error_message.text == "Username must be at least 3 characters."
        self.log.info("Error message match to expected")

    def test_special_sumbols_login_sign_up(self, driver: object):
        """
        - Open start page
        - Clear login field
        - Enter login with special symbols
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear login field and enter invalid login
        username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        username.clear()
        username.send_keys("$%^&")
        self.log.info("Special symbols login entered")
        sleep(2)

        # Verify error message
        error_message = driver.find_element_by_xpath(
            ".//div[contains(text(),  'Username can only contain letters and numbers.')]")
        assert error_message.text == "Username can only contain letters and numbers."
        self.log.info("Error message match to expected")


    def test_spaces_login_sign_up(self, driver: object):
        """
        - Open start page
        - Clear login field
        - Enter login with only spaces
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear login field and enter invalid login
        username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        username.clear()
        username.send_keys("    ")
        self.log.info("Spaces only login entered")
        sleep(1)

        # Verify error message
        error_message = driver.find_element_by_xpath(
            ".//div[contains(text(),  'Username can only contain letters and numbers.')]")
        assert error_message.text == "Username can only contain letters and numbers."
        self.log.info("Error message match to expected")

    def test_taken_login_sign_up(self, driver: object):
        """
        - Open start page
        - Clear login field
        - Enter login that is already taken ("123")
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear login field and enter already taken login login
        username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        username.clear()
        username.send_keys("123")
        self.log.info("Already taken login is entered")
        sleep(2)

        # Verify error message
        error_message = driver.find_element_by_xpath(".//div[contains(text(),  'That username is already taken.')]")
        assert error_message.text == "That username is already taken."
        self.log.info("Error message match to expected")

    def test_invalid_email_sign_up(self, driver: object):
        """
        - Open start page
        - Clear login field
        - Enter valid login
        - Clear email field
        - Enter invalid email
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear login field and enter valid login
        username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        username.clear()
        username.send_keys("Anna12345")
        self.log.info("Valid login is entered")
        sleep(1)

        # Clear email field and enter valid email
        email = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        email.clear()
        email.send_keys("test.ua")
        self.log.info("Invalid email is entered")
        sleep(1)

        # Verify error message
        error_message = driver.find_element_by_xpath(
            ".//div[contains(text(),  'You must provide a valid email address.')]")
        assert error_message.text == "You must provide a valid email address."
        self.log.info("Error message match to expected")

    def test_invalid_password_sign_up(self, driver: object):
        """
        - Open start page
        - Clear login field
        - Enter valid login
        - Clear email field
        - Enter invalid email
        - Clear password field
        - Enter invalid password
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear login field and enter valid login
        username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        username.clear()
        username.send_keys("Anna12345")
        self.log.info("Valid login is entered")
        sleep(1)

        # Clear email field and enter invalid email
        email = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        email.clear()
        email.send_keys("test@com.ua")
        self.log.info("Valid email is entered")
        sleep(1)

        # Clear password field and enter valid pass
        password = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        password.clear()
        password.send_keys("124")
        self.log.info("Invalid pass entered")
        sleep(1)

        # Verify error message
        error_message = driver.find_element_by_xpath(
            ".//div[contains(text(),  'Password must be at least 12 characters.')]")
        assert error_message.text == "Password must be at least 12 characters."
        self.log.info("Error message match to expected")

    def test_register(self, driver, logout):
        """
        - Open start page
        - fill email, login and password fields
        - click on Sign Up button
        - Verify register success
        """
        username_value = self.register_user(driver)[0]
        self.log.info("User was registered")

        # Verify register message
        hello_message = driver.find_element_by_xpath(".//h2")
        assert username_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
        assert driver.find_element_by_xpath(".//strong").text == username_value.lower()
        self.log.info("Registration was successful and verified.")

    def test_sign_in_1(self, register, driver, logout):
        """
        - Open start page
        - Clear login field
        - Enter valid login
        - Clear password field
        - Enter valid password
        - Click on "Sign in button"
        - Validate successful log in
        - Click "Sign out"
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        username_value, _, password_value = register

        # Clear login field and enter valid login
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys(username_value)
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Valid are filled with valid username and password")
        sleep(1)

        # Click on Sign in button
        sign_in_button = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        sign_in_button.click()
        self.log.info("Clicked on 'Sign In'")

        # Verify register message
        hello_message = driver.find_element_by_xpath(".//h2")
        assert username_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
        assert driver.find_element_by_xpath(".//strong").text == username_value.lower()
        self.log.info("Registration was successful and verified.")


