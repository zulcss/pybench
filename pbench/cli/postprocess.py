#!/usr/bin/python

import sys

import click


@click.command()
def main():
    print(sys.argv[0])
