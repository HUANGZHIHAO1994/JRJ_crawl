#!/bin/bash

# bash ./start_crawl_by_year.sh 2007


for((i=5;i<=12;i++))
do
    python main_crawl_shell.py $* $i &
done