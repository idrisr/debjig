import pytest
import logging
from debjig import log 

LOGGER = logging.getLogger(__name__)

@pytest.fixture
def A():
    class A:
        @log()
        def b(self): pass
    return A

@pytest.fixture
def clearlog(caplog): caplog.clear()

def test_default_log(caplog, A, clearlog):
    with caplog.at_level(logging.DEBUG):
        A().b()
        assert 'A.b' in caplog.text

def test_custom_msg(caplog, A, clearlog):
    A.b = log(msg='hey man')(A.b)
    with caplog.at_level(logging.DEBUG):
        A().b()
        assert 'hey man' in caplog.text

def test_clear_custom_msg(caplog, A, clearlog):
    A.b = log(msg='hey man')(A.b)
    A.b = log()(A.b)

    with caplog.at_level(logging.DEBUG):
        A().b()
        assert 'A.b' in caplog.text

def test_level_setting(caplog, A, clearlog):
    with caplog.at_level(logging.WARNING):
        A().b.set_level(logging.WARNING-1)
        A().b.set_msg("yo man")
        A().b()
        assert not caplog.text

