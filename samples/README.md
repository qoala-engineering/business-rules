sample-implementation
==============

This module is for showing the sample implementation you can do using this business rule engine

## Guideline

- Create the virtual environment by running this command:
```bash
make init_env
```

- Start the virtual environment by running this command:
```bash
make start_env
```
or if doesn't work just run this:
```bash
source ./venv/bin/activate
```

- Install dependecies by running this command:
```bash
make init_dep
```

- Start sample application:
```bash
make start_sample_app
```

## API

The APIs that implemented in this sample is `validate` and `validateBulk` APIs, these api will receive the `rule(s)` which will include the condition, and the `data`. And then will do validation based on those inputs and generate the `validation_result(s)`. 

- Can checkout the api available in this endpoint in your local:
```
http://localhost:8000/docs
```

- For the sample now we have `validate` and `validateBulk` APIs, these are the curl for testing purposes:

Curl for `validate` API:

```bash
curl --location --request POST 'localhost:8000/api/rule/validate' \
--header 'Content-Type: application/json' \
--data-raw '{
    "rule":
        {
            "conditions": {
                "all": [
                    {
                        "name": "price",
                        "operator": "greater_than",
                        "value": 20
                    }
                ]
            }
        },
    "data": {
        "name": "Product 123",
        "inventory": 100,
        "price": 100000
    }
}'
```
Sample response from `validate`:
```bash
{
    "status": "success",
    "code": 200,
    "message": "validation success",
    "data": {
        "validation_result": true
    },
    "meta": null
}
```

Curl for `validateBulk` API:

```bash
curl --location --request POST 'localhost:8000/api/rule/validate-bulk' \
--header 'Content-Type: application/json' \
--data-raw '{
    "rules": [
        {
            "conditions": {
                "all": [
                    {
                        "name": "price",
                        "operator": "greater_than",
                        "value": 20
                    }
                ]
            }
        },
        {
            "conditions": {
                "all": [
                    {
                        "any": [
                            {
                                "name": "price",
                                "operator": "greater_than",
                                "value": 20
                            },
                             {
                                "name": "inventory",
                                "operator": "greater_than",
                                "value": 20
                            }
                        ]
                    },
                    {
                        "any": [
                            {
                                "name": "price",
                                "operator": "equal_to",
                                "value": 0
                            }
                        ]
                    }
                ]
            }
        }
    ],
    "data": {
        "name": "Product 123",
        "inventory": 100,
        "price": 100000
    }
}'
```
Sample response from `validateBulk`:
```bash
{
    "status": "success",
    "code": 200,
    "message": "bulk validation success",
    "data": {
        "validation_results": [
            true,
            false
        ]
    },
    "meta": null
}
```