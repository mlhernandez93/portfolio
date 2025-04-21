# features/steps/my_steps.py
from behave import given, when, then
from playwright.sync_api import Page
import time

@given(u'I navigate to "{url}"')
def step_impl(context, url: str):
    context.page.goto(url)

@when(u'I logged in using my username "{username}" and password "{password}"')
def step_impl(context, username: str, password: str):
    context.page.fill('#user-name', username)
    time.sleep(3)
    context.page.fill('#password', password)
    time.sleep(3)
    context.page.click('#login-button')

@then(u'the page title should contain "{expected_title}"')
def step_impl(context, expected_title: str):
    time.sleep(10)
    assert expected_title in context.page.title()