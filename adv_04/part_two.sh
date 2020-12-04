#!/bin/bash

regex=''\
'^'\
'(?=.*byr:((19[2-9]\d)|200[0-2]))'\
'(?=.*iyr:20((1\d)|(20)))'\
'(?=.*eyr:20((2\d)|(30)))'\
'(?=.*hgt:(((1(([5-8]\d)|(9[0-3])))cm)|(((59)|(6\d)|7[0-6])in)))'\
'(?=.*hcl:#[\da-f]{6})'\
'(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth))'\
'(?=.*pid:\d{9}(\s|$))'\
'.+'

# replace empty lines with passport control emoji
sed -z 's/\n\n/🛂/g' $1 | \
# replace line break with space
sed -ze 's/\n/ /g' | \
# replace emoji with new line -> each passport is in a single line now
sed -z 's/🛂/\n/g' | \
# count matches of this extended regex
rg -c --pcre2 "$regex"
#echo "$regex"
