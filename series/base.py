#! usr/bin/env python
__author__ = 'dasDachs'
__version__ = '0.1'

"""
A simple CLI programm written in Python that uses the
TvMaze API (http://www.tvmaze.com/api).

This project rests on the shoulders of two great libraries:
    Requests https://github.com/kennethreitz/requests
    Click    https://github.com/pallets/click
"""
import sys

import click
import requests


@click.command()
def main():
    """
    A simple CLI interface to show you the date of the prevoius and
    next air date of a given series and optionaly display some info.

    Data provided by the magic of TVMaze (www.tvmaze.com)
    """
    # Python 2 compatibility
    prompt = 'Name of the series: '
    try:
        name = raw_input(prompt)
    except NameError:
        name = input(prompt)
    # The app takes user input
    # constructs a requests
    # parses the response JSON
    # end prints the values
    series = requests.get(
        'http://api.tvmaze.com/singlesearch/shows?q={}'.format(name)
    )
    assert series.status_code == 200, "Problems with the query or connection."
    # saftey check
    if not series:
        click.echo(
            "Your query returned no results. Refine it or try something else."
        )
        sys.exit()
    # prep the data
    series = series.json()
    prev_episode = "No previous episode. New show?"
    next_episode = "No next episode. Show ended?"
    for elm in series['_links'].keys():
        if elm.endswith('episode'):
            episode = requests.get(series['_links'][elm]['href']).json()
            episode = 'Title: {} | Air date: {} | Season, Episode: {}'.format(
                                      episode['name'], episode['airdate'],
                                      (str(episode['season']) + ", " + str(episode['number']))
            )
            if elm.startswith('next'):
                next_episode = episode
            elif elm.startswith('prev'):
                prev_episode = episode

    # stdout
    click.secho(series['name'] + ' ', fg='blue', nl=False)
    click.echo(
        '| First aired: {} | Duration: {} | Status: {} | Rating: {}'.
        format(series['premiered'], series['runtime'],
               series['status'].lower(), str(series['rating'].get('average'))
        )
    )
    click.secho(series['url'], fg='red')
    click.secho('Next episode: ', fg='blue', nl=False)
    click.echo(next_episode)
    click.secho('Previous episode: ', fg='blue', nl=False)
    click.echo(prev_episode)


if __name__ == '__main__':
    main()
