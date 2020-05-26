from .base_page import BasePage
from .locators import BasePageLocators

languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty."
}


class BasketPage(BasePage):
    def should_not_items_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS_IN_BASKET), 'The basket is not empty'
        assert self.is_disappeared(*BasePageLocators.ITEMS_IN_BASKET), 'The basket is not empty'

    def should_basket_empty_text(self):
        assert languages[self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")] in \
               self.browser.find_element(*BasePageLocators.BASKET_EMPTY_TEXT).text, 'no text that the basket is empty'