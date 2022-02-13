from cerberus import Validator


def validate_data_to_update_space_flight(body: dict) -> bool:
    schema = {
        "id": {"type": "integer", "required": True},
        "data": {
            "type": "dict",
            "required": True,
            "schema": {
                "id": {"type": "integer", "required": False},
                "_id": {"required": False},
                "featured": {"type": "boolean", "required": False},
                "title": {"type": "string", "required": False},
                "url": {"type": "string", "required": False},
                "imageUrl": {"type": "string", "required": False},
                "newsSite": {"type": "string", "required": False},
                "summary": {"type": "string", "required": False},
                "publishedAt": {"type": "string", "required": False},
                "updatedAt": {"type": "string", "required": False},
                "launches": {
                    "type": "list",
                    "required": False,
                    "schema": {
                        "type": "dict",
                        "required": False,
                        "schema": {
                            "id": {"type": "string", "required": False},
                            "provider": {"type": "string", "required": False},
                        },
                    },
                },
                "events": {
                    "type": "list",
                    "required": False,
                    "schema": {
                        "type": "dict",
                        "required": False,
                        "schema": {
                            "id": {"type": "string", "required": False},
                            "provider": {"type": "string", "required": False},
                        },
                    },
                },
            },
        },
    }
    valid = Validator(schema)
    return valid.validate(body)
