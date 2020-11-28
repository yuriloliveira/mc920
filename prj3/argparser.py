from argparse import ArgumentParser

class Parser:
    __parser = ArgumentParser('Filters image applying mask')
    __args = []

    def __init__(self):
        self.__parser.add_argument('--image', '-i',\
            help='path to image which will be processed',\
            dest='image'
        )
        self.__parser.add_argument('--method', '-m',\
            help='thresholding method',\
            dest='method',
            choices=['global', 'bernsen', 'niblack', 'sauvola', 'phansalskar', 'contrast', 'mean', 'median']
        )
        self.__args = vars(self.__parser.parse_args())

    def get_arg(self, arg_id):
        return self.__args[arg_id]