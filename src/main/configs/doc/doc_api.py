from fastapi.openapi.utils import get_openapi


def custom_openapi(api):
    if api.openapi_schema:
        return api.openapi_schema
    openapi_schema = get_openapi(
        title="Back-end Challenge 🏅 2021",
        version="1.0.0",
        description="Este é um desafio para que possamos ver as suas habilidades\
 como Back-end Developer. Nesse desafio você deverá desenvolver uma REST API\
 que utilizará os dados do projeto Space Flight News, uma API pública com\
 informações relacionadas a voos espaciais. O projeto a ser desenvolvido por\
 você tem como objetivo criar a API permitindo assim a conexão de outras aplicações.",
        routes=api.routes,
    )

    openapi_schema["paths"]["/"] = {
        "get": {
            "tags": ["Challenge"],
            "responses": {
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "msg": {"type": "string"},
                                },
                            },
                            "examples": {
                                "msg": {
                                    "value": {
                                        "msg": "Back-end Challenge 2021 🏅 - Space Flight News"
                                    }
                                }
                            },
                        }
                    }
                }
            },
        }
    }

    openapi_schema["paths"]["/articles/"] = {
        "post": {
            "description": "Insert one Articles",
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "required": ["id"],
                            "type": "object",
                            "properties": {
                                "id": {"type": "number"},
                                "title": {"type": "string"},
                                "url": {"type": "string"},
                                "imageUrl": {"type": "string"},
                                "newsSite": {"type": "string"},
                                "summary": {"type": "string"},
                                "publishedAt": {"type": "string"},
                                "updatedAt": {"type": "string"},
                                "featured": {"type": "boolean"},
                                "launches": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "string"},
                                            "provider": {"type": "string"},
                                        },
                                    },
                                },
                                "events": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "string"},
                                            "provider": {"type": "string"},
                                        },
                                    },
                                },
                            },
                        }
                    }
                },
                "required": True,
            },
            "responses": {
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {"inserted_id": {"type": "string"}},
                            }
                        }
                    }
                }
            },
            "tags": ["Challenge"],
        }
    }

    openapi_schema["paths"]["/articles"] = {
        "get": {
            "description": "Find pigination Articles",
            "parameters": [
                {
                    "name": "limit_page",
                    "in": "query",
                    "description": "Limit of the articles to response",
                    "required": True,
                    "schema": {"type": "number"},
                },
                {
                    "name": "skip_page",
                    "in": "query",
                    "description": "Skip of the articles to response",
                    "required": True,
                    "schema": {"type": "number"},
                },
            ],
            "responses": {
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "number"},
                                        "title": {"type": "string"},
                                        "url": {"type": "string"},
                                        "imageUrl": {"type": "string"},
                                        "newsSite": {"type": "string"},
                                        "summary": {"type": "string"},
                                        "publishedAt": {"type": "string"},
                                        "updatedAt": {"type": "string"},
                                        "featured": {"type": "boolean"},
                                        "launches": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "id": {"type": "string"},
                                                    "provider": {"type": "string"},
                                                },
                                            },
                                        },
                                        "events": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "id": {"type": "string"},
                                                    "provider": {"type": "string"},
                                                },
                                            },
                                        },
                                    },
                                },
                            }
                        }
                    },
                }
            },
            "tags": ["Challenge"],
        }
    }

    openapi_schema["paths"]["/articles/{id}"] = {
        "get": {
            "description": "Find one Article",
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": "ID to find one article",
                    "required": True,
                    "schema": {"type": "number"},
                }
            ],
            "responses": {
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "required": ["id"],
                                "type": "object",
                                "properties": {
                                    "id": {"type": "number"},
                                    "title": {"type": "string"},
                                    "url": {"type": "string"},
                                    "imageUrl": {"type": "string"},
                                    "newsSite": {"type": "string"},
                                    "summary": {"type": "string"},
                                    "publishedAt": {"type": "string"},
                                    "updatedAt": {"type": "string"},
                                    "featured": {"type": "boolean"},
                                    "launches": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "string"},
                                                "provider": {"type": "string"},
                                            },
                                        },
                                    },
                                    "events": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "string"},
                                                "provider": {"type": "string"},
                                            },
                                        },
                                    },
                                },
                            }
                        }
                    },
                }
            },
            "tags": ["Challenge"],
        },
        "put": {
            "description": "Updated one Article",
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": "ID to update one article",
                    "required": True,
                    "schema": {"type": "number"},
                }
            ],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "required": ["id"],
                            "type": "object",
                            "properties": {
                                "id": {"type": "number"},
                                "title": {"type": "string"},
                                "url": {"type": "string"},
                                "imageUrl": {"type": "string"},
                                "newsSite": {"type": "string"},
                                "summary": {"type": "string"},
                                "publishedAt": {"type": "string"},
                                "updatedAt": {"type": "string"},
                                "featured": {"type": "boolean"},
                                "launches": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "string"},
                                            "provider": {"type": "string"},
                                        },
                                    },
                                },
                                "events": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "string"},
                                            "provider": {"type": "string"},
                                        },
                                    },
                                },
                            },
                        }
                    }
                },
                "required": True,
            },
            "responses": {
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "modified_count": {"type": "number"},
                                },
                            }
                        }
                    },
                }
            },
            "tags": ["Challenge"],
        },
        "delete": {
            "description": "Delete one Article",
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": "ID to delete one article",
                    "required": True,
                    "schema": {"type": "number"},
                }
            ],
            "responses": {
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "deleted_count": {"type": "number"},
                                },
                            }
                        }
                    },
                }
            },
            "tags": ["Challenge"],
        },
    }

    api.openapi_schema = openapi_schema
    return api.openapi_schema
