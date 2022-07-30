backend for the react api

## the program cannot successfully hosting by heroku, because the database of django is using SQLite, which will not save anything under the eph-system.



## update - using aws

because Heroku cannot shoulder the SQLite database, actually there are some aids. for example change to [PostgreSQL Database](https://www.youtube.com/watch?v=5d8AQFF0Ot0&list=LL&index=1), stick with heroku. I tried to think to use a monoDB, but I am not willing to try the old thing. So I choose to use AWS.



king for genius. if you don't watch many cases, only depends on their docs, you cannot walk the first step... (each time you search things in google about AWS, it's all AWS self's docs.) I found this link is [useful](https://www.youtube.com/watch?v=z5XiVh6v4uI&list=PLz7fadzpgueymSne9Ya2mtyab6guwsIb-&index=2&t=791s), it reminds me the days that I coding flask.

although I met a lot problems, for example the basic 127.0.0.1 and the 0.0.0.0 for the server version, I ran it successfully finally.
