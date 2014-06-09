.PHONY: install
SHELL := /bin/zsh

install: venv
	. venv/bin/activate; pip install --editable .

nopyc:
	find . -name '*.pyc' | xargs rm -f || true
	find . -name __pycache__ | xargs rm -rf || true

venv:
	virtualenv venv

clean:
	rm -rf venv
