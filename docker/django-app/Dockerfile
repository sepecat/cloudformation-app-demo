FROM python
RUN mkdir -p /home/ubuntu/django-app/
WORKDIR /home/ubuntu/django-app/
COPY . .
RUN python -m venv /home/ubuntu/django-app
RUN /bin/bash -c "source bin/activate; pip3 install -r requirements.txt"
VOLUME /home/ubuntu/django-app/run/
VOLUME /home/ubuntu/django-app/static/
EXPOSE 8000
ENTRYPOINT ["/home/ubuntu/django-app/bin/gunicorn_start"]
