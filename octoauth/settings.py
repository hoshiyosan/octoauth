from os import getenv as __getenv
from octoauth.middleware.configure import Configuration

# Development configuration
dev_config = Configuration(
    JWT_SECRET_KEY=3, 
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
)

# Test configuration
test_config = Configuration(
    JWT_SECRET_KEY=5,
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
)

# Production configuration
prod_config = Configuration(
    JWT_SECRET_KEY=3, 
    SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite'
)

# Select appropriate environment based on OCTOAUTH_ENV environment variable.
ENVIRONMENT = __getenv("OCTOAUTH_ENV", "develop")
SETTINGS = {
    "develop": dev_config,
    "test": test_config,
    "production": prod_config
}[ENVIRONMENT]
