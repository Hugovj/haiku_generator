# haiku_generator

Main file = markov_haiku.py.\n
Requires all files to run, plus nltk.cmudict, see below.

Requires nltk, run following in terminal:\n
  pip install nltk\n
Then, in python:\n
  import nltk\n
  nltk.download()\n
This opens a downloader window. Install cmudict in this window. Then run:\n
  from nltk.corpus import cmudict \n
If this doesn't give an error, you can try and run markov_haiku.py\n

Other files:\n
train.txt as database for haiku.\n
missing_words.json as supplement to cmudict for counting syllables\n

If you want to change the training database, replace train.txt, and edit main function of markov_haiku to use your new file (or name it train.txt).\n
Run missing_words_finder first, to add a new missing_words.json, to supplement cmudict. \n
You can test if every word has been added by running test_count_syllables_w_full_corpus.py\n
