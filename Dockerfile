FROM python as build
RUN apt update && apt install -y build-essential
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM python:slim
WORKDIR /opt/app
COPY --from=build /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY . .

CMD ["python", "signs/sign.py"]
