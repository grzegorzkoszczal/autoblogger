# !/bin/bash

# How to run script:
# Type "source install.sh" in the game's directory to create and activate virtual env

echo Creating Python virtual environment

create=$(python -m venv .autoblogger_dev)
OS=$(uname -s)
if [[ "$OS" == "Darwin" || "$OS" == "Linux" ]]
then
    echo "OS detected: macOS/Linux"
    activate() {
        . $PWD/.autoblogger_dev/bin/activate
    }
    activate    
else
    echo Error. Bash is unavailable for Windows.
fi

# Check if pip is installed:
# And ask for installation if it isn't
# DO BE IMPLEMENTED

echo "Installing dependencies"
install=$(pip install -r requirements.txt)
verify=$(pip list)
echo "(Advice) If You are running Your code in VS Code, use ctrl+shift+p in order to clear Python cache and reload window"