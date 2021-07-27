FROM python:3.9

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PYTHONBUFFERED=1

WORKDIR /app/
RUN pip install poetry
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install

EXPOSE 8000

COPY . /app/
