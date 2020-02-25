from random import randint 

def main():
    
    mat = []
    
    mat.append([])
    for j in range(10):
        mat[0].append(randint(1,20))
    
    mat.append([])
    for j in range(10):
        mat[1].append(pow(mat[0][j],2))

    mat.append([])
    for j in range(10):
        mat[2].append(mat[0][j]+mat[1][j])
        
    for i in range(3):
        print '{} '.format(mat[i])
    
if __name__ == "__main__":
    main()
