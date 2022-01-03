# Wikipedia: Getting to Philosophy and Beyond

Webscraping Wikipedia links and hopping to the first unique hyperlink embedded in the content resulting in a WILD adventure through the topics under and over the sky.

#### NOTE: This is a slightly modified version of original 'Getting to Philosophy' Challenge. This version of code does not abide to the rule of 'not clicking the paranthesized hyperlink'
To know more : [https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy) 

Example: 
Twitter -> Microblogging -> Broadcasting -> Distribution (marketing) -> Marketing mix -> Marketing ->...

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium and Rich.

```bash
pip install selenium
pip install rich
```

# Usage
## Run : Hop from a topic endlessly (Monitor the unique pages crawled)

```python
> python wiki-digger.py
[10:47:03] 1. Hop from a topic endlessly                                                                                                                                                                   wiki-digger.py:13
           2. Find out number of hops to reach 'Philosophy'
           Your choice(1 / 2):
            1
Enter KEYWORD:google
```
## Run : Find out # of hops to reach 'Philosophy'

```python
> python wiki-digger.py
[10:47:03] 1. Hop from a topic endlessly                                                                                                                                                                   wiki-digger.py:13
           2. Find out number of hops to reach 'Philosophy'
           Your choice(1 / 2):
            2
Enter KEYWORD:google
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)