import traceback

try:
    raise Exception('This is the error messsage')
except:
    with open('error_info.txt', 'w') as error_info:
        error_info.write(traceback.format_exc())
    print('The traceback info was written to error_info.txt')