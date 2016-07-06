init:
	pip install -r requirements.txt

test:
	clear
	PYTHONPATH=. python -m unittest discover -s tests -v

