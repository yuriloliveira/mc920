from argparse import ArgumentParser

class Parser:
    __parser = ArgumentParser('Filters image applying mask')
    __args = []

    def __init__(self):
        self.__parser.add_argument('--image', '-i',\
            help='path to image which will be filtered',\
            dest='image'
        )
        self.__parser.add_argument('--mask', '-m',\
            help='mask to be applied to the image. Available masks are h1..h11',\
            default='h1', dest='mask'
        )
        self.__parser.add_argument('--out', '-o',\
            help='path to output of filtering (output will be an .png image)',\
            dest='output_path'
        )
        self.__parser.add_argument('--outc', '-oc', \
            help='path to output of combined images',\
            dest='output_combined_path'
        )
        self.__parser.add_argument('--hflip', '-hf',\
            help='if passed, flips the resulting image horizontally',\
            dest='hflip',\
            action='store_true'
        )
        self.__parser.add_argument('--skip-image-show', '-ss',\
            help="if passed, a window showing the source image and the filtered won't be open",\
            dest='skip_image_show',\
            action='store_true'
        )
        self.__args = vars(self.__parser.parse_args())

    def get_arg(self, arg_id):
        return self.__args[arg_id]