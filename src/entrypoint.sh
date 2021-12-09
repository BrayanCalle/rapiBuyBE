#!/bin/bash

# mkdir -p $HOME/.ipython/profile_default/
# cp ./ipython_config.py $HOME/.ipython/profile_default/

if [ $1 = "shell_plus" ]
then
    exec python manage.py shell_plus
elif [ $1 = "manage" ]
then
    shift
    #exec pipenv run python manage.py $@
    exec python manage.py $@
elif [ $1 = "install" ]
then
    shift
    exec pipenv install $@
elif [ $1 = "runtests" ]
then
    exec python manage.py test -v 2
else
    #exec pipenv run $@
    exec $@
fi
