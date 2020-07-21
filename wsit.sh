#!/bin/bash
norad_id="$1"
min_norad=10000
max_norad=99999

if [[ $norad_id =~ ^-?[0-9]+$ ]]; then
  echo ""
else
  echo "NORAD ID not an integer - exiting"
  exit 1
fi

if [ $norad_id -lt $min_norad ]; then 
  echo "NORAD too low - exiting"
  exit 2
fi

if [ $norad_id -gt $max_norad ]; then 
  echo "NORAD too high - exiting"
  exit 3
fi

echo "NORAD ID $norad_id is"
test -f /home/doctorvenables/satnogs.txt ||  wget https://celestrak.com/NORAD/elements/satnogs.txt 

grep -B 1 $norad_id /home/doctorvenables/satnogs.txt | head -n1 - 


