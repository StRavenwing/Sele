import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument(f'--lang={user_language}')
    options.add_argument(f'accept-language={user_language}')
    
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def user_language(request):
    return request.config.getoption("--language")

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="ru", help="language"
    )
