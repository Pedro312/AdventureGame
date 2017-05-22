import sys

def message(x):
    print(x)

commands = "pick up, n, e, w, s, quit"


def combat(target):
    print("You have %d health left." % ed.health)
    print("%s has %d health left." % (target.name, target.health))
    while target.health > 0 and ed.health > 0:
        comm = input("> ")
        if comm in ['q', 'quit', 'exit']:
            sys.exit(0)
        elif comm == 'attack':
            ed.attack(target)
            if target.armor > 0:
                print('%s has %d armor left.' % (target.name, target.armor))
            print("%s has %d health left." % (target.name, target.health))
            print()
            target.attack(ed)
            if ed.armor > 0:
                print('You have %d armor left.' % ed.armor)
            print("You have %d health left." % ed.health)
            print()
        if ed.health <= 0:
            print("You have been defeated.")
            sys.exit(0)
        if target.health <= 0:
            print("You have slain %s" % target.name)


class Item(object):
    def __init__(self, name, value, isweapon):
        self.name = name
        self.value = value
        self. isweapom = isweapon


    def sell(self):
        print("You sell the %s for %d gold." % (self.name, self.value))


class Weapon(Item):
    def __init__(self, name, value, damage, isweapon):
        super(Weapon, self).__init__(name, value, isweapon)
        self.damage = damage

    def attack(self, target):
        print("You attack %s for %d damage." % (target.name, self.damage))

class Pistol(Weapon):
    def __init__(self, name, value, damage, isweapon):
        super(Weapon, self).__init__(name, value, isweapon)
        self.damage = damage
        self.isweapon = isweapon


class Sword(Weapon):
    def __init__(self, name, value, damage, isweapon):
        super(Weapon, self).__init__(name, value, isweapon)
        self.damage = damage
        self.isweapon = isweapon


class Dagger(Weapon):
    def __init__(self, name, value, damage, isweapon):
        super(Weapon, self).__init__(name, value, isweapon)
        self. damage = damage
        self. isweapon = isweapon


class Food(Item):
    def __init__(self, name, value, health, isweapon):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.health = health
        self.isweapon = isweapon


class Armor(Item):
    def __init__(self, name, value, durability, isweapon):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.durability = durability
        self.isweapon = isweapon


class Consumables(Item):
    def __init__(self, name, value, amount, isweapon):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.amount = amount
        self.isweapon = isweapon

    def consume(self, target):
        if self.amount > 0:
            print("%s takes in the item." % target.name)
            self.amount -= 1
            if target.health > 100:
                target.health = 100
            if self.amount <= 0:
                print("You run out of the item.")
        else:
            print('You no longer have that item')


class HealthPotion(Consumables):
    def __init__(self, name, value, amount, health_boost, isweapon):
        super(HealthPotion, self).__init__(name, value, amount, isweapon)
        self.health_boost = health_boost
        self.isweapon = isweapon

    def heal(self, target):
        if target.health >= 100:
            print("You can not take the health potion, you are not damaged.")
        else:
            target.health += self.health_boost
            print("You have regained %s health, your health is now at %s." % (self.health_boost, target.health))


edw = HealthPotion("Health Restoration Potion", 25, 2, 40, False)
cookie = Food("Cookie", 15, 20, False)
glo = Pistol("The Glock", 15, 40, True)
swo = Sword('El Dorito', 10, 30, True)
ird = Dagger('Irrelevant Dagger', 5, 25, True)


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

    def equip(self, items):
        self.damage = items.damage
        print('Your damage has been changed to %s' % self.damage)

    def pick_up(self, items):
        self.bag.append(items)
        print("You put the %s in your bag." % items.name)

    def attack(self, target):
        if target.health <= 0:
            print("%s is already dead." % target.name)
        else:
            target.take_damage(self.damage)

    def take_damage(self, damage):
        if self.armor > 0:
            self.armor -= damage
        elif self.armor <= 0:
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

fillet = Food('Fillet', 20, 20, False)
orc1 = Character('The First Orc', 100, 20, 2, 0)
orc2 = Character('The Second Orc', 100, 25, 2, 0)
ed = Character('Edwin Burgos', 100, 25, 1, 100)
rob = Character('Roberto Moreno', 125, 25, 2, 50)
bobb = Character('Bobby Vixathep', 100, 20, 2, 0)
wiebe = Character('Senor Wiebe', 100, 50, 2, 100)


class Room:
    def __init__(self, the_name, N, W, E, S, U, D, the_description, items, npc=None):
        if items is None:
            items = []
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
 mall front doors, but they are nailed shut.', [cookie], orc1)

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
bathroom. The stalls are locked and the mirrors are shattered.', [edw], orc2)

# Room7
jail = Room('Mall Jail', None, None, 'hw', None, None, None, ' This is \
the mall jail. It is extremely cold, and a badge is gleaming on the desk.', [glo], None)

# Room8
ftl = Room('Footlocker', None, None, None, 'hw', None, None, ' It\'s a \
store. There are shoes thrown all over the ground and fairly large footprints,', None, rob)

# Room9
hw2 = Room('Hallway', 'pp', 'hw', 'pa', 'hg', None, None, ' It\'s a \
long hallway.', None, None)

# Room10
pp = Room('Pretzel Palace', 'kc', None, None, 'hw2', None, None, 'There is a cold\
 pretzel on the counter, and the cash register is empty. There is a sword stabbed into the ground.', [swo], None)

# Room11
kc = Room('Kitchen', 'frz', None, None, 'pp', None, None, "It's a kitchen. There\
 is a freezer towards the back and pans on the ground.", None, wiebe)

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
 water bottles.", [ird], None)

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
 is lying on the counter.", None, wiebe)

# Room20
co = Room('Clothing Outlet', 'hw3', None, None, None, None, None, "There is \
tons of clothes thrown on the ground, and all the metal racks are flipped over.", None, None)

node = mentr

# static variables
is_alive = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
Pick = ['pick up', 'Pick up', 'get']
good = ["good", "Good"]
Equip = ['Equip', 'use', 'equip']
une = ['unequip', 'drop']
consume = ['drink', 'eat']
health = ['health', 'armor']
while is_alive is True:
    if node.npc is not None:
        print(node.name)
        print(node.description)
        print()
        combat(node.npc)
        node.npc = None
        print()
    #Print room name and description
    print(node.name)
    print(node.description)
    print()
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
    if command in Equip:
        print("Enter the number of the item to equip it:")
        for num, Weapon in enumerate(ed.bag):
            print(str(num + 1) + ": " + Weapon.name)
        print()
        command = int(input('>')) - 1
        if ed.bag[command].isweapon is True:
            ed.damage = ed.bag[command].damage
            print("You now have %d damage." % ed.damage)
            print()
        elif ed.bag[command].isweapon is not True:
            print('Item is not weapon')
            print()
    elif command in une:
        ed.damage = 25
        print('Your damage is now %d.' % ed.damage)
        print()
    else:
        if command in consume:
            print("Enter the number of the item you wish to take in:")
            for num, Consumable in enumerate(ed.bag):
                print(str(num + 1) + ": " + Consumable.name)
            print()
            command = int(input('>')) - 1
            ed.bag[command].consume(ed)
            ed.bag.pop(command)
            if ed.health < 100:
                ed.health = 100
                print('Your health is now at %d' % ed.health)
            else:

        if command in health:
            print('You have %d armor left.' % ed.armor)
            print('You have %d health left.' % ed.health)
            print()
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
                # Allows us to change nodes
            if command in short_directions:
                command = directions[short_directions.index(command)]
                try:
                    node.move(command)
                except:
                    print('You can\'t')
            else:
                if command in ['help', 'instructions']:
                    print("some commands include;", commands)