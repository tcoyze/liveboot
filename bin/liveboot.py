# -*- coding: utf-8 -*-

import click
import requests
from tqdm import tqdm


@click.command()
@click.argument('url', type=str)
@click.argument('out', type=click.File('wb'))
@click.option('-c', '--chunk', type=int, default=1024, help='Chunk size (bytes) to write to file.')
def cli(url, out, chunk):
    if not url:
	click.echo('You must specify a url. See --help for more information.')
	return	

    if not out:
	click.echo('You must specify an output file path. See --help for more information.')
	return

    response = requests.get(url, stream=True)
    content_length = response.headers.get('content-length', None)
    
    num_bytes = None

    if content_length:
	num_bytes = int(content_length)/chunk    

    for part in tqdm(response.iter_content(chunk_size=chunk), total=num_bytes):
        if part:
	    out.write(part)
