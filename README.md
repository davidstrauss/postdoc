# POSTDoc
Echoes the body of any POSTs to the shell. Powered by Twisted Web.

## Installation

 1. sudo apt-get install python-twisted-web

## Running

    python run.py

## Usage

    curl -X POST -d "content-for-job" http://localhost:8080/

## Limitations

 * Only listens on *:8080
