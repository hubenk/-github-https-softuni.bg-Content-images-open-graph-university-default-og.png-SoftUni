class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split("@")

    if len(username) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    end_mail = domain.split(".")

    if end_mail[-1] not in ("com", "bg", "org", "net"):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
