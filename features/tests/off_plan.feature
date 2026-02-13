# Created by Sharpes at 2/11/2026
Feature: Test Scenarios for Off-plan functionality


  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page
    And Log in to the page
    When Click on “Off-plan” in the left side menu
    And Verify Off-plan page opened
    And Filter the products by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range (1200000 - 2000000)
