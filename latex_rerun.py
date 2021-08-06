import latex_profile
import file_handling

def need_rerun_log_entry(tex_profile) :
    log_file = tex_profile.log_file_name()
    # rerun_txt = "Rerun to get cross-references right"
    rerun_txt = "Rerun to get cross-references right"
    need_run = file_handling.is_string_in_file(rerun_txt, log_file)
    if need_run :
        print("##### Latex rerun induced from log file")
    return need_run

def need_rerun(tex_profile) :
    needed = need_rerun_log_entry(tex_profile)
    needed = needed or tex_profile.trigger_from_bibtex()
    needed = needed or tex_profile.trigger_from_makeindex()
    if tex_profile.trigger_from_bibtex() :
        print("##### Latex rerun induced by bibtex")
    if tex_profile.trigger_from_makeindex() :
        print("##### Latex rerun induced by makeindex")
    return needed
