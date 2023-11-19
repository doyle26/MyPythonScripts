from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=news&oq=news&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDE1NjNqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8")
    page.get_by_role("link", name="NBC News Matthew Perry's 'Friends' cast mates say his loss is 'utterly devastating' 29 mins ago").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
