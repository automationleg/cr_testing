# Created by kramuk at 27/04/2022
Feature: Set of scenarios to validate public MarketData endpoints
  # Enter feature description here

  @api @task-1
  Scenario: Validate "Get Server Time" via /Time endpoint
    Given Request is sent to "/0/public/Time" URI
    Then Response is "200"
    And Json response is matching the "get_server_time_response" json schema from "market_data" file


  @api @task-1
  Scenario: Validate "Get Asset Info" via /AssetPairs endpoint
    Given Request is sent to "/0/public/AssetPairs?pair=XXBTZUSD" URI
    Then Response is "200"
    And Json response is matching the "get_asset_pair_response" json schema from "market_data" file