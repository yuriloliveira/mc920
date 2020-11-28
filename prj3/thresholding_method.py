import thresholding_implementations
from inspect import signature, _empty

class ThresholdingMethod:
    METHODS = {
        'global': thresholding_implementations.thres_global,
        'bernsen': thresholding_implementations.thres_bernsen,
        'niblack': thresholding_implementations.thres_niblack,
        'sauvola': thresholding_implementations.thres_sauvola_pietaksinen,
        'phansalskar': thresholding_implementations.thres_phansalskar,
        'contrast': thresholding_implementations.thres_contrast,
        'mean': thresholding_implementations.thres_mean,
        'median': thresholding_implementations.thres_median
    }

    def __init__(self, method_id):
        self.__method_fn = ThresholdingMethod.get_method_fn(method_id)

    @staticmethod
    def get_method_fn(method_id):
        return ThresholdingMethod.METHODS[method_id]

    def exec(self, img, config=None):
        call_args = build_args_dict(self.__method_fn, config)
        return self.__method_fn(img, **call_args)

def build_args_dict(fn, _config):
    config = _config if _config is not None else ThresholdingConfig()
    args_dict = {}
    for _, arg in signature(fn).parameters.items():
        if (arg.default == _empty):
            continue
        config_val = getattr(config, arg.name)
        args_dict[arg.name] = arg.default if config_val is None else config_val
    return args_dict

class ThresholdingConfig:
    def __init__(self, T=None, n=None, k=None, R=None, p=None, q=None):
        self.T = T
        self.n = n
        self.k = k
        self.R = R
        self.p = p
        self.q = q