# WikiLinkCountGame
A game service inspired by a [DougDoug stream](https://www.youtube.com/watch?v=u55MKYCoY2M) and [Wiki-Link Game](https://en.wikipedia.org/wiki/Wikipedia:Wiki-Link_Game), The goal of the game is go through the largest amount of Wikipedia pages by always taking the X.th link within the text, Where x is an integer from 1 to "*how risky you wanna go*". The game stops upon meeting a page twice or entering a page that does not have a X.th link. 

The service simply goes through wikipedia under the condition of the game and counts the pages meet.

To give Wikipedia space for more *serius usage*, the service will wait 1 secound between requests.

## How to run
There are 3 options:
1. Run ```docker-compose up``` to run the service with compose, this will result in the service running at `http://localhost` unless the docker-compose file is changed.
2. Run ```docker build . --tag someName``` then ```docker run -p 80:5000 someName``` to run the service at `http://localhost`
3. Run the service with flask. For more information see the [quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/).