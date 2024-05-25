Feature: Image Classification

  Scenario: Classify image of socks
    Given I have passed an image of socks to the model
    Then it is classified as Accessories

  Scenario: Classify image of shoes
    Given I have passed an image of shoes to the model
    Then it is classified as Footwear

  Scenario: Classify image of a tracksuit
    Given I have passed an image of a tracksuit to the model
    Then it is classified as Apparel
