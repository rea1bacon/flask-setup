# Eazy Flask Setup
### Setup a flask website in one minute

## Installation
```bash
git clone https://github.com/evilcater/flask-setup.git
cd flask-setup
python3  -m venv venv
```
For linux
```bash
source venv/bin/activate
```
For windows
```powershell
venv\scripts\activate.bat
```

```bash
sudo make
cd src/
python3 app.py # Or py app.py for windows
```

## If you can't make 

```bash
pip install -r requirements.txt
bash scripts/setup.sh
py scripts/setup.py
```
And change host file by adding this two lines :
```
127.0.0.1 flaskezs.com
127.0.0.1 api.flaskezs.com
```
