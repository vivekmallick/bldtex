import latex_profile
import sys_iface
import os

def list_files_to_remove(tp) :
    # tp is a tex profile
    file_extn = ['.aux',
            '.log',
            '.toc',
            '.bbl',
            '.blg',
            '.ilg',
            '.ind',
            '.idx',
            '.snm'
            ]
    all_tex_files = tp.included_files
    files_to_remove = []
    for t in all_tex_files :
        for e in file_extn :
            pos_file = t[:-4] + e
            if os.path.isfile(pos_file) :
                files_to_remove.append(pos_file)
    return files_to_remove

def clean_up(tp) :
    print("========= Cleaning up.")
    to_rm = list_files_to_remove(tp)
    lgfl = tp.iface_log
    with open(lgfl, 'a') as lgfld :
        for f in to_rm :
            print("Removing", f, file=lgfld)
            os.remove(f)


if __name__ == "__main__" :
    tp = latex_profile.TexProfile('test1.tex')
    print(list_files_to_remove(tp))
    clean_up(tp)
