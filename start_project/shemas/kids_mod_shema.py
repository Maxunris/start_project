kids = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "_id": {
      "type": "string"
    },
    "ab": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "exp_id": {
            "type": "integer"
          },
          "exp_name": {
            "type": "string"
          },
          "group_id": {
            "type": "integer"
          },
          "group_name": {
            "type": "string"
          }
        },
        "required": [
          "exp_id",
          "exp_name",
          "group_id",
          "group_name"
        ]
      }
    },
    "apple_id": {
      "type": "null"
    },
    "apple_info": {
      "type": "object"
    },
    "authentication_token": {
      "type": "string"
    },
    "contact_info": {
      "type": "object",
      "properties": {
        "email_is_confirmed": {
          "type": "boolean"
        }
      },
      "required": [
        "email_is_confirmed"
      ]
    },
    "country_code": {
      "type": "string"
    },
    "current_country_code": {
      "type": "string"
    },
    "date_created": {
      "type": "string"
    },
    "devices": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "last_use": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "uid": {
            "type": "string"
          }
        },
        "required": [
          "last_use",
          "name",
          "type",
          "uid"
        ]
      }
    },
    "email": {
      "type": "string"
    },
    "externals": {
      "type": "array",
      "items": {
        "items": {}
      }
    },
    "facebook_id": {
      "type": "null"
    },
    "facebook_info": {
      "type": "object"
    },
    "google_id": {
      "type": "null"
    },
    "is_registered": {
      "type": "boolean"
    },
    "language": {
      "type": "object",
      "properties": {
        "audio": {
          "type": "string"
        },
        "content_lang": {
          "type": "array",
          "items": {
            "items": {}
          }
        },
        "interface": {
          "type": "string"
        },
        "subtitles": {
          "type": "string"
        }
      },
      "required": [
        "audio",
        "content_lang",
        "interface",
        "subtitles"
      ]
    },
    "mf_info": {
      "type": "object",
      "properties": {
        "is_mf": {
          "type": "boolean"
        },
        "mf_pop_up": {
          "type": "null"
        },
        "to_paid_period": {
          "type": "null"
        },
        "to_paid_price": {
          "type": "null"
        },
        "to_trial_period": {
          "type": "null"
        }
      },
      "required": [
        "is_mf",
        "mf_pop_up",
        "to_paid_period",
        "to_paid_price",
        "to_trial_period"
      ]
    },
    "phone": {
      "type": "string"
    },
    "pin_status": {
      "type": "string"
    },
    "profile_for_child": {
      "type": "boolean"
    },
    "profile_id": {
      "type": "string"
    },
    "promo_manager": {
      "type": "boolean"
    },
    "segmentation_id": {
      "type": "string"
    },
    "status_gdpr": {
      "type": "null"
    },
    "subscriptions": {
      "type": "array",
      "items": {
        "items": {}
      }
    },
    "tags": {
      "type": "array",
      "items": {
        "items": {}
      }
    },
    "traffic_source": {
      "type": "object"
    },
    "trial_is_available": {
      "type": "boolean"
    },
    "type": {
      "type": "string"
    },
    "virtual": {
      "type": "boolean"
    },
    "vk_id": {
      "type": "null"
    },
    "vk_info": {
      "type": "object"
    },
    "yandex_id": {
      "type": "null"
    },
    "yandex_info": {
      "type": "object"
    }
  },
  "required": [
    "_id",
    "ab",
    "apple_id",
    "apple_info",
    "authentication_token",
    "contact_info",
    "country_code",
    "current_country_code",
    "date_created",
    "devices",
    "email",
    "externals",
    "facebook_id",
    "facebook_info",
    "google_id",
    "is_registered",
    "language",
    "mf_info",
    "phone",
    "pin_status",
    "profile_for_child",
    "profile_id",
    "promo_manager",
    "segmentation_id",
    "status_gdpr",
    "subscriptions",
    "tags",
    "traffic_source",
    "trial_is_available",
    "type",
    "virtual",
    "vk_id",
    "vk_info",
    "yandex_id",
    "yandex_info"
  ]
}