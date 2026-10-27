from pages.base_page import BasePage
from pages.cart_page import CartPage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_item_to_cart(self):
        self.add_to_cart_button.click()
        return self

    def go_to_cart(self):
        self.cart_icon.click()
        return CartPage(self.page)