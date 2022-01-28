import os


class InvestTokenNotFound(Exception):
    pass


try:
    INVEST_TOKEN = os.environ["INVEST_TOKEN"]
except KeyError as e:
    raise InvestTokenNotFound("env INVEST_TOKEN not found") from e
