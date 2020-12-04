#!/bin/bash

# replace empty lines with passport control emoji
sed -z 's/\n\n/🛂/g' input.txt | \
# replace line break with space
sed -ze 's/\n/ /g' | \
# replace emoji with new line -> each passport is in a single line now
sed -z 's/🛂/\n/g' | \
# count matches of this extended regex
rg -c --pcre2 "^(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).+"

