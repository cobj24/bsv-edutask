import pytest
from src.util.dao import DAO

@pytest.fixture(scope="function")
def user_dao():
    # creat DAO (create collection + validator)
    dao = DAO("test_user")

    # clear collection before test
    dao.drop()

    # create if validatorn is restored
    dao = DAO("test_user")

    yield dao

    # removes collection after test
    dao.drop()