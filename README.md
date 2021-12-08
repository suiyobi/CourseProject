# FAANGMULA Job Search Engine

## Project Proposal
The project proposal is under the `docs/` directory, or can be found [here](https://github.com/tonymuu/CourseProject/blob/main/docs/CS410%20Project%20Proposal.pdf)


## How to Run Locally

### Server
To successfully run the server, you will need to have installed the `flask` package, which is a light weight web API framework. You may check out installation guides here https://flask.palletsprojects.com/en/2.0.x/installation/

To run the server, run the following commands from root directory:
```
cd search
python app.py config.toml
```
The server is up and running if you see the following texts:
![image](https://user-images.githubusercontent.com/10318596/144959517-a16078e3-2716-41d3-922d-476c583549d4.png)



### Frontend

We use Node.js to compile, build, and run the frontend app. For quick installation guide for Node.js, go to https://nodejs.org/en/download/ 

Once you have verified successful installation of Node.js (typing `node --version` in the commandline returns current version), simply navigate to the `frontend/` directory:
```
cd frontend
```

Then install all necessary dependencies:
```
npm install
```

Then simply 
```
npm start
```

If all goes well, you should be able to see this UI
![image](https://user-images.githubusercontent.com/10318596/144959958-b3f39bb6-b92b-426b-a725-36cc7843737a.png)



### Crawlers (Optional)
You can use existing crawled data in the repo, or you may also run the crawlers yourself by doing the following steps:
1. Navigating to the `crawler/` directory in this repo using the following command from a commandline
```
cd crawler
```
2. Edit `main.py` with the company you would like to crawl like so:
```
import google
...

if __name__ == "__main__":
    scrape(google)
```
3. Crawled data will be in the parent directory of the crawler. 
4. To build an index on the crawled data using our search engine, combine all crawed description files *in order*, and change its name to `faang-data.dat`, and move it to `search/faang-data/` directory. Also rename the combined urls file to `job_urls.txt` and move it to `search/` directory. 

