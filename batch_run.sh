#!/bin/bash
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_only_config.yml -n embedding_ted_only -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_multi_chitchat_per_story_1_config.yml -n embedding_ted_multi_chitchat_per_story_1 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_multi_chitchat_per_story_2_config.yml -n embedding_ted_multi_chitchat_per_story_2 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_multi_chitchat_per_story_3_config.yml -n embedding_ted_multi_chitchat_per_story_3 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_multi_chitchat_per_story_4_config.yml -n embedding_ted_multi_chitchat_per_story_4 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_multi_chitchat_per_story_5_config.yml -n embedding_ted_multi_chitchat_per_story_5 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_single_chitchat_per_story_1_config.yml -n embedding_ted_single_chitchat_per_story_1 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_single_chitchat_per_story_2_config.yml -n embedding_ted_single_chitchat_per_story_2 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_single_chitchat_per_story_3_config.yml -n embedding_ted_single_chitchat_per_story_3 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_single_chitchat_per_story_4_config.yml -n embedding_ted_single_chitchat_per_story_4 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
./run_train_test.sh -d embedding_domain.yml -c js/conf/ted_single_chitchat_per_story_5_config.yml -n embedding_ted_single_chitchat_per_story_5 -t data/embedding_paper/train -e data/embedding_paper/test -x config.yml
