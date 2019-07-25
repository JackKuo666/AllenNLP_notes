# 3.crf_tagger.json
## 1.1 train
```
allennlp train crf_tagger.json -s ./tmp/crf_tagger
```
```
2019-07-25 22:43:11,369 - INFO - allennlp.models.archival - archiving weights and vocabulary to ./tmp/crf_tagger/model.tar.gz
2019-07-25 22:43:12,423 - INFO - allennlp.common.util - Metrics: {
  "best_epoch": 6,
  "peak_cpu_memory_MB": 572.12,
  "training_duration": "0:23:14.892918",
  "training_start_epoch": 0,
  "training_epochs": 15,
  "epoch": 15,
  "training_accuracy": 0.9976812092064583,
  "training_accuracy3": 0.9978815985342953,
  "training_loss": 6.6538102898681375,
  "training_cpu_memory_MB": 572.12,
  "validation_accuracy": 0.9544075582907168,
  "validation_accuracy3": 0.9564878217907602,
  "validation_loss": 155.8506969652678,
  "best_validation_accuracy": 0.9545809135823871,
  "best_validation_accuracy3": 0.957007887665771,
  "best_validation_loss": 108.52731242932771,
  "test_accuracy": 0.9545809135823871,
  "test_accuracy3": 0.957007887665771,
  "test_loss": 108.52731242932771
}

```


## 1.2 evaluation
```
allennlp evaluate ./tmp/crf_tagger/model.tar.gz ./data/twitter_dev.ner
```
```
2019-07-25 22:44:20,238 - INFO - allennlp.commands.evaluate - Finished evaluating.
2019-07-25 22:44:20,239 - INFO - allennlp.commands.evaluate - Metrics:
2019-07-25 22:44:20,239 - INFO - allennlp.commands.evaluate - accuracy: 0.9545809135823871
2019-07-25 22:44:20,239 - INFO - allennlp.commands.evaluate - accuracy3: 0.957007887665771
2019-07-25 22:44:20,239 - INFO - allennlp.commands.evaluate - loss: 108.52731242932771

```

## 1.3 prediction
```
allennlp predict ./tmp/crf_tagger/model.tar.gz ./data/inputs.txt
```

```
"tags": ["B-sportsteam", "I-sportsteam", "O", "B-person", "O", "O", "O", "O"], "words": ["Yayaayayay", "kings", "of", "leon", "tonight", "!", "!", "!"]

"tags": ["O", "O", "O", "O", "B-person", "O"], "words": ["I", "am", "talking", "with", "Robert", "."]
```