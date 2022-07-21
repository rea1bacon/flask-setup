init:
	pip install -r requirements.txt --quiet
	bash scripts/startup.sh
	sudo chmod +x scripts/setup.py
	./scripts/setup.py