Feature: Product Management

  Background:
    Given the following products exist:
      | Name         | Description         | Category    | Price  | In Stock |
      | Product A    | Sample description  | Electronics | 99.99  | true     |
      | Product B    | Another product     | Apparel     | 49.99  | true     |
      | Product C    | Great product       | Electronics | 149.99 | false    |

  Scenario: Read a Product by ID
    When I request the product with ID 1
    Then I receive a product with the following details:
      | Name       | Description         | Category    | Price  | In Stock |
      | Product A  | Sample description  | Electronics | 99.99  | true     |

  Scenario: Update a Product by ID
    When I update the product with ID 2 to have the following details:
      | Name       | Description      | Category    | Price  | In Stock |
      | New Name   | Updated product  | Apparel     | 59.99  | false    |
    Then the product with ID 2 should be updated to:
      | Name      | Description      | Category    | Price  | In Stock |
      | New Name  | Updated product  | Apparel     | 59.99  | false    |

  Scenario: Delete a Product by ID
    When I delete the product with ID 3
    Then the product with ID 3 should be deleted
    And I should not be able to request the product with ID 3

  Scenario: List All Products
    When I request the list of all products
    Then I receive a list with at least 3 products

  Scenario: Search Products by Name
    When I search for products by name "Product A"
    Then I receive a list with the following product(s):
      | Name       | Description         | Category    | Price  | In Stock |
      | Product A  | Sample description  | Electronics | 99.99  | true     |

  Scenario: Search Products by Category
    When I search for products by category "Electronics"
    Then I receive a list with the following product(s):
      | Name       | Description         | Category    | Price  | In Stock |
      | Product A  | Sample description  | Electronics | 99.99  | true     |
      | Product C  | Great product       | Electronics | 149.99 | false    |

  Scenario: Search Products by Availability
    When I search for products by availability "true"
    Then I receive a list with the following product(s):
      | Name       | Description         | Category    | Price  | In Stock |
      | Product A  | Sample description  | Electronics | 99.99  | true     |
      | Product B  | Another product     | Apparel     | 49.99  | true     |

