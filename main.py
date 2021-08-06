#!/usr/bin/env python3

import latex_profile
import compilation
import sys

def print_help() :
    help_str = """
        Usage:

            $ bldtex <filename>

        or

            $ bldtexrm <filename>

        bldtex just compiles but keeps all the temporary files. Use bldtexrm
        to clean up at the end of compilation.
    """

def extract_basename(fpath) :
    e = len(fpath)
    found_slash = False
    while (not found_slash) and e > 0 :
        e = e - 1
        if fpath[e] == '/' :
            sp = e
            found_slash = True
    if found_slash :
        basename = fpath[e+1:]
    else :
        basename = fpath
    return basename

bldtex_name="bldtex"
bldtex_version="0.1"

if __name__ == '__main__':
    print("Welcome to", bldtex_name, "( version", bldtex_version, ")!")
    if len(sys.argv) != 2 :
        print("Wrong number of arguments.")
        print_help()
    else :
        called_using = extract_basename(sys.argv[0])
        if called_using == "bldtex" :
            tex_profile = latex_profile.TexProfile(sys.argv[1])
        elif called_using == "bldtexrm" :
            tex_profile = latex_profile.TexProfile(sys.argv[1])
            tex_profile.set_trigger_clean_up()
        else :
            print("Do not know how to process command name:", called_using)
            print("Running as bldtex.")
            tex_profile = latex_profile.TexProfile(sys.argv[1])

        compilation.main_compile_fn(tex_profile)
