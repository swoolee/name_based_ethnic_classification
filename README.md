<h1> Name-based ethnic classificaction with 
<p>tensorflow and long short term memory(LSTM)</p></h1>

<h2>Motivation</h2>

People with different ethnic groups differ in the cultural preference like food, clothes

Especially, Malaysia consists of the three main ethnic groups: Malay, Chinese, Indian

Ethnic classification can help to develop a marketing strategy to appeal to customers

<h2>Data</h2>

I collected the total 12,623 numbers of unique names on each ethinic grop: Indian, Malay, Chinese


<h2>Methodology</h2>

<h3>1. Data preprocessing.</h3>
- It is an unstructured dataset(name), which is not organized in the model. 
- So I had to unify the format of the name. There are techniques that I did as below.

- Convert capital letter into small letters with regular expression

- Change the letter into number
..Alphabet consists of 27 characters.I gave each character the number from 0 to 26 including space.

- Each name contains different numbers of alphabet, which mean different length of names.
..I set maximum number of alphabet as 40. 
..I add zero(0) into the empty spaces, which are padding.  

- One hot encoding
- batch issue

