init:
	pip install -r requirements.txt --quiet
	bash scripts/setup.sh
	sudo chmod +x scripts/setup.py
	./scripts/setup.py