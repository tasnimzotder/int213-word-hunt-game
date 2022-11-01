# change the directory
cd ./int213-word-hunt-game

# check for pip3 and install if not found
if ! [ -x "$(command -v pip3)" ]; then
    echo 'Error: pip3 is not installed.' >&2
    sudo apt install python3-pip
fi

# check for virtualenv and install if not found
if ! [ -x "$(command -v virtualenv)" ]; then
    echo 'Error: virtualenv is not installed.' >&2
    pip3 install virtualenv
fi

# create virtual environment
virtualenv .venv

# activate virtual environment
source .venv/bin/activate

# install dependencies
pip3 install -r requirements.txt

# run the game
python3 main.py
