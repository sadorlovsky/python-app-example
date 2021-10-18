# Python app example

## Code

First, install [pipenv](https://github.com/pypa/pipenv#installation)

👩‍💻

```bash
brew install pipenv
```

Then clone this repo and go to the app directory

```bash
cd python-app-example
```

Create a project with pipenv

```bash
pipenv --python 3.10
```

Install dependencies

```bash
pipenv install
```

Finally, run the app

```bash
pipenv run python main.py
```

Now you can check http://localhost:8000 in your browser

## Build for production

```bash
docker build -t hardcode-studio/python-app .
```

```bash
docker run -d -p 8000:8000 hardcode-studio/python-app
```
