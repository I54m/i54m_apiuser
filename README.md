# i54m_apiuser
Reusable django app for custom users

# Changelog

## v0.1.0
 - Created app

## v0.2.0
 - made app_id a unique field with a unique prefix
 - added update_last_accessed to update last accessed fields and correctly get users ip
 - added django-ipware v6.0.4+ as a dependency

## v0.2.1
 - Fixed has_valid_api_secret not working correctly
 - Fixed ValueError when getting user's ip

## v0.2.2
 - Fixed last accessed ip always defaulting to "UNKNOWN" (may need tuned later if site is accessible outside cloudflare proxy)