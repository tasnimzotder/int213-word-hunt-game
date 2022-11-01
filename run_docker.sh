# script to run the game in docker

# create docker image
docker build -t word-hunt-game .

# run docker image
docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --rm word-hunt-game
