trailer = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "_cls": {
      "type": "string"
    },
    "_id": {
      "type": "string"
    },
    "additional_content": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "announcement": {
            "type": "boolean"
          },
          "description": {
            "type": "string"
          },
          "packshot": {
            "type": "object",
            "properties": {
              "image_1x": {
                "type": "string"
              },
              "image_15x": {
                "type": "string"
              }
            },
            "required": [
              "image_1x",
              "image_15x"
            ]
          },
          "restrictions": {
            "type": "array",
            "items": {
              "items": {}
            }
          },
          "title": {
            "type": "string"
          },
          "start_id": {
            "type": "integer"
          },
          "uid": {
            "type": "string"
          },
          "video_src": {
            "type": "string"
          }
        },
        "required": [
          "announcement",
          "description",
          "packshot",
          "restrictions",
          "title",
          "start_id",
          "uid",
          "video_src"
        ]
      }
    },
    "alias": {
      "type": "string"
    },
    "background": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "badges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "alias": {
            "type": "string"
          },
          "background_color": {
            "type": "string"
          },
          "background_color_right": {
            "type": "string"
          },
          "image_1x": {
            "type": "null"
          },
          "name": {
            "type": "string"
          },
          "size": {
            "type": "string"
          },
          "structure": {
            "type": "string"
          },
          "text": {
            "type": "string"
          },
          "text_right": {
            "type": "string"
          },
          "text_color": {
            "type": "string"
          },
          "text_color_right": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "under_logo_position": {
            "type": "boolean"
          }
        },
        "required": [
          "id",
          "alias",
          "background_color",
          "background_color_right",
          "image_1x",
          "name",
          "size",
          "structure",
          "text",
          "text_right",
          "text_color",
          "text_color_right",
          "type",
          "under_logo_position"
        ]
      }
    },
    "banner": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "null"
        },
        "image_15x": {
          "type": "null"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "budget": {
      "type": "string"
    },
    "cast": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "alias": {
            "type": "string"
          },
          "character": {
            "type": "object",
            "properties": {
              "biography": {
                "type": "string",
                "enum": [
                  ""
                ]
              },
              "main_character": {
                "type": "boolean"
              },
              "name": {
                "type": "string"
              },
              "photo": {
                "type": "null"
              },
              "photo_app_section": {
                "type": "null"
              },
              "start_id": {
                "type": "integer"
              },
              "weight": {
                "type": [
                  "integer",
                  "null"
                ]
              }
            },
            "required": [
              "biography",
              "main_character",
              "name",
              "photo",
              "photo_app_section",
              "start_id",
              "weight"
            ]
          },
          "filmography": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "photo": {
            "type": "object",
            "properties": {
              "image_1x": {
                "type": "string"
              },
              "image_15x": {
                "type": "string"
              }
            },
            "required": [
              "image_1x",
              "image_15x"
            ]
          }
        },
        "required": [
          "alias",
          "character",
          "filmography",
          "name",
          "photo"
        ]
      }
    },
    "color": {
      "type": "object",
      "properties": {
        "back_color_1": {
          "type": "string"
        },
        "back_color_2": {
          "type": "string"
        },
        "font_color": {
          "type": "string"
        }
      },
      "required": [
        "back_color_1",
        "back_color_2",
        "font_color"
      ]
    },
    "composers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "alias": {
            "type": "string"
          },
          "character": {
            "type": "object",
            "properties": {
              "photo": {
                "type": "null"
              },
              "photo_app_section": {
                "type": "null"
              }
            },
            "required": [
              "photo",
              "photo_app_section"
            ]
          },
          "filmography": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "photo": {
            "type": "object",
            "properties": {
              "image_1x": {
                "type": "string"
              },
              "image_15x": {
                "type": "string"
              }
            },
            "required": [
              "image_1x",
              "image_15x"
            ]
          }
        },
        "required": [
          "alias",
          "character",
          "filmography",
          "name",
          "photo"
        ]
      }
    },
    "description": {
      "type": "string"
    },
    "directors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "alias": {
            "type": "string"
          },
          "character": {
            "type": "object",
            "properties": {
              "photo": {
                "type": "null"
              },
              "photo_app_section": {
                "type": "null"
              }
            },
            "required": [
              "photo",
              "photo_app_section"
            ]
          },
          "filmography": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "photo": {
            "type": "object",
            "properties": {
              "image_1x": {
                "type": "string"
              },
              "image_15x": {
                "type": "string"
              }
            },
            "required": [
              "image_1x",
              "image_15x"
            ]
          }
        },
        "required": [
          "alias",
          "character",
          "filmography",
          "name",
          "photo"
        ]
      }
    },
    "display": {
      "type": "boolean"
    },
    "downloadable": {
      "type": "boolean"
    },
    "duration": {
      "type": "integer"
    },
    "duration_minutes": {
      "type": "string"
    },
    "enabled_for_partner": {
      "type": "boolean"
    },
    "facts": {
      "type": "array",
      "items": {
        "items": {}
      }
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
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "slug",
          "title",
          "url"
        ]
      }
    },
    "hashtags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "alias": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "text_color": {
            "type": "string",
            "enum": [
              "#00E4BB",
              "#FFF900",
              "#FF987D",
              "#9300FF",
              "#00B9F1"
            ]
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "alias",
          "title",
          "text_color",
          "url"
        ]
      }
    },
    "horizontal": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "horizontal_poster": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
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
    "is_premier": {
      "type": "boolean"
    },
    "is_preview": {
      "type": "boolean"
    },
    "kinopoisk_id": {
      "type": "string"
    },
    "locales": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "logotype": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "null"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "operators": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "alias": {
            "type": "string"
          },
          "character": {
            "type": "object",
            "properties": {
              "photo": {
                "type": "null"
              },
              "photo_app_section": {
                "type": "null"
              }
            },
            "required": [
              "photo",
              "photo_app_section"
            ]
          },
          "filmography": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "photo": {
            "type": "object",
            "properties": {
              "image_1x": {
                "type": "string"
              },
              "image_15x": {
                "type": "string"
              }
            },
            "required": [
              "image_1x",
              "image_15x"
            ]
          }
        },
        "required": [
          "alias",
          "character",
          "filmography",
          "name",
          "photo"
        ]
      }
    },
    "origin_countries": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string"
          },
          "title": {
            "type": "string"
          }
        },
        "required": [
          "code",
          "title"
        ]
      }
    },
    "packshot": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "null"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "play_last_season": {
      "type": "boolean"
    },
    "playback_options": {
      "type": ["string", "null"]
    },
    "producers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "alias": {
            "type": "string"
          },
          "character": {
            "type": "object",
            "properties": {
              "photo": {
                "type": "null"
              },
              "photo_app_section": {
                "type": "null"
              }
            },
            "required": [
              "photo",
              "photo_app_section"
            ]
          },
          "filmography": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "photo": {
            "type": "object",
            "properties": {
              "image_1x": {
                "type": "string"
              },
              "image_15x": {
                "type": "string"
              }
            },
            "required": [
              "image_1x",
              "image_15x"
            ]
          }
        },
        "required": [
          "alias",
          "character",
          "filmography",
          "name",
          "photo"
        ]
      }
    },
    "quote": {
      "type": "string"
    },
    "quote_source": {
      "type": "string"
    },
    "rating_age": {
      "type": "string"
    },
    "rating_imdb": {
      "type": "integer"
    },
    "rating_kp": {
      "type": "number"
    },
    "rating_start": {
      "type": "integer"
    },
    "release_date": {
      "type": "integer"
    },
    "release_year_end": {
      "type": "null"
    },
    "release_year_start": {
      "type": "integer"
    },
    "restrictions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          }
        },
        "required": [
          "id"
        ]
      }
    },
    "seo": {
      "type": "object",
      "properties": {
        "long_description": {
          "type": "string"
        },
        "short_description": {
          "type": "string"
        },
        "subject": {
          "type": "string"
        }
      },
      "required": [
        "long_description",
        "short_description",
        "subject"
      ]
    },
    "slug": {
      "type": "string"
    },
    "similar": {
      "type": "string"
    },
    "special": {
      "type": "boolean"
    },
    "special_description": {
      "type": "object",
      "properties": {
        "paragraph_1": {
          "type": "string"
        },
        "paragraph_2": {
          "type": "string"
        },
        "paragraph_3": {
          "type": "string"
        },
        "paragraph_4": {
          "type": "string"
        }
      },
      "required": [
        "paragraph_1",
        "paragraph_2",
        "paragraph_3",
        "paragraph_4"
      ]
    },
    "standard": {
      "type": "boolean"
    },
    "start_release_date": {
      "type": "string"
    },
    "subtitle": {
      "type": "string"
    },
    "thumbnail": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "null"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "title": {
      "type": "string"
    },
    "title_original": {
      "type": "string"
    },
    "trailer_src": {
      "type": "string"
    },
    "uid": {
      "type": "string"
    },
    "unpublish": {
      "type": "integer"
    },
    "unavailable_by_geo": {
      "type": "boolean"
    },
    "url": {
      "type": "string"
    },
    "vertical": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "null"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "vertical_poster": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "web_url": {
      "type": "string"
    },
    "weight": {
      "type": "null"
    },
    "writers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "alias": {
            "type": "string"
          },
          "character": {
            "type": "object",
            "properties": {
              "photo": {
                "type": "null"
              },
              "photo_app_section": {
                "type": "null"
              }
            },
            "required": [
              "photo",
              "photo_app_section"
            ]
          },
          "filmography": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "photo": {
            "type": "object",
            "properties": {
              "image_1x": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "image_15x": {
                "type": [
                  "string",
                  "null"
                ]
              }
            },
            "required": [
              "image_1x",
              "image_15x"
            ]
          }
        },
        "required": [
          "alias",
          "character",
          "filmography",
          "name",
          "photo"
        ]
      }
    },
    "year": {
      "type": "integer"
    }
  },
  "required": [
    "_cls",
    "_id",
    "additional_content",
    "alias",
    "background",
    "badges",
    "banner",
    "budget",
    "cast",
    "color",
    "composers",
    "description",
    "directors",
    "display",
    "downloadable",
    "duration",
    "duration_minutes",
    "enabled_for_partner",
    "facts",
    "for_kids",
    "genres",
    "hashtags",
    "horizontal",
    "horizontal_poster",
    "in_subscription",
    "is_4k",
    "is_51",
    "is_disabled",
    "is_free",
    "is_premier",
    "is_preview",
    "kinopoisk_id",
    "locales",
    "logotype",
    "operators",
    "origin_countries",
    "packshot",
    "play_last_season",
    "playback_options",
    "producers",
    "quote",
    "quote_source",
    "rating_age",
    "rating_imdb",
    "rating_kp",
    "rating_start",
    "release_date",
    "release_year_end",
    "release_year_start",
    "restrictions",
    "seo",
    "slug",
    "similar",
    "special",
    "special_description",
    "standard",
    "start_release_date",
    "subtitle",
    "thumbnail",
    "title",
    "title_original",
    "trailer_src",
    "uid",
    "unpublish",
    "unavailable_by_geo",
    "url",
    "vertical",
    "vertical_poster",
    "web_url",
    "weight",
    "writers",
    "year"
  ]
}
