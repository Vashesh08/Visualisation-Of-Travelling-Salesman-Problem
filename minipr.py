from tkinter import *
import time
import threading

def wait_func(timer=1):
    time.sleep(timer)

def run(list2=['A','B','C', 'D','E'], dist=[[0, 74, 4109, 3047, 2266],[74, 0, 4069, 2999, 2213],[4109, 4069, 0, 1172, 1972], [3047, 2999, 1172, 0, 816],[2266, 2213, 1972, 816, 0]],cities=[0,1,2,3,4,5,6]):
    root = Tk()
    length = len(list2)
    for i in range(length-1, 6):
        list2.append(None)

    myCanvas = Canvas(root,height=500,width=500)
    myCanvas.pack()    

    def draw():
        list_of_nodes = []
        matrix = dist
        list_of_nodes.append(myCanvas.create_oval(225,100,275,150)) # A
        wait_func()
        myCanvas.create_text((225+275)/2,(100+150)/2,text=list2[0])
        wait_func()

        matrix[0][1] = myCanvas.create_line(140 ,175, 225, 125) # AB
        wait_func()
        list_of_nodes.append(myCanvas.create_oval(120,175,170,225)) # B
        wait_func()
        myCanvas.create_text((120+170)/2,(175+225)/2,text=list2[1])
        wait_func()
        
        matrix[1][2] = myCanvas.create_line(140 ,225, 140, 300) # BC
        wait_func()
        list_of_nodes.append(myCanvas.create_oval(120,300,170,350)) # C
        wait_func()
        myCanvas.create_text((120+170)/2,(300+350)/2,text=list2[2])
        wait_func()
        matrix[0][2] = myCanvas.create_line(250 ,150,170 ,325) # AC 
        wait_func()
        
        if list2[3] != None:
            matrix[2][3] = myCanvas.create_line(145 ,350,225, 400) # CD
            wait_func()
            list_of_nodes.append(myCanvas.create_oval(225,375,275,425)) # D
            wait_func()
            myCanvas.create_text((225+275)/2,(375+425)/2,text=list2[3])
            wait_func()
            matrix[0][3] = myCanvas.create_line(250 ,150, 250, 375) # AD
            wait_func()
            matrix[1][3] = myCanvas.create_line(170 ,200,250, 375) # BD
            wait_func()

            if list2[4] != None:
                matrix[3][4] = myCanvas.create_line( 250, 375,330, 200) # DE
                wait_func()
                list_of_nodes.append(myCanvas.create_oval(330,175,380,225)) # E
                wait_func()
                myCanvas.create_text((330+380)/2,(175+225)/2,text=list2[4])
                wait_func()
                matrix[0][4] = myCanvas.create_line(275,125,355,175) # AE
                wait_func()
                matrix[1][4] = myCanvas.create_line(170 ,200, 330, 200) # BE
                wait_func()
                matrix[2][4] = myCanvas.create_line(170 ,325,330, 200) # CE
                wait_func()

                if list2[5] != None:
                    matrix[4][5] = myCanvas.create_line(355,225,355,300, tags="Hey") # EF
                    wait_func()
                    list_of_nodes.append(myCanvas.create_oval(330,300,380,350)) # F
                    wait_func()
                    myCanvas.create_text((330+380)/2,(300+350)/2,text=list2[5])
                    wait_func()
                    matrix[0][5] =myCanvas.create_line(250 ,150, 330, 325) # AF
                    wait_func()
                    matrix[1][5] = myCanvas.create_line(170 ,200,330, 325) # BF 
                    wait_func()
                    matrix[2][5] = myCanvas.create_line(170 ,325, 330, 325) # CF
                    wait_func()
                    matrix[3][5] = myCanvas.create_line(275, 400,355, 350) # DF
                    wait_func()
        # o1.config(fill="blue")
            # myCanvas.create_text(375,250,text="Hey") # EF

        def path_len(path):
            return sum(dist[i][j] for i, j in zip(path, path[1:]))

        to_visit = set(range(len(dist)))

        state = {(i, frozenset([0, i])): [0, i] for i in range(1, len(dist[0]))}

        for _ in range(len(dist) - 2):
            next_state = {}
            for position, path in state.items():
                current_node, visited = position

                for node in to_visit - visited:
                    new_path = path + [node]
                    new_pos = (node, frozenset(new_path))

                    if new_pos not in next_state or path_len(new_path) < path_len(next_state[new_pos]):
                        next_state[new_pos] = new_path

            state = next_state

        shortest = min((path + [0] for path in state.values()), key=path_len)
        # y = 'path: {0}, length: {1}'.format(shortest, path_len(shortest))
        y = "Path: "
        ans = myCanvas.create_text(250, 450,text=y) 
        prev = shortest[0]
        for k in shortest:
            myCanvas.itemconfig(matrix[prev][k],fill="blue", width=2)
            myCanvas.itemconfig(matrix[k][prev],fill="blue", width=2)
            wait_func(2)
            myCanvas.itemconfig(list_of_nodes[k], fill='orange')
            wait_func(1)
            y += str(list2[k])
            prev = k
            myCanvas.itemconfig(ans, text=y)
            wait_func(1)
            y += "-->"
        y = y.rstrip("-->")
        myCanvas.itemconfig(ans, text=y)
        length_of_shortest_path = "Minimum Distance: " + str(path_len(shortest))
        myCanvas.create_text(250,480,text=length_of_shortest_path)

    root.after(1000,threading.Thread(target=draw).start())
    root.mainloop()

if __name__ == '__main__':
    run()
