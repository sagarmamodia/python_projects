print('Order of Matrix:')
n = int(input())

print('Enter Matrix A: ')
A = [list(map(int, input().split())) for i in range(n)]

def print_matrix(M):
    print('---------------------------')
    for row in M:
        for col in row:
            print(col, " ", end=' ')
        print()	
    print('---------------------------')

def get_minor(A, i, j, n):
    minor = []
    for r in range(n-1):
        minor.append([])    
    
    counter = 0
    for row in range(n):
        if row != i:
            for col in range(n):
                if col != j:
                    minor[counter].append(A[row][col])
            counter += 1
    return minor


def determinant(A, order):
    det = 0
    if order == 2:
        det = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return det
    if order > 2:
        for i in range(0, order):
            if 0+i % 2 == 0:
                det += A[0][i] * determinant(get_minor(A, 0, i, order), order-1)
            if 0+i % 2 != 0:
                det += -A[0][i] * determinant(get_minor(A, 0, i, order), order-1)
    return det

def adjoint(A, order):
    adj = []
    for i in range(order):
        adj.append([])
        for j in range(order):
            if (i+j) % 2 == 0: #this was a bug as I was writing it as i+j % 2 ==0 I had overlooked the fact that % is given preference first over +
                c_i_j = determinant(get_minor(A, i, j, order), order-1)
            elif (i+j) % 2 != 0:
                c_i_j = -1 * determinant(get_minor(A, i, j, order), order-1)
            # print('cofactor of' + str(i) + ' ' + str(j) + 'is' + str(c_i_j))
            adj[i].append(c_i_j)
    return transpose(adj, order)
    
    
def transpose(A, order):
    temp = []
    for i in range(order): #this is for identification of col
        temp.append([])
        for j in range(order):
            temp[i].append(A[j][i])
    return temp

#can only multiple square lists of same length
def multiply_list(a, b):
	result = 0
	for i in range(len(a)):
		result += a[i] * b[i]
	return result

def matrix_multiply(A, B):
    AB = []
    t_B = transpose(B, len(B))
    for i in range(len(A)):
        AB.append([])
        for j in range(len(A[0])):
            AB[i].append(multiply_list(A[i], t_B[j]))
    return AB

def scalar_multiplication(A, x):
    r = []
    for i in range(len(A)):
        r.append([])
        for j in range(len(A)):
            product = A[i][j] * x
            r[i].append(round(product, 2))
    return r

def inverse_matrix(A, order):
    det = determinant(A, order)
    # print(det)
    adj_A = adjoint(A, order)
    # print(adj_A)
    if det == 0:
        print('inverse of singular matrix does not exist')
    else:
        print_matrix(scalar_multiplication(adj_A, (1/det)))

inverse_matrix(A, n)
