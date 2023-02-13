from playwright.sync_api import Page
from .util.elements_identifiers import (
    FILTER_INIT_DATE,
    FILTER_END_DATE,
    FILTER_BUTTON
)

def set_filter(page: Page, date):
    page.type(FILTER_INIT_DATE, date['init_date']) # dd-mm-yyyy
    page.type(FILTER_END_DATE, date['end_date']) # dd-mm-yyyy

    page.click(FILTER_BUTTON)