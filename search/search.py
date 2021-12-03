""" System imports """
import math
import sys
import time
import metapy
import pytoml


class JobSearch:
    def __init__(self, cfg):
        self.idx = metapy.index.make_inverted_index(cfg)
        self.ranker = self.load_ranker(cfg)

        with open('job_urls.txt') as url_file:
            file_str = url_file.read()
            self.urls = file_str.splitlines()

    def search(self, query_str):
        query = metapy.index.Document()
        query.content(query_str)
        
        results = self.ranker.score(self.idx, query)
        indices = [res[0] for res in results]
        final_urls = [self.urls[i] for i in indices]

        return final_urls

    def load_ranker(self, cfg_file):
        """
        Use this function to return the Ranker object to evaluate, 
        The parameter to this function, cfg_file, is the path to a
        configuration file used to load the index.
        """
        return metapy.index.OkapiBM25()



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} config.toml [some_query]".format(sys.argv[0]))
        sys.exit(1)

    cfg = sys.argv[1]
    query_str = sys.argv[2]

    search = JobSearch(cfg)
    res = search.search(query_str)
    print(res)
