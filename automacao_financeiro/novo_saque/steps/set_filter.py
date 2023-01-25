from playwright.sync_api import Page
from .util.elements_identifiers import (
    FILTER_INIT_DATE,
    FILTER_END_DATE,
    FILTER_BUTTON
)

def set_filter(page: Page):
    page.type(FILTER_INIT_DATE, '01-01-2023') # dd-mm-yyyy
    page.type(FILTER_END_DATE, '25-01-2023') # dd-mm-yyyy

    page.click(FILTER_BUTTON)