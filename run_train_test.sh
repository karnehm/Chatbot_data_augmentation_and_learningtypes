#!/bin/bash
while getopts d:t:e:c:n:x: option
do
case "${option}"
in
d) DOMAIN=${OPTARG};;
t) TRAIN=${OPTARG};;
e) TEST=${OPTARG};;
c) CONFIG=${OPTARG};;
n) NAME=${OPTARG};;
x) TESTCONFIG=${OPTARG};;
esac
done

if [ \( -z "$DOMAIN" \) -o \( -z "$TRAIN" \) -o \( -z "$TEST" \) -o \( -z "$CONFIG" \) -o \( -z "$NAME" \) -o \( -z "$TESTCONFIG" \) ]
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
printf "Run with configurations\n\nDomain: $DOMAIN\nConfig: $CONFIG\nTrain-Data: $TRAIN\nTest-Data: $TEST\nName: $NAME" > $res_dir/input_values.txt
cp $CONFIG ./results/$(date '+%Y%m%d_%H%M')$NAME/config.yml
printf "Start Train\n"
rasa train --data $TRAIN -c $CONFIG -d $DOMAIN --out $res_dir
printf "Start Test\n"
echo $res_dir
python test.py -m $res_dir -t $TRAIN -e $TEST -c $TESTCONFIG -n $NAME -o $CONFIG
printf "Test finished"

