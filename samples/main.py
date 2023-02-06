from fastapi import FastAPI
from samples.product_variables import ProductVariables
from samples.product import Product
from business_rules.engine import Engine
from utils.response import SuccessResponse
from samples.request import *


app = FastAPI()
@app.post("/api/rule/validate-bulk")
def BulkValidateRuleRequest(request: BulkValidateRuleRequest):
    productData = request.data
    product = Product(productData.name, productData.inventory, productData.price)
    engine = Engine()
    res = engine.validate(request.rules, ProductVariables(product))
    return SuccessResponse(message="bulk validation success", data = res, meta=None)

@app.post("/api/rule/validate")
def validate(request: ValidateRuleRequest):
    productData = request.data
    product = Product(productData.name, productData.inventory, productData.price)
    engine = Engine()
    res = engine.validate(request.rules, ProductVariables(product))
    return SuccessResponse(message="validation success", data = res, meta=None)
