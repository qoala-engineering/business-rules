from business_rules.actions import BaseActions

class ProductActions(BaseActions):

    def __init__(self, product):
        self.product = product