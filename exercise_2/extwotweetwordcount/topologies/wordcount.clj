(ns tweetcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetcount [options]
   [
    ;; spout configuration
    {"tweet-spout" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          :p 3
          )
    }
    ;; bolt configuration
    {"parse-bolt" (python-bolt-spec
          options
          {"tweet-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["word"]
          :p 3
          )
     "count-bolt" (python-bolt-spec
         options
         {"parse-bolt" :shuffle}
         "bolts.wordcount.WordCounter"
         ["word" "count"]
         :p 2
         )
    }
  ]
)
