# TS3000_TheChatBot
Tony Stark 3000 - The Chat Bot Its a very basic level conversational AI.
## Data Preprocessing :
[Downoad Reddit Data From Here](http://files.pushshift.io/reddit/comments/)

### Follow These :
- Put Downloaded data in Data_Preprocessing directory .
- Unzip the .bz2 file  **bzip2 -dk filename.bz2**
    * *Install Bzip2 on Ubuntu * *
          - sudo apt-get update
          - sudo apt-get install bzip2
          - Useful Links : </br>
                [Installing Bzip2](https://www.techwalla.com/articles/how-to-install-bzip2-on-ubuntu) </br>
                [Unzipping Error](https://superuser.com/questions/480950/how-to-decompress-a-bz2-file)
- Run createDB.py 
   > python3 createDB.py 


     This will create Database from Raw JSON text file which you unzipped earlier.
- Run createCORPUS.py
   > python3 createCORPUS.py


     This will create corpus .For example I created 2011-08small.txt

- Move this created corpus to Data directory .

___

## Trainining Model :

- Train model with 



___

## Testing Model :




___

## Acknowledgements :

- [Pytorch-Tutorial-NMT](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)
- [Pytorch-Tutorial-Chatbot](https://pytorch.org/tutorials/beginner/chatbot_tutorial.html)
- [Python Tensorflow Chatbot](https://pythonprogramming.net/chatbot-deep-learning-python-tensorflow/)
- [Sentdex Git-REPO](https://github.com/daniel-kukiela/nmt-chatbot)
- [Reddit Data](http://files.pushshift.io/reddit/comments/)
- [Great Coursera-SeqtoSeq Tutorial](https://www.coursera.org/learn/nlp-sequence-models)





___
## License :
MIT License

Copyright (c) 2019 Aryan Chaudhary

[LICENSE](https://github.com/aryanc55/TS3000_TheChatBOT/blob/master/LICENSE)




