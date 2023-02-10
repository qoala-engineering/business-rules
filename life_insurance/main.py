from fastapi import FastAPI
from life_insurance.plan_validation_variables import PlanValidationVariables
from life_insurance.plan_validation import PlanValidation
from business_rules.engine import Engine
from utils.response import SuccessResponse, FailedResponse
from life_insurance.request import *

app = FastAPI()
@app.post("/api/rule/validate-bulk")
def BulkValidateRuleRequest(request: BulkValidateRuleRequest):
    rule_map = request.rule_map
    data = request.data
    plan_validation_data = PlanValidation(
        smoking_status = data.smoking_status,
        entry_age_policy_holder = data.entry_age_policy_holder,
        entry_age_insured = data.entry_age_insured,
        policy_term = data.policy_term,
        premium_payment_term = data.premium_payment_term,
        annual_premium = data.annual_premium,
        sum_assured = data.sum_assured,
        premium_payment_frequency = data.premium_payment_frequency,
        coverage_period = data.coverage_period,
        maximum_age_coverage = data.maximum_age_coverage,
        gender = data.gender,
    )
    engine = Engine()
    res = engine.validate_bulk(rule_map, PlanValidationVariables(plan_validation_data))
    return SuccessResponse(message="bulk validation success", data = res, meta=None)

@app.post("/api/rule/validate")
def validate(request: ValidateRuleRequest):
    data = request.data
    plan_validation_data = PlanValidation(
        smoking_status = data.smoking_status,
        entry_age_policy_holder = data.entry_age_policy_holder,
        entry_age_insured = data.entry_age_insured,
        policy_term = data.policy_term,
        premium_payment_term = data.premium_payment_term,
        annual_premium = data.annual_premium,
        sum_assured = data.sum_assured,
        premium_payment_frequency = data.premium_payment_frequency,
        coverage_period = data.coverage_period,
        maximum_age_coverage = data.maximum_age_coverage,
        gender = data.gender,
    )
    engine = Engine()
    res = engine.validate(request.rule, PlanValidationVariables(plan_validation_data))
    return SuccessResponse(message="validation success", data = res, meta=None)

@app.get("/api/variables/{variable_id}")
def validate(variable_id: str):
    engine = Engine()
    if variable_id == "PLAN_VALIDATION":
        res = engine.get_variables(PlanValidationVariables)
    else:
        return FailedResponse(message="get variables failed", data = None, meta=None, code=404)
    return SuccessResponse(message="get variables success", data = res, meta=None)