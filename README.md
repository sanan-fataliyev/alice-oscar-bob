## Key Exchange and Symmetric encryption imitation project

Imagine Alice and Bob. Alice would like to send a simple message to Bob – “I will meet you at
the central square at 3PM.” We do not have any secure channel to send this information over
and Alice knows that there is an intruder, namely Oscar who would like to intercept her message.
I wrote a small application that imitates message exchange between Alice and Bob
using:
1) key exchange and
2) symmetric encryption

The keyword that Alice decided to use is “victory”. I helped her to deliver this key to Bob
so that he can use it to decrypt the messages coming from Alice.

#### Used tools
- python3 programming language
- Crypto library for python

#### Pre-requirements
- python3 installed

#### Setting up project:
- `git clone https://github.com/sanan-fataliyev/alice-oscar-bob.git`
- `cd alice-oscar-bob`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

#### To run, type:
- `python example.py`


### Logs from example:

=====================================  
Internet:  
`- Alice joined`

=====================================  
Internet:  
`- Oscar joined`  

=====================================  
Internet:  
`- Bob joined`  

=====================================  
Alice:  
`- Sending a message to Bob over Internet`  

=====================================  
Internet:  
`- Sending message...`  
`- sender =   Alice`  
`- to_person =   Bob`  
`- data =   Hi Bob, I want to tell you our meeting place and time`  
`- is_encrypted =   False`  

=====================================  
Oscar:  
`- This message is not for me.`  
`- But I will try to intercept it, cuz i'm a bad man!`  
`- The message is not encrypted`  
`- Text is:   "Hi Bob, I want to tell you our meeting place and time"`  

=====================================  
Bob:  
`- I got new message from Alice!`  
`- The message is not encrypted`  
`- Text is:   "Hi Bob, I want to tell you our meeting place and time"`  

=====================================  
Alice:  
`- I'm trying to share my symmetric key "victory" with Bob`  
`- After we share this key, we'll able to communicate securely even over insecure network`  
`- But this key must be send in secure way that nobody can get it except Bob!`  
`- To achieve this, I'll encrypt it with Bob's RSA public key before sending`  

=====================================  
Internet:  
`- Sending symmetric key...`  
`- sender =   Alice`  
`- to_person =   Bob`  
`- data =   bksvEbk0ytFRXkhMM1/qAva0HwAi204EglZaKCB1DHcx6Q3SLRkRDVRY5W+mssPix/bSe+bl567x7hTG1HMt92zeNyySnAGBIrh/Jdyixr5ArbPDsA4R0t12PL7bQ2ZmmbaDhS8AE79nOyfdJkRWY0aQwWhdKYF0WHxAcowAjAI=  `  
`- is_encrypted =   True`  

=====================================  
Oscar:  
`- I cannot decrypt this RSA encrypted key since I don't own the private key`  

=====================================  
Bob:  
`- Okay, it seems Alice wants to chat with me in more secure way.`  
`- From now, i will use the "victory" to encrypt/decrypt my further messages with Alice`  

=====================================  
Alice:  
`- Sending a message to Bob over Internet`  

=====================================  
Internet:  
`- Sending message...`  
`- sender =   Alice`  
`- to_person =   Bob`  
`- data =   b'QiSfRhNcEQ6G+Prw5Jd49VB9GGWdYVPzufOCwM72hhOIG79O9uiaEVqyV2MXpqeLYx4mEC60YWuurYlcseBwzszNtEPXuNqDPlyO1pc0ebU=  '`  
`- is_encrypted =   True`  

=====================================  
Oscar:  
`- This message is not for me.`  
`- But I will try to intercept it, cuz i'm a bad man!`  
`- The message is encrypted:   b'QiSfRhNcEQ6G+Prw5Jd49VB9GGWdYVPzufOCwM72hhOIG79O9uiaEVqyV2MXpqeLYx4mEC60YWuurYlcseBwzszNtEPXuNqDPlyO1pc0ebU=  '`  
`- But I don't have a key to decrypt it -_-`  

=====================================  
Bob:  
`- I got new message from Alice!`  
`- The message is encrypted:   b'QiSfRhNcEQ6G+Prw5Jd49VB9GGWdYVPzufOCwM72hhOIG79O9uiaEVqyV2MXpqeLYx4mEC60YWuurYlcseBwzszNtEPXuNqDPlyO1pc0ebU=  '`  
`- And I have a key to decrypt it`  
`- Decrypted! Text is:   "I will meet you at the central square at 3PM."`  

=====================================  
Bob:  
`- Sending a message to Alice over Internet`  

=====================================  
Internet:  
`- Sending message...`  
`- sender =   Bob`  
`- to_person =   Alice`  
`- data =   b'VMzBuM49YO51Em/HNDZ9c5OoH2jyRzXqbJfppJOKinD5pFz84Yh6zaOVTYN0blYnKyZ3A+N8s79iU4udld6/r9XGc4oAX6fE+Toft+mubCQ=  '`  
`- is_encrypted =   True`  

=====================================  
Alice:  
`- I got new message from Bob!`  
`- The message is encrypted:   b'VMzBuM49YO51Em/HNDZ9c5OoH2jyRzXqbJfppJOKinD5pFz84Yh6zaOVTYN0blYnKyZ3A+N8s79iU4udld6/r9XGc4oAX6fE+Toft+mubCQ=  '`  
`- And I have a key to decrypt it`  
`- Decrypted! Text is:   "Okay Alice, I got you. I cant wait to see you again!"`  

=====================================  
Oscar:  
`- This message is not for me.`  
`- But I will try to intercept it, cuz i'm a bad man!`  
`- The message is encrypted:   b'VMzBuM49YO51Em/HNDZ9c5OoH2jyRzXqbJfppJOKinD5pFz84Yh6zaOVTYN0blYnKyZ3A+N8s79iU4udld6/r9XGc4oAX6fE+Toft+mubCQ=  '`  
`- But I don't have a key to decrypt it -_-`  



### References
https://gist.github.com/syedrakib/241b68f5aeaefd7ef8e2
https://stackoverflow.com/a/21928790/4791963