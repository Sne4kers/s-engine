#Hope Popen wont be broken in coming
FROM python:latest

LABEL Maintainer="Sne4kers"

WORKDIR /usr/grading_sys/

COPY ./ ./

CMD [ "python3", "./main.py"]