class SuccessResponse:
    status: str
    code: int
    message: str
    data: object
    meta: object
    def __init__(self, message, data, meta, code=200) -> None:
        self.status = "success"
        self.code = code
        self.message = message
        self.data = data
        self.meta = meta

class FailedResponse:
    status: str
    message: str
    data: object
    meta: object
    def __init__(self, message, data, meta,code=500) -> None:
        self.status = "failed"
        self.code = code
        self.message = message
        self.data = data
        self.meta = meta