# change the directory
cd .\int213-word-hunt-game

# check for pip and install if not found
if (Get-Command pip -ErrorAction SilentlyContinue) { 
    Write-Host "pip found" 
} else { 
    Write-Host "pip not found, installing pip" 
    python -m ensurepip --default-pip
}

# install virtualenv if not found
if (Get-Command virtualenv -ErrorAction SilentlyContinue) { 
    Write-Host "virtualenv found" 
} else { 
    Write-Host "virtualenv not found, installing virtualenv" 
    pip install virtualenv
}

# create virtual environment
Write-Host "creating virtual environment"
virtualenv .venv

# activate virtual environment
Write-Host "activating virtual environment"
. .venv\Scripts\activate

# install dependencies
Write-Host "installing dependencies"
pip install -r requirements.txt

# run the game
python main.py

