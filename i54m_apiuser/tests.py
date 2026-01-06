from django.test import TestCase
from i54m_apiuser.models import ApiUser, ApiKey
from django.test import RequestFactory
from unittest.mock import patch

# Create your tests here.
class ApiKeyTestCase(TestCase):
    def setUp(self):
        self.api_user = ApiUser.objects.create(username="testuser")
        self.factory = RequestFactory()

    def test_creation_generates_app_id_and_api_secret(self):
        key = ApiKey.objects.create(api_user=self.api_user, app_id="TESTAPP")
        key.refresh_from_db()

        # Check app_id modified with prefix
        self.assertTrue(key.app_id.endswith("_TESTAPP"))
        self.assertEqual(len(key.api_secret), 64)

    def test_has_valid_api_secret(self):
        key = ApiKey.objects.create(api_user=self.api_user, app_id="TEST")
        key.refresh_from_db()

        self.assertTrue(key.has_valid_api_secret(key.api_secret))
        self.assertFalse(key.has_valid_api_secret("wrong_secret"))

    @patch("i54m_apiuser.models.get_client_ip")
    def test_update_last_accessed_sets_ip_and_timestamp(self, mock_get_ip):
        mock_get_ip.return_value = ["123.45.67.89", None]

        key = ApiKey.objects.create(api_user=self.api_user, app_id="TEST")
        key.refresh_from_db()

        request = self.factory.get("/")
        key.update_last_accessed(request)

        self.assertIsNotNone(key.last_accessed)
        self.assertEqual(key.last_accessed_ip, "123.45.67.89")

        # Test UNKNOWN IP fallback
        mock_get_ip.return_value = [None, None]
        key.update_last_accessed(request)
        self.assertEqual(key.last_accessed_ip, "UNKNOWN")

    def test_str_returns_app_id(self):
        key = ApiKey.objects.create(api_user=self.api_user, app_id="MYAPP")
        key.refresh_from_db()

        self.assertEqual(str(key), key.app_id)