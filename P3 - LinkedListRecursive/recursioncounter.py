''' Used to count recursion depths, mainly in Unit Testing phase '''
#pylint: disable=too-few-public-methods
class RecursionCounter:
    ''' instanciate one of these objects at the beginning of EVERY recursive function '''
    recursion_count = 0
    def __init__(self):
        RecursionCounter.recursion_count += 1
