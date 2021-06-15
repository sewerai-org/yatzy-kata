# Yatzy Kata

Creates Yatzy categories and runs tests on those categories.


```shell
docker build -t yatzy .
docker run --rm -v "$(pwd)"/htmlcov:/app/htmlcov yatzy:latest
open htmlcov/index.html
```