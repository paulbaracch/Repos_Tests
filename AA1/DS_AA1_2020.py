#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time,IPython.core.display

print("début")
  
# Commandes Javascript pour bloquer les accès Ctrl+C/Ctrl+V aux étudiants + compteur de sorties
 
jscode_cmd = """

document.body.addEventListener('keydown', event => {
    if (event.ctrlKey && 'cvxspwuaz'.indexOf(event.key) !== -1) {
            event.preventDefault()}})

jQuery(document).bind("contextmenu", function(e) {
    e.preventDefault();});
	
var cpt=0;
var markdown_cell = Jupyter.notebook.get_cell(5);

window.addEventListener('blur', (event) => {
    cpt=cpt+1
    alert("Vous n'avez pas le droit de quitter la page")
    markdown_cell.set_text('Vous avez quitté ' + cpt +' fois la page');
    Jupyter.notebook.execute_cells([5]);  
    
});
"""
display(IPython.core.display.Javascript(jscode_cmd))
print("Vous pouvez commencer l'épreuve")
