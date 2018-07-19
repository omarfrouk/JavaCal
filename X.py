Em='====='
x='--X--'
o='--O--' 
mat=[[Em,Em,Em],[Em,Em,Em],[Em,Em,Em]]

class Prints():
    
    def print_Board():
        print() 
        print('    a     b     c  ')
        for xx in range(0,3):
            print(xx+1,end=' ')
            for yy in range(0,3):
                print(mat[xx][yy],end=" ")
            print() 
        print()

class Game():
    def Move(i,j,T):
            mat[i][j]=T
    def WIN(T):
        Win=False
        x='--X--'
        o='--O--' 
        if T==x:
            PosstT=o 
        else:
            PosstT=x
        for x in range(0,3):
            if mat[x][0]==PosstT and mat[x][1]==PosstT and mat[x][2]==PosstT:#Horizontal
                Win=True
                break
            elif mat[0][x]==PosstT and mat[1][x]==PosstT and mat[2][x]==PosstT:#vertical
                Win=True
                break
            else:
                continue
        if Win==False:
            if mat[0][0]==PosstT and mat[1][1]==PosstT and mat[2][2]==PosstT:
                Win=True
                return True
            elif mat[0][2]==PosstT and mat[1][1]==PosstT and mat[2][0]==PosstT:
                Win=True
                return True
            else:
                Win=False
                return False
        else:
            return True
def main():
        print()
        Prints.print_Board()
        PosstT=o
        while True:
            if Game.WIN(PosstT):
                print('You win')
                break
            else:
                print('Play for {T}'.format(T=PosstT))
                while True:
                    try:
                        st= input('Enter  (i,j) : ')
                        i=int(st[0])-1
                        j=ord(st[1])-97
                        s=mat[i][j]
                        break
                    except:
                        print('Error I/P')
                if s!=Em:
                    print('Eroor position')
                    continue
                else:
                    Game.Move(i, j, PosstT)
                    Prints.print_Board()
                    if PosstT==x:
                        PosstT=o 
                        continue
                    else:
                        PosstT=x
                        continue    
main()