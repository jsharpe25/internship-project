# Created by Sharpes at 5/25/2026
Feature: Test Scenarios for University functionality


  Scenario: Verify the availability of content sections within the Bali Course tab in the University section
    Given Open the main page
    And Log in to the page
    When Select University in the sidebar
    Then Verify the University page opens
    When Click on the “Calendar” option
    And Click on the “Bali Course” option
    Then Verify "Bali Course Lessons", "Q/A sessions", and "Discover last podcast" content headers and media cards
