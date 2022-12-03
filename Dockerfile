FROM python:3.8

RUN mkdir -p /opt/services/indospace/src
WORKDIR /opt/services/indospace/src

#RUN pip install gunicorn django
# we use --system flag because we don't need an extra virtualenv
COPY requirements.txt /opt/services/indospace/src/
RUN pip install -r requirements.txt

COPY . /opt/services/indospace/src

EXPOSE 8000

CMD ["gunicorn", "--chdir", "myshop", "--bind", ":8000", "myshop.wsgi:application" ]



# ------------ Original ------------------------------
# FROM python:3.8

# RUN mkdir -p /opt/services/onlineshopantonio/src
# WORKDIR /opt/services/onlineshopantonio/src

# #RUN pip install gunicorn django
# # we use --system flag because we don't need an extra virtualenv
# COPY Pipfile Pipfile.lock /opt/services/onlineshopantonio/src/
# RUN pip install pipenv && pipenv install --system

# COPY . /opt/services/onlineshopantonio/src

# EXPOSE 8000

# CMD ["gunicorn", "--chdir", "myshop", "--bind", ":8000", "myshop.wsgi:application" ]