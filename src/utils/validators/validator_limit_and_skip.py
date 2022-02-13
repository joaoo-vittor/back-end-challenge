from cerberus import Validator


def validate_limit_and_skip(body: dict) -> bool:
    schema = {
        "limit_page": {"type": "integer", "required": True},
        "skip_page": {"type": "integer", "required": True},
    }
    valid = Validator(schema)

    return valid.validate(body)
