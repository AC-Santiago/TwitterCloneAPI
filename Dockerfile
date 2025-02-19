FROM python:3.11.11

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV PYTHONUNBUFFERED=1

WORKDIR /TwitterClone

COPY ./requirements.txt /TwitterClone/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /TwitterClone/requirements.txt

COPY ./src /TwitterClone/app

EXPOSE 8000

#CMD ["ls","-la"]
#CMD ["pip","list"]
CMD ["fastapi", "run", "src/main.py", "--port", "8000"]
