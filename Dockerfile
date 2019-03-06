FROM python:3-alpine
MAINTAINER Andreas Haug "andreas-stusvik.haug@capgemini.com"
COPY ./service /service
WORKDIR /service
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
ENTRYPOINT ["python"]
CMD ["gcloud-bucket.py"]
