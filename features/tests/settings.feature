# Created by Sharpe at 4/28/2026
Feature: Test Scenarios for Dashboard functionality

  Scenario: User can verify their referral link on the Dashboard
    Given Open the main page
    And Log in to the page
    When Click on "Settings" in the sidebar
    And Click on "My clients" profile button
    And Click on "Dashboard" tab
    Then Verify Dashboard page is opened
    And Verify the referral link contains "https://soft.reelly.io/sign-up"
