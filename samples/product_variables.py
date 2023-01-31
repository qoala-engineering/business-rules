from business_rules.variables import BaseVariables
from business_rules.variables import numeric_rule_variable

class ProductVariables(BaseVariables):

    def __init__(self, product):
        self.product = product

    @numeric_rule_variable
    def inventory(self):
        return self.product.inventory

    @numeric_rule_variable
    def price(self):
        return self.product.price