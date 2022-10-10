print('\t\t\t\nData Types  ')
#
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Sring
var1=str('Ajay')
print(var1)
print(type(var1),'\n')

#Integer FLoating COmplex
var2=int(25)
print(var2)
print(type(var2),'\n')

var3=float(23.54)
print(var3)
print(type(var3),'\n')

var3=complex(1j+8)
print(var3)
print(type(var3))

# Sequence Types : List touple range
a=["ajay","Raut","CP","AR"]
b=("ajay,'Raut","AR","C")
c=range(0,100)
print('List is : ',a,'\nTouple is:',b,'\nRange is:',c)

#Mapping Type :Dict
a={'name':'Ajay','lname':'Raut'}
print(a)
print('Name Of Candidate is:',a['name'])


#Set_Type     : Set and Frozenset[Immutable]
a={'a','b','c','d'}
b=frozenset({'a','b','c'})
print(type(a),type(b))
print(a,b)

#bool          :true false

a=True
b=False

#None_Type


a=None
print(a)
print(type(a))


#Binary Type : Byte ,Bytearray , Memoryview

a=bytes(b"Hello")
a=print(a)
print(memoryview(a))