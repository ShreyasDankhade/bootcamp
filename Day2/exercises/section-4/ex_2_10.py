from ex_2_1 import simple_logger
from ex_2_3 import timer
from ex_2_5 import debug_info


@simple_logger
@timer
@debug_info
def sample_function(x, y):
    return x + y

sample_function(5, 3)
