FROM python:3.6
RUN mkdir -p /home/ubuntu/hello_django/
WORKDIR /home/ubuntu/hello_django
ADD ./* /home/ubuntu/hello_django/
RUN ln -s lib lib64
# TODO: replace jank tarball install with pkg installs only
WORKDIR /home/ubuntu/hello_django/lib
RUN bash -c "export TARBALL=../python3.6-lib.tgz; tar xzf \$TARBALL; rm -f \$TARBALL"
RUN pip3 install -r /home/ubuntu/hello_django/requirements.txt
WORKDIR /home/ubuntu/hello_django/bin
RUN ln -s /usr/local/bin/python3 python3
RUN ln -s python3 python
VOLUME /home/ubuntu/hello_django/run/
EXPOSE 8000
ENTRYPOINT ["/home/ubuntu/hello_django/bin/gunicorn_start"]
