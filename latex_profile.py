import convert
import file_handling

class TexProfile :
    latex_file = ""
    aux_file = ""
    log_file = ""
    idx_file = ""
    included_files = []
    need_bibtex="Auto"
    need_makeindex="Auto"
    trigger_bibtex=False
    trigger_makeindex=False
    trigger_clean_up=False
    iface_log = "lp_log.txt"

    def set_latex_file(tp, tex_file) :
        tp.latex_file = tex_file

    def latex_file_name(tp) :
        return tp.latex_file

    def set_aux_log_idx_file(tp) :
        lfn = tp.latex_file_name()
        if lfn != "" :
            tp.aux_file = convert.aux_file(lfn)
            tp.log_file = convert.log_file(lfn)
            tp.idx_file = convert.idx_file(lfn)
        else :
            print("set_aux_log: LaTeX file not set. Aborting.")

    def aux_file_name(tp) :
        return tp.aux_file

    def log_file_name(tp) :
        return tp.log_file

    def idx_file_name(tp) :
        return tp.idx_file

    def scan_for_files(tp) :
        tp.included_files = file_handling.file_tree(tp.latex_file_name())
        return tp.included_files

    def set_trigger_from_bibtex(tp) :
        tp.trigger_bibtex = True

    def set_trigger_from_makeindex(tp) :
        tp.trigger_makeindex = True

    def unset_trigger_from_bibtex(tp) :
        tp.trigger_bibtex = False

    def unset_trigger_from_makeindex(tp) :
        tp.trigger_makeindex = False

    def set_trigger_clean_up(tp) :
        tp.trigger_clean_up = True

    def unset_trigger_clean_up(tp) :
        tp.trigger_clean_up = False

    def trigger_from_bibtex(tp) :
        return tp.trigger_bibtex

    def trigger_from_makeindex(tp) :
        return tp.trigger_makeindex

    def show_profile(tp) :
        print("Filename:", tp.latex_file_name())
        print("Aux:", tp.aux_file_name(), "Log:", tp.log_file_name())
        print("Bibtex set to:", tp.need_bibtex)
        print("MakeIndex set to:", tp.need_makeindex)
        print("Triggers: bibtex:", tp.trigger_from_bibtex(), ", Makeindex:",
                tp.trigger_makeindex)
        print("Included files: ", tp.included_files)
        print("="*30)

    def __init__(tp, tex_file) :
        tp.set_latex_file(tex_file)
        tp.set_aux_log_idx_file()
        tp.scan_for_files()

    def __str__(tp) :
        s = "Filename: " + tp.latex_file_name() + "\n"
        s += "Aux: " + tp.aux_file_name() + " Log: " + tp.log_file_name() + "\n"
        s += "Bibtex: " + tp.need_bibtex + "  , Makeindex: " + tp.need_makeindex + "."
        return s

    def __repr__(tp) :
        return tp.__str__()

if __name__ == "__main__" :
    eg_tp = TexProfile('test1.tex')
    print(eg_tp)

    eg_tp.show_profile()

    eg_tp.set_trigger_from_bibtex()

    eg_tp.show_profile()
