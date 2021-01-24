# face_gender
Simple face gender detection for an online meeting, modified based on [face-emotion](https://github.com/DeepSE/face-emotion)


## Run
```bash
pip install -r requirements.txt
python main.py
```

## Recommendations

- To avoid polluting the Python environment, please consider to use `venv` in Python 
- You should also setup `pyenv`
    - This application needs `Tcl/Tk` support, you need to follow this [stackoverflow discussion](https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos) in order to install a Python environment with `Tcl/Tk` support

### Demo screenshots

Example 1 - Only 1 male on the screen

![Example 1](screenshots/example1.png)

Example 2 - 1 male and 1 female on the screen 

![Example 2](screenshots/example2.png)

Example 3 - Multiple people on the screen

- Note: The sample Zoom screenshot is downloaded from the web

![Example 3](screenshots/example3.png)




