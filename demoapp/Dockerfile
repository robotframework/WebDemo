FROM python:alpine
COPY ./ /demoapp/
EXPOSE 7272
RUN chmod +x /demoapp/server.py
ENTRYPOINT [ "/demoapp/server.py" ]
