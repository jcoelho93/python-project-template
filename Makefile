.PHONY: build tests

clean:
	rm -rf build dist *.egg-info

build:
	python3 setup.py bdist_wheel

install:
	pip install -r requirements.txt

tests:
	pytest
