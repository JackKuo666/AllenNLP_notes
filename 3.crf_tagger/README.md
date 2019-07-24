# 3.crf_tagger.json
## 1.1 train
```
allennlp train crf_tagger.json -s ./tmp/ctf_tagger
```
## 1.2 evaluation
```
allennlp evaluate ./tmp/crf_tagger/model.tar.gz ./data/twitter_test.pos
```
## 1.3 prediction
```
allennlp predict ./tmp/crf_tagger/model.tar.gz ./data/inputs.txt
```
