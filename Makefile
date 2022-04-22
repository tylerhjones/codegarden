.PHONY: build
.DEFAULT_GOAL := build

build:
	@python -m install requirements.txt
	@python build.py