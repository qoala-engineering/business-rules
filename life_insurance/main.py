from fastapi import FastAPI
from life_insurance.plan_validation_variables import PlanValidationVariables
from life_insurance.plan_validation_actions import PlanValidationActions
from life_insurance.plan_validation import PlanValidation, PlanValidationData
from business_rules import run
from utils.response import SuccessResponse
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
    res = []
    validIdentifiers = []
    respData = object
    if not ruleMap:
        for ruleData in request.rules:
            resData = run(rule=ruleData,
                defined_variables=PlanValidationVariables(planValidation),
                defined_actions=PlanValidationActions(planValidation))
            res.append(resData)
        respData = {
            "validation_results": res
        }
    else:
        for item in ruleMap.keys():
            resData = run(rule=ruleMap[item],
                defined_variables=PlanValidationVariables(planValidation),
                defined_actions=PlanValidationActions(planValidation))
            res.append(resData)
            if resData:
                validIdentifiers.append(item)
        respData = {
            "validation_results": res,
            "valid_identifiers": validIdentifiers
        }
    return SuccessResponse(message="bulk validation success", data = respData, meta=None)

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
    res = run(rule=request.rule,
        defined_variables=PlanValidationVariables(planValidation),
        defined_actions=PlanValidationActions(planValidation))
    return SuccessResponse(message="validation success", data = {"validation_result":res}, meta=None)
