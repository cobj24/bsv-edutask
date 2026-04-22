import pytest

from src.util.validators import getValidator
from src.util.dao import DAO
# tests user.json as validator

# TEMPLATE FOR TESTS

# fixture


# 1. valid user (has all required fields)
# firstName, lastName och email måste vara ifyllt
# om lyckas ska _id returneras
def test_valid_user():


# 2. missing firstName
# saknar firstName
# WriteError
def test_missing_firstName():


# 3. missing lastName
# saknar lastName
# WriteError
def test_missing_lastName():


# 4. missing email
# saknar email
# WriteError
def test_missing_email():


# 5. wrong datatype (firstName)
# ska vara str
# WriteError
def test_wrong_datatype_firstName():


# 6. wrong datatype (lastName)
# ska vara str
# WriteError
def test_wrong_datatype_lastName():


# 7. wrong datatype (email)
# ska vara str
# WriteError
def test_wrong_datatype_email():


# 8. email need to be unique
# WriteError
def test_email_needs_to_be_unique():


# 9. invalid objectID in task
# WriteError
def test_task_should_be_objectID():
