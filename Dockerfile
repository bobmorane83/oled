FROM python
RUN apt-get update && apt-get -y install python3-pil python3-numpy python3-smbus
WORKDIR /data
COPY . .
RUN pip install -r requirements.txt 
CMD ["python", "example/OLED_1in5_rgb_test.py"]
