FROM python:3.12 as base
# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
# Add path to poetry to container PATH var
ENV PATH=$PATH:/root/.local/bin

# Copy app files to container
COPY . /opt/app

# Install project dependencies
WORKDIR /opt/app
RUN poetry install

# Run app
ENTRYPOINT poetry run flask run --host=0.0.0.0

# ---------------------------------------------------------------

FROM base as development
ENV FLASK_DEBUG=true
# Run app
ENTRYPOINT poetry run flask run --host=0.0.0.0
# ---------------------------------------------------------------

FROM base as production
ENV FLASK_DEBUG=false
# Run app
ENTRYPOINT poetry run flask run --host=0.0.0.0
