.PHONY: install
SHELL := /bin/zsh

install: venv
	venv/bin/activate; pip install --editable \
		--index-url http://pypi.python.org/simple --upgrade \
		--download-cache /tmp/pipcache
nopyc:
	find . -name '*.pyc' | xargs rm -f || true
	find . -name __pycache__ | xargs rm -rf || true

venv:
	virtualenv venv

clean:
	rm -rf venv
