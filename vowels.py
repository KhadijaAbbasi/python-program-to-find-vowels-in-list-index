list=['apple','bottle','lemon','peach','mango']
count=0
for x in range(len(list)):
    name=str(list[x])
    for y in str(name):
        if y=='a' or y=='e' or y=='i' or y=='o' or y=='u':
            count=count+1
print(count)