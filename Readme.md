# Create Virtual Env

    python3 -m venv /path/to/new/virtual/environment
    or
    python -m venv venv

# Activate Virtual Env

    cd venv/Scripts
    activate
    pip install -r requirements.txt

# Freeze the packages

    python -m pip freeze

# Factory faker creating models

    Providers here --> https://faker.readthedocs.io/en/master/providers/faker.providers.python.html
    To create in batch --> "posts = PostFactory.create_batch(10)"
