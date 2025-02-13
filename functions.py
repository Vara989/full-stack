def info(**kargs):
    for m,v in kargs.items():
        print(m,v,sep="=")
info(Name="vishnu", Age=24,place="Hyderabad")
info(Name="kishore", Age=22,place="ongole")