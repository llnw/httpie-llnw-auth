from httpie.plugins import AuthPlugin
from httpie.status import ExitStatus
from requests_llnw_auth import LLNWAuth
import sys
import os

class LLNWAuthPlugin(AuthPlugin):
    name = 'Limelight Networks API Authentication'
    auth_type = 'llnw'
    auth_require = False
    prompt_password = True

    def get_auth(self, username=None, password=None):
        username = os.environ.get('LLNW_API_USERNAME') if username is None else username
        password = os.environ.get('LLNW_API_KEY') if password is None else password

        missing_params = []

        if username is None:
            missing_params.append('API user (env LLNW_API_USERNAME)')
        if password is None:
            missing_params.append('API key (env LLNW_API_KEY)')

        if len(missing_params) > 0:
            sys.stderr.write(f'httpie-llnw-auth error: missing {" and ".join(missing_params)}')
            sys.exit(ExitStatus.PLUGIN_ERROR)

        return LLNWAuth(username, password)
