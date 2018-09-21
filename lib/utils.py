class POJO: pass
def as_obj(dc):
    obj = POJO()
    for key, val in dc.items(): setattr(obj, key, val)
    return obj
