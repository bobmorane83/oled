FROM python
WORKDIR /data
RUN pip install -r requirements.txt 
COPY . .
CMD ["python", "signs/sign.py"]
