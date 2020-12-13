from argparse import ArgumentParser

class Parser:
    __parser = ArgumentParser('Filters image applying mask')
    __args = []

    def __init__(self):
        self.__parser.add_argument('--mode', '-m',\
            help='Mode to run in (codify or decodify)',
            dest='mode',
            choices=['codify', 'decodify']
        )
        self.__parser.add_argument('--imagein', '-ii',\
            help='Path to the image in',\
            dest='imagein'
        )
        self.__parser.add_argument('--imageout', '-io',\
            help='Path to the image out',
            dest='imageout'
        )
        self.__parser.add_argument('--textin', '-ti',\
            help='Path to the file of the message to be codified',
            dest='textin'
        )
        self.__parser.add_argument('--textout', '-to',\
            help='Path to the file to save the decodified message',
            dest='textout'
        )
        self.__args = vars(self.__parser.parse_args())

    def get_arg(self, arg_id):
        return self.__args[arg_id]