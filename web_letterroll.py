#!/usr/bin/env python


from flask import Flask, request, redirect, url_for, render_template

import letterroll


# config
DEBUG = True
SECRET_KEY = 'development key'
DICTIONARY = 'american-english'


# create app!
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['POST', 'GET'])
def show_form():
    if request.method == 'POST':
        return redirect('/results/' + request.form['q'])

    return render_template('layout.html')


@app.route('/results/<letters>')
def show_results_for_letters(letters):
    # open dictionary
    dictionary = open(DICTIONARY)
    # TODO: don't pass entire dictionary, huge waste o' memory?
    matching_words = letterroll.get_matching_words(letters, dictionary)
    dictionary.close()
    return render_template('show_results.html', letters=letters, matching_words=matching_words)


if __name__ == '__main__':
    app.run()
