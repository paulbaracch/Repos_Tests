import time,IPython.core.display

def tests(*args,num):
    try:
        start_test = time.time()
        for name, value in args: globals()[name]=value
        print("========================== début du test =========================="+'\n')
        
        #------------------------------------------condition(s) que l'on teste
        #---------------------------------------------------------------------
        if num==1:
            var_A=[[52,[1,2,3]],[21,[4]],[54,[]],[45,[5,6]],[22,[]],[53,[]],[15,[]]]
            assert recherche_pere(var_A, 53)==45, "La valeur retournée du père par la fonction n'est pas correcte"
        
        elif num==2:
            assert arbre==[[45,[1,2]],[21,[3,4]],[54,[5,6]],[7,[]],[28,[-1,7]],[50,[]],[89,[]],[41,[]]], "L'arbre implémenté n'est pas correct"
        
        elif num==3:
            var_arbre=[[45,[1,2]],[21,[3,4]],[54,[5,6]],[7,[]],[28,[-1,7]],[50,[]],[89,[]],[41,[]]]
            assert interne(var_arbre)[0]==[45, 21, 54], "La liste 'val' retournée par la fonction n'est pas correcte"
            
            assert interne(var_arbre)[1]==[0, 1, 2], "La liste 'ind' retournée par la fonction n'est pas correcte"
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