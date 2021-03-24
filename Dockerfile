FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut \
    pip install git+https://github.com/deepy/glicko2 \
    pylint \
    pytest \
    pytest-cov
