from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np


#MNIST 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
mnist = fetch_openml('mnist_784')
mnist.data = mnist.data/255.0
x_train = mnist.data[:60000]; x_test = mnist.data[600000:]
y_train = np.int16(mnist.target[:60000]);
y_test = np.int16(mnist.target[60000:])

#MPL 분류기 모델을 학습
mlp1 = MLPClassifier(hidden_layer_sizes = (200,1), learning_rate_init = 0.001, batch_size = 512,
                       max_iter = 300, solver='adam',verbose=True)
mlp2 = MLPClassifier(hidden_layer_sizes = (200,2), learning_rate_init = 0.001, batch_size = 512,
                       max_iter = 300, solver='adam',verbose=True)

mlp3 =  MLPClassifier(hidden_layer_sizes = (200,3), learning_rate_init = 0.001, batch_size = 512,
                       max_iter = 300, solver='adam',verbose=True)

mlp4 =  MLPClassifier(hidden_layer_sizes = (200,4), learning_rate_init = 0.001, batch_size = 512,
                       max_iter = 300, solver='adam',verbose=True)

mlp5 = MLPClassifier(hidden_layer_sizes = (200,5), learning_rate_init = 0.001, batch_size = 512,
                       max_iter = 300, solver='adam',verbose=True)


mlp1.fit(x_train,y_train)
res1 = mlp1.predict(x_test)

mlp2.fit(x_train,y_train)
res2 = mlp2.predict(x_test)

mlp3.fit(x_train,y_train)
res3 = mlp3.predict(x_test)

mlp4.fit(x_train,y_train)
res4 = mlp4.predict(x_test)

mlp4.fit(x_train,y_train)
res4 = mlp4.predict(x_test)

#테스트 집합으로 예측

#혼동 행렬
conf = np.zeros((10,10),dtype=np.int16)
for i in range(len(res)):
    conf[res1[i]][y_test[i]] += 1
print(conf)

#테스트 집합으로 예측

#혼동 행렬
conf = np.zeros((10,10),dtype=np.int16)
for i in range(len(res)):
    conf[res2[i]][y_test[i]] += 1
print(conf)

#테스트 집합으로 예측

#혼동 행렬
conf = np.zeros((10,10),dtype=np.int16)
for i in range(len(res)):
    conf[res3[i]][y_test[i]] += 1
print(conf)

#테스트 집합으로 예측

#혼동 행렬
conf = np.zeros((10,10),dtype=np.int16)
for i in range(len(res)):
    conf[res4[i]][y_test[i]] += 1
print(conf)

#테스트 집합으로 예측

#혼동 행렬
conf = np.zeros((10,10),dtype=np.int16)
for i in range(len(res)):
    conf[res5[i]][y_test[i]] += 1
print(conf)

# 정확률 계산

no_correct = 0
for i in range(10):
    no_correct += conf[i][i]

accuracy1 = no_correct / len(res1)
accuracy2 = no_correct / len(res2)
accuracy3 = no_correct / len(res3)
accuracy4 = no_correct / len(res4)
accuracy5 = no_correct / len(res5)

print("테스트 집합( 은닉층 1개 ) 에 대한 정확률은", accuracy1 * 100, "%입니다.")
print("테스트 집합( 은닉층 2개 ) 에 대한 정확률은", accuracy2 * 100, "%입니다.")
print("테스트 집합( 은닉층 3개 ) 에 대한 정확률은", accuracy3 * 100, "%입니다.")
print("테스트 집합( 은닉층 4개 ) 에 대한 정확률은", accuracy4 * 100, "%입니다.")
print("테스트 집합( 은닉층 5개 ) 에 대한 정확률은", accuracy5 * 100, "%입니다.")







