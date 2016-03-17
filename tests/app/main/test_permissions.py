import pytest

from app.utils import user_has_permissions
from app.main.views.index import index
from werkzeug.exceptions import Forbidden


def _test_permissions(app_, usr, permissions, will_succeed, or_=False, admin_override=False):
    with app_.test_request_context():
        with app_.test_client() as client:
            client.login(usr)
            decorator = user_has_permissions(*permissions, or_=or_, admin_override=admin_override)
            decorated_index = decorator(index)
            if will_succeed:
                response = decorated_index()
            else:
                try:
                    response = decorated_index()
                    pytest.fail("Failed to throw a forbidden exception")
                except Forbidden:
                    pass


def test_user_has_permissions_on_endpoint_fail(app_,
                                               api_user_active,
                                               mock_login,
                                               mock_get_user_with_permissions):
    _test_permissions(
        app_,
        api_user_active,
        ['something'],
        False)


def test_user_has_permissions_success(app_,
                                      api_user_active,
                                      mock_login,
                                      mock_get_user_with_permissions):
    _test_permissions(
        app_,
        api_user_active,
        ['manage_users'],
        True)


def test_user_has_permissions_or(app_,
                                 api_user_active,
                                 mock_login,
                                 mock_get_user_with_permissions):
    _test_permissions(
        app_,
        api_user_active,
        ['something', 'manage_users'],
        True,
        or_=True)


def test_user_has_permissions_multiple(app_,
                                       api_user_active,
                                       mock_login,
                                       mock_get_user_with_permissions):
    _test_permissions(
        app_,
        api_user_active,
        ['manage_templates', 'manage_users'],
        True)


def test_exact_permissions(app_,
                           api_user_active,
                           mock_login,
                           mock_get_user_with_permissions):
    _test_permissions(
        app_,
        api_user_active,
        ['manage_users', 'manage_templates', 'manage_settings'],
        True)


def test_platform_admin_user_can_access_page(app_,
                                             platform_admin_user,
                                             mock_login,
                                             mock_get_platform_admin_user_with_permissions):
    _test_permissions(
        app_,
        platform_admin_user,
        [],
        True,
        admin_override=True)


def test_platform_admin_user_can_not_access_page(app_,
                                                 platform_admin_user,
                                                 mock_login,
                                                 mock_get_platform_admin_user_with_permissions):
    _test_permissions(
        app_,
        platform_admin_user,
        [],
        will_succeed=False)
