open_orders_get_response = """{
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
        "open": {
          "type": "object",
          "patternProperties": {
            "^[A-Z0-9]{6}-[A-Z0-9]{5}-[A-Z0-9]{6}$": {
              "type": "object",
              "properties": {
                "refid": {
                  "type": "null"
                },
                "userref": {
                  "type": "integer"
                },
                "status": {
                  "type": "string"
                },
                "opentm": {
                  "type": "number"
                },
                "starttm": {
                  "type": "integer"
                },
                "expiretm": {
                  "type": "integer"
                },
                "descr": {
                  "type": "object",
                  "properties": {
                    "pair": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "ordertype": {
                      "type": "string"
                    },
                    "price": {
                      "type": "string"
                    },
                    "price2": {
                      "type": "string"
                    },
                    "leverage": {
                      "type": "string"
                    },
                    "order": {
                      "type": "string"
                    },
                    "close": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "pair",
                    "type",
                    "ordertype",
                    "price",
                    "price2",
                    "leverage",
                    "order",
                    "close"
                  ]
                },
                "vol": {
                  "type": "string"
                },
                "vol_exec": {
                  "type": "string"
                },
                "cost": {
                  "type": "string"
                },
                "fee": {
                  "type": "string"
                },
                "price": {
                  "type": "string"
                },
                "stopprice": {
                  "type": "string"
                },
                "limitprice": {
                  "type": "string"
                },
                "misc": {
                  "type": "string"
                },
                "oflags": {
                  "type": "string"
                }
              },
              "required": [
                "refid",
                "userref",
                "status",
                "opentm",
                "starttm",
                "expiretm",
                "descr",
                "vol",
                "vol_exec",
                "cost",
                "fee",
                "price",
                "stopprice",
                "limitprice",
                "misc",
                "oflags"
              ]
            }
          },
          "additionalProperties": false
        }
      },
      "required": [
        "open"
      ]
    }
  },
  "required": [
    "error",
    "result"
  ]
}"""