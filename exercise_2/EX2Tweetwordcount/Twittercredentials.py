import tweepy

consumer_key = "0IqUcNNGuKaY59epn9E3jhinY";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "zeoSux7U40WJWgEkzw9RNTrmDsGh69MaeEsERbtwtOPUap5cuF";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "711680708222128128-XRUg8vuqnjklE4RnqGXCFyJ6WZnG4Sx";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "Cma3CmKO8CIxTGZ2TBxEcU5AiXN6oAsTvmrR3qmYzTgKw";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



