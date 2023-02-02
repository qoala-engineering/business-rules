class PlanValidationData:
    def __init__(self, smoker, policyTerm, age, paymentTerm, maturityAge, insuredAge, policyHolderAge):
        self.smoker = smoker
        self.policyTerm = policyTerm
        self.age = age
        self.paymentTerm = paymentTerm
        self.maturityAge = maturityAge
        self.insuredAge = insuredAge
        self.policyHolderAge = policyHolderAge

class PlanValidation:
    smoker: bool
    policyTerm: int
    age: int
    paymentTerm: str
    maturityAge: int
    insuredAge: int
    policyHolderAge: int
    def __init__(self, identifier, data):
        self.identifier = identifier
        self.smoker = data.smoker
        self.policyTerm = data.policyTerm
        self.age = data.age
        self.paymentTerm = data.paymentTerm
        self.maturityAge = data.maturityAge
        self.insuredAge = data.insuredAge
        self.policyHolderAge = data.policyHolderAge