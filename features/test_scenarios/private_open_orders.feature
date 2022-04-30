# Created by automationleg at 28/04/2022
Feature: Test UserData endpoints
  Set of scenarios to validate private UserData endpoints
  My assumption in first scenario is that I don't know order Ids for opened orders

  @api @task-2
  Scenario: Validate "Get Open Orders" via /OpenOrders endpoint
    Given POST Request is sent to get "/0/private/OpenOrders" User Data
    Then Response is "200"
    And Json response is matching the "open_orders_get_response" json schema from "user_data" file
    And There are 2 opened orders found in response
    And Opened orders with corresponding descr attributes are found in the response
      | order                                  | pair    | type | ordertype | price   | leverage |
      | buy 0.00500000 ETHUSDT @ limit 2000.00 | ETHUSDT | buy  | limit     | 2000.00 | none     |
      | buy 0.00050000 XBTUSDT @ limit 29000.0 | XBTUSDT | buy  | limit     | 29000.0 | none     |


  @api @task-2
  Scenario Outline: Validate "Get Open Orders" for specific orders via /OpenOrders endpoint
    Given POST Request is sent to get "/0/private/OpenOrders" User Data
      """
      {"trades": "false"}
      """
    Then Response is "200"
    And Json response is matching the "open_orders_get_response" json schema from "user_data" file
    And Field "$.result.<status>.<order_id>.descr.pair" in response json is equal to "<pair>"
    And Field "$.result.<status>.<order_id>.descr.type" in response json is equal to "<type>"
    And Field "$.result.<status>.<order_id>.descr.ordertype" in response json is equal to "<ordertype>"
    And Field "$.result.<status>.<order_id>.descr.price" in response json is equal to "<price>"
    And Field "$.result.<status>.<order_id>.descr.leverage" in response json is equal to "<leverage>"
    And Field "$.result.<status>.<order_id>.descr.order" in response json is equal to "<type> <vol> <pair> @ <ordertype> <price>"
    And Field "$.result.<status>.<order_id>.vol" in response json is equal to "<vol>"
    And Field "$.result.<status>.<order_id>.fee" in response json is equal to "<fee>"
    And Field "$.result.<status>.<order_id>.oflags" in response json is equal to "<oflags>"
    And Timestamp field "$.result.<status>.<order_id>.opentm" for order id "<order_id>" equal to date: "2022-04-29"

  Examples: Open orders
    | order_id            | status | pair    | type | ordertype | price   | leverage | vol        | fee     | oflags |
    | OQ2N7S-7F2QH-U4EG3H | open   | ETHUSDT | buy  | limit     | 2000.00 | none     | 0.00500000 | 0.00000 | fciq   |
    | OBTWLQ-LDUJG-R3I4XB | open   | XBTUSDT | buy  | limit     | 29000.0 | none     | 0.00050000 | 0.00000 | fciq   |