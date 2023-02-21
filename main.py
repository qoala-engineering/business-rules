from fastapi import FastAPI
from business_rules.engine import Engine
from utils.response import SuccessResponse, FailedResponse

app = FastAPI()

@app.get("/api/sample")
def sample():
        # this is a sample method only, later on all these variables 
        # and rule datas is going to be stored in database
        sample_rule_variables = [ 
        {
            "name":"age",
            "type":"numeric",
        },
        {
            "name":"gender",
            "type":"string",
        },
        {
            "name":"payment_frequency",
            "type":"select_multiple",
        }
        ]
        
        sample_rule_data = {
             "conditions": {
                "all": [
                    {
                        "name": "age",
                        "operator": "greater_than_or_equal_to",
                        "value": 18
                    },
                    {
                        "name": "gender",
                        "operator": "equal_to",
                        "value": "Male",
                    },
                    {
                        "name": "payment_frequency",
                        "operator": "shares_at_least_one_element_with",
                        "value": ["Single", "Semi-Annual", "Quarterly", "Monthly"]
                    }
                ]
            }
        }

        sample_input_data = [
            {
                "name":"age",
                "value":18,
            },
            {
                "name":"gender",
                "value":"Male",
            },
            {
                "name":"payment_frequency",
                "value":"Single",
            }
        ]

        res = Engine().validate(rule_variables=sample_rule_variables, rule_data=sample_rule_data, input_data=sample_input_data)
        return SuccessResponse(message="validation success", data = res, meta=None)