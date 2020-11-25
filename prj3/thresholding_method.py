import thresholding_implementations

class ThresholdingMethod:
    METHODS = {
        'global': thresholding_implementations.thres_global,
        'bernsen': thresholding_implementations.thres_bernsen,
    }

    def __init__(self, method_id):
        self.__method_fn = ThresholdingMethod.get_method_fn(method_id)

    @staticmethod
    def get_method_fn(method_id):
        return ThresholdingMethod.METHODS[method_id]

    def process(self, img):
        return self.__method_fn(img)