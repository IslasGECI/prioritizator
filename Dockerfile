FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    git+https://github.com/deepy/glicko2 \
    mutmut \
    pandas \
    pylint \
    pytest \
    pytest-cov \
    rope
