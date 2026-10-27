from conftest import site_url
from pages.login_page import LoginPage

def test_successful_purchase(page, site_url):
    # Реализация пользовательского пути с помощью цепочки вызовов (Method Chaining / Fluent Interface)
    (
        LoginPage(page)
        .open(site_url)
        .login("standard_user", "secret_sauce")
        .add_item_to_cart()
        .go_to_cart()
        .proceed_to_checkout()
        .fill_shipping_info("Иван", "Иванов", "123456")
        .finish_checkout()
        .verify_order_success("Thank you for your order!")
    )