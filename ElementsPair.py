class Elements:
    def DoSum(self,Numbers,Target):
        lookup={}
        for i,Numbers in enumerate(Numbers):
            if Target-Numbers in lookup:
                return(lookup[Target-Numbers],i)
            lookup[Numbers]=i
Value=int(input("Enter sum of which you want to make this search"))
print("Index1= %d,Index2= %d" %Elements().DoSum((10,20,30,40,50,60,70),Value))
