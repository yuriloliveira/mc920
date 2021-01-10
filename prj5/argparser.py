from argparse import ArgumentParser

class Parser:
    __parser = ArgumentParser('Filters image applying mask')
    __args = []

    def __init__(self):
        self.__parser.add_argument('--mode', '-m',\
            help='Mode to run in',
            dest='mode',
            choices=[]
        )
        self.__parser.add_argument('--input-image', '-i',\
            help='Path to source image',\
            dest='input-image'
        )
        self.__parser.add_argument('--output-image', '-o',\
            help='Path to which the image will be saved',
            dest='output-image'
        )
        self.__parser.add_argument('--angle', '-a',\
            help='Rotation angle of the output image',
            dest='angle',
            type=float
        )
        self.__parser.add_argument('--scale-factor', '-e',\
            help='Factor to which the image will be scaled',
            dest='scale-factor',
            type=float
        )
        self.__parser.add_argument('--image-dimension', '-d',\
            help='Dimension of the image output image (dxd)',
            dest='image-dimension',
            type=int
        )
        self.__args = vars(self.__parser.parse_args())

    def get_arg(self, arg_id):
        return self.__args[arg_id]