# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:58:58 2017

@author: Sangwoo
"""

import re
import numpy as np
import random
import pandas as pd
import tensorflow as tf

indian = pd.read_csv('/Users/Sangwoo/race_classfication/indian.csv', sep = ",", encoding ='ISO-8859-1')
chinese = pd.read_csv('/Users/Sangwoo/race_classfication/chinese.csv', sep = ",", encoding ='ISO-8859-1')
malay = pd.read_csv('/Users/Sangwoo/race_classfication/malay.csv', sep = ",", encoding ='ISO-8859-1')

#full_name = df[:50]



def clean(full_name):
    full_name = ' '.join(full_name.split())
    full_name = re.sub('[^a-zA-Z\s]', '', full_name)
    return full_name.lower()

def create_feature_vector(cleaned_full_name):
    list_of_numbers = []
    
    for char in cleaned_full_name:
        if char.isspace(): #if char is a space
            list_of_numbers.append(0)
        else:
            list_of_numbers.append(ord(char) - 96)
    return list_of_numbers


def padding(sequence):
    process = np.pad(sequence, (0, 40 - len(sequence)), mode = 'constant')
    return list(process)


def sample_handling(csv, classification):
    samples = []

    names = csv.name.tolist()
    for name in names:
        samples.append([padding(create_feature_vector(clean(name))), classification])

    return samples


class lstm:
    
    def __init__(self, indian, malay, chinese):

        self.learning_rate = 0.001 #94%
        self.n_hidden = 100
        self.max_length = 40
        self.total_epoch = 500
        self.n_input = 27
        self.n_class = 3
        self.batch_size = 100


        all_samples = []
        all_samples += sample_handling(chinese, 0)
        all_samples += sample_handling(malay, 1)
        all_samples += sample_handling(indian, 2)
        
        random.shuffle(all_samples)
        all_samples = np.array(all_samples)
        
    
        test_size = 0.3
        testing_size = int(test_size * len(all_samples))
        self.train_x = np.array(list(all_samples[:,0][:-testing_size]))
        self.train_y = all_samples[:,1][:-testing_size]
        self.test_x = np.array(list(all_samples[:,0][-testing_size:]))
        self.test_y = all_samples[:,1][-testing_size:]


        self.X = tf.placeholder(tf.int32, [None, self.max_length])
        self.Y = tf.placeholder(tf.int32, [None])
        
    def TrainModel(self):
        #one_hot_encoding
        X_one_hot = tf.one_hot(self.X, self.n_input)


        #weight and bias
        W = tf.Variable(tf.random_normal([self.n_hidden, self.n_class]))
        b = tf.Variable(tf.random_normal([self.n_class]))

        #create cell
        cell1 = tf.contrib.rnn.BasicLSTMCell(num_units = self.n_hidden, state_is_tuple=True)
        #dropout_method
        cell1 = tf.contrib.rnn.DropoutWrapper(cell1, output_keep_prob=0.5)

        cell2 = tf.contrib.rnn.BasicLSTMCell(self.n_hidden)


        multi_cell = tf.contrib.rnn.MultiRNNCell([cell1, cell2])


        outputs, states = tf.nn.dynamic_rnn(multi_cell, X_one_hot, dtype=tf.float32)


#outputs = tf.reshape(outputs, [1, 50, 3])
        outputs = tf.transpose(outputs, [1,0,2])
        outputs = outputs[-1]
        self.model = tf.matmul(outputs, W) + b
        
        cost = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
                logits = self.model, labels=self.Y))                 
                 
        optimizer = tf.train.AdamOptimizer(self.learning_rate).minimize(cost)

        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())


        for epoch in range(100):
            for i in range(0, len(self.train_x), self.batch_size):
                x_batch = self.train_x[i:i + self.batch_size]
                y_batch = self.train_y[i:i + self.batch_size]
        #        x_batch = x_batch.reshape((batch_size, max_length))
                _, loss = self.sess.run([optimizer, cost],
                                   feed_dict = {self.X: x_batch, self.Y: y_batch})
            print('Epoch:', '%04d' % (epoch + 1),
                  'cost =', '{:.6f}'.format(loss))

    def testModel(self):
        self.prediction = tf.cast(tf.argmax(self.model, 1), tf.int32)
        prediction_check = tf.equal(self.prediction, self.Y)
        accuracy = tf.reduce_mean(tf.cast(prediction_check, tf.float32))



        predict, accuracy_val = self.sess.run([self.prediction, accuracy],
                                         feed_dict= {self.X: self.test_x, self.Y: self.test_y})             
                 
        print(accuracy_val)
        
    def predict(self, names):
        #{'chinese': 0, 'malay':1, 'indian':2}
        for name in names:
            maxs = [padding(create_feature_vector(clean(name)))]
            print(self.sess.run(self.prediction, feed_dict={self.X: maxs}), name)



names = ['Neil Sebastian DSouza', 'fang jin','siti nurhaliza']        
        
ad = lstm(indian, malay, chinese)
ad.TrainModel()
ad.testModel()
ad.predict(names)