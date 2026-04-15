import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController

# Mocka databas med epost-adresser?

# kollar om en användare finns med särskild epost
@pytest.mark.lab1
def test_find_one_user():
    # Arrange
    mock_dao = mock.MagicMock()
    mock_dao.find.return_value = [{"email": "hej@kalas.se"}]
    controller = UserController(mock_dao)

    result = controller.get_user_by_email("hej@kalas.se")

    assert result == {"email":"hej@kalas.se"}


# test för att kolla om flera användare finns

# test för att kolla att error blir lyft om email är invalid

# test för inga användare?
