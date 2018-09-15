def new_password(oldpass,newpass):
    numberlist = ['1','2','3','4','5','6','7','8','9','0']
    if newpass != oldpass and len(newpass) >= 6:
        result = 'True maar no number';
        for char in newpass:
            if char in numberlist:
                result = True
    else:
        result = False
    return result

print(new_password('dasfasdfasdf','adsfasdf'))