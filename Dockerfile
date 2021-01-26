FROM python:3.7
RUN pip3 install pipenv
COPY ./app /app
RUN cd /app && pipenv update
CMD ["uvicorn", "app.main:app", "--host" ,"0.0.0.0" ,"--port" ."15400"]
