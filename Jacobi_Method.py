n = int(input("Enter number of unknowns: "))
data = []
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    row = []
    for j in range(n+1):
        value = float(input( 'data['+str(i)+']['+ str(j)+']='))
        row.append(value)
    data.append(row)
te = int(input("Enter tolerable Error : "))
x = []
accuracy = []
acceptance = []
# Initial Guess 0
for __ in range(n):
    x.append(0)
    accuracy.append(0)
    acceptance.append("Not Accepted")
while ("Not Accepted" in acceptance):
    for i in range(n):
        rhs = data[i][-1]
        i_coeff = data[i][i]
        except_i = 0
        for j in range(n):
            if i != j:
                except_i += data[i][j]*x[j]
        x[i] = (rhs - except_i) / i_coeff
#     for n = 3        
#     x[0] = (data[0][3]-(data[0][1]*x[1]+data[0][2]*x[2]))/data[0][0]
#     x[1] = (data[1][3]-(data[1][0]*x[0]+data[1][2]*x[2]))/data[1][1]
#     x[2] = (data[2][3]-(data[2][0]*x[0]+data[2][1]*x[1]))/data[2][2]
    for i in range(n):
        rhs = data[i][-1]
        lhs = 0
        for j in range(n):
            lhs += data[i][j]*x[j]
        accuracy[i] = abs(rhs-lhs)
#     for n = 3
#     accuracy[0] = data[0][3]-(data[0][0]*x[0]+data[0][1]*x[1]+data[0][2]*x[2])
#     accuracy[1] = data[1][3]-(data[1][0]*x[0]+data[1][1]*x[1]+data[1][2]*x[2])
#     accuracy[2] = data[2][3]-(data[2][0]*x[0]+data[2][1]*x[1]+data[2][2]*x[2])
    for i in range(n):
        if accuracy[i] <= te:
            acceptance[i] = "Accepted"
#     for n = 3 
#     if abs(accuracy[0])<=te:
#         acceptance[0] = "Accepted"
#     if abs(accuracy[1])<=te:
#         acceptance[1] = "Accepted"
#     if abs(accuracy[2])<=te:
#         acceptance[2] = "Accepted"
print(x)
