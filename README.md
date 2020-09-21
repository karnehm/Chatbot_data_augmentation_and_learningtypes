# Master Arbeit - Datenaugmentierung im Dialog Management 

Bei diesem Projekt handelt es sich um die Implementierungen, welche im Rahmen  der Master Arbeit *Datenaugmentierung und der Vergleich verschiedener Lernvarianten im Dialog Management von Gesprächsassistenten* umgesetzt wurden.

Der theoretische Hintergrund ist zum aktuellen Zeitpunkt nicht frei zugänglich.

## Installation

Die Implementierung erfolgte unter Verwendung von `python 3.7.7`, `pip 20.0.2` und `node 12.16.1`.

Das Projekt ist wie folgt zu installieren:

```shell
pip install -Iv rasa==1.8.2
git clone https://github.com/karnehm/Chatbot_data_augmentation_and_learningtypes
```

## Tests 

Tests sind ausführbar über eine Konfiguration unter `js/config.json`. Innerhalb dieser Konfiguration lassen sich die einzelnen Varianten der Trainingsdaten, Augmentierungen und deren Konfigurationen, sowie Lernvarianten in Form der Policies konfigurieren. 

### Definition des Formats

```json
{
  "test_config": "<path_to_test_config.yml>",
  "send_mail": "<sending_email_after_test_boolean>",
  "email": "<your@email.address.com>",
  "runs": {
    "<name_of_configuration>": {
      "importer": {
        "name": "<Package_of_Augmentation_importer",
        "param": {
          "<pamam_1>": "<value_1>",
          "<pamam_2>": "<value_2>"
        }
      },
      "policy": [
        {
          "name": "<Package_of_Policy>",
          "param": {
            "<pamam_1>": "<value_1>",
            "<pamam_2>": "<value_2>"
          }
        }
      ],
      "data": [
        {
          "name": "<name_of_data>",
          "domain": "path_to_domain.yml",
          "train": "path_to_train_data",
          "test": "path_to_test_data"
        }
      ]
    }
  }
}
```


### Testlauf

Um einen Testlauf durchzuführen sind folgende Befehle notwendig.

```bash
cd js
node run_configurator.js
cd ..
./batch_run.sh
```

Nach erfolgreicher Beendigung sind die Ergebnisse innerhalb des Ordners `./results` nachzusehen und mittels der Methoden in `Trainingsanalyse.ipynb` im Jupyter Notebook auswertbar. 

