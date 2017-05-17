import sys

def message(x):
    print(x)

commands = "pick up, n, e, w, s, quit"


class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def sell(self):
        print("You sell the %s for %d gold." % (self.name, self.value))


class Weapon(Item):
    def __init__(self, name, value, damage):
        super(Weapon, self).__init__(name, value)
        self.damage = damage

    def attack(self, target):
        print("You attack %s for %d damage." % (target.name, self.damage))


class Bomb(Weapon):
    def __init__(self, name, value, damage):
        super(Weapon, self).__init__(name, value)
        self.damage = damage

    def blow_up(self, target):
        print("You have bombed %s and done %d damage." % (target.name, self.damage))
        target.take_damage(self.damage)


class Vehicle(Item):
    def __init__(self, motor, name, material, vtype):
        super(Item, self).__init__()
        self.motor = motor
        self.material = material
        self.name = name
        self.vtype = vtype


class Car(Vehicle):
    def __init__(self, name, motor, material):
        super(Car, self).__init__(name, motor, material, "Car")
        self.engine_status = False

    def move(self):
        if self.engine_status:
            print("You move forward")
        else:
            print("The car is off.")

    def engine_on(self):
        self.engine_status = True
        print("You turn the key and the engine turns on.")


class Food(Item):
    def __init__(self, name, value, health):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.health = health


class Armor(Item):
    def __init__(self, name, value, durability):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.durability = durability


class Consumables(Item):
    def __init__(self, name, value, amount):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.amount = amount


class HealthPotion(Consumables):
    def __init__(self, name, value, amount, health_boost):
        super(HealthPotion, self).__init__(name, value, amount)
        self.health_boost = health_boost

    def heal(self, target):
        if target.health >= 100:
            print("You can not take the health potion, you are not damaged.")
        else:
            target.health += self.health_boost
            print("You have regained %s health, your health is now at %s." % (self.health_boost, target.health))


edw = HealthPotion("Health Restoration Potion", 25, 2, 40)
bobby = Bomb("Bobby's Bomb", 2, 20)
cookie = Food("Cookie", 15, 20)
bobe = Car("Bobby's Car", "V8", "Carbon Fiber")


class Character(object):
    def __init__(self, name, hp, damage, attack_speed, armor, bag=None):
        if bag is None:
            bag = []
        self.name = name
        self.damage = damage
        self.health = hp
        self.attack_speed = attack_speed
        self.armor = armor
        self.bag = bag

    def pick_up(self, items):
        self.bag.append(items)
        print("You put the %s in your bag." % items.name)

    def attack(self, target):
        if target.health == 0:
            print("%s is already dead." % target.name)
        else:
            target.take_damage(self.damage)
            print("You attacked %s for %d damage." % (target.name, self.damage))

    def take_damage(self, damage):
        if self.armor > 0:
            self.armor -= damage
        elif self.armor == 0:
            if self.health > 0:
                self.health -= damage
        else:
            print("%s is already dead" % self.name)

    def eat(self, comida):
        if self.health < 100:
            self.health += comida.health
            print("You have eaten %s and gained %d health." % (comida.name, comida.health))
        else:
            print("You can not eat anymore, or you may explode.")

fillet = Food('Fillet', 20, 20)
orc1 = Character('The First Orc', 100, 20, 2, 0)
orc2 = Character('The Second Orc', 100, 20, 2, 0)
sam = Character("Sam V", 100, 0.000000000001, 0.0000000001, 50)
ed = Character('Edwin Burgos', 100, 2, 1, 500)
rob = Character('Roberto Moreno', 100, 100, 2, 200)
bobb = Character('Bobby Vixathep', 100, 20, 2, 0)
wiebe = Character('Senor Wiebe', 100, 66, 2, 200)


class Room:
    def __init__(self, the_name, N, W, E, S, U, D, the_description, items, npc):
        if items is None:
            items = []
        if npc is None:
            npc = []
        self.name = the_name
        self.description = the_description
        self.north = N
        self.west = W
        self.east = E
        self.south = S
        self.up = U
        self.down = D
        self.items = items
        self.npc = npc

    def move(self, direction):
        ##This function allows movement to a different node.
        global node
        node = globals()[getattr(self, direction)]


# Room1
mentr = Room('Mall Entrance', 'hw', 'food', 'elev', None, None, None, ' You\
 are in the front mall entrance. Behind you are the\
 mall front doors, but they are nailed shut.', [cookie], None)

# Room2
hw = Room('Hallway', 'ftl', 'jail', 'hw2', 'mentr', None, None, ' It\'s a long \
hallway.', None, None)

# Room3
food = Room('Foodcourt', None, 'wfr', 'mentr', 'bath', None, None, ' There are\
tons of empty tables. The light is flickering.', None, None)

# Room4
elev = Room('Elevator', None, 'mentr', None, None, None, None, ' It\'s \
an elevator. The power is down.', None, None)

# Room5
wfr = Room('Wet Floor', None, None, 'food', None, None, None, ' The floor is \
significantly moist.', None, None)

# Room6
bath = Room('Bathroom', 'food', None, None, None, None, None, ' It\'s a \
bathroom. The stalls are locked and the mirrors are shattered.', [edw], None)

# Room7
jail = Room('Mall Jail', None, None, 'hw', None, None, None, ' This is \
the mall jail. It is extremely cold, and a badge is gleaming on the desk.', None, None)

# Room8
ftl = Room('Footlocker', None, None, None, 'hw', None, None, ' It\'s a \
store. There are shoes thrown all over the ground and fairly large footprints,', None, None)

# Room9
hw2 = Room('Hallway', 'pp', 'hw', 'pa', 'hg', None, None, ' It\'s a \
long hallway.', None, None)

# Room10
pp = Room('Pretzel Palace', 'kc', None, None, 'hw2', None, None, 'There is a cold\
 pretzel on the counter, and the cash register is empty.', None, None)

# Room11
kc = Room('Kitchen', 'frz', None, None, 'pp', None, None, "It's a kitchen. There\
 is a freezer towards the back and pans on the ground.", None, None)

# Room12
hg = Room('Hunting Goods', 'hw2', None, None, 'ws', None, None,
          "It's a hunting shop. There are firearms hung on the walls and on the counters.", None, None)

# Room13
ws = Room('Weapon Storage', 'hg', None, None, None, None, None, "There are\
 racks of weapons on the walls and aligned on shelves, and stacks of\
 ammunition in the corner of the room.", None, None)

# Room14
pa = Room('Play Area', 'ts', 'hw2', 'hw3', 'jwr', None, None, "There are\
 multiple obstacle courses for children, but a few are broken in half\
 and most have spider webs.", None, None)

# Room15
frz = Room('Freezer', None, None, None, 'kc', None, None, "It is extremely\
 cold (obviously, it's a freezer) and to your right there are frozen\
 water bottles.", None, None)

# Room16
ts = Room('Toy Store', None, None, None, 'pa', None, None, "This room seems to\
 be oddly clean, compared to the rest. Although some shelves are still snapped.", None, None)

# Room17
jwr = Room('Jewelry Store', 'pa', None, None, None, None, None, "There are\
 diamond rings in the glass cases, and a sparkling diamond necklace\
 sitting alone on a counter top.", None, None)

# Room18
hw3 = Room('Hallway', 'fs', 'pa', 'hbp', 'co', None, None, "It's \
the end of a hall the hall continues ahead.", None, None)

# Room19
hbp = Room('Hli\'s Beauty Products', None, 'hw3', None, None, None, None, "A\
 very neat beauty store, with makeup products on  the shelves,\
 and clothing hanging on racks organized by color. A name tag reading 'Hli'\
 is lying on the counter.", None, None)

# Room20
co = Room('Clothing Outlet', 'hw3', None, None, None, None, None, "There is \
tons of clothes thrown on the ground, and all the metal racks are flipped over.", None, None)

node = mentr

# static variables
is_alive = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
Pick = ['pick up', 'Pick up']
good = ["good", "Good"]
while is_alive is True:
    # Print room name and description
    print(node.name)
    print(node.description)
    print("You have the following items in your bag:")
    for item in ed.bag:
        print(item.name)
    if len(node.items) > 0:
        print()
        print("There are the following items:")
        for num, item in enumerate(node.items):
            print(str(num + 1) + ": " + item.name)
    command = input('> ')
    if command in Pick:
        if len(node.items) > 0:
            print()
            print('Enter the number to pick the item up.')
            for num, item in enumerate(node.items):
                print(str(num + 1) + ": " + item.name)
            print()
            command = int(input('>')) - 1
            ed.pick_up(node.items[command])
            node.items.pop(command)
    else:
            # Ask for input
        if command in ['quit', 'exit']:
            sys.exit(0)
        else:
                # Allows us to change nodes
            if command in short_directions:
                command = directions[short_directions.index(command)]
                try:
                    node.move(command)
                except:
                    print('You can\'t')
            else:
                if command in ['help', 'instructions']:
                    print ("some commands include;", commands)