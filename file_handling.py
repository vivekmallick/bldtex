import os

def is_string_in_file(s, f) :
    found_s = False
    if os.access(f, os.R_OK) :
        with open(f, "r", encoding='ISO-8859-1') as of :
            for l in of :
                # remove comments
                al = ""
                found_cmnt = False
                for c in l :
                    if c == '%' :
                        found_cmnt = True
                    else :
                        if not found_cmnt :
                            al += c
                    
                if s in al :
                    found_s = True
                    # print("is_string_in_file: ", f, s, found_s)
    else :
        print("file_handling: is_string_in_file: file", f, "cannot be read.")
        found_s = False
    return found_s

def locate_word_end(w, s) :
    locations = []
    l = len(w)
    mt = 0 # mt = matched till
    loc = 0
    for c in s :
        # print(loc, mt)
        if w[mt] == c :
            mt += 1
            if mt == l :
                # print(loc, mt, end=" ")
                locations.append(loc)
                mt = 0
        else : 
            mt = 0
        loc += 1
    return locations

def locate_next_char (st, ch, pos) :
    found_c = False
    j = pos+1
    b_pos=j
    for c in st[pos+1:] :
        if c == ch :
            if not found_c :
                found_c = True
                b_pos = j
            else :
                j = j + 1
        else :
            j = j + 1
    if found_c :
        ret_val = b_pos
    else :
        ret_val = -1
    return ret_val

def extract_name_in_braces(s, pos) :
    a = locate_next_char(s, '{', pos)
    b = locate_next_char(s, '}', a)
    if a == -1 or b == -1 :
        print("file_handling: extract_name_in_braces: cannot find matching",
                "pair of braces")
        ret_val = "ERR_bracket_error"
    else :
        ret_val = s[a+1:b]
        return ret_val

def file_tree(f) :
    c1 = "\\input"
    c2 = "\\include"
    fllst = []
    fllst.append(f)
    found_loop = False
    file_left = True
    ii = 0
    while file_left :
        if not os.access(fllst[ii], os.R_OK) :
            print("file_handling: file_tree: file", fllst[ii],
                    "is not readable. Skipping.")
        else :
            with open(fllst[ii], 'r') as lines :
                for l in lines :
                    found_comment = False
                    s = ""
                    for c in l :
                        if c == '%' :
                            found_comment = True
                        else :
                            if not found_comment :
                                s += c
                    for i in locate_word_end('\\include', s) :
                        fname = extract_name_in_braces(s, i)
                        fname = fname + '.tex'
                        if fname != "ERR_bracket_error" :
                            if fname in fllst :
                                print("file_handling: file_tree: repeated",
                                "filename")
                                file_left = False
                            else :
                                fllst.append(fname)
                    for i in locate_word_end('\\input', s) :
                        fname = extract_name_in_braces(s, i)
                        fname = fname + '.tex'
                        if fname != "ERR_bracket_error" :
                            if fname in fllst :
                                print("file_handling: file_tree: repeated filename")
                                file_left = False
                            else :
                                fllst.append(fname)
        ii += 1
        if ii == len(fllst) :
            file_left = False
    return fllst

def is_str_in_project(st, prfile) :
    files_in_proj = file_tree(prfile)
    ret_val = False
    for f in files_in_proj :
        ret_val = ret_val or is_string_in_file(st, f)
    return ret_val

if __name__ == '__main__' :
    print(locate_word_end('wer', "There were wendy wolf and werewolves."))
    print(locate_word_end('\\cite', "There were \\cite wolf and werewolves."))
    print(locate_word_end('tree', "There were \\cite wolf and werewolves."))

    print(extract_name_in_braces("care? Of course { said me }. Who else?  {..}",  0))
    print(extract_name_in_braces("care? Of course { said me }. Who else?  {..}",  16))

    print(file_tree("test1.tex"))
    print(is_str_in_project("\\indices","test1.tex"))
