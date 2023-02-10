from pydantic import BaseModel
from typing import List, Optional

class PlanValidationData(BaseModel):
    smoking_status: Optional[bool]
    entry_age_policy_holder: Optional[int]
    entry_age_insured: Optional[int]
    policy_term: Optional[int]
    premium_payment_term: Optional[int]
    annual_premium: Optional[int]
    sum_assured: Optional[int]
    premium_payment_frequency: Optional[str]
    coverage_period: Optional[int]
    maximum_age_coverage: Optional[int]
    gender: Optional[str]

class BulkValidateRuleRequest(BaseModel):
    data: PlanValidationData
    rules: Optional[List[object]]
    rule_map: Optional[dict]

class ValidateRuleRequest(BaseModel):
    data: PlanValidationData
    rule: object