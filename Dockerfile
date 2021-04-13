FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut \
    pandas \
    git+https://github.com/deepy/glicko2 \
    pylint \
    pytest \
    pytest-cov \
    rope
