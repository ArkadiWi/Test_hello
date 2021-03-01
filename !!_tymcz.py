def  fun (a):
    print (a)
    if a > 30:
        return 3
    else:
        return a + fun (a+3)
    print (a)

print (fun(25))