# 1.simple_tagger.json
## 1.1 train
```
allennlp train 1.simple_tagger.json -s ./tmp/simple_tagger
```
## 1.2 evaluation
```
allennlp evaluate ./tmp/simple_tagger/model.tar.gz ./data/sentences.small.dev
```
## 1.3 prediction
```
allennlp evaluate ./tmp/simple_tagger/model.tar.gz ./input.txt
```
# 2.crf
coming soon