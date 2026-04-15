import pytest
from src.util.helpers import hasAttribute

@pytest.mark.unit
def obj():
    return {'name': 'Jane'}

def test_hasAttribute_true(obj):
    result = hasAttribute(obj, 'name')
    assert result == True