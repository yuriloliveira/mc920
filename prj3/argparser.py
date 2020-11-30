from argparse import ArgumentParser

class Parser:
    __parser = ArgumentParser('Filters image applying mask')
    __args = []

    def __init__(self):
        self.__parser.add_argument('--image', '-i',\
            help='path to image which will be processed',\
            dest='image'
        )
        self.__parser.add_argument('--out', '-o',\
            help='path to save the processed image',
            dest='out'
        )
        self.__parser.add_argument('--method', '-m',\
            help='thresholding method',\
            dest='method',
            choices=['global', 'bernsen', 'niblack', 'sauvola', 'phansalskar', 'contrast', 'mean', 'median']
        )
        self.__parser.add_argument('-T',\
            help='Threshold param used in global method',
            dest='T',
            required=False,
            type=int
        )
        self.__parser.add_argument('-n',\
            help='Size of the neighborhood',
            dest='n',
            required=False,
            type=int
        )
        self.__parser.add_argument('-k',\
            help='k param used in niblack, sauvola and phansalskar methods',
            dest='k',
            required=False,
            type=float
        )
        self.__parser.add_argument('-R',\
            help='R param used in sauvola and phansalskar methods',
            dest='R',
            required=False,
            type=float
        )
        self.__parser.add_argument('-p',\
            help='p param used in phansalskar methods',
            dest='p',
            required=False,
            type=float
        )
        self.__parser.add_argument('-q',\
            help='q param used in phansalskar methods',
            dest='q',
            required=False,
            type=float
        )
        self.__parser.add_argument('-dm',\
            help='What mode of display should be shown',
            dest='display_mode',
            required=False,
            choices=['default', 'hist', 'off']
        )
        self.__args = vars(self.__parser.parse_args())

    def get_arg(self, arg_id):
        return self.__args[arg_id]