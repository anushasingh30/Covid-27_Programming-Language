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

    # Exit a parse tree produced by covid27Parser#program.
    def exitProgram(self, ctx):
        from pprint import pprint
        pprint(self.interim_code)
        with open(self.filename, 'w+') as f:
            f.write(''.join(self.interim_code))

    # Enter a parse tree produced by covid27Parser#idDeclaration.
    def enterIdDeclaration(self, ctx):
        typename = ctx.typename.getText()
        variable_name = ctx.varname.getText()
        if typename == 'real' and variable_name not in self.__get_all_var_names():
            self.__add(Constants.DECDOUBLE, variable_name)
            self.real_list.append(variable_name)
        elif typename == 'string' and variable_name not in self.__get_all_var_names():
            self.__add(Constants.DECSTRING, variable_name)
            self.str_list.append(variable_name)
        elif typename == 'bool' and variable_name not in self.__get_all_var_names():
            self.__add(Constants.DECBOOL, variable_name)
            self.bool_list.append(variable_name)
        else: 
            print('Error: Compile time Error..! You know the variable:', variable_name, 'is already present!')
            sys.exit()

    # Enter a parse tree produced by covid27Parser#listIdDeclaration.
    def enterListIdDeclaration(self, ctx):
        listElementList = ctx.listElementList.getText()
        variable_name = ctx.varname.getText()
        if variable_name not in self.__get_all_var_names():
            self.__add(Constants.DECLIST, variable_name)
            self.list_list.append(variable_name)
            elements = []
            for element in listElementList.split(','):
                try:
                    float(element)
                except:
                    print('Error: Compile time Error..! List', variable_name, ' contains non numerical value')
                    sys.exit()
                self.__add(Constants.PUSHLIST, element)
            self.__add(Constants.STORE, variable_name)
        else:
            print('Error: Compile time Error..! You know the variable:', variable_name, 'is already present!')
            sys.exit()

    # Exit a parse tree produced by covid27Parser#idDeclarationAssign.
    def exitIdDeclarationAssign(self, ctx):
        variable_name = ctx.varname.getText()
        typename = ctx.typename.getText()
        element_name = ctx.elemName.getText()

        if typename == 'real':
            try:
                float(element_name)
            except Exception as e:
                print('Error: Compile time Error', str(e))
                sys.exit()
            self.__add(Constants.ASSIGNDOUBLE, variable_name + ' ' + element_name)
            self.__add(Constants.STORE, variable_name)
            self.real_list.append(variable_name)
        elif typename == 'bool':
            if element_name not in ['true', 'false']:
                print('Error: Compile time Error boolean variable', variable_name, 'not assigned any value.')
                sys.exit()
            self.__add(Constants.ASSIGNBOOL, variable_name + ' ' + element_name)
            self.__add(Constants.STORE, variable_name)
            self.bool_list.append(variable_name)
        elif typename == 'string':
            if element_name[0] != '"' and element_name[len(element_name)-1] != '"':
                print('Error: Compile time Error string variable', variable_name, ' is not a valid string.')
                sys.exit()
            self.__add(Constants.ASSIGNSTRING, variable_name + ' ' + element_name)
            self.__add(Constants.STORE, variable_name)
            self.str_list.append(variable_name)
        else:
            print('Error: Compile time Error variable', variable_name, ' is not defined.')
            sys.exit()

    # Exit a parse tree produced by covid27Parser#identifierExpr.
    def exitIdExpressionDeclaration(self, ctx):
        variable_name = ctx.varname.getText()
        typename = ctx.typename.getText()
        if typename == 'real':
            if variable_name not in self.__get_all_var_names():
                self.__add(Constants.DECDOUBLE, variable_name)
                self.__add(Constants.STORE, variable_name)
                self.real_list.append(variable_name)
            else:
                print('Error: Compile time Error..! You know the variable:', variable_name, 'is already present!')
                sys.exit()
        else:
            print('Error: Compile time Error..! Variable:', variable_name, 'must be of type real!')
            sys.exit()

    # Exit a parse tree produced by covid27Parser#stdIfStatement.
    def exitStdIfStatement(self, ctx):
        self.__add(Constants.EXITIF, '')

    # Exit a parse tree produced by covid27Parser#condition.
    def exitCondition(self, ctx):
        if 'else' in ctx.parentCtx.getText():
            self.__add(Constants.JIF, Constants.BEGINELSE)
        else:
            self.__add(Constants.JIF, Constants.EXITIF)

    def enterElseStatement(self, ctx):
        self.__add(Constants.BEGINELSE, '')

    # Exit a parse tree produced by covid27Parser#elseStatement.
    def exitElseStatement(self, ctx):
        self.__add(Constants.ENDELSE, '')

    # Enter a parse tree produced by covid27Parser#curlyBraceClose.
    def enterCurlyBraceClose(self, ctx):
        self.__add(Constants.JMP, Constants.ENDELSE)