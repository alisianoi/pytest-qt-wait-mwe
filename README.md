First, install the dependencies:

```
pip install -r requirements.txt
```

Then, run the test multiple times:

```
pytest --count 100
```

There is a good chance that the tests will hang indefinitely :(
Sometimes they crash with a segfault instead (hard to catch)