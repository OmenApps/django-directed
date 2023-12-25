"""This is a sample test for the django-directed Django app with Playwright using Docker Compose."""
import logging
import re

import pytest
import requests
from playwright.sync_api import Page
from playwright.sync_api import expect
from requests.exceptions import ConnectionError


def is_responsive(url):
    """Check if a response is returned for a provided url."""
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def http_service():
    """Ensure that the service is up and responsive."""
    url = "http://0.0.0.0:8111/"
    try:
        response = requests.get(url, timeout=60)
        logging.info(f"test_status_code response: {response} for url: {url}")

        assert response.status_code == 200
    except ConnectionError as e:
        logging.info(f"ConnectionError: {e}")
    return url


def test_has_corrrect_title(http_service, page: Page):
    """Test that the page has the correct title."""
    try:
        page.goto(http_service)

        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("The install worked successfully! Congratulations!"))
    except ConnectionError as e:
        logging.info(f"ConnectionError: {e}")
