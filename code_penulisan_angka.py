import os
kata = ['','one ','two ','three ','four ','five ','six ','seven ','eight ','nine ']
belasan = ['','eleven','twelve','thirteen','fourteen','fifthteen','sixteen','seventeen','eighteen','nineteen']
puluhan = ['','ten ','twenty ','thirty ','fourty ','fifty ','sixty ','seventy ','eighty ','ninety ']
def perhitungan(n):
    if n <10:
        return kata[n]
    elif n>=1_000_000_000:
        return perhitungan(n//1_000_000_000)+"billion "+(perhitungan(n%1_000_000_000)if n%1_000_000_000 != 0 else '')
    elif n>=1_000_000:
        return perhitungan(n//1_000_000)+"million "+(perhitungan(n%1_000_000)if n%1_000_000 != 0 else '')
    elif n>=1_000:
        return perhitungan(n//1000)+"thousand "+(perhitungan(n%1000)if n%1000 != 0 else '')
    elif n ==100:
        return perhitungan(n//100)+"hundred "+(perhitungan(n%100)if n%100 != 0 else '')    
    elif n >100:
        return perhitungan(n//100)+"hundred and "+(perhitungan(n%100)if n%100 != 0 else '')

    else:
        if n%10 == 0:
            return puluhan[n//10]
        elif n<20 and n>10:
            return belasan[n//10]
        else:
            return puluhan[n//10]+ (perhitungan(n%10) if n%10!=0 else ' ')
nomor= int(input('Number? '))
print  (perhitungan(nomor))
os.system("pause")