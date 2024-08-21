# Vyper

## Requirements

- Have `python3` installed
- Have [`pipenv`](https://pipenv.pypa.io/en/latest/) installed
- Have [`nodemon`](https://github.com/remy/nodemon) installed

## Setup

(Replace `py` with `pipenv` if you don't have it aliased)

Install dependencies

```
py install
```

## Run the bot

```
py run dev
```

Any changes you make to any files will automatically restart the bot.

## Commands

You can run these commands in the Discord server to control the bot.

### !save

This will save any arbitrary message to the database.

```
!save Hello there, this is a test.
!save Save this message too pls
```

### !load

This will load all messages that the user had previously saved and displays them in an embedded message.

```
!load
```
