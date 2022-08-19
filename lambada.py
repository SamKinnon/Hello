pe0ple = [
	{"name":"Sam","House":"Floor2"},
	{"name":"Queen","House":"Floor1"},
	{"name":"King","House":"Floor0"}

]
#def f(person):
	#return person["name"]
#pe0ple.sort(key=f)
pe0ple.sort(key=lambda person:person["name"])
print (pe0ple)
