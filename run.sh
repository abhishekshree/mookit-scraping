#!/usr/bin/bash
mv *.html ./index.html
test=$(cat index.html | grep -oE '<title id="courseTitle">.*</title>' | sed 's/<title id="courseTitle">//' | sed 's/<\/title>//')

mkdir -pv "$test"

python3 scraper.py $1

mv data.csv ./"$test"
mv index.html ./"$test"

echo "Task Completed."