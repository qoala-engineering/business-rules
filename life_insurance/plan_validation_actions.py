from business_rules.actions import BaseActions

class PlanValidationActions(BaseActions):
    def __init__(self, planValidation):
        self.planValidation = planValidation