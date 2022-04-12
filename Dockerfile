FROM python:3.9
ADD converter.py   /
CMD [ "python3", "-u", "converter.py" ]