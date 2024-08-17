from fastapi import Response as FastApiRes

class Response:
    def __init__(self, payload={}, message='Request completed successfully.', code=200, error=None):
        self.code = code if code else 200
        self.message = message if message else 'Request completed successfully.'
        self.error = error if error else None
        self.payload = payload if payload else {}

    def send(self, response: FastApiRes=None):
        if response:
            response.status_code = self.code

        return {
            'message': self.message,
            'error': self.error,
            'status': self.code,
            **self.payload
        }


class RespondOk(Response):
    def __init__(self, payload={}, message='Request completed successfully.', code=200, error=None):
        super(RespondOk, self).__init__(payload=payload, message=message, code=code, error=error)
        self.code = code if code else 200
        self.message = message if message else 'Request completed successfully.'


class RespondCreated(Response):
    def __init__(self, payload={}, message='Request created successfully.', code=201, error=None):
        super(RespondOk, self).__init__(payload=payload, message=message, code=code, error=error)
        self.code = code if code else 201
        self.message = message if message else 'Request created successfully.'


class RespondBadRequest(Response):
    def __init__(self, payload={}, message='Please check your request format and try again.', code=400, error=None):
        super(RespondOk, self).__init__(payload=payload, message=message, code=code, error=error)
        self.code = code if code else 400
        self.message = message if message else 'Please check your request format and try again.'


class RespondUnauthenticated(Response):
    def __init__(self, payload={}, message='You are not authenticated. Please login again.', code=401, error=None):
        super(RespondOk, self).__init__(payload=payload, message=message, code=code, error=error)
        self.code = code if code else 401
        self.message = message if message else 'You are not authenticated. Please login again.'


class RespondUnauthorised(Response):
    def __init__(self, payload={}, message='You do not have sufficient authorisation to view this.', code=403, error=None):
        super(RespondOk, self).__init__(payload=payload, message=message, code=code, error=error)
        self.code = code if code else 403
        self.message = message if message else 'You do not have sufficient authorisation to view this.'


class RespondServerError(Response):
    def __init__(self, payload={}, message='A conflict was encountered processing this request.', code=409, error=None):
        super(RespondOk, self).__init__(payload=payload, message=message, code=code, error=error)
        self.code = code if code else 409
        self.message = message if message else 'A conflict was encountered processing this request.'


class RespondServerError(Response):
    def __init__(self, payload={}, message='Unprocessable request format. Please check and try again.', code=422, error=None):
        super(RespondOk, self).__init__(payload=payload, message=message, code=code, error=error)
        self.code = code if code else 422
        self.message = message if message else 'Unprocessable request format. Please check and try again.'


class RespondServerError(Response):
    def __init__(self, payload={}, message='Unexpected server error.', code=500, error=None):
        super(RespondOk, self).__init__(payload=payload, message=message, code=code, error=error)
        self.code = code if code else 500
        self.message = message if message else 'Unexpected server error.'
