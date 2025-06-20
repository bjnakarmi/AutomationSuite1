from utils.config import CONFIG
from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize('email,password', [(CONFIG['login_email'], CONFIG['login_password'])])
def test_login(browser, email, password):
    browser.get(CONFIG['base_url'])
    loggin_page = LoginPage(browser)
    loggin_page.set_email(email)
    loggin_page.set_password(password)
    loggin_page.click_login_button()
    assert browser.title == 'Piiink Admin Panel'

