import scraper

from flask import Flask, request, render_template, stream_with_context
app = Flask(__name__)

bannedPrefixes = [
    "//",
    "/wiki/Help",
    "/wiki/Wikipedia:",
    "/wiki/File:"
]

bannedLinks = []

@app.route('/')
def index_route():
    return render_template("index.html")

@app.route('/play')
def play_route():
    pathArgument = request.args.get('path')
    numberArgument = request.args.get('number')

    if (pathArgument == None or numberArgument == None or not numberArgument.isdigit()):
        return "A path and a valid number must be given"

    linkNumber = int(numberArgument)

    if(pathArgument == ""):
        return "You need to give a page!"
    if(linkNumber < 1):
        return "You need to give a number larger than 0"

    chooser = scraper.makeChooser(linkNumber)

    return app.response_class(stream_with_context(scraper.scrapeYield(chooser,'https://en.wikipedia.org/wiki/' + pathArgument, bannedLinks, bannedPrefixes)))

if __name__ == "__main__":
    app.run(debug=False)
