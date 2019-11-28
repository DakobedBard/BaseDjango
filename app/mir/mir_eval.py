'''
This file is intended to have functions that will evaluate the results of the tablature model.


'''

import mir_eval
from tabs.models import MirModel

class MirEval:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
    def evaulate_model(model):
        '''
        This function will evaluate an MIR model, pass in the MirModel object, from which the model will be loaded from S3,
        :param model:
        :return:
        '''

    def generate_results_model(self):
        '''
        This method will create the model.... Or I could just have the results of the model be included within the MirModel.


        :return:
        '''
        pass
