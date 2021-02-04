# Todoist-CanvasAPI
Using [Python API wrapper for Canvas](https://github.com/ucfopen/canvasapi) made by @ufcopen and [Todoist Python API](https://github.com/Doist/todoist-python) to transfer all Canvas Assignments to Todoist.

## Todo
- [ ] Integrate to Todoist
- [ ] Clean up Code
- [ ] Experiment more with API
 
## Tokens

1. Create .env file
2. Add your canvas and todoist tokens without "" like below

```
CANVAS_TOKEN = 
TODOIST_TOKEN = 
```

## Installation Guide

Guide to using [pyenv](https://github.com/pyenv/pyenv) for this project

1. `git clone https://github.com/benthecoder/Todoist-CanvasAPI.git` 
2. `cd Todoist-CanvasAPI`
3. `pyenv virtualenv 3.8.0 env_name`
4. `pyenv local env_name`
4. `pip3 install -r requirements.txt`

Using pyenv automatically sets your venv versions within a project directory. 
More on using pyenv [here](https://realpython.com/intro-to-pyenv/#installing-pyenv)

## References 
* https://github.com/scottquach/Canvas-Assignments-Transfer-For-Todoist
