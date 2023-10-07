# Activate the virtual environment (on Windows)
& "C:\Users\paliw\OneDrive\Desktop\Quantum_softdev\venv\Scripts\activate"

# Run the test suite (assumes your test file is named 'test_app.py')
python -m pytest test_app.py

# Capture the exit code of the previous command
$exitCode = $LASTEXITCODE

# Deactivate the virtual environment
deactivate

# Exit with the appropriate exit code
exit $exitCode
