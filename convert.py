# This package assumes tex files are named as ***.tex

def check_tex_end(tex_file) :
    if len(tex_file) < 5 :
        print("The tex file should end with a .tex for this package.")
        ret_val = False
    else :
        if tex_file[-4:] != ".tex" :
            print("The tex file should end with a .tex for this package.")
            ret_val = False
        else :
            ret_val = True
    return ret_val

def aux_file(tex_file) :
    if check_tex_end(tex_file) :
        return (tex_file[:-4] + ".aux")

def log_file(tex_file) :
    if check_tex_end(tex_file) :
        return (tex_file[:-4] + ".log")

def idx_file(tex_file) :
    if check_tex_end(tex_file) :
        return (tex_file[:-4] + ".idx")

