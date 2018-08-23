def info_required(fn):
    def inner(arg):
        if arg.title == None or arg.text == None:
            print ('Title and Text are required for a snippet')
            return
        return fn
    return inner