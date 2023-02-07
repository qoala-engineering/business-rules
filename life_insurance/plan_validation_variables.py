from business_rules.variables import BaseVariables
from business_rules.variables import numeric_rule_variable
from business_rules.variables import boolean_rule_variable
from business_rules.variables import select_multiple_rule_variable

class PlanValidationVariables(BaseVariables):
    def __init__(self, plan_validation):
        self.plan_validation = plan_validation

    @boolean_rule_variable
    def smoking_status(self):
        return self.plan_validation.smoking_status

    @numeric_rule_variable
    def entry_age_policy_holder(self):
        return self.plan_validation.entry_age_policy_holder
    
    @numeric_rule_variable
    def entry_age_insured(self):
        return self.plan_validation.entry_age_insured

    @numeric_rule_variable
    def policy_term(self):
        return self.plan_validation.policy_term

    @numeric_rule_variable
    def premium_payment_term(self):
        return self.plan_validation.premium_payment_term

    @numeric_rule_variable
    def annual_premium(self):
        return self.plan_validation.annual_premium

    @numeric_rule_variable
    def sum_assured(self):
        return self.plan_validation.sum_assured

    paymentFrequencyOptions = {
        "Single":"Single",
        "Annual":"Annual",
        "Semi-Annual":"Semi-Annual",
        "Quarterly":"Quarterly",
        "Monthly":"Monthly",
    }
    @select_multiple_rule_variable(options=paymentFrequencyOptions)
    def premium_payment_frequency(self):
        return [self.plan_validation.premium_payment_frequency]

    @numeric_rule_variable
    def coverage_period(self):
        return self.plan_validation.coverage_period

    @numeric_rule_variable
    def maximum_age_coverage(self):
        return self.plan_validation.maximum_age_coverage