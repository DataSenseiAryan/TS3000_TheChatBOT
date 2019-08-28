# TS3000_TheChatBot
Tony Stark 3000 - The Chat Bot Its a very basic level conversational AI.
## Data Preprocessing :
[Downoad Reddit Data From Here](http://files.pushshift.io/reddit/comments/)

### Follow These :
- Put Downloaded data in Data_Preprocessing directory .
- Unzip the .bz2 file  **bzip2 -dk filename.bz2**
    * *Install Bzip2 on Ubuntu
          - sudo apt-get update
          - sudo apt-get install bzip2
          - Useful Links :
               - [Installing Bzip2](https://www.techwalla.com/articles/how-to-install-bzip2-on-ubuntu) 
               - [Unzipping Error](https://superuser.com/questions/480950/how-to-decompress-a-bz2-file)
- Run createDB.py 
   > python3 createDB.py 


     This will create Database from Raw JSON text file which you unzipped earlier.
- Run createCORPUS.py
   > python3 createCORPUS.py


     This will create corpus .For example I created 2011-08small.txt

- Move this created corpus to Data directory .

___

## Trainining Model :

- Start training model using this command :
   >python3 main.py -tr data/2013-09small.txt -l -lr 0.0001 -it 50000 -b 64 -p 500 -s 1000


- To resume training from last where yiu left :
   > python3 main.py -tr data/2013-09small.txt -l save/model/2013-09small/1-1_512/3000_backup_bidir_model.tar -lr 0.0001 -it      50000 -b 64 -p 500 -s 1000

___

## Testing Model :

- To test the model in interactive mode :
   > python3 main.py -te save/model/movie_subtitles/1-1_512/50000_backup_bidir_model.tar -c data/movie_subtitles.txt -i

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




