FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN apk add build-base openldap-dev python2-dev python3-dev 
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

#docker run --hostname ldap.my-company.com --detach osixia/openldap:1.3.0
#e1NTSEF9VElDWTN1OUlqUkJ6WUdMNzIxMWFpNkQvVnEwMkhJYTg=