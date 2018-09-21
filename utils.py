class POJO: pass
def as_obj(dc):
    obj = POJO()
    for key, val in dc.items(): setattr(obj, key, val)
    return obj


__CONFIG = {
   "DESCRIPTION":'Small utility to retrieve tweets as JSON from twitter api.'
}

config = as_obj(__CONFIG)
