import time,IPython.core.display,
from IPython.display import Javascript

def tests(*args,num):
    try:
        start_test = time.time()
        for name, value in args: globals()[name]=value
        print("========================== début du test =========================="+'\n')
        
        #------------------------------------------condition(s) que l'on teste
        #---------------------------------------------------------------------
        if num==1:
            pile_emp=[1,2,3]
            empiler(pile_emp,4)
            assert pile_emp==[1,2,3,4],"La pile retournée par la fonction empiler() n'est pas correcte"
        
        elif num==2:
            pile_dep=[1,2,3]
            depiler(pile_dep)
            assert pile_dep==[1,2],"La pile retournée par la fonction dépiler() n'est pas correcte"
        
        elif num==3:
            assert exo1(8)==[3, 6],"La pile retournée par la fonction exo1() n'est pas correcte"
        
        elif num==4:
            L_exo2 = [34, 7, 52, 1, 40]
            assert exo2(L_exo2,"croissant")==[1, 7, 34, 40, 52],"La valeur de la liste retrounée triée par ordre croissant n'est pas correcte"           
            assert exo2(L_exo2,"décroissant")==[52, 40, 34, 7, 1],"La valeur de la liste retrounée triée par ordre décroissant n'est pas correcte"
        #---------------------------------------------------------------------
        #---------------------------------------------------------------------
        stop_test = time.time()
        tps = stop_test -start_test
        print ("Test réussi en ",round(tps,2)," secondes",'\n')
        print("=========================== fin du test ===========================")
        
    except (AssertionError, NameError) as err:
        stop_test = time.time()
        tps = stop_test -start_test
        print(err,"\n")
        print ("Test échoué en ",round(tps,2)," secondes",'\n')
        print("=========================== fin du test ===========================")

def eval_compteur(cpt):
    print("Vous avez quitté",cpt,"fois la page")
    
# Commandes Javascript pour bloquer les accès Ctrl+C/Ctrl+V aux étudiants + compteur de sorties
 
jscode_cmd = """

document.body.addEventListener('keydown', event => {
    if (event.ctrlKey && 'cvxspwuaz'.indexOf(event.key) !== -1) {
            event.preventDefault()}})

jQuery(document).bind("contextmenu", function(e) {
    e.preventDefault();});
	
var cpt=0;

window.addEventListener('blur', (event) => {
    cpt=cpt+1
    alert("Vous n'avez pas le droit de quitter la page")
    IPython.notebook.kernel.execute("cpt = '" + cpt + "'")
    Jupyter.notebook.execute_cells([5]);
    
});
"""
display(IPython.core.display.Javascript(jscode_cmd))
print("Vous pouvez commencer l'épreuve")
display(IPython.core.display.Javascript("Jupyter.notebook.execute_cells([5])"))