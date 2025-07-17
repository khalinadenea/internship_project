
Feature: Accessing the User Guide


  Scenario: User can open User Guide page and see the lesson video title
    Given the user navigates to the main page
    And the user clicks on the sign in button
    When the user logs in with valid credentials
   When the user clicks on the settings option
    And the user clicks on the User Guide option
   Then the User Guide page should open with the lesson video title visible