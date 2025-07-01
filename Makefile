install:
	"C:/Users/Jam/AppData/Local/Programs/Python/Python310/python.exe" -m pip install -r requirements.txt
	"C:/Users/Jam/AppData/Local/Programs/Python/Python310/python.exe" -m pip install -r requirements-dev.txt

run:
	"C:/Users/Jam/AppData/Local/Programs/Python/Python310/python.exe" run.py

test:
	PYTHONPATH=. "C:/Users/Jam/AppData/Local/Programs/Python/Python310/python.exe" -m pytest
