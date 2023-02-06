from fastapi import FastAPI
from life_insurance.plan_validation_variables import PlanValidationVariables
from life_insurance.plan_validation import PlanValidation, PlanValidationData
from business_rules.engine import Engine
from utils.response import SuccessResponse, FailedResponse
from life_insurance.request import *

app = FastAPI()
@app.post("/api/rule/validate-bulk")
def BulkValidateRuleRequest(request: BulkValidateRuleRequest):
    requestData = request.data
    ruleMap = request.rule_map
    planValidationData = PlanValidationData(
        smoker = requestData.smoker,
        policyTerm = requestData.policyTerm,
        age = requestData.age,
        paymentTerm = requestData.paymentTerm,
        maturityAge = requestData.maturityAge,
        insuredAge = requestData.insuredAge,
        policyHolderAge = requestData.policyHolderAge,
    )
    planValidation = PlanValidation(requestData.identifier, planValidationData)
    engine = Engine()
    res = engine.validate_bulk(ruleMap, PlanValidationVariables(planValidation))
    return SuccessResponse(message="bulk validation success", data = res, meta=None)

@app.post("/api/rule/validate")
def validate(request: ValidateRuleRequest):
    requestData = request.data
    planValidationData = PlanValidationData(
            smoker = requestData.smoker,
            policyTerm = requestData.policyTerm,
            age = requestData.age,
            paymentTerm = requestData.paymentTerm,
            maturityAge = requestData.maturityAge,
            insuredAge = requestData.insuredAge,
            policyHolderAge = requestData.policyHolderAge,
    )
    planValidation = PlanValidation(requestData.identifier, planValidationData)
    engine = Engine(PlanValidationVariables(planValidation))
    res = engine.validate(request.rule, PlanValidationVariables(planValidation))
    return SuccessResponse(message="validation success", data = res, meta=None)

@app.get("/api/variables/{variable_id}")
def validate(variable_id: str):
    engine = Engine()
    if variable_id == 'PLAN_VALIDATION':
        res = engine.get_variables(PlanValidationVariables)
    else:
        return FailedResponse(message="get variables failed", data = None, meta=None, code=404)
    return SuccessResponse(message="get variables success", data = res, meta=None)