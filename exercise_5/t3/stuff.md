# Hello World

## Elevation of Privilege

Removed taking additional parameters (that are not required!) from the URL:

```text
# self._AddParameter('is_author', params, profile_data)
# self._AddParameter('is_admin', params, profile_data)
# self._AddParameter('private_snippet', params, profile_data)
```

## Cookie Manipulation

My solution for cookie creation is

I will create a cryptographically secure hash from the text `username|admin|author`, anytime I will need to identify someone I will use this same technique

I will hash it from the user_id and then figure out the rest. <_CreateCookie function> and <_ParseCookie function>

and I will fix how new user is created. [DONE]

```python
import re
pattern = r"^[a-zA-Z0-9]+$"
regex = re.compile(pattern)
match = regex.match(uid)

if match is None:
    message = 'Invalid Character in username. Alphanumeric characters are acceptable only!'
    return self._SendError(message, cookie, specials, params, new_cookie_text)
```
