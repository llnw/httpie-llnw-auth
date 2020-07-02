# httpie-llnw-auth
This module provides an authentication plugin for HTTPie to generate the X-LLNW-Security-* request headers required by Limelight Networks APIs.

## Getting Started
Firstly, install the package:
```
pip install httpie-llnw-auth
```
Then:
```sh
# Simplest example, if LLNW_API_USERNAME and LLNW_API_KEY environment variables are set
http -A llnw https://apis.llnw.com/config-api/v1/svcinst/delivery/shortname/<your shortname>

# Providing API user and key inline (be careful since this will add your API key to your shell history)
http -A llnw -a "myuser:myapikey" https://apis.llnw.com/config-api/v1/svcinst/delivery/shortname/<your shortname>

# Providing API user inline, and interactively prompting for API key
http -A llnw -a myuser https://apis.llnw.com/config-api/v1/svcinst/delivery/shortname/<your shortname>
```
