#!/bin/bash

# bash ./start_crawl_by_year.sh 2007 股票频道


for((i=11;i<=12;i++))
do
    python main_crawl_shell.py $1 $i &
done

echo "=============================================================="