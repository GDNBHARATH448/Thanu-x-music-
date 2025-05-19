import git

git.Git("D:/madhav/myrep/").clone("@github.com:myrepo/scripts")
========= and it throws the following exception =================

Traceback (most recent call last):   
File "C:\Users\1096506\Desktop\gitclone.py", line 1, in <module>
    from git import Repo   
File "C:\Users\1096506\AppData\Local\Programs\Python\Python36-32\lib\site-packages\git\__init__.py", line 84, in <module>
    refresh()   
File "C:\Users\1096506\AppData\Local\Programs\Python\Python36-32\lib\site-packages\git\__init__.py", line 73, in refresh
    if not Git.refresh(path=path):   
File "C:\Users\1096506\AppData\Local\Programs\Python\Python36-32\lib\site-packages\git\cmd.py", line 293, in refresh
    raise ImportError(err) ImportError: Bad git executable. The git executable must be specified in one of the following ways:
     - be included in your $PATH
     - be set via $GIT_PYTHON_GIT_EXECUTABLE
     - explicitly set via git.refresh()

All git commands will error until this is rectified.

This initial warning can be silenced or aggravated in the future by setting the
$GIT_PYTHON_REFRESH environment variable. Use one of the following values:
    - quiet|q|silence|s|none|n|0: for no warning or exception
    - warn|w|warning|1: for a printed warning
    - error|e|raise|r|2: for a raised exception

Example:
    export GIT_PYTHON_REFRESH=quiet
