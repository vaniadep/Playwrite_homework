from pages.base_page import BasePage
from pages.checkout_step_one_page import CheckoutStepOnePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator("#checkout")

    def proceed_to_checkout(self):
        self.checkout_button.click()
        return CheckoutStepOnePage(self.page)