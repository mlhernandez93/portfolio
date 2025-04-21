# environment.py
from playwright.sync_api import sync_playwright

def before_feature(context, feature):
    print(f"Starting feature: {feature.name}")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)  # Initialize Chromium
    context.context = context.browser.new_context()
    context.page = context.context.new_page()

def after_feature(context, feature):
    print(f"Finishing feature: {feature.name}")
    if hasattr(context, 'page'):
        context.page.close()
        context.context.close()
        context.browser.close()
        context.playwright.stop()

def before_scenario(context, scenario):
    print(f"  Starting scenario: {scenario.name}")

def after_scenario(context, scenario):
    print(f"  Finishing scenario: {scenario.name}")