from os import getenv as __getenv
from datetime import timedelta
from octoauth.middleware.configure import Configuration, file_content

# Development configuration
dev_config = Configuration(
    JWT_LIFETIME=timedelta(hours=10),
    JWT_SECRET_KEY=file_content('tests/pki/private.pem'),
    SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite'
)

# Test configuration
test_config = Configuration(
    JWT_LIFETIME=timedelta(hours=1),
    JWT_SECRET_KEY=file_content('tests/pki/private.pem'),
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
)

# Production configuration
prod_config = Configuration(
    JWT_LIFETIME=timedelta(minutes=15),
    JWT_SECRET_KEY=file_content('tests/pki/private.pem'),
    SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite'
)

# Select appropriate environment based on OCTOAUTH_ENV environment variable.
ENVIRONMENT = __getenv("OCTOAUTH_ENV", "develop")
SETTINGS = {
    "develop": dev_config,
    "test": test_config,
    "production": prod_config
}[ENVIRONMENT]
