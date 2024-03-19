FROM python:3.10


WORKDIR /app

# Copier le contenu du répertoire bookmyparking dans /app/
COPY bookmyparking/. /app/
COPY poetry.lock pyproject.toml /app/

# Installation des dépendances Python
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi


COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]




