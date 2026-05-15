import matplotlib
import matplotlib.pyplot as plt


def _set_style(use_tex: bool = True) -> None:
    '''LaTeX and plot configuration'''
    if use_tex:
        matplotlib.rcParams['text.usetex'] = True
        matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{lmodern}\usepackage{amsmath}'
    
    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['font.size'] = 8  

    matplotlib.rcParams['axes.grid'] = False           
    matplotlib.rcParams['axes.grid.which'] = 'both'   
    matplotlib.rcParams['grid.alpha'] = 0.3           
    matplotlib.rcParams['grid.linewidth'] = 0.5       
    matplotlib.rcParams['axes.linewidth'] = 0.8       
    
    matplotlib.rcParams['xtick.minor.visible'] = True 
    matplotlib.rcParams['ytick.minor.visible'] = True
    matplotlib.rcParams['xtick.direction'] = 'in'     
    matplotlib.rcParams['ytick.direction'] = 'in'    
    matplotlib.rcParams['lines.linewidth'] = 1.5      
    matplotlib.rcParams["savefig.directory"] = './figures/'