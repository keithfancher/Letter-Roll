from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

import letterroll


# config
DEBUG = True
SECRET_KEY = 'development key'


# create app!
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True) # override!


@app.route('/<letters>')
def show_results_for_letters(letters):
    # open dictionary
    dictionary = open('american-english')
    matching_words = letterroll.get_matching_words(letters, dictionary)
    return render_template('show_results.html', letters=letters, matching_words=matching_words)


if __name__ == '__main__':
    app.run()
