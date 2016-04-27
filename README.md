# POSTDoc
Echoes the body of any POSTs to the shell. Powered by Twisted Web.

## Installation

### Ubuntu

    sudo apt-get install python-twisted-web

### Fedora

    sudo dnf install python-twisted

## Running

    python run.py

## Usage

    curl -X POST -d "content-for-job" http://localhost:8080/

## Limitations

 * Only listens on *:8080
