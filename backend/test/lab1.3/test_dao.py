import pytest
from pymongo.errors import WriteError
from src.util.dao import DAO

# 1. valid user (has all required fields)
# firstName, lastName och email måste vara ifyllt
# om lyckas ska _id returneras
def test_valid_user(user_dao):
    data = {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane@test.com"
    }

    result = user_dao.create(data)

    assert result["firstName"] == "Jane"
    assert result["lastName"] == "Doe"
    assert result["email"] == "jane@test.com"
    assert "_id" in result


# 2. missing firstName
# saknar firstName
# WriteError
def test_missing_firstName(user_dao):
    data = {
        "lastName": "Doe",
        "email": "test@test.com"
    }

    with pytest.raises(WriteError):
        user_dao.create(data)



# 3. missing lastName
# saknar lastName
# WriteError
def test_missing_lastName(user_dao):
    data = {
        "firstName": "Jane",
        "email": "test@test.com"
    }

    with pytest.raises(WriteError):
        user_dao.create(data)

# 4. missing email
# saknar email
# WriteError
def test_missing_email(user_dao):
    data = {
        "firstName": "Jane",
        "lastName": "Doe"
    }

    with pytest.raises(WriteError):
        user_dao.create(data)


# 5. wrong datatype (firstName)
# ska vara str
# WriteError
def test_wrong_datatype_firstName(user_dao):
    data = {
        "firstName": 76,
        "lastName": "Doe",
        "email": "hej@hej.com"
    }

    with pytest.raises(WriteError):
        user_dao.create(data)

# 6. wrong datatype (lastName)
# ska vara str
# WriteError
def test_wrong_datatype_lastName(user_dao):
    data = {
        "firstName": "Jane",
        "lastName": True,
        "email": "hej@hej.com"
    }

    with pytest.raises(WriteError):
        user_dao.create(data)

# 7. wrong datatype (email)
# ska vara str
# WriteError
def test_wrong_datatype_email(user_dao):
    data = {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": 1231
    }

    with pytest.raises(WriteError):
        user_dao.create(data)


# 8. email need to be unique
# WriteError
def test_email_needs_to_be_unique(user_dao): #### Det här testet funkar inte?
    data1 = {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "same@test.com"
    }

    data2 = {
        "firstName": "John",
        "lastName": "Smith",
        "email": "same@test.com"
    }

    # första insert ska funka
    user_dao.create(data1)

    # andra ska faila
    with pytest.raises(WriteError):
        user_dao.create(data2)

# 9. invalid objectID in task
# WriteError
def test_task_should_be_objectID(user_dao):
    data = {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "test@test.com",
        "tasks": ["bananas"]
    }

    with pytest.raises(WriteError):
        user_dao.create(data)
