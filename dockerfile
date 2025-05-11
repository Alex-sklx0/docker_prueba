FROM ubuntu:22.04
RUN apt update
RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN pip3 install flask
WORKDIR /app
COPY * ./
EXPOSE 5000
CMD ["python3.10","main.py"]
