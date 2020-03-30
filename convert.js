// Script to pre-process Multi-Chitchat Files of Microsoft
// Input-Source: https://github.com/microsoft/BotBuilder-PersonalityChat/tree/master/CSharp/Datasets

const fs = require('fs');

INPUT_FILE = './test.csv';
OUTPUT_NLU = './nlu.md';
OUTPUT_RESPONSES = './responses.yml';

try {
	let data = fs.readFileSync(INPUT_FILE, 'utf-8')
	data = data.split('\n')
	res = []
	for(i = 0; i < data.length; i++) {
		f = data[i].split('\t')
		res.push({intent: f[0], utter: f[1]});
	}
	nlu = "## intent:chitchat1\n- " + res[0].intent;
	responses = "responses:\n  utter_chitchat1:\n  - text: \"" + res[0].utter + "\"";
	intents = "intents:\n  - chitchat1";
	chitchatcounter = 1;

	for(i = 1; i < res.length; i++) {
		if(res[i].utter === res[i-1].utter)
			nlu += "\n- " + res[i].intent;
		else {
			chitchatcounter++;
			nlu += "\n\n## intent:chitchat" + chitchatcounter + "\n- " + res[i].intent;
			responses += "\n  utter_chitchat" + chitchatcounter + ":\n  - text: \"" + res[i].utter + "\"";
			intents += "\n  - chitchat" + chitchatcounter;
		}
	}
	intents += "\n\n";
	fs.writeFileSync(OUTPUT_NLU, nlu)
	fs.writeFileSync(OUTPUT_RESPONSES, intents + responses)
} catch (err) {
	console.error(err)
}
