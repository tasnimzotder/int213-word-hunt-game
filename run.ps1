try {
    $poetry_ver = poetry --version
    Write-Information $poetry_ver
}
catch {
    try {
        (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
    }
    catch {
        Write-Error "Unable to install Poetry"
    }
}
$currDir = Get-Location
Set-Location $currDir\int213-word-hunt-game\
try {
    poetry version
    poetry install
    poetry run python main.py
}
catch {
    Write-Error "Error in executing the program"
}
Set-Location $currDir