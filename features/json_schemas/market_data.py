get_server_time_response = """
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "array",
      "items": {}
    },
    "result": {
      "type": "object",
      "properties": {
        "unixtime": {
          "type": "integer"
        },
        "rfc1123": {
          "type": "string"
        }
      },
      "required": [
        "unixtime",
        "rfc1123"
      ]
    }
  },
  "required": [
    "error",
    "result"
  ]
}"""

get_asset_pair_response = """
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "array",
      "items": {}
    },
    "result": {
      "type": "object",
      "properties": {
        "^X[A-Z]+": {
          "type": "object",
          "properties": {
            "altname": {
              "type": "string"
            },
            "wsname": {
              "type": "string"
            },
            "aclass_base": {
              "type": "string"
            },
            "base": {
              "type": "string"
            },
            "aclass_quote": {
              "type": "string"
            },
            "quote": {
              "type": "string"
            },
            "lot": {
              "type": "string"
            },
            "pair_decimals": {
              "type": "integer"
            },
            "lot_decimals": {
              "type": "integer"
            },
            "lot_multiplier": {
              "type": "integer"
            },
            "leverage_buy": {
              "type": "array",
              "items": [
                {
                  "type": "integer"
                }
              ]
            },
            "leverage_sell": {
              "type": "array",
              "items": [
                {
                  "type": "integer"
                }
              ]
            },
            "fees": {
              "type": "array",
              "items": [
                {
                  "type": "array",
                  "items": [
                    {
                      "type": "integer"
                    },
                    {
                      "type": "number"
                    }
                  ]
                }
              ]
            },
            "fees_maker": {
              "type": "array",
              "items": [
                {
                  "type": "array",
                  "items": [
                    {
                      "type": "integer"
                    },
                    {
                      "type": "number"
                    }
                  ]
                }
              ]
            },
            "fee_volume_currency": {
              "type": "string"
            },
            "margin_call": {
              "type": "integer"
            },
            "margin_stop": {
              "type": "integer"
            },
            "ordermin": {
              "type": "string"
            }
          },
          "required": [
            "altname",
            "wsname",
            "aclass_base",
            "base",
            "aclass_quote",
            "quote",
            "lot",
            "pair_decimals",
            "lot_decimals",
            "lot_multiplier",
            "leverage_buy",
            "leverage_sell",
            "fees",
            "fees_maker",
            "fee_volume_currency",
            "margin_call",
            "margin_stop",
            "ordermin"
          ]
        }
      },
      "required": [
        "XXBTZUSD"
      ]
    }
  },
  "required": [
    "error",
    "result"
  ]
}"""