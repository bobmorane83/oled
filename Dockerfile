FROM python
WORKDIR /data
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
COPY . .
CMD ["python", "signs/sign.py"]
