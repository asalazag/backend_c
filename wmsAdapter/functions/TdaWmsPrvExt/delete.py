from wmsAdapter.functions.TdaWmsPrvExt.read import read_prvext


def delete_prvext(request, db_name):
    try:
        prv = read_prvext(request, db_name=db_name)
        if type(prv) == str:
            return prv
        else:
            if len(list(prv)) == 1:
                prv = prv[0]
                prv.delete(using=db_name)
                return 'Deleted successfully'
            elif len(list(prv)) == 0:
                return 'Prv not found'
            else:
                return 'More than one prv found'
    except Exception as e:
        print(e)
        return str(e.__cause__)