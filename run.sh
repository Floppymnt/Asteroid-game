if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv

    echo "Installing dependencies..."

    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        source .venv/Scripts/activate
    else
        source .venv/bin/activate
    fi

    uv pip install .
fi




source .venv/bin/activate
uv run main.py