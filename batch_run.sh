#!/bin/bash
./run_train_test.sh -d data/embedding_paper/domain.yml -c js/conf/rl_only_config.yml -n embedding_5_rl_only -t data/embedding_paper/train_pr/embedding_5.md -e data/embedding_paper/test -x ted_config.yml
./run_train_test.sh -d data/embedding_paper/domain.yml -c js/conf/rl_only_config.yml -n embedding_25_rl_only -t data/embedding_paper/train_pr/embedding_25.md -e data/embedding_paper/test -x ted_config.yml
./run_train_test.sh -d data/embedding_paper/domain.yml -c js/conf/rl_only_config.yml -n embedding_100_rl_only -t data/embedding_paper/train -e data/embedding_paper/test -x ted_config.yml
