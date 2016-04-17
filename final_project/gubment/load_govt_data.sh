#!/bin/bash

rm *.xml
wget https://travel.state.gov/_res/rss/TAs.xml
wget https://travel.state.gov/_res/rss/TWs.xml

if [ -f TAs.xml ];
then
   if [ -f TWs.xml ];
   then
      python load_govt_data.py
   else
      echo "File TWs.xml does not exist!"
   fi
else
   echo "File TAs.xml does not exist."
fi
