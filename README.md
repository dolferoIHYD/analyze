
### Setup on Windows x64

Anaconda 4.2 (Python 3.5)

Packages:

1. scikit-learn  
2. theano  
`conda install mingw libpython theano=0.8`  
3. tensorflow (optional)  
`pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.0.1-cp35-cp35m-win_amd64.whl`  
or  
`pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.0.1-cp35-cp35m-win_amd64.whl`
3. keras  
`conda install -c conda-forge keras`
4. lasagne  
`pip install https://github.com/Lasagne/Lasagne/archive/master.zip`
5. nolearn  
`pip install nolearn`
6. seaborn (optional)   
`conda install seaborn`

### Examples

learn.py:

1. Logistic regression
2. kNN
3. SVM
4. Naive Bayes
5. Random forest
6. Gaussian Process (don't run on > 5000 samples!)
7. Multi-layer Perceptron (scikit built-in Neural Network) - 2 solvers
8. Keras
9. Lasagne

Use flag variables to switch models on/off

Use Env variables on top to tune NN backends

Settings for all NN examples are similar so result are very close


### Depends:

python3.5-dev (via apt)
python3.5-tk (via apt)
