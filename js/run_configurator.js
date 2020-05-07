const fs = require('fs')

EXEC_FOLDER = 'js'
SAVE_RUN_FOLDER = '..'
RUN_FILE_NAME = 'batch_run.sh'
INPUT_FILE = 'config.json'
RUN_TRAIN_TEST_PATH = './run_train_test.sh';
CONFIG_FOLDER = 'conf'
PIPELINE_CONFIG = 'language: en\npipeline:\n  - name: WhitespaceTokenizer\n  - name: RegexFeaturizer\n  - name: LexicalSyntacticFeaturizer\n  - name: CountVectorsFeaturizer\n  - name: CountVectorsFeaturizer\n    analyzer: "char_wb"\n    min_ngram: 1\n    max_ngram: 4\n  - name: DIETClassifier\n    epochs: 100\n  - name: EntitySynonymMapper\n  - name: ResponseSelector\n    epochs: 100'
let run = fs.readFileSync(INPUT_FILE, 'utf-8')
run = JSON.parse(run)

let run_script = '#!/bin/bash\n';

for(let run_name in run) {
    const config_name = `${run_name}_config.yml`;
    let config_file = ''
    const importer = run[run_name].importer
    if(importer) {
        config_file += 'importers:\n';
        config_file += `  - name: "${importer.name}"\n`;
        for (let importer_param in importer.param) {
            config_file += `    ${importer_param}: ${importer.param[importer_param]}\n`;
        }
    }
    config_file += `\n\n${PIPELINE_CONFIG}\n\npolicies:\n`;
    const policies = run[run_name].policy;
    for(let policy of policies) {
        config_file += `  - name: ${policy.name}\n`
        for(let policy_param in policy.param) {
            config_file += `    ${policy_param}: ${policy.param[policy_param]}\n`
        }
    }
    fs.writeFileSync(`${CONFIG_FOLDER}/${config_name}`, config_file);
    const data = run[run_name].data;
    for(let d of data) {
        run_script += `${RUN_TRAIN_TEST_PATH} -d ${d.domain} -c ${EXEC_FOLDER}/${CONFIG_FOLDER}/${config_name} -n ${d.name}_${run_name} -t ${d.train} -e ${d.test}\n`
    }
}
fs.writeFileSync(`${SAVE_RUN_FOLDER}/${RUN_FILE_NAME}`, run_script)