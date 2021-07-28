`说明`：这个笔记是依赖allennlp 0.9版本，最近重新看的时候AllenNLP已经更新到2.6了，所以根据官方教程跑了最近版本的，可以参见我的新的project： 【[learn_allennlp_get_start](https://github.com/JackKuo666/learn_allennlp_get_start)】, 基本把Allennlp的两种训练方式（python脚本、Allennlp train）以及分别使用lstm和bert来训练分类的例子，以及如何自己预测介绍完了。

# AllenNLP_notes
这是我学习AllenNLP的笔记

# 1.安装

## 1.1 创建 Conda environment with Python 3.6
```py
    conda create -n allennlp python=3.6
```
## 1.2 打开allennlp环境
```py
    source activate allennlp
```
## 1.3 使用pip安装allennlp依赖和包
```py
pip install allennlp
```
## 测试
直接终端：
```py
$ allennlp
```
或者：
```py
python
import allennlp
```
# 2.例子：AllenNLP tutorials
- [x] [AllenNLP tutorials](https://allennlp.org/tutorials)
    - [x] [1.基于LSTM的词性标注（POS）](https://allennlp.org/tutorials)
        
        代码(中文注释)：https://github.com/JackKuo666/NLP_Learning_Way/blob/master/AllenNLP_code/POS_tagger_AllenNLP.py
    - [ ] [2.使用json文本配置的例子]
    - [ ] [3,4,5,...]
# 3.计划
- [ ] [realworldnlp系列教程](http://www.realworldnlpbook.com/blog/)
    - [x] [1.Training a Sentiment Analyzer using AllenNLP (in less than 100 lines of Python code)](http://www.realworldnlpbook.com/blog/training-sentiment-analyzer-using-allennlp.html)
    - [x] [知乎中对realworldnlp的一篇翻译文章](https://zhuanlan.zhihu.com/p/48070968)
    - [ ] [2.Improving a Sentiment Analyzer using ELMo — Word Embeddings on Steroids](http://www.realworldnlpbook.com/blog/improving-sentiment-analyzer-using-elmo.html) [完成一半]
    - [ ] [3,4,5,...]
- [ ] [简书中的一篇教程](https://www.jianshu.com/p/17abfefc1b5b)


# 4.使用allennlp进行中文分类
https://zhuanlan.zhihu.com/p/72854270
