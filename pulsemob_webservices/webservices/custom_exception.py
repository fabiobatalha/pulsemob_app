
class CustomException(Exception):
    pass


class CustomErrorMessages:
    INVALID_CREDENTIALS = 'INVALID_CREDENTIALS'
    TOKEN_EXPIRED = 'TOKEN_EXPIRED'
    TOKEN_INVALID = 'TOKEN_INVALID'
    USER_NOT_FOUND = 'USER_NOT_FOUND'
    USER_ALREADY_EXISTS = 'USER_ALREADY_EXISTS'
    NOT_ALLOWED_FOR_PROFILE = 'NOT_ALLOWED_FOR_PROFILE'
    ARTICLE_NOT_FOUND = 'ARTICLE_NOT_FOUND'
    UNEXPECTED_ERROR = 'UNEXPECTED_ERROR'
    SOLR_COMMUNICATION_FAILURE = 'SOLR_COMMUNICATION_FAILURE'
    TOKEN_MISSING = 'TOKEN_MISSING'