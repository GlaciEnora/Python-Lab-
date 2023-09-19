def rev(arg):
    if len(arg) == 0:
        return ()
    else:
        return (arg[-1],) + rev(arg[:-1])