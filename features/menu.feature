Feature: Verify proper functioning of menu items and ability to navigate through pages.

    #  Scenario Outline: Bevri
    #    Given I am on the homepage
    #    When I click on the "<page>" button
    #    Then I am on the "<page>" page
    #    And Title contains "<page>"
    #
    #    Examples:
    #    |page|
    #    |Who we are|
    #    |What we do|
    #    |Our Work  |
    #    |Big Ideas |
    #    |Careers   |
    #    |Blog      |
    #    |Contact   |

    Scenario: Who we are
    Given I am on the homepage
    When I click on the "Who we are" button
    Then I am on the "Who we are" page
    And Title contains "Who we are"

    Scenario: What we do
    Given I am on the homepage
    When I click on the "What we do" button
    Then I am on the "What we do" page
    And Title contains "What we do"

    Scenario: Our work
    Given I am on the homepage
    When I click on the "Our work" button
    Then I am on the "Our work" page
    And Title contains "Our work"

    Scenario: Big ideas
    Given I am on the homepage
    When I click on the "Big ideas" button
    Then I am on the "Big ideas" page
    And Title contains "Big ideas"

    Scenario: Careers
    Given I am on the homepage
    When I click on the "Careers" button
    Then I am on the "Careers" page
    And Title contains "Careers"

    Scenario: Blog
    Given I am on the homepage
    When I click on the "Blog" button
    Then I am on the "technology-insights" page
    And Title contains "Technology Resources"

    Scenario: Contact
    Given I am on the homepage
    When I click on the "Contact" button
    Then I am on the "Contact" page
    And Title contains "Contact"