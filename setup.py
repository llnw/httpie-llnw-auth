from setuptools import setup

setup(
    name='httpie-llnw-auth',
    version='1.0.0',
    description='LLNW header-based auth plugin for HTTPie.',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',
    author='Limelight Networks',
    author_email='opensource@llnw.com',
    url='https://github.com/llnw/httpie-llnw-auth',
    py_modules=['httpie_llnw_auth'],
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_llnw_auth = httpie_llnw_auth:LLNWAuthPlugin'
        ]
    },
    python_requires='>=3.6',
    install_requires=[
        'httpie>=2.0.0',
        'requests-llnw-auth>=1.0.1'
    ],
)
