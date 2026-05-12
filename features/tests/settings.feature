# Created by Sharpe at 4/28/2026
Feature: Test Scenarios for Settings functionality

  Scenario: User can verify their referral link on the Dashboard
    Given Open the main page
    And Log in to the page
    When Select profile in the sidebar
    And Select "My clients" profile option
    And Select "Dashboard"
    Then Verify Dashboard page is opened
    And Verify the referral link contains "https://soft.reelly.io/sign-up"

  Scenario: User can verify the presence of the "Contact us for details" form in the "For agency" section
    Given Open the main page
    And Log in to the page
    When Select profile in the sidebar
    And Select "For agency" profile option
    Then Verify the Agency page opens
    When Scroll to the "Contact us for details" form
    Then Verify the "Contact us for details" form is available
