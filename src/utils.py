# utils.py
def class_adj(classfr):
    if classfr == "'0'":
        return 0
    elif classfr == "'1'":
        return 1
    else:
        raise ValueError(f"Unexpected class value: {classfr}")
