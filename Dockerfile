FROM python:3.11.11-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV PYTHONUNBUFFERED=1

WORKDIR /TwitterCloneAPI

COPY ./requirements.txt /TwitterCloneAPI/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /TwitterCloneAPI/requirements.txt

COPY ./src /TwitterCloneAPI/app

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
