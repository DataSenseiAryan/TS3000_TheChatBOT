# TS3000_TheChatBot
Tony Stark 3000 - The Chat Bot Its a very basic level conversational AI.
## Data Preprocessing :
[Downoad Reddit Data From Here](http://files.pushshift.io/reddit/comments/)

### Follow These :
- Put Downloaded data in Data_Preprocessing directory .
- Unzip the .bz2 file  ** bzip2 -dk filename.bz2 **
    * * Install Bzip2 on Ubuntu * *
          - sudo apt-get update
          - sudo apt-get install bzip2
          - Useful Links :
              -[Installing Bzip2](https://www.techwalla.com/articles/how-to-install-bzip2-on-ubuntu)
              -[Unzipping Error](https://superuser.com/questions/480950/how-to-decompress-a-bz2-file)
- Run createDB.py 
> python3 createDB.py 
Quote break.
This will create Database from Raw JSON text file which you unzipped earlier.

