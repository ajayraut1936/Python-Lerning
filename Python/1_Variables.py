print('\n\t\t\tVariables and Its Types')

var1='V1_Global_Variable';                  #Global Variable

class Class_Name:
    var2='V2_Instance_Variable'             #Instance Variable
    def Pirnt_Data(self):
        var3='V3_Local_Variable'            #Local Variable
        print(var3)


obj1=Class_Name()

print(var1)
print(obj1.var2)
print(obj1.Pirnt_Data())