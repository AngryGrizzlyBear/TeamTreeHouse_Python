list('hello')
'hello'.split()
'hello there students'.split()
"red:blue:green".split()

flavors = ['chocolate', 'mint', 'strawberry']
','.join(flavors)
print("My favorite flavors are: " + ', '.join(flavors))
print("My favorite flavors are: {}".format(", ".join(flavors))

available = "banana split;hot fudge;cherry;malted;black and white"
sundaes = available.split(";")
menu = "Our available flavors are: {}.".format(", ".join(sundaes))
print(menu)
#had to do it. Can probably make this better.