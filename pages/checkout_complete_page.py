from pages.base_page import BasePage
from playwright.sync_api import expect

class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.complete_header = page.locator(".complete-header")

    def verify_order_success(self, expected_text: str = "Thank you for your order!"):
        expect(self.complete_header).to_have_text(expected_text)
        return self