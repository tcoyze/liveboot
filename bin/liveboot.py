# -*- coding: utf-8 -*-

import click
import requests
from tqdm import tqdm


@click.command()
@click.option('-u', '--url', required=True, type=str, help='URL of resource to stream to output file.')
@click.option('-o', '--out', required=True, type=click.File('wb'), help='Output file path for URL resource.')
@click.option('-c', '--chunk', type=int, default=1024, help='Chunk size (bytes) to write to file.')
def cli(url, out, chunk):
    if chunk < 1:
	click.echo('You must specify a chunk size of at least 1. See --help for more information.')
	return

    response = requests.get(url, stream=True)
    content_length = response.headers.get('content-length', None)
    
    if response.status_code not in range(200, 300):
	click.echo('Url returned unsuccessfully with status code %d. Try a different url.' % response.status_code)
	return

    if not content_length:
	click.echo('Url returned no content. Try a different url.')
	return

    num_chunks = (int(content_length)/chunk) + 1

    for part in tqdm(response.iter_content(chunk_size=chunk), total=num_chunks):
        if part:
	    out.write(part)
