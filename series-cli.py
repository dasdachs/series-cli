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
import click
import requests


@click.command()
def main():
    """
    A simple CLI interface to show you the date of the prevoius and
    next air date of a given series and optionaly display some info.

    Data provided by the magic of TVMaze (www.tvmaze.com)
    """
    name = input('Ime serije: ')
    series = requests.get(
        'http://api.tvmaze.com/singlesearch/shows?q={}'.format(name)
    )
    # saftey check
    if not series.status_code == requests.codes.ok or not series:
        click.echo(
            """
            Nekaj ni vredu z iskalnim nizom ali pa ni odziva. Spremeni niz,
            ali gnjavi avtorja programa.
            """
        )
    # prep the data
    series = series.json()
    prev_episode = series['_links'].get('previousepisode')['href']
    next_episode = series['_links'].get('nextepisode')['href']
    if prev_episode:
        prev_episode = requests.get(prev_episode).json()
        prev_episode = 'Title: {} | Air date: {} | Season, Episode: {}'.format(
            prev_episode['name'], prev_episode['airdate'],
            (str(prev_episode['season']) + ", " + str(prev_episode['number']))
        )
    else:
        prev_episode = """
            Ni podatkov o prehodni epizodi. Je to prvi del serije? Ni? Gnjavi
            programerja.
                       """
    if next_episode:
        next_episode = requests.get(next_episode).json()
        next_episode = 'Title: {} | Air date: {} | Season, Episode: {}'.format(
            next_episode['name'], next_episode['airdate'],
            (str(next_episode['season']) + ", " + str(next_episode['number']))
        )
    else:
        next_episode = """
            Ni podatkov o naslednji epizodi. Je to zadnji del serije? Ni? Gnjavi
            programerja.
                       """

    # stdout
    click.secho(series['name'] + ' ', fg='blue', nl=False)
    click.echo(
        '| First aired: {} | Duration: {} | Status: {} | Rating: {}'.
        format(series['premiered'], series['runtime'],
               series['status'].lower(), str(series['rating'].get('average'))
        )
    )
    click.secho(series['url'], fg='red')
    click.secho('Naslednja epizoda: ', fg='blue', nl=False)
    click.echo(next_episode)
    click.secho('Predhonda epizoda: ', fg='blue', nl=False)
    click.echo(prev_episode)


if __name__ == '__main__':
    main()
