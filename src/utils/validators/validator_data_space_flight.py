from cerberus import Validator


def validate_data_space_flight(body: dict) -> bool:
    schema = {
        "id": {"type": "integer", "required": True},
        "featured": {"type": "boolean", "required": False},
        "title": {"type": "string", "required": False},
        "url": {"type": "string", "required": False},
        "imageUrl": {"type": "string", "required": False},
        "newsSite": {"type": "string", "required": False},
        "summary": {"type": "string", "required": False},
        "publishedAt": {"type": "string", "required": False},
        "launches": {
            "type": "list",
            "required": False,
            "schema": {
                "type": "dict",
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
                "schema": {
                    "id": {"type": "string", "required": False},
                    "provider": {"type": "string", "required": False},
                },
            },
        },
    }
    valid = Validator(schema)

    return valid.validate(body)
