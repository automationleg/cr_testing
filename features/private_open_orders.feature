# Created by kramuk at 28/04/2022
Feature: Test UserData endpoints
  Set of scenarios to validate private UserData endpoints

  @api @task-2
  Scenario: Validate "Get Open Orders" via /OpenOrders endpoint
    Given Request is sent to get "/0/private/OpenOrders" User Data
    Then Response is "200"
