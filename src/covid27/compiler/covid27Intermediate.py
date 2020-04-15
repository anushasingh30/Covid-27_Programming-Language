import sys

from covid27.antlr import covid27Listener, covid27Parser
from covid27.common.constants import Constants

class InterimCodeGenerator(covid27Listener.covid27Listener):

    def __init__(self, filename):
        if InterimCodeGenerator.__instance != None:
            raise Exception('Cannot re-instantiate a singleton class.')
        InterimCodeGenerator.__instance = self
        self.if_block_cnt = 0
        self.while_block_cnt = 0

        self.interim_code = []
        self.var_list = []
        self.if_block_stack = []
        self.real_list = []
        self.bool_list = []
        self.str_list = []
        self.list_list = []
        self.filename = filename

    def __get_all_var_names(self):
        return self.real_list + self.bool_list + self.str_list + self.list_list

    def __add(self, command, var):
        self.interim_code.append(command + ' ' + var + '\n')

    # TODO: Add exit and entry points for the grammar tree