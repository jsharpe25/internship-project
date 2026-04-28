# Created by Sharpe at 2/11/2026
Feature: Test Scenarios for Off-plan functionality


  @smoke
  Scenario: User can filter off-plan projects by Developer
    Given Open the main page
    And Log in to the page
    When Verify Off-plan page opened
    And Filter by Developer
    Then Verify results are filtered by Developer


  @smoke
  Scenario: User can filter off-plan projects by Per unit Price range
    Given Open the main page
    And Log in to the page
    When Verify Off-plan page opened
    And Filter the projects by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range (1200000 - 2000000)
