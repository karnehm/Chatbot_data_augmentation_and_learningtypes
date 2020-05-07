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
printf "Run with configurations\n\nDomain: $DOMAIN\nConfig: $CONFIG\nTrain-Data: $TRAIN\nTest-Data: $TEST\nName: $NAME" > $res_dir/input_values.txt
cp $CONFIG ./results/$(date '+%Y%m%d_%H%M')$NAME/
printf "Start Train\n"
rasa train --data $TRAIN -c $CONFIG -d $DOMAIN --out $res_dir
printf "Start Test\n"
rasa test core -s $TEST -m $res_dir --out $res_dir > $res_file 2>&1
grep -v '%' $res_file | grep -v ' 0 ' | grep -v 'rasa' > $res_dir/tmp 2>&1
mv $res_dir/tmp $res_file
rasa test core -s $TRAIN -m $res_dir > $train_file 2>&1
grep -v '%' $train_file | grep -v ' 0 ' | grep -v 'rasa' > $res_dir/tmp 2>&1
mv $res_dir/tmp $train_file
printf "Test finished"

