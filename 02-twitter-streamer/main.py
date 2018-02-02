import yaml
from lib.twitter_streamer import Twitterator

if __name__ == "__main__":

    try:
        with open("data/credentials.yml", 'r') as stream:
            credentials = yaml.load(stream)

        westwood_bbox = "-118.4653781129,34.0353221283,-118.4084723665,34.0785727593"

        this_twitterator = Twitterator(credentials, westwood_bbox)
        this_twitterator.collect_tweets()

    except FileNotFoundError:
        print("Did you forget to create you credentials.yml file in the data directory?")