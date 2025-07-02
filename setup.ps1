Write-Host "Installing project dependencies..."
pip install -r requirements.txt

Write-Host "Installing dev/test dependencies..."
pip install -r requirements-dev.txt

Write-Host "Running tests..."
$env:PYTHONPATH="."
pytest
