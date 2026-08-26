from playwright.sync_api import sync_playwright


DESCRIPTION_SELECTOR = (
    ".description__text.description__text--rich "
    ".show-more-less-html__markup"
)


def fetch_rendered_html(url: str) -> str:

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            channel="chrome",
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=30000,
        )

        page.wait_for_selector(
            DESCRIPTION_SELECTOR,
            state="attached",
            timeout=10000,
        )

        html = page.content()

        browser.close()

        return html