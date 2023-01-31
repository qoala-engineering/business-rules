from pydantic import BaseModel
from typing import List

class ProductDataRequest(BaseModel):
    name: str
    inventory: int 
    price: int

class BulkValidateRuleRequest(BaseModel):
    data: ProductDataRequest
    rules: List[object]

class ValidateRuleRequest(BaseModel):
    data: ProductDataRequest
    rule: object