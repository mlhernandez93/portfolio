Feature: Website Interactions

  As a user of a website
  I want to perform basic interactions and verify page information
  So that I can ensure the website functions as expected.

@swag
  Scenario: Navigating and checking the title
    Given I navigate to "https://www.saucedemo.com/v1/index.html"
    When I login using my username "standard_user" and password "secret_sauce"
    Then the page title should contain "Swag Labs"
