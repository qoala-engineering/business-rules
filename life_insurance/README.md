life-insurance-implementation
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

- Start life application:
```bash
make start_life_app
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
    "rule": {
            "conditions": {
                "all": [
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "policy_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 60
                    },
                    {
                        "name": "policy_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 12
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "smoking_status",
                        "operator": "is_false",
                        "value": null
                    },
                    {
                        "name": "sum_assured",
                        "operator": "greater_than_or_equal_to",
                        "value": 500000000
                    },
                    {
                        "name": "premium_payment_frequency",
                        "operator": "shares_at_least_one_element_with",
                        "value": [
                            "Single",
                            "Annual",
                            "Semi-Annual",
                            "Quarterly",
                            "Monthly"
                        ]
                    }
                ]
            }
        },
    "data": {
        "smoking_status": false,
        "entry_age_policy_holder": 25,
        "entry_age_insured": 25,
        "policy_term": 60,
        "premium_payment_term": 96,
        "annual_premium": 10000000,
        "sum_assured": 50000000,
        "premium_payment_frequency": "Annual",
        "coverage_period": 30,
        "maximum_age_coverage": 30
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
        "validation_result": false
    },
    "meta": null
}
```

Curl for `validateBulk` API:

```bash
curl --location --request POST 'localhost:8000/api/rule/validate-bulk' \
--header 'Content-Type: application/json' \
--data-raw '{
    "rule_map": {
        "BAJAJ_ALLIANZ": {
            "conditions": {
                "all": [
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "policy_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 60
                    },
                    {
                        "name": "policy_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 12
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "smoking_status",
                        "operator": "is_false",
                        "value": null
                    },
                    {
                        "name": "sum_assured",
                        "operator": "greater_than_or_equal_to",
                        "value": 500000000
                    },
                    {
                        "name": "premium_payment_frequency",
                        "operator": "shares_at_least_one_element_with",
                        "value": [
                            "Single",
                            "Annual",
                            "Semi-Annual",
                            "Quarterly",
                            "Monthly"
                        ]
                    }
                ]
            }
        },
        "TATA_AIA": {
            "conditions": {
                "all": [
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "policy_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 120
                    },
                    {
                        "name": "policy_term",
                        "operator": "less_than_or_equal_to",
                        "value": 984
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 12
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "less_than_or_equal_to",
                        "value": 984
                    },
                    {
                        "name": "smoking_status",
                        "operator": "is_false",
                        "value": null
                    },
                    {
                        "name": "sum_assured",
                        "operator": "greater_than_or_equal_to",
                        "value": 500000000
                    },
                    {
                        "name": "premium_payment_frequency",
                        "operator": "shares_at_least_one_element_with",
                        "value": [
                            "Single",
                            "Annual",
                            "Semi-Annual",
                            "Quarterly",
                            "Monthly"
                        ]
                    }
                ]
            }
        },
        "MAX_LIFE_INSURANCE": {
            "conditions": {
                "all": [
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "policy_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 120
                    },
                    {
                        "name": "policy_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 12
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "smoking_status",
                        "operator": "is_false",
                        "value": null
                    },
                    {
                        "or": [
                            {
                                "and": [
                                    {
                                        "name": "entry_age_insured",
                                        "operator": "greater_than_or_equal_to",
                                        "value": 18
                                    },
                                    {
                                        "name": "entry_age_insured",
                                        "operator": "less_than_or_equal_to",
                                        "value": 45
                                    },
                                    {
                                        "name": "sum_assured",
                                        "operator": "less_than_or_equal_to",
                                        "value": 100000000
                                    }
                                ]
                            },
                            {
                                "and": [
                                    {
                                        "name": "entry_age_insured",
                                        "operator": "greater_than_or_equal_to",
                                        "value": 46
                                    },
                                    {
                                        "name": "entry_age_insured",
                                        "operator": "less_than_or_equal_to",
                                        "value": 55
                                    },
                                    {
                                        "name": "sum_assured",
                                        "operator": "less_than_or_equal_to",
                                        "value": 50000000
                                    }
                                ]
                            },
                            {
                                "and": [
                                    {
                                        "name": "entry_age_insured",
                                        "operator": "greater_than_or_equal_to",
                                        "value": 56
                                    },
                                    {
                                        "name": "entry_age_insured",
                                        "operator": "less_than_or_equal_to",
                                        "value": 60
                                    },
                                    {
                                        "name": "sum_assured",
                                        "operator": "less_than_or_equal_to",
                                        "value": 25000000
                                    }
                                ]
                            },
                            {
                                "and": [
                                    {
                                        "name": "entry_age_insured",
                                        "operator": "greater_than_or_equal_to",
                                        "value": 61
                                    },
                                    {
                                        "name": "sum_assured",
                                        "operator": "less_than_or_equal_to",
                                        "value": 100000000
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "premium_payment_frequency",
                        "operator": "shares_at_least_one_element_with",
                        "value": [
                            "Single",
                            "Annual",
                            "Semi-Annual",
                            "Quarterly",
                            "Monthly"
                        ]
                    }
                ]
            }
        },
        "ICICI_PRUDENTIAL": {
            "conditions": {
                "all": [
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "policy_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 60
                    },
                    {
                        "name": "policy_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 12
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "smoking_status",
                        "operator": "is_false",
                        "value": null
                    },
                    {
                        "name": "sum_assured",
                        "operator": "greater_than_or_equal_to",
                        "value": 500000
                    },
                    {
                        "name": "premium_payment_frequency",
                        "operator": "shares_at_least_one_element_with",
                        "value": [
                            "Single",
                            "Annual",
                            "Semi-Annual",
                            "Quarterly",
                            "Monthly"
                        ]
                    }
                ]
            }
        },
        "HDFC_LIFE": {
            "conditions": {
                "all": [
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "less_than_or_equal_to",
                        "value": 65
                    },
                    {
                        "name": "policy_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 1
                    },
                    {
                        "name": "policy_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 12
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "less_than_or_equal_to",
                        "value": 804
                    },
                    {
                        "name": "smoking_status",
                        "operator": "is_false",
                        "value": null
                    },
                    {
                        "name": "annual_premium",
                        "operator": "greater_than_or_equal_to",
                        "value": 500000000
                    },
                    {
                        "name": "premium_payment_frequency",
                        "operator": "shares_at_least_one_element_with",
                        "value": [
                            "Single",
                            "Annual",
                            "Semi-Annual",
                            "Quarterly",
                            "Monthly"
                        ]
                    }
                ]
            }
        },
        "AXA_LIFE": {
            "conditions": {
                "all": [
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "greater_than_or_equal_to",
                        "value": 17
                    },
                    {
                        "name": "entry_age_policy_holder",
                        "operator": "less_than_or_equal_to",
                        "value": 70
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "greater_than_or_equal_to",
                        "value": 15
                    },
                    {
                        "name": "entry_age_insured",
                        "operator": "less_than_or_equal_to",
                        "value": 54
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "greater_than_or_equal_to",
                        "value": 96
                    },
                    {
                        "name": "premium_payment_term",
                        "operator": "less_than_or_equal_to",
                        "value": 120
                    },
                    {
                        "name": "sum_assured",
                        "operator": "greater_than_or_equal_to",
                        "value": 30000000
                    },
                    {
                        "name": "sum_assured",
                        "operator": "less_than_or_equal_to",
                        "value": 300000000
                    },
                    {
                        "name": "premium_payment_frequency",
                        "operator": "shares_at_least_one_element_with",
                        "value": [
                            "Annual",
                            "Monthly"
                        ]
                    }
                ]
            }
        }
    },
    "data": {
        "smoking_status": false,
        "entry_age_policy_holder": 25,
        "entry_age_insured": 25,
        "policy_term": 60,
        "premium_payment_term": 96,
        "annual_premium": 10000000,
        "sum_assured": 50000000,
        "premium_payment_frequency": "Annual",
        "coverage_period": 30,
        "maximum_age_coverage": 30
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
        "valid_identifiers": [
            "ICICI_PRUDENTIAL",
            "AXA_LIFE"
        ]
    },
    "meta": null
}
```