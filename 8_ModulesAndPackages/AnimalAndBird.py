# Module3: AnimalAndBird
print("Same fn is multiple modules")

print("---Apr2-----")
from Animal import fly,colour
fly()
colour()


from Bird import fly,colour
fly()
colour()


print("---Apr1-----")
import Bird
import Animal

Bird.fly()
Bird.colour()

Animal.fly()
Animal.colour()