from typing import Text
import click
from richterator import Matrix


@click.command()
@click.option('-cs', '--charset',                   help='Chars to fill blocks. Default is "#"')
@click.option('-m', '--mode',                       help='Fill pattern for blocks. Default is "Block"')
@click.option('-r', '--rows', type=int,             help='Number of rows. Default is 4')
@click.option('-c', '--columns', type=int,          help='Number of columns. Default is 4')
@click.option('-bw', '--block-width', type=int,     help='Width of each block by num of characters. Default is 20')
@click.option('-bh', '--block-height', type=int,    help='Height of each block by num of characters. Default is block-width/2 rounded up')
@click.option('-i', '--iterations', type=int,       help='Number of matrices to print. Default is 1')
def cli(**kwargs):    
    '''
    I pursue no objectives, no systems, no tendency; I have no program, no style, no direction. I have no time for specialized concerns, working themes, or variations that lead to mastery. I steer clear of definitions. I don’t know what I want. I am inconsistent, non-committal, passive; I like the indefinite, the boundless; I like continual uncertainty.
    
    - Gerhard Richter
    '''
    filtered_kwargs = {k:v for k,v in kwargs.items() \
        # remove unpassed options and remove interations
        if v and k != 'iterations'}
        
    m = Matrix(**filtered_kwargs)

    iterations = int(kwargs['iterations']) if kwargs['iterations'] else 1
    for _ in range(iterations):
        print('\n')
        print(m.generate_matrix())
