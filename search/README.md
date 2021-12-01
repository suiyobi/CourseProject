# Search Component Docs

## How to Run the standalone app
Navigate to the `search` directory and run:
```
python search.py config.toml android
```

where `config.toml` is the config file that speicfies what analyers/filters to use for creating the inverted index, and `android` is the query.


## How to Run the Search Server
*If not already, create a virtual env, activate it, and install Flask:*
```
python3 -m venv venv
. venv/bin/activate
pip install Flask
```

Run the server like so:
```
python app.py config.toml 
```


## Sample Request

![image](https://user-images.githubusercontent.com/10318596/144204988-82ffa33f-c9e4-45e7-a7be-ea04c9723181.png)
