{
    poetry --version
} || {
    {
        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
    } || {
        echo "Unable to install Poetry"
        exit $1
    }
}
dir=$(pwd)
cd $dir/int213-word-hunt-game/
{
    poetry install
    poetry run python3 main.py
} || {
    echo "Error in executing the program"
    exit $1
}
cd $dir
