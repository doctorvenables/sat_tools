#!/bin/bash
norad_id="$1"
min_norad=10000
max_norad=99999
#echo ${HOME}
#ls ${HOME}
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
file_dest=${HOME}/satnogs.txt
echo "NORAD ID $norad_id is"
test -f ${HOME}/satnogs.txt ||  wget https://celestrak.com/NORAD/elements/satnogs.txt -P ${HOME}

grep -B 1 $norad_id ${HOME}/satnogs.txt | head -n1 -


