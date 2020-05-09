import time,IPython.core.display

def exercices(*args,exercice):
     try:
          start_test = time.time()
          for name, value in args: globals()[name]=value
          print("========================== début du test =========================="+'\n')

          #-----------------------------------------condition(s) que l'on teste
          #--------------------------------------------------------------------
          if exercice==1:
               assert arbre==[[50,[1,2,3,4]],[118,[5]],[7,[6, 7, 8]],[72,[]],[3,[]],[8,[]],[9,[9]],[76,[10]],[987,[]],[0,[]],[65,[]]], "La valeur de l'arbre implémenté n'est pas exacte"
          elif exercice==2:
               assert feuille([[50,[1,2,3,4]],[118,[5]],[7,[6, 7, 8]],[72,[]],[3,[]],[8,[]],[9,[9]],[76,[10]],[987,[]],[0,[]],[65,[]]])==[72, 3, 8, 987, 0, 65], "La liste retournée par la fonction feuille() n'est pas exacte"

          #--------------------------------------------------------------------
          #--------------------------------------------------------------------

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