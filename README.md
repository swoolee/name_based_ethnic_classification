<h1> Name-based ethnic classificaction with 
<p>tensorflow and Long Short Term Memory(LSTM)</p></h1>

<h2>Motivation</h2>

People with different ethnic groups differ in the cultural preference like food, clothes

Especially, Malaysia consists of the three main ethnic groups: Malay, Chinese, Indian

Ethnic classification can help to develop a marketing strategy to appeal to customers

<h2>Data</h2>

I collected the total 12,623 numbers of unique names on each ethinic grop: Indian, Malay, Chinese


<h2>Methodology</h2>

<h3>1. Data preprocessing.</h3>
<p>- It is an unstructured dataset(name), which is not organized in the model.</p> 
<p>- There are techniques to unify the format of the name as below.</p>

- Convert capital letters into small letters with regular expression

- Change the letter into number
<p>&nbsp;*Alphabet consists of 26 characters.</p>
<p>&nbsp;*I gave each character the number from 0 to 26, including empty space.</p>

- Each name consists of different alphabet letters, which mean different length.
<p>*I set maximum number of alphabet as 40.</p> 
<p>*I added zero(0) into the empty spaces, which are padding.</p>  

- One hot encoding
- batch issue

