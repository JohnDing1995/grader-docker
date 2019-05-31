#!/bin/sh -eu

setuidgid $USER python3 manage.py migrate
