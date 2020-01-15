from codebeamer import Codebeamer


def test_client_can_be_created():
    cb = Codebeamer(url='test_url', login='test_login', password='test_password')
    assert cb.base_url == 'test_url'
