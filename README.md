<h1> Name-based ethnic classificaction with 
<p>tensorflow and Long Short Term Memory(LSTM)</p></h1>

<h2>Motivation</h2>

People with different ethnic groups differ in the cultural preference like food, clothes

Especially, Malaysia consists of the three main ethnic groups: Malay, Chinese, Indian

So ethnic classification can help to develop a marketing strategy to appeal to customers

<h2>Data</h2>

I collected the total 12,623 numbers of unique names on each ethinic grop: Indian, Malay, Chinese


<h2>Methodology</h2>

<h3>1. Data preprocessing.</h3>
<p>- It is an unstructured dataset(name), which is not organized in the model.</p> 
<p>- There are techniques to unify the format of the name as below.</p>

- Convert capital letters into small letters with regular expression

- Change the letter into number
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Alphabet consists of 26 characters.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*I gave each character the number from 0 to 26, including empty space.</p>

- Each name consists of different alphabet letters, which mean different length.
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*I set maximum number of alphabet as 40.</p> 
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*I added zero(0) into the empty spaces, which is called padding.</p>  
                                                    
- One hot encoding
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Tensorflow provides the function that transforms categorical features to a format that works better with LSTM.</p> 

<h2>Model</h2>
- LSTM
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Used for complex sequence issues which involve NLP .</p> 

- batch issue
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*I set up batch_size which is equal to 100.</p> 

- Dropout
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*It helps to prevent LSTM models from overfitting.(rate=.5)</p> 
<h2>Reference</h2>
<p>- https://github.com/hunkim/DeepLearningZeroToAll</p> 
<p>- https://github.com/golbin/TensorFlow-Tutorials</p> 
<p>- https://jasdeep06.github.io/posts/Understanding-LSTM-in-Tensorflow-MNIST/</p> 


