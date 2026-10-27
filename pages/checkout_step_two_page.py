from pages.base_page import BasePage
from pages.checkout_complete_page import CheckoutCompletePage

class CheckoutStepTwoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.finish_button = page.locator("#finish")

    def finish_checkout(self):
        self.finish_button.click()
        return CheckoutCompletePage(self.page)