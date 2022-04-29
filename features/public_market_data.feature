# Created by automationleg at 27/04/2022
Feature: Set of scenarios to validate public MarketData endpoints
  # Enter feature description here

  @api @task-1a
  Scenario: Validate "Get Server Time" via /Time endpoint
    Given Request is sent to "/0/public/Time" URI
    Then Response is "200"
    And Json response is matching the "get_server_time_response" json schema from "market_data" file


  @api @task-1b
  Scenario: Validate selected fields in response from /AssetPairs endpoint
    Given Request is sent to "/0/public/AssetPairs?pair=XXBTZUSD" URI
    Then Response is "200"
    And Field "$.result..wsname" in response json is equal to "XBT/USD"
    And Field "$.result..aclass_base" in response json is equal to "currency"
    And Field "$.result..base" in response json is equal to "XXBT"
    And Field "$.result..aclass_quote" in response json is equal to "currency"
    And Field "$.result..quote" in response json is equal to "ZUSD"
    And Field "$.result..quote" in response json is equal to "ZUSD"
    And Field "$.result..lot" in response json is equal to "unit"
    And Field "$.result..pair_decimals" in response json is equal to "1"
    And Field "$.result..lot_decimals" in response json is equal to "8"
    And Field "$.result..lot_multiplier" in response json is equal to "1"
    And List Field "$.result..leverage_buy[*]" in response json contains the following integer values
      | value |
      | 2     |
      | 3     |
      | 4     |
      | 5     |
    And List Field "$.result..fees[*]" in response json contains the following fee value pairs
      | size     | fee  |
      | 50000    | 0.24 |
      | 100000   | 0.22 |
      | 250000   | 0.2  |
      | 500000   | 0.18 |
      | 1000000  | 0.16 |
      | 2500000  | 0.14 |
      | 5000000  | 0.12 |
      | 10000000 | 0.1  |
    And List Field "$.result..fees_maker[*]" in response json contains the following fee value pairs
      | size     | fee  |
      | 50000    | 0.14 |
      | 100000   | 0.12 |
      | 250000   | 0.1  |
      | 500000   | 0.08 |
      | 1000000  | 0.06 |
      | 2500000  | 0.04 |
      | 5000000  | 0.02 |
      | 10000000 | 0.0  |
    And List Field "$.result..leverage_sell[*]" in response json contains the following integer values
      | value |
      | 2     |
      | 3     |
      | 4     |
      | 5     |
    And Field "$.result..fee_volume_currency" in response json is equal to "ZUSD"
    And Field "$.result..margin_call" in response json is equal to "80"
    And Field "$.result..margin_stop" in response json is equal to "40"
    And Field "$.result..ordermin" in response json is equal to "0.0001"


  @api @task-1b
  Scenario: Validate full json response from /AssetPairs endpoint
    Given Request is sent to "/0/public/AssetPairs?pair=XXBTZUSD" URI
    Then Response is "200"
    And Json response is matching the "get_asset_pair_response" json schema from "market_data" file
    And Json response is equal to
    """
    {"error": [],
     "result": {"XXBTZUSD": {"altname": "XBTUSD",
       "wsname": "XBT/USD",
       "aclass_base": "currency",
       "base": "XXBT",
       "aclass_quote": "currency",
       "quote": "ZUSD",
       "lot": "unit",
       "pair_decimals": 1,
       "lot_decimals": 8,
       "lot_multiplier": 1,
       "leverage_buy": [2, 3, 4, 5],
       "leverage_sell": [2, 3, 4, 5],
       "fees": [[0, 0.26],
        [50000, 0.24],
        [100000, 0.22],
        [250000, 0.2],
        [500000, 0.18],
        [1000000, 0.16],
        [2500000, 0.14],
        [5000000, 0.12],
        [10000000, 0.1]],
       "fees_maker": [[0, 0.16],
        [50000, 0.14],
        [100000, 0.12],
        [250000, 0.1],
        [500000, 0.08],
        [1000000, 0.06],
        [2500000, 0.04],
        [5000000, 0.02],
        [10000000, 0.0]],
       "fee_volume_currency": "ZUSD",
       "margin_call": 80,
       "margin_stop": 40,
       "ordermin": "0.0001"}}}
    """