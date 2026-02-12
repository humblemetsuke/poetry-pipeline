FROM ubuntu:latest
LABEL authors="tonyn"

ENTRYPOINT ["top", "-b"]
