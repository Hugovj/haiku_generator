# haiku_generator

Main file = markov_haiku.py.

Requires all files to run, plus nltk.cmudict, see below.

Requires nltk, run following in terminal:

  pip install nltk
  
Then, in python:

  import nltk
  
  nltk.download()
  
This opens a downloader window. Install cmudict in this window. Then run:

  from nltk.corpus import cmudict 
  
If this doesn't give an error, you can try and run markov_haiku.py


Other files:

train.txt as database for haiku.

missing_words.json as supplement to cmudict for counting syllables


If you want to change the training database, replace train.txt, and edit main function of markov_haiku to use your new file (or name it train.txt).

Run missing_words_finder first, to add a new missing_words.json, to supplement cmudict.

You can test if every word has been added by running test_count_syllables_w_full_corpus.py

