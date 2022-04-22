.PHONY: build
.DEFAULT_GOAL := build

build:
	@python -m pip install -r requirements.txt
	@python build.py