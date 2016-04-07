

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/henriquebastos/eventex.svg?branch=master)]
[![Code Health](https://landscape.io/github/henriquebastos/eventex/master/landscape)]


## Como desenvolver?

1. Clone o repositorio.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instacia com o .env
6. Execute os testes.

'''console
git clone git@github.com:henriquebastos/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/active
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
'''
