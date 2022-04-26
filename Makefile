.PHONY: build
.DEFAULT_GOAL := build

build:
	@python -m pip install -r requirements.txt
	@python build.py

serve:
	python3 -m http.server 8888 --directory ./generated