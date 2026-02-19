# Created by Sharpes a t 2/11/2026
Feature: Test Scenarios for Off-plan functionality


  @smoke
  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page
    And Log in to the page
    When Verify Off-plan page opened
    And Filter the products by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range (1200000 - 2000000)
