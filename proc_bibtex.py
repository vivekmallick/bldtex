import latex_profile
import file_handling

def bibliography_cmd(tex_profile) :
    main_file = tex_profile.latex_file_name()
    looking_for = "\\bibliography{"
    fnd_bib = file_handling.is_string_in_file(looking_for, main_file)
    return fnd_bib

def cite_no_cite_call(tex_profile) :
    main_file = tex_profile.latex_file_name()
    cite_used = file_handling.is_str_in_project('\\cite', main_file)
    nocite_used = file_handling.is_str_in_project('\\nocite', main_file) 
    return cite_used or nocite_used

def need_bibtex(tex_profile) :
    if tex_profile.need_bibtex == "Yes" :
        ret_val = True
    elif tex_profile.need_bibtex == "No" :
        ret_val = False
    else :
        ret_val = False
        ret_val = ret_val or bibliography_cmd(tex_profile)
        ret_val = ret_val or cite_no_cite_call(tex_profile)
    if ret_val :
        print("*************  Bibtex needed")
    return ret_val

