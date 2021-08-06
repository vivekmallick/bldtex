import subprocess
import convert

def sys_echo(s) :
    subprocess.run(["echo", s])

def run_latex(tex_profile, latex_cmd="pdflatex",
        switches="--interaction=nonstopmode") :
    file_name = tex_profile.latex_file_name()
    lgfl = tex_profile.iface_log
    with open(lgfl, 'a') as lgfld :
        subprocess.run([latex_cmd, switches, file_name], stdout=lgfld,
                stderr=lgfld)
    if tex_profile.trigger_from_bibtex() :
        tex_profile.unset_trigger_from_bibtex()
    if tex_profile.trigger_from_makeindex() :
        tex_profile.unset_trigger_from_makeindex()
    print("-------- Ran pdflatex.")

def run_bibtex(tex_profile, bibtex_cmd="bibtex") :
    aux_file = tex_profile.aux_file_name()
    tex_profile.set_trigger_from_bibtex()
    lgfl = tex_profile.iface_log
    with open(lgfl, 'a') as lgfld:
        subprocess.run([bibtex_cmd, aux_file], stdout=lgfld, stderr=lgfld)
    print("-------- Ran bibtex.")

def run_makeindex(tex_profile, makeindex_cmd="makeindex") :
    idx_file = tex_profile.idx_file_name()
    tex_profile.set_trigger_from_makeindex()
    lgfl = tex_profile.iface_log
    with open(lgfl, 'a') as lgfld:
        subprocess.run([makeindex_cmd, idx_file], stdout=lgfld, stderr=lgfld)
    print("-------- Ran makeindex.")

