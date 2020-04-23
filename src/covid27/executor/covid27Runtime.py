import sys
import traceback

from covid27.common.constants import Constants

class Runtime:
    def __init__(self, interim_code_path):
    
        self.double_stack = []
        self.bool_stack = []
        self.string_stack = []
        self.list_name_stack = []
        self.double_list_stack = []

        self.double_map = {}
        self.bool_map = {}
        self.string_map = {}
        self.double_list_map = {}
        self.interim_code_path = interim_code_path
        self.f = open(interim_code_path)
        self.interim_code = iter(self.f)

    def get_next_instruction(self, label):
        try:
            line = next(self.interim_code)
            if label == '':
                return line
            else:
                while not line.startswith(label):
                    line = next(self.interim_code)
                return line
        except Exception as e:
            print(str(e))
        return ""

    def checkFloat(self, val):
        try:
            float(val)
            return True
        except:
            return False
            

    def execute(self):
        var_list = []
        double_list = []
        try:
            line = self.get_next_instruction('')
            take_line_flag = True
            while line != '':
                cmd = line.split()[0]
                if cmd == Constants.STORE:
                    var_name = line.split()[1]
                    if var_name in self.double_map:
                        d = self.double_stack.pop()
                        self.double_map[var_name] = d
                        self.double_stack.append(d)
                    elif var_name in self.bool_map:
                        b = self.bool_stack.pop()
                        self.bool_map[var_name] = b
                        self.bool_stack.append(b)
                    elif var_name in self.string_map:
                        s = self.string_stack.pop()
                        self.string_map[var_name] = s
                        self.string_stack.append(s)
                    elif var_name in self.double_list_map:
                        new_double_list = list(self.double_list_stack.pop())
                        self.double_list_map[var_name] = new_double_list
                        self.double_list_stack.append(new_double_list)
                elif cmd == Constants.LOAD:
                    s = line.split()[1]
                    if s in self.double_map:
                        self.double_stack.append(self.double_map[s])
                    elif s in self.bool_map:
                        self.bool_stack.append(self.bool_map[s])
                    elif s in self.string_map:
                        self.string_stack.append(self.string_map[s])
                    elif s in self.double_list_map:
                        self.double_list_stack.append(self.double_list_map[s])
                elif cmd == Constants.EQB:
                    first_val = self.bool_stack.pop()
                    second_val = self.bool_stack.pop()
                    self.bool_stack.append(first_val == second_val)
                elif cmd == Constants.NEQ:
                    first_val = self.double_stack.pop()
                    second_val = self.double_stack.pop()
                    self.bool_stack.append(first_val != second_val)
                elif cmd == Constants.EQ:
                    first_val = self.double_stack.pop()
                    second_val = self.double_stack.pop()
                    self.bool_stack.append(first_val == second_val)
                elif cmd == Constants.NEQB:
                    second_val = self.bool_stack.pop()
                    first_val = self.bool_stack.pop()
                    self.bool_stack.append(first_val != second_val)
                elif cmd == Constants.LT:
                    second_val = self.double_stack.pop()
                    first_val = self.double_stack.pop()
                    self.bool_stack.append(first_val < second_val)
                elif cmd == Constants.LTE:
                    second_val = self.double_stack.pop()
                    first_val = self.double_stack.pop()
                    self.bool_stack.append(first_val <= second_val)
                elif cmd == Constants.GT:
                    second_val = self.double_stack.pop()
                    first_val = self.double_stack.pop()
                    self.bool_stack.append(first_val > second_val)
                elif cmd == Constants.GTE:
                    second_val = self.double_stack.pop()
                    first_val = self.double_stack.pop()
                    self.bool_stack.append(first_val >= second_val)
                elif cmd == Constants.AND:
                    second_val = self.bool_stack.pop()
                    first_val = self.bool_stack.pop()
                    self.bool_stack.append(first_val and second_val)
                elif cmd == Constants.OR:
                    second_val = self.bool_stack.pop()
                    first_val = self.bool_stack.pop()
                    self.bool_stack.append(first_val or second_val)
                elif cmd == Constants.NOT:
                    self.bool_stack.append(not self.bool_stack.pop())
                elif cmd == Constants.DECDOUBLE:
                    var_name = line.split()[1]
                    self.double_map[var_name] = 0.0
                elif cmd == Constants.DECBOOL:
                    self.bool_map[line.split()[1]] = False
                elif cmd == Constants.DECSTRING:
                    self.bool_map[line.split()[1]] = ""
                elif cmd == Constants.ASSIGNDOUBLE:
                    var_name1, val = line.split()[1:]
                    self.double_map[var_name1] = float(val)
                    self.double_stack.append(float(val))
                elif cmd == Constants.ASSIGNBOOL:
                    var_name1, val = line.split()[1:]
                    self.bool_map[var_name1] = val == 'true'
                    self.bool_stack.append(val == 'true')
                elif cmd == Constants.ASSIGNSTRING:
                    var_name1, val = line.split()[1:]
                    self.string_map[var_name1] = val
                    self.string_stack.append(val)
                elif cmd == Constants.DECLIST:
                    var_name1 = line.split()[1]
                    self.double_list_map[var_name1] = double_list
                    self.list_name_stack.append(var_name1)
                    self.double_list_stack.append(double_list)
                elif cmd == Constants.PUSHLIST:
                    val = line.split()[1]
                    list_val = float(val)
                    var_name = self.list_name_stack.pop()
                    cur_list = list(self.double_list_stack.pop())
                    self.list_name_stack.append(var_name)
                    cur_list.append(list_val)
                    self.double_list_map[var_name] = cur_list
                    self.double_list_stack.append(cur_list)
                elif cmd == Constants.ADDLIST:
                    second = list(self.double_list_stack.pop())
                    first = list(self.double_list_stack.pop())
                    min_size = min(len(first), len(second))
                    res = [first[i]+second[i] for i in range(min_size)]
                    if min_size != len(first):
                        res = res + first[min_size:]
                    if min_size != len(second):
                        res = res + second[min_size:]
                    self.double_list_stack.append(res)
                    self.double_list_map[self.list_name_stack[-2]] = res
                elif cmd == Constants.PUSH:
                    s = line.split()[1]
                    if self.checkFloat(s):
                        self.double_stack.append(float(s))
                    else:
                        self.bool_stack.append("true" == s)
                elif cmd == Constants.SUBLIST:
                    second = list(self.double_list_stack.pop())
                    first = list(self.double_list_stack.pop())
                    min_size = min(len(first), len(second))
                    res = [first[i]-second[i] for i in range(min_size)]
                    if min_size != len(first):
                        res = res + first[min_size:]
                    if min_size != len(second):
                        res = res + second[min_size:]
                    self.double_list_stack.append(res)
                    self.list_name_stack.pop()
                    self.double_list_map[self.list_name_stack[-1]] = res
                elif cmd == Constants.DISPLAY:
                    display_content = line.split()[1]
                    if display_content in self.double_map or self.checkFloat(display_content):
                        print(self.double_map[display_content], end='')
                    elif display_content in self.bool_map:
                        print(self.bool_map[display_content], end='')
                    elif display_content in self.double_list_map:
                        print(self.double_list_map[display_content], end='')
                    elif display_content in self.string_map:
                        print(self.string_map[display_content], end='')
                    else:
                        s = ' '.join(line.split()[1:])
                        s = '\n'.join(s.split('\\n'))
                        print(str(s[1:-1]), end='')
                elif cmd == Constants.ADD:
                    self.double_stack.append(self.double_stack.pop() + self.double_stack.pop())
                elif cmd == Constants.SUB:
                    self.double_stack.append(self.double_stack.pop() - self.double_stack.pop())
                elif cmd == Constants.MUL:
                    self.double_stack.append(self.double_stack.pop() * self.double_stack.pop())
                elif cmd == Constants.DIV:
                    x = self.double_stack.pop()
                    y = self.double_stack.pop()
                    if (x != 0.0):
                        self.double_stack.append(y / x)
                    else:
                        print("ERROR:Cannot Divide by zero")
                elif cmd == Constants.MOD:
                    secondValue = self.double_stack.pop()
                    firstValue = self.double_stack.pop()
                    self.double_stack.append(firstValue % secondValue)

                elif cmd == Constants.JIF:
                    if not self.bool_stack.pop():
                        label = line.split()[1]
                        line = self.get_next_instruction(label)
                        if label == Constants.ENDWHILE:
                            line = self.get_next_instruction(label + line.split()[2])
                        take_line_flag = False
                        
                elif cmd == Constants.JMP:
                    variable = line.split()[1]
                    if Constants.WHILE in line:
                        self.f.close()
                        self.f = open(self.interim_code_path)
                        self.interim_code = iter(self.f)
                        line = self.get_next_instruction(Constants.BEGINWHILE + ' ' + line.split()[2])
                        take_line_flag = False
                    elif Constants.ELSE in line:
                        label = line.split()[1]
                        line = self.get_next_instruction(label)
                        take_line_flag = False
                elif cmd == Constants.HALT:
                    sys.exit()
                elif cmd == Constants.EXITWHILE:
                    take_line_flag = True
                elif cmd == Constants.EXITIF:
                    take_line_flag = True
                elif cmd == Constants.ENDELSE:
                    take_line_flag = True
                elif cmd == Constants.BEGINELSE:
                    take_line_flag = True
                elif cmd == Constants.BEGINWHILE:
                    take_line_flag = True
                # TODO: Complete the command structure!
                if take_line_flag:
                    line = self.get_next_instruction('')
        except Exception as e:
            print('Runtime Error:', e)
            traceback.print_exc()
                