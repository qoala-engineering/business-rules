class PlanValidation:
    smoking_status: bool
    entry_age_policy_holder: int
    entry_age_insured: int
    policy_term: int
    premium_payment_term: int
    annual_premium: int
    sum_assured: int
    premium_payment_frequency: str
    coverage_period: int
    maximum_age_coverage: int
    gender: str
    def __init__(self, **kwargs):
        self.smoking_status = kwargs["smoking_status"]
        self.entry_age_policy_holder = kwargs["entry_age_policy_holder"]
        self.entry_age_insured = kwargs["entry_age_insured"]
        self.policy_term = kwargs["policy_term"]
        self.premium_payment_term = kwargs["premium_payment_term"]
        self.annual_premium = kwargs["annual_premium"]
        self.sum_assured = kwargs["sum_assured"]
        self.premium_payment_frequency = kwargs["premium_payment_frequency"]
        self.coverage_period = kwargs["coverage_period"]
        self.maximum_age_coverage = kwargs["maximum_age_coverage"]
        self.gender = kwargs["gender"]