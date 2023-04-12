number_of_scrambles = 5

import random

class GetOutOfLoop( Exception ):
    pass

class Move:
    direction = True # true = clockwise, false = counterclockwise
    piece = 'n'
    cycle_nums = []
    
    def __init__(self, direction_, piece_, cycle_nums_):
        self.direction = direction_
        self.piece = piece_
        self.cycle_nums = cycle_nums_
    
    def turn(self):
        if (self.piece == 'center'):
            temp = cubestate[self.cycle_nums[2]]
            cubestate[self.cycle_nums[2]] = cubestate[self.cycle_nums[1]]
            cubestate[self.cycle_nums[1]] = cubestate[self.cycle_nums[0]]
            cubestate[self.cycle_nums[0]] = temp
            
            if (self.direction == False):
                temp = cubestate[self.cycle_nums[2]]
                cubestate[self.cycle_nums[2]] = cubestate[self.cycle_nums[1]]
                cubestate[self.cycle_nums[1]] = cubestate[self.cycle_nums[0]]
                cubestate[self.cycle_nums[0]] = temp
                
        else:
            temp = cubestate[self.cycle_nums[2]]
            cubestate[self.cycle_nums[2]] = cubestate[self.cycle_nums[0]]
            cubestate[self.cycle_nums[0]] = cubestate[self.cycle_nums[1]]
            cubestate[self.cycle_nums[1]] = temp

            temp = cubestate[self.cycle_nums[3]]
            cubestate[self.cycle_nums[3]] = cubestate[self.cycle_nums[4]]
            cubestate[self.cycle_nums[4]] = cubestate[self.cycle_nums[5]]
            cubestate[self.cycle_nums[5]] = temp
            
            if (self.direction == False):
                temp = cubestate[self.cycle_nums[2]]
                cubestate[self.cycle_nums[2]] = cubestate[self.cycle_nums[0]]
                cubestate[self.cycle_nums[0]] = cubestate[self.cycle_nums[1]]
                cubestate[self.cycle_nums[1]] = temp
    
                temp = cubestate[self.cycle_nums[3]]
                cubestate[self.cycle_nums[3]] = cubestate[self.cycle_nums[4]]
                cubestate[self.cycle_nums[4]] = cubestate[self.cycle_nums[5]]
                cubestate[self.cycle_nums[5]] = temp
                
cycle_U = [0, 7, 14, 1, 8, 15]
cycle_L = [3, 21, 12, 2, 22, 11]
cycle_R = [10, 24, 19, 9, 23, 18]
cycle_B = [5, 17, 26, 4, 16, 25]

cycle_l = [1, 2, 4]
cycle_f = [8, 9, 11]
cycle_r = [15, 16, 18]
cycle_d = [22, 23, 25]

U = Move(True, 'corner', cycle_U)
L = Move(True, 'corner', cycle_L)
R = Move(True, 'corner', cycle_R)
B = Move(True, 'corner', cycle_B)

Ui = Move(False, 'corner', cycle_U)
Li = Move(False, 'corner', cycle_L)
Ri = Move(False, 'corner', cycle_R)
Bi = Move(False, 'corner', cycle_B)

l = Move(True, 'center', cycle_l)
f = Move(True, 'center', cycle_f)
r = Move(True, 'center', cycle_r)
d = Move(True, 'center', cycle_d)

li = Move(False, 'center', cycle_l)
fi = Move(False, 'center', cycle_f)
ri = Move(False, 'center', cycle_r)
di = Move(False, 'center', cycle_d)

def random_pos():
    c1 = random.randint(0,2)
    c2 = random.randint(0,2)
    c3 = random.randint(0,2)
    c4 = random.randint(0,2)
    
    if (c1 == 0):
        U.turn()
    elif (c1 == 1):
        Ui.turn()
    
    if (c2 == 0):
        L.turn()
    elif (c2 == 1):
        Li.turn()
    
    if (c3 == 0):
        R.turn()
    elif (c3 == 1):
        Ri.turn()
    
    if (c4 == 0):
        B.turn()
    elif (c4 == 1):
        Bi.turn()
    
    center_list = ['r', 'r', 'r', 'g', 'g', 'g', 'b', 'b', 'b', 'y', 'y', 'y']
    bad_indexes = [0, 3, 5, 6, 7, 10, 12, 13, 14, 17, 19, 20, 21, 24, 26, 27]
    
    for i, piece in enumerate(cubestate):
        if i not in bad_indexes and len(center_list) > 0:
            rand_index = random.randint(0, len(center_list) - 1)
            cubestate[i] = center_list.pop(rand_index)
            
def optimal_solver(gen, pieces):
    temp_state = []
    solver_moves = gen
    le = len(solver_moves)
    max_moves = 0
    
    global good_solution
    
    number = 0
    
    try:
        for m1 in range(le):
            for m2 in range(le):
                for m3 in range(le):
                    for m4 in range(le):
                        for m5 in range(le):
                            for m6 in range(le):
                                for m7 in range(le):
                                    for m8 in range(le):
                                        for m9 in range(le):
                                            for m10 in range(le):
                                                for m11 in range(le):
                                                    for m12 in range(le):
                                                        for m13 in range(le):
                                                            for m14 in range(le):
                                                                for m15 in range(le):
                                                                    for m16 in range(le):
                                                                        for m17 in range(le):
                                                                            for m18 in range(le):
                                                                                temp_state = copy_list(cubestate)
                                                                                tryAlg = ""
                                                                                
                                                                                tryAlg = tryAlg + solver_moves[m18]
                                                                                tryAlg = tryAlg + solver_moves[m17]
                                                                                tryAlg = tryAlg + solver_moves[m16]
                                                                                tryAlg = tryAlg + solver_moves[m15]
                                                                                tryAlg = tryAlg + solver_moves[m14]
                                                                                tryAlg = tryAlg + solver_moves[m13]
                                                                                tryAlg = tryAlg + solver_moves[m12]
                                                                                tryAlg = tryAlg + solver_moves[m11]
                                                                                tryAlg = tryAlg + solver_moves[m10]
                                                                                tryAlg = tryAlg + solver_moves[m9]
                                                                                tryAlg = tryAlg + solver_moves[m8]
                                                                                tryAlg = tryAlg + solver_moves[m7]
                                                                                tryAlg = tryAlg + solver_moves[m6]
                                                                                tryAlg = tryAlg + solver_moves[m5]
                                                                                tryAlg = tryAlg + solver_moves[m4]
                                                                                tryAlg = tryAlg + solver_moves[m3]
                                                                                tryAlg = tryAlg + solver_moves[m2]
                                                                                tryAlg = tryAlg + solver_moves[m1]
                                                                                
                                                                                num_coded_moves = len(tryAlg)
                                                                                
                                                                                # translates alg to legible & cancels moves
                                                                                tryAlg = trans_and_cancel(tryAlg)
                                                                                
                                                                                
                                                                                if (tryAlg.count(' ') + 1 >= max_moves):
                                                                                    
                                                                                    if (tryAlg.count(' ') + 1 > max_moves):
                                                                                        max_moves = tryAlg.count(' ') + 1
                                                                                    
                                                                                    if (trya(tryAlg, pieces)):
                                                                                        good_solution = good_solution + tryAlg + " "
                                                                                        raise GetOutOfLoop
                                                                                
        
    except GetOutOfLoop:
        pass

def trans_and_cancel(coded_alg):
    coded_alg = coded_alg.replace("?", "")
    decoded_alg = ""
    
    for i in range(len(coded_alg)):
        coded_alg = coded_alg.replace("UU", "V")
        coded_alg = coded_alg.replace("RR", "S")
        coded_alg = coded_alg.replace("LL", "M")
        coded_alg = coded_alg.replace("BB", "C")
        coded_alg = coded_alg.replace("VV", "U")
        coded_alg = coded_alg.replace("SS", "R")
        coded_alg = coded_alg.replace("MM", "L")
        coded_alg = coded_alg.replace("CC", "B")
        coded_alg = coded_alg.replace("ff", "g")
        coded_alg = coded_alg.replace("ll", "b")
        coded_alg = coded_alg.replace("rr", "s")
        coded_alg = coded_alg.replace("dd", "e")
        coded_alg = coded_alg.replace("gg", "f")
        coded_alg = coded_alg.replace("bb", "l")
        coded_alg = coded_alg.replace("ss", "r")
        coded_alg = coded_alg.replace("ee", "d")        
    
    al = list(coded_alg)
    for mov in al:
        mov = mov.replace("V", "Ui")
        mov = mov.replace("S", "Ri")
        mov = mov.replace("M", "Li")
        mov = mov.replace("C", "Bi")
        mov = mov.replace("g", "fi")
        mov = mov.replace("b", "li")
        mov = mov.replace("s", "ri")
        mov = mov.replace("e", "di")
        
        decoded_alg = decoded_alg + mov + " "
    
    decoded_alg = decoded_alg[:-1]
    
    return decoded_alg

def solver():
    # corners
    trya("U", [0, 6])
    trya("Ui", [0, 6])
    trya("L", [3, 6])
    trya("Li", [3, 6])
    trya("R", [10, 13])
    trya("Ri", [10, 13])
    trya("B", [5, 6])
    trya("Bi", [5, 6])
    
    solve_centers(1, 2, 4, 6)

def solve_centers(c1, c2, c3, cen):
    while (not same(c1, c2, c3, cen)):
        if (not same(c1, cen)):
            # SWAP CENTER TO ONE OF GOOD ADJACENT FACE
            ooo = 0
               

def same(pieces):
    if (len(set(cubestate_values(pieces))) == 1):
        return True
    else:
        return False

def trya(algorithm, pieces):
    global cubestate
    global solution
    
    temp_state = []
    temp_state = copy_list(cubestate)
    alg(algorithm)
    
    if (pieces != "all"):
        if (len(set(cubestate_values(pieces))) == 1):
            #solution = solution + algorithm + " "
            return True
        
        else:
            cubestate = copy_list(temp_state)
            return False
        
    else:
        if (solved()):
            cubestate = copy_list(temp_state)
            return True
        else:
            cubestate = copy_list(temp_state)
            return False

def cubestate_values(i_list):
    color_list = []
    for index in i_list:
        color_list.append(cubestate[index])
    return color_list

def copy_list(lis):
    new_list = []
    for i, item in enumerate(lis):
        new_list.append(item)
    
    return new_list

def solved():
    if (len(set(cubestate[0:7])) == 1) and (len(set(cubestate[7:14])) == 1):
        if (len(set(cubestate[14:21])) == 1):
            return True
        else:
            return False
    else:
        return False
    
            
                
def alg(a):
    a = a.replace("'", 'i')
    a = a.split()
    for m in a:
        if (m == "U"):
            U.turn()
        elif (m == "Ui"):
            Ui.turn()
        elif (m == "L"):
            L.turn()
        elif (m == "Li"):
            Li.turn()
        elif (m == "R"):
            R.turn()
        elif (m == "Ri"):
            Ri.turn()
        elif (m == "B"):
            B.turn()
        elif (m == "Bi"):
            Bi.turn()
        elif (m == "l"):
            l.turn()
        elif (m == "li"):
            li.turn()
        elif (m == "f"):
            f.turn()
        elif (m == "fi"):
            fi.turn()
        elif (m == "r"):
            r.turn()
        elif (m == "ri"):
            ri.turn()
        elif (m == "d"):
            d.turn()
        elif (m == "di"):
            di.turn()

# set up cube state

def reset_state():
    #cubestate.clear()
    for i in range(7):
        cubestate.append('r')
    for i in range(7):
        cubestate.append('g')
    for i in range(7):
        cubestate.append('b')
    for i in range(7):
        cubestate.append('y')
        
def inverse_solution(sol):
    sol_list = sol.split()
    sol_list.reverse()
    inv_str = ""
    
    for mo in sol_list:
        if mo.endswith("i"):
            inv_str = inv_str + mo[:-1] + " "
        else:
            inv_str = inv_str + mo + "i" + " "
            
    inv_str = inv_str[:-1]
    return inv_str

def cancel_turns(al):
    al = al.replace("Ui Ui ", "U ")
    al = al.replace("U U ", "Ui ")
    al = al.replace("U Ui ", "")
    al = al.replace("Ui U ", "")
    al = al.replace("Ri Ri ", "R ")
    al = al.replace("R R ", "Ri ")
    al = al.replace("R Ri ", "")
    al = al.replace("Ri R ", "")
    al = al.replace("Li Li ", "L ")
    al = al.replace("L L ", "Li ")
    al = al.replace("L Li ", "")
    al = al.replace("Li L ", "")
    al = al.replace("Bi Bi ", "B ")
    al = al.replace("B B ", "Bi ")
    al = al.replace("Bi B ", "")
    al = al.replace("B Bi ", "")
    al = al.replace("fi fi ", "f ")
    al = al.replace("f f ", "fi ")
    al = al.replace("f fi ", "")
    al = al.replace("fi f ", "")
    al = al.replace("li li ", "l ")
    al = al.replace("l l ", "li ")
    al = al.replace("li l ", "")
    al = al.replace("li l ", "")
    al = al.replace("ri ri ", "r ")
    al = al.replace("r r ", "ri ")
    al = al.replace("r ri ", "")
    al = al.replace("ri r ", "")
    al = al.replace("di di ", "d ")
    al = al.replace("d d ", "di ")
    al = al.replace("di d ", "")
    al = al.replace("d di ", "")
    al = al.replace("L U Li ", "U ")
    al = al.replace("L U L ", "Li U ")
    al = al.replace("L Ui L ", "Li U ")
    al = al.replace("L Ui Li ", "Ui ")
    al = al.replace("Li U L ", "U ")
    al = al.replace("Li U Li ", "L U ")
    al = al.replace("Li Ui L ", "Ui ")
    al = al.replace("Li Ui Li ", "L Ui ")
    al = al.replace("R U Ri ", "U ")
    al = al.replace("R U R ", "Ri U ")
    al = al.replace("R Ui R ", "Ri U ")
    al = al.replace("R Ui Ri ", "Ui ")
    al = al.replace("Ri U R ", "U ")
    al = al.replace("Ri U Ri ", "R U ")
    al = al.replace("Ri Ui R ", "Ui ")
    al = al.replace("Ri Ui Ri ", "R Ui ")
    al = al.replace("B U Bi ", "U ")
    al = al.replace("B U B ", "Bi U ")
    al = al.replace("B Ui B ", "Bi U ")
    al = al.replace("B Ui Bi ", "Ui ")
    al = al.replace("Bi U B ", "U ")
    al = al.replace("Bi U Bi ", "B U ")
    al = al.replace("Bi Ui B ", "Ui ")
    al = al.replace("Bi Ui Bi ", "B Ui ")
    al = al.replace("U d Ui ", "d ")
    al = al.replace("U d U ", "Ui d ")
    al = al.replace("U di U ", "Ui d ")
    al = al.replace("U di Ui ", "di ")
    al = al.replace("Ui d U ", "d ")
    al = al.replace("Ui d Ui ", "U d ")
    al = al.replace("Ui di U ", "di ")
    al = al.replace("Ui di Ui ", "U di ")
    
    return al

for nu, inte in enumerate(range(number_of_scrambles)):
    solution = ""
    cubestate = []
    saved_cubestate = []
    good_solution = ""
            
    reset_state()

    random_pos()

    optimal_solver(['?', 'U', 'R', 'L', 'B', 'V', 'S', 'M', 'C', 'f', 'l', 'r', 'd', 'g', 'b', 's', 'e'], [21, 22, 25, 26, 27]) # 5x1 block
    optimal_solver(['?', 'U', 'R', 'L', 'B', 'V', 'S', 'M', 'C', 'f', 'l', 'r', 'g', 'b', 's'], [21, 22, 23, 24, 25, 26, 27]) # finish 1st layer
    optimal_solver(['?', 'U', 'V', 'f', 'l', 'r', 'g', 'b', 's'], [2, 3, 4, 5, 6]) # left
    optimal_solver(['?', 'U', 'V', 'r', 'f', 's', 'g'], [9, 10, 11, 12, 13]) # front
    optimal_solver(['?', 'U', 'V', 'r', 's'], "all") # right

    good_solution = good_solution[:-1]
    good_solution = inverse_solution(good_solution)
    good_solution = good_solution + " "
    good_solution = cancel_turns(good_solution)
    good_solution = good_solution[:-1]
    good_solution = good_solution.replace("i", "'")

    print(str(nu + 1) + ") " + good_solution)

