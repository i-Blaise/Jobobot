import tweepy

access_token = '1793711715835666432-xNWv8Aq7iKV6xgLN2xyZdl18hf5nLK'
access_token_secret = '4sXlZzeN5kxAiXDOTqPEHaafsXPHFXONUjwLosQ6ZZ3oY'
api_key = 'tYfNUd6kU2RcZj8m60lCG731D'
api_key_secret = 'pTk92Ze6XyzkjohUGtYa915hS2QE6qfM9aCKfRn96RlJGLPHRe'
bearer_token = "AAAAAAAAAAAAAAAAAAAAACUXwAEAAAAAA4afc9YZfh8jBYvFJ%2Fu3yuDFZdo%3DHUtWlFfpA0ZcQCqjEvaoVXy2GJccC5HDqQIexbYgEgNHc7B009" 
client_id = 'NUh4U1k4ZDd5SFVjVXFZU3Rjb0s6MTpjaQ'
client_secret = 'hFSS8dSCesfv2xG4FAoKch6HRkjABeuhN-SUPkn0z3avt0ZZK_'

# auth = tweepy.OAUTHHandler(client_id, client_secret)
# auth.set_access_token(access_taken, access_token_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(
    bearer_token = bearer_token,
    consumer_key = client_id, 
    consumer_secret = client_secret, 
    access_token = access_token, 
    access_token_secret = access_token_secret,
    wait_on_rate_limit=True
)

# response = client.create_tweet(
#     text='hello world!'
# )

text = 'Hello World'

client.create_tweet(text=text)
print('tweeted')