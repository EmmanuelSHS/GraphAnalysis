#!/bin/bash

for SCRIPT in ./*
do 
    if [[ $SCRIPT =~ .py ]];then
        python $SCRIPT
    fi
done
