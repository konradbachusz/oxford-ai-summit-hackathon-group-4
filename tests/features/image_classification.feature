Feature: Image Classification

  Scenario: Classify image of socks
    Given I have passed an image of socks to the model
    Then it is classified as Accessories
