search = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "_cls": {
            "type": "string",
            "enum": [
              "Product.Series",
              "Product.Movie"
            ]
          },
          "_id": {
            "type": "string"
          },
          "alias": {
            "type": "string"
          },
          "background": {
            "type": "object",
            "properties": {
              "image_15x": {
                "type": "string"
              },
              "image_1x": {
                "type": "string"
              }
            },
            "required": [
              "image_15x",
              "image_1x"
            ]
          },
          "badges": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "alias": {
                  "type": "string"
                },
                "background_color": {
                  "type": "string",
                  "enum": [
                    "#FF2800"
                  ]
                },
                "background_color_right": {
                  "type": "string",
                  "enum": [
                    ""
                  ]
                },
                "id": {
                  "type": "string"
                },
                "image_1x": {
                  "type": "null"
                },
                "name": {
                  "type": "string",
                  "enum": [
                    "новые серии под постером"
                  ]
                },
                "size": {
                  "type": "string",
                  "enum": [
                    "medium"
                  ]
                },
                "structure": {
                  "type": "string",
                  "enum": [
                    "single"
                  ]
                },
                "text": {
                  "type": "string",
                  "enum": [
                    "НОВЫЕ СЕРИИ"
                  ]
                },
                "text_color": {
                  "type": "string",
                  "enum": [
                    "#FFFFFF"
                  ]
                },
                "text_color_right": {
                  "type": "string",
                  "enum": [
                    ""
                  ]
                },
                "text_right": {
                  "type": "string",
                  "enum": [
                    ""
                  ]
                },
                "type": {
                  "type": "string",
                  "enum": [
                    "badge"
                  ]
                },
                "under_logo_position": {
                  "type": "boolean"
                }
              },
              "required": [
                "alias",
                "background_color",
                "background_color_right",
                "id",
                "image_1x",
                "name",
                "size",
                "structure",
                "text",
                "text_color",
                "text_color_right",
                "text_right",
                "type",
                "under_logo_position"
              ]
            }
          },
          "banner": {
            "type": "object",
            "properties": {
              "image_15x": {
                "type": "null"
              },
              "image_1x": {
                "type": "null"
              }
            },
            "required": [
              "image_15x",
              "image_1x"
            ]
          },
          "description": {
            "type": "string"
          },
          "download_options": {
            "type": "string"
          },
          "downloadable": {
            "type": "boolean"
          },
          "drm_encrypted": {
            "type": "boolean"
          },
          "duration": {
            "type": "integer",
            "enum": [
              0,
              1484760,
              1331280
            ]
          },
          "enabled_for_partner": {
            "type": "boolean"
          },
          "for_kids": {
            "type": "boolean"
          },
          "genres": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "slug": {
                  "type": "string",
                  "enum": [
                    "/genres/cartoon",
                    "/genres/kids",
                    "/genres/entertainment",
                    "/genres/nurseryrhymes",
                    "/genres/adventure"
                  ]
                },
                "title": {
                  "type": "string",
                  "enum": [
                    "Мультфильм",
                    "Для детей",
                    "Развлечения",
                    "Музыка",
                    "Приключение"
                  ]
                }
              },
              "required": [
                "slug",
                "title"
              ]
            }
          },
          "genres_string": {
            "type": "string"
          },
          "horizontal": {
            "type": "object",
            "properties": {
              "image_15x": {
                "type": "string"
              },
              "image_1x": {
                "type": "string"
              }
            },
            "required": [
              "image_15x",
              "image_1x"
            ]
          },
          "hot_content": {
            "type": "boolean"
          },
          "in_subscription": {
            "type": "boolean"
          },
          "is_4k": {
            "type": "boolean"
          },
          "is_51": {
            "type": "boolean"
          },
          "is_disabled": {
            "type": "boolean"
          },
          "is_free": {
            "type": "boolean"
          },
          "is_maxmind_proxy_enabled": {
            "type": "boolean"
          },
          "is_premier": {
            "type": "boolean"
          },
          "is_preview": {
            "type": "boolean"
          },
          "is_top250": {
            "type": "boolean"
          },
          "logotype": {
            "type": "object",
            "properties": {
              "image_15x": {
                "type": "string"
              },
              "image_1x": {
                "type": [
                  "string",
                  "null"
                ]
              }
            },
            "required": [
              "image_15x",
              "image_1x"
            ]
          },
          "meta": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "_id": {
                  "type": "string"
                },
                "alias": {
                  "type": "string"
                },
                "downloadable": {
                  "type": "boolean"
                },
                "drm_encrypted": {
                  "type": "boolean"
                },
                "enabled_for_partner": {
                  "type": "boolean"
                },
                "episodes_count": {
                  "type": "integer"
                },
                "episodes_titles": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "episodes_uids": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "for_kids": {
                  "type": "boolean"
                },
                "hot_content": {
                  "type": "boolean"
                },
                "in_subscription": {
                  "type": "boolean"
                },
                "is_disabled": {
                  "type": "boolean"
                },
                "is_free": {
                  "type": "boolean"
                },
                "is_maxmind_proxy_enabled": {
                  "type": "boolean"
                },
                "is_premier": {
                  "type": "boolean"
                },
                "is_preview": {
                  "type": "boolean"
                },
                "is_top250": {
                  "type": "boolean"
                },
                "number": {
                  "type": "integer"
                },
                "play_last_season": {
                  "type": "boolean"
                },
                "premium": {
                  "type": "boolean"
                },
                "rating_age": {
                  "type": "string",
                  "enum": [
                    "0+"
                  ]
                },
                "special": {
                  "type": "boolean"
                },
                "standart": {
                  "type": "boolean"
                },
                "title": {
                  "type": "string"
                },
                "uid": {
                  "type": "string"
                }
              },
              "required": [
                "_id",
                "alias",
                "downloadable",
                "drm_encrypted",
                "enabled_for_partner",
                "episodes_count",
                "episodes_titles",
                "episodes_uids",
                "for_kids",
                "hot_content",
                "in_subscription",
                "is_disabled",
                "is_free",
                "is_maxmind_proxy_enabled",
                "is_premier",
                "is_preview",
                "is_top250",
                "number",
                "play_last_season",
                "premium",
                "rating_age",
                "special",
                "standart",
                "title",
                "uid"
              ]
            }
          },
          "packshot": {
            "type": "object",
            "properties": {
              "image_15x": {
                "type": "string"
              },
              "image_1x": {
                "type": "null"
              }
            },
            "required": [
              "image_15x",
              "image_1x"
            ]
          },
          "play_last_season": {
            "type": "boolean"
          },
          "playback_options": {
            "type": "string"
          },
          "premium": {
            "type": "boolean"
          },
          "quote": {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "enum": [
                  ""
                ]
              },
              "text": {
                "type": "string"
              }
            },
            "required": [
              "source",
              "text"
            ]
          },
          "quote_source": {
            "type": "string",
            "enum": [
              ""
            ]
          },
          "rating_age": {
            "type": "string",
            "enum": [
              "0+"
            ]
          },
          "rating_start": {
            "type": "number"
          },
          "release_date": {
            "type": "integer"
          },
          "slug": {
            "type": "string"
          },
          "special": {
            "type": "boolean"
          },
          "standard": {
            "type": "boolean"
          },
          "subtitle": {
            "type": "string",
            "enum": [
              ""
            ]
          },
          "summary": {
            "type": "string"
          },
          "thumbnail": {
            "type": "object",
            "properties": {
              "image_15x": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "image_1x": {
                "type": "null"
              }
            },
            "required": [
              "image_15x",
              "image_1x"
            ]
          },
          "title": {
            "type": "string"
          },
          "title_original": {
            "type": "string",
            "enum": [
              ""
            ]
          },
          "trailer_src": {
            "type": "string"
          },
          "uid": {
            "type": "string"
          },
          "url": {
            "type": "string"
          },
          "vertical": {
            "type": "object",
            "properties": {
              "image_15x": {
                "type": "string"
              },
              "image_1x": {
                "type": "null"
              }
            },
            "required": [
              "image_15x",
              "image_1x"
            ]
          },
          "video_cover": {
            "type": "string"
          },
          "web_url": {
            "type": "string"
          },
          "year": {
            "type": "integer",
            "enum": [
              2022,
              2023,
              2008
            ]
          }
        },
        "required": [
          "_cls",
          "_id",
          "alias",
          "background",
          "badges",
          "banner",
          "description",
          "download_options",
          "downloadable",
          "drm_encrypted",
          "duration",
          "enabled_for_partner",
          "for_kids",
          "genres",
          "genres_string",
          "horizontal",
          "hot_content",
          "in_subscription",
          "is_4k",
          "is_51",
          "is_disabled",
          "is_free",
          "is_maxmind_proxy_enabled",
          "is_premier",
          "is_preview",
          "is_top250",
          "logotype",
          "meta",
          "packshot",
          "play_last_season",
          "playback_options",
          "premium",
          "quote",
          "quote_source",
          "rating_age",
          "rating_start",
          "release_date",
          "slug",
          "special",
          "standard",
          "subtitle",
          "summary",
          "thumbnail",
          "title",
          "title_original",
          "trailer_src",
          "uid",
          "url",
          "vertical",
          "video_cover",
          "web_url",
          "year"
        ]
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "items_count": {
          "type": "integer"
        },
        "items_limit": {
          "type": "integer"
        },
        "items_offset": {
          "type": "integer"
        }
      },
      "required": [
        "items_count",
        "items_limit",
        "items_offset"
      ]
    },
    "original_query": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "suggestion": {
      "type": "null"
    }
  },
  "required": [
    "items",
    "meta",
    "original_query",
    "status",
    "suggestion"
  ]
}