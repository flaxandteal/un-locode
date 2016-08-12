#!/usr/bin/env python3

import pandas

def run():
    df = pandas.read_csv('../data/code-list.csv', dtype=str, keep_default_na=False)

    df['SubdivisionFaT'] = df['Subdivision']

    df.to_csv('../data/code-list-sdn.csv', index=False)


if __name__ == '__main__':
    run()
