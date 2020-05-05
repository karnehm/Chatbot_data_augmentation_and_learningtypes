#!/bin/bash
while getopts d:t:e:c:n: option
do
case "${option}"
in
d) DOMAIN=${OPTARG};;
t) TRAIN=${OPTARG};;
e) TEST=${OPTARG};;
c) CONFIG=${OPTARG};;
n) NAME=${OPTARG};;
esac
done

if [ \( -z "$DOMAIN" \) -o \( -z "$TRAIN" \) -o \( -z "$TEST" \) -o \( -z "$CONFIG" \) -o \( -z "$NAME" \) ]
then
  RED='\033[0;31m'
  NC='\033[0m' # No Color
  printf "${RED}Some Variables haven't been set. You have to set following:\n -d Domain \n -t Train\n -e Test\n -c Config\n -n Name\n${NC}"
  exit 0
fi

res_dir=./results/$(date '+%Y%m%d_%H%M')$NAME
res_file=$res_dir/test_result.txt
train_file=$res_dir/train_result.txt
mkdir $res_dir
cp $CONFIG ./results/$(date '+%Y%m%d_%H%M')$NAME/
printf "Start Train\n"
rasa train --data $TRAIN -c $CONFIG -d $DOMAIN --out $res_dir
printf "Start Test\n"
rasa test -s $TEST -c $CONFIG  -m $res_dir > $res_file 2>&1
rasa test -s $TEST -c $CONFIG -m $res_dir > $train_file 2>&1
printf "Test finished"

