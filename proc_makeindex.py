import latex_profile
import file_handling

def make_index_cmd(tp) :
    rootfile = tp.latex_file_name()
    makeindex_called = file_handling.is_string_in_file("\\makeindex",
            rootfile)
    return makeindex_called

def print_index_cmd(tp) :
    rootfile = tp.latex_file_name()
    printindex_called = file_handling.is_str_in_project("\\printindex",
            rootfile)
    return printindex_called

def index_cmd(tp) :
    rootfile = tp.latex_file_name()
    printindex_called = file_handling.is_str_in_project("\\index",
            rootfile)
    return printindex_called

def need_makeindex(tp) :
    if tp.need_makeindex == "Yes" :
        ret_val = True
    elif tp.need_makeindex == "No" :
        ret_val = False
    else :
        ret_val = False
        ret_val = ret_val or make_index_cmd(tp)
        ret_val = ret_val or print_index_cmd(tp)
        ret_val = ret_val or index_cmd(tp)
    if ret_val :
        print("%%%%%%%%%%%%% Need makeindex")
    return ret_val
