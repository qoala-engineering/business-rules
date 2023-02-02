from business_rules.variables import BaseVariables
from business_rules.variables import numeric_rule_variable
from business_rules.variables import boolean_rule_variable
from business_rules.variables import string_rule_variable

class PlanValidationVariables(BaseVariables):
    def __init__(self, planValidation):
        self.planValidation = planValidation

    @boolean_rule_variable
    def smoker(self):
        return self.planValidation.smoker

    @numeric_rule_variable
    def policyTerm(self):
        return self.planValidation.policyTerm
    
    @numeric_rule_variable
    def age(self):
        return self.planValidation.age

    @string_rule_variable
    def paymentTerm(self):
        return self.planValidation.paymentTerm

    @numeric_rule_variable
    def maturityAge(self):
        return self.planValidation.maturityAge

    @numeric_rule_variable
    def insuredAge(self):
        return self.planValidation.insuredAge

    @numeric_rule_variable
    def policyHolderAge(self):
        return self.planValidation.policyHolderAge