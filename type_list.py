#l = ['magical unicorns',19,'hello',98.98,'world']
#l = [2,3,1,7,4,12]
l = ['magical','unicorns']
master_sum = 0
master_int = 0
master_str = ''
list_type = None
for val in l:
    if (type(val) == str):
        master_str += " " + val
        if list_type == None:
            list_type ='String'
        elif list_type == 'Integer' or list_type == "Float":
            list_type = 'Mixed'


    elif (type(val) == int):
        master_sum += val
        if list_type == None:
            list_type = 'Integer'
        elif list_type == 'String' or list_type == "Float":
                list_type = 'Mixed'



    elif (type(val) == float):
        master_sum += val
        if list_type == None:
            list_type = 'float'
        elif list_type == 'String' or list_type == "Integer":
                list_type = 'Mixed'


print "The list you entered is of ", list_type, "type."

if list_type == 'Mixed':
    if master_str != "":
        print 'String: ', master_str
        print 'Sum: ', master_sum
elif list_type == 'Integer':
    print 'Sum: ', master_sum
elif list_type == 'Float':
    print 'Sum: ', master_sum
elif list_type == 'String':
    print master_str
