Feature: Verify Lineate Bot Availability on Website for Interaction
  Scenario: Access Chat Functionality and Receive a Greeting Message
    Given I am on the homepage
    When Chat icon is displayed and I click on the chat icon
    And I see greetings messages
    And I click on the "I want to talk to Sales" chat button
    And I click on the "front-end development" chat button
    And I click on the "B2B" chat button
    And I type "I love python" in the chat
    And I type "I love selenium" in the chat
    And I type "I love BDD" in the chat
    And I click on the "Director" chat button
    And I type "tester_bachukilabadze@gmail.com" in the chat
    Then The chat is ended
