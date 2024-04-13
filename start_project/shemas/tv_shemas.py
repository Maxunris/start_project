tv = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "selections": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "alias": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "title",
          "alias",
          "url"
        ]
      }
    }
  },
  "required": [
    "title",
    "description",
    "selections"
  ]
}