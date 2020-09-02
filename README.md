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

## Todo
- Toggle command color output
- Save the command output to a variable
- The command should only be blocked explicitly if it is being run, i.e. `echo rm` shouldn't be blocked, however, `true | rm` should be. 