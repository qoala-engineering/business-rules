from fastapi import FastAPI
from samples.product_variables import ProductVariables
from samples.product_actions import ProductActions
from samples.product import Product
from business_rules import run
from samples.response import SuccessResponse
from samples.request import *


app = FastAPI()
@app.post("/api/rule/validate-bulk")
def BulkValidateRuleRequest(request: BulkValidateRuleRequest):
    productData = request.data
    product = Product(productData.name, productData.inventory, productData.price)
    res = []
    for ruleData in request.rules:
        resData = run(rule=ruleData,
            defined_variables=ProductVariables(product),
            defined_actions=ProductActions(product))
        res.append(resData)
    return SuccessResponse(message="bulk validation success", data = {"validation_results":res}, meta=None)

@app.post("/api/rule/validate")
def validate(request: ValidateRuleRequest):
    productData = request.data
    product = Product(productData.name, productData.inventory, productData.price)
    res = run(rule=request.rule,
        defined_variables=ProductVariables(product),
        defined_actions=ProductActions(product))
    return SuccessResponse(message="validation success", data = {"validation_result":res}, meta=None)
