#!/bin/bash

echo "Please enter your Shodan API key, followed by [ENTER]:"
read shodankey

shodan init $shodankey

shodan data list --dataset=raw-daily > shodan_list_daily_files.txt

cat shodan_list_daily_files.txt | while read filename filesize id link
do 
	echo $filename
	aria2c -x4 -s4 -o shodan_raw_$filename $link
	zgrep -i 'mikrotik' shodan_raw_$filename| gzip > shodan_mikrotik_$filename
	python3 simplify_json_gz.py -i shodan_mikrotik_$filename
	mv $filename /Volumes/LaCie
done