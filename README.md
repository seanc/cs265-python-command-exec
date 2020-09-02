### Python Command Executor

This is a dangerous script that executes its arguments in a shell. You can put any command you like and it will be executed, however, some are blacklisted and will error if used.

Usage:
```
$ python run.py ls
```

Advanced Usage:
```
$ python run.py ls | grep run.py
```