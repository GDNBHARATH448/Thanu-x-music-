In termux
$HOME=/data/data/com.termux/files/home/
$PREFIX=/data/data/com.termux/files/usr

Traceback (most recent call last):
  File "/data/data/com.termux/files/usr/lib/python3.6/site-packages/pipenv-11.10.2.dev1-py3.6.egg/pipenv/patched/safety.zip/safety/cli.py", line 15, in <module>
ImportError: cannot import name 'get_installed_distributions'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/data/com.termux/files/usr/lib/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/data/data/com.termux/files/usr/lib/python3.6/runpy.py", line 85, in _run_code
exec(code, run_globals)
  File "/data/data/com.termux/files/usr/lib/python3.6/site-packages/pipenv-11.10.2.dev1-py3.6.egg/pipenv/patched/safety.zip/__main__.py", line 5, in <module>
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 656, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 626, in _load_backward_compatible
  File "/data/data/com.termux/files/usr/lib/python3.6/site-packages/pipenv-11.10.2.dev1-py3.6.egg/pipenv/patched/safety.zip/safety/cli.py", line 18, in <module>
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_internal/__init__.py", line 42, in <module>
    from pip._internal import cmdoptions
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_internal/cmdoptions.py", line 16, in <module>
    from pip._internal.index import (
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_internal/index.py", line 25, in <module>
    from pip._internal.download import HAS_TLS, is_url, path_to_url, url_to_path
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_internal/download.py", line 40, in <module>
    from pip._internal.utils.logging import indent_log
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_internal/utils/logging.py", line 9, in <module>
    from pip._internal.utils.misc import ensure_dir
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_internal/utils/misc.py", line 21, in <module>
    from pip._vendor import pkg_resources
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 3088, in <module>
    @_call_aside
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 3072, in _call_aside
f(*args, **kwargs)
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 3101, in _initialize_master_working_set
    working_set = WorkingSet._build_master()
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 565, in _build_master
    ws = cls()
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 558, in __init__
    self.add_entry(entry)
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 614, in add_entry
    for dist in find_distributions(entry, True):
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1882, in find_eggs_in_zip
    if metadata.has_metadata('PKG-INFO'):
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1399, in has_metadata
    return self.egg_info and self._has(self._fn(self.egg_info, name))
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1755, in _has
    zip_path = self._zipinfo_name(fspath)
  File "/data/data/com.termux/files/home/.local/share/virtualenvs/bi12-aQzmaZd4/lib/python3.6/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1618, in _zipinfo_name
    "%s is not a subpath of %s" % (fspath, self.zip_pre)
AssertionError: /data/data/com.termux/files/usr/lib/python3.6
