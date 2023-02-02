from pydantic import BaseModel
from typing import List, Optional

class PlanValidationRequest(BaseModel):
    identifier: str
    smoker: Optional[bool]
    policyTerm: Optional[int]
    age: Optional[int]
    paymentTerm: Optional[str]
    maturityAge: Optional[int]
    insuredAge: Optional[int]
    policyHolderAge: Optional[int]

def returnStr(s):
    return str(s)

class BulkValidateRuleRequest(BaseModel):
    data: PlanValidationRequest
    rules: Optional[List[object]]
    rule_map: Optional[dict]

class ValidateRuleRequest(BaseModel):
    data: PlanValidationRequest
    rule: object