# Created by Sharpe at 4/28/2026
Feature: Test Scenarios for Settings functionality

  Scenario: User can verify their referral link on the Dashboard
    Given Open the main page
    And Log in to the page
    When Select "Settings" in the sidebar
    And Select "My clients" profile option
    And Select "Dashboard"
    Then Verify Dashboard page is opened
    And Verify the referral link contains "https://soft.reelly.io/sign-up"
