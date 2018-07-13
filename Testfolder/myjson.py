f= open("testfile.txt,"w"
f.close()
myJson=[{},{},{}]
dump{myJson,f}
jsonName,load(f)

print(f.read())
f.write("hello")
f.close()
