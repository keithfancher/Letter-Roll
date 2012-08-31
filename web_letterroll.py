#!/usr/bin/env python


from flask import Flask, redirect, render_template, request, url_for

import letterroll


# config
DEBUG = True
SECRET_KEY = 'development key'
DICTIONARY = 'american-english'


# create app!
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/results/') # empty results just points to index
def index():
    if request.method == 'POST' and request.form['q']:
        return redirect(url_for('show_results', letters=request.form['q']))

    return render_template('layout.html')


@app.route('/results/<letters>')
def show_results(letters):
    dictionary = open(DICTIONARY)
    matching_words = letterroll.get_matching_words(letters, dictionary)
    dictionary.close()
    return render_template('show_results.html', letters=letters,
                           matching_words=matching_words)


if __name__ == '__main__':
    app.run(host='0.0.0.0') # listen on public IPs
