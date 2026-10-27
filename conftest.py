import pytest

@pytest.fixture
def site_url():
    """Фикстура, предоставляющая базовый URL сайта"""
    return "https://www.saucedemo.com/"