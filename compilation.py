import sys_iface
import convert
import latex_rerun
import latex_profile
import proc_bibtex
import proc_makeindex
import clean_up

def run_latex_till_done(tex_profile, max_count=10) :
    count = 0
    while latex_rerun.need_rerun(tex_profile) and count < max_count :
        sys_iface.run_latex(tex_profile)
        count += 1

def main_compile_fn(tex_profile, max_count=10) :
    sys_iface.run_latex(tex_profile)
    if proc_bibtex.need_bibtex(tex_profile) :
        sys_iface.run_bibtex(tex_profile)
    if proc_makeindex.need_makeindex(tex_profile) :
        sys_iface.run_makeindex(tex_profile)
    run_latex_till_done(tex_profile, max_count)
    if proc_makeindex.need_makeindex(tex_profile) :
        sys_iface.run_makeindex(tex_profile)
        run_latex_till_done(tex_profile, max_count)
    if tex_profile.trigger_clean_up :
        clean_up.clean_up(tex_profile)
