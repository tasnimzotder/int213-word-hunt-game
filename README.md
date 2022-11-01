![image](assets/game_play.jpg)

<p align="center">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/tasnimzotder/int213-word-hunt-game?style=flat-square">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/tasnimzotder/int213-word-hunt-game?style=flat-square">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/tasnimzotder/int213-word-hunt-game?style=flat-square" />
    <img alt="Python GUI library" src="https://img.shields.io/badge/GUI-Tkinter-blue?style=flat-square" / >
    <img alt="GitHub" src="https://img.shields.io/github/license/tasnimzotder/int213-word-hunt-game?style=flat-square">
</p>

# 🎮 INT213 - Word Hunt Game

### Let's hunt the lost words 🔍

## 🎉 Getting Started

1. Clone (Download) the project

```bash
git clone https://github.com/tasnimzotder/int213-word-hunt-game.git
```

2. Run the program

a. Windows

```bash
./run.ps1
```

b. Linux

```bash
bash run.sh
```

3. Or to run the program in a docker container

```bash
docker build -t word-hunt-game .
docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --rm word-hunt-game
```

## 🧑‍🤝‍🧑 Collaborators

<p align="center">
    <a href="https://github.com/tasnimzotder">
        <img alt="Tasnim Zotder" src="assets/tasnim.png"  height="75"/>
        &nbsp&nbsp&nbsp&nbsp
    </a>
    <a href="https://github.com/Souvik-Ghosal">
        <img alt="Tasnim Zotder" src="assets/souvik.png"  height="75"/>
        &nbsp&nbsp&nbsp&nbsp
    </a>
    <a href="https://github.com/fizannaik">
        <img alt="Tasnim Zotder" src="assets/fizan.png"  height="75"/>
        &nbsp&nbsp&nbsp&nbsp
    </a>
<p>

## 📷 Screenshots

![game setup](assets/game_setup.jpg)

## 📃 References

- **YAML Docs**: [Stack Abuse](https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/)
- **Tkinter GUI Docs**: [Real Python](https://realpython.com/python-gui-tkinter/)
- **Word Search Logic**: [PythonWordSearch](https://github.com/SpartanApple/PythonWordSearch)

## 📝 License

This project is licensed under [MIT License](LICENSE).
