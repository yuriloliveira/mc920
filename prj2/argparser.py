from argparse import ArgumentParser

class Parser:
    __parser = ArgumentParser('Filters image applying mask')
    __args = []

    def __init__(self):
        self.__parser.add_argument('--image', '-i',\
            help='path to image which will be filtered',\
            dest='image'
        )
        self.__parser.add_argument('--error-distribution', '-ed',\
            help='error distribution form item (a, b, c, d, e, f)',\
            dest='error_dist'
        )
        self.__parser.add_argument('--sweep-mode', '-sm',\
            help='sweep mode (default or alternate)',\
            dest='sweep_mode'
        )
        self.__parser.add_argument('--out', '-o',\
            help='path to output of filtering (output will be an .png image)',\
            dest='output_path'
        )
        self.__parser.add_argument('--display_mode', '-dm',\
            help="what will be displayed (images (default): source and result image, hist: histogram, off: nothing will be displayed).",\
            dest='display_mode',\
            default='images',\
            choices=['images', 'hist', 'off']
        )
        self.__parser.add_argument('--show-histogram', '-sh',\
            help="if passed, a window showing the histogram of the result image will be displayed",\
            dest='show_histogram',\
            action='store_true'
        )
        self.__args = vars(self.__parser.parse_args())

    def get_arg(self, arg_id):
        return self.__args[arg_id]