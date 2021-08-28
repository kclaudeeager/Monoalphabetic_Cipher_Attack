from GASolver import GeneticSolver
solver = GeneticSolver()
solver.verbose = True
#"Rm nb blfmtvi zmw nliv efomvizyov bvzih nb uzgsvi tzev nv hlnv zwerxv gszg R'ev yvvm gfimrmt levi rm nb nrmw vevi hrmxv. Dsvmvevi blf uvvo orpv xirgrxrarmt zmblmv, sv glow nv, qfhg ivnvnyvi gszg zoo gsv kvlkov rm gsrh dliow szevm'g szw gsv zwezmgztvh gszg blf'ev szw."
ciphertext =input("Enter the cipher text to decrypt:\n") 
if ciphertext=="" or " " or None:
    ciphertext="Rm nb blfmtvi zmw nliv efomvizyov bvzih nb uzgsvi tzev nv hlnv zwerxv gszg R'ev yvvm gfimrmt levi rm nb nrmw vevi hrmxv. Dsvmvevi blf uvvo orpv xirgrxrarmt zmblmv, sv glow nv, qfhg ivnvnyvi gszg zoo gsv kvlkov rm gsrh dliow szevm'g szw gsv zwezmgztvh gszg blf'ev szw."
solver.solve(ciphertext)
#print(plaintext)
