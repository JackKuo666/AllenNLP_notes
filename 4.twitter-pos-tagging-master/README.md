# twitter-pos-tagging
from : https://github.com/mrdanshih/twitter-pos-tagging

Exploration of POS tagging via sequence labeling, via a conditional random field model.
Utilizes the AllenNLP library for simplifying embedding and encoding.

CRF allows incorporating of sequential information of labels as a feature into the model. Predicting the best sequence from CRF requires a decoding step, the Viterbi algorithm for CRF sequence tagging, which is implemented in ```viterbi.py```.


### Usage
To run allennlp training/evaluation with CRF implementation:

```allennlp train ./config/neural_crf_pos.json -s ./model/neural_crf --include-package neural_crf```

```allennlp evaluate <MODEL_DIR>/model.tar.gz [JSON test data file path] --include-package neural_crf```
