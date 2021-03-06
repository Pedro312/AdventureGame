import sys

def message(x):
    print(x)

commands = "pick up, n, e, w, s, quit, attack, hit, drop, eat, drink"


def combat(target):
    if ed.armor > 0:
        print('You have %d armor left.' % ed.armor)
    print("You have %d health left." % ed.health)
    print()
    if target.armor > 0:
        print('%s has %d armor left.' % (target.name , target.armor))
    print("%s has %d health left." % (target.name, target.health))
    while target.health > 0 and ed.health > 0:
        command = input("> ")
        if command in ['q', 'quit', 'exit']:
            sys.exit(0)
        elif command in consume:
            print("Enter the number of the item you wish to take in:")
            for num, consumable in enumerate(ed.bag):
                print(str(num + 1) + ": " + consumable.name)
            print()
            command = int(input('>')) - 1
            if ed.bag[command].isweapon is False:
                if ed.bag[command].amount > 0:
                    ed.bag[command].consume(ed)
                    if ed.health > 100:
                        ed.health = 100
                    print("You now have %d health." % ed.health)
                    print()
                if ed.bag[command].amount <= 0:
                    print('You have run out of this item.')
                    ed.bag.pop(command)
                    print()
            elif ed.bag[command].isweapon is not False:
                print('Item is not consumable;')
                print()
        elif command == 'attack':
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
    def __init__(self, name, value, isweapon, isgun):
        self.name = name
        self.value = value
        self. isweapon = isweapon
        self.isgun = isgun

    def sell(self):
        print("You sell the %s for %d gold." % (self.name, self.value))


class Weapon(Item):
    def __init__(self, name, value, damage, isweapon, isgun):
        super(Weapon, self).__init__(name, value, isweapon, isgun)
        self.damage = damage
        self.isgun = isgun

    def attack(self, target):
        print("You attack %s for %d damage." % (target.name, self.damage))


class Guns(Weapon):
    def __init__(self, name, value, damage, isweapon, ammo, isgun):
        super(Weapon, self).__init__(name, value, isweapon, isgun)
        self.damage = damage
        self.ammo = ammo
        self.isgun = isgun

    def attack(self, target):
        if self.ammo <= 0:
            print('You have no more ammo.')
        elif self.ammo > 0:
            print("You attack %s for %d damage." % (target.name, self.damage))
            target.health -= self.damage


class Pistol(Guns):
    def __init__(self, name, value, damage, isweapon, ammo, isgun):
        super(Weapon, self).__init__(name, value, isweapon, isgun)
        self.damage = damage
        self.isweapon = isweapon
        self.ammo = ammo
        self.isgun = isgun

    def attack(self, target):
        if self.ammo <= 0:
            print('You have no more ammo.')
        elif self.ammo > 0:
            print("You attack %s for %d damage." % (target.name, self.damage))
            target.health -= self.damage


class Sword(Weapon):
    def __init__(self, name, value, damage, isweapon, isgun):
        super(Weapon, self).__init__(name, value, isweapon, isgun)
        self.damage = damage
        self.isweapon = isweapon
        self.isgun = isgun


class Dagger(Weapon):
    def __init__(self, name, value, damage, isweapon, isgun):
        super(Weapon, self).__init__(name, value, isweapon, isgun)
        self. damage = damage
        self. isweapon = isweapon
        self.isgun = isgun


class Food(Item):
    def __init__(self, name, value, health, isweapon, amount, isgun):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.health = health
        self.isweapon = isweapon
        self.amount = amount
        self.isgun = isgun

    def consume(self, target):
        if self.amount > 0:
            print("%s takes in the item." % target.name)
            self.amount -= 1
            if target.health < 100:
                target.health += self.health
        if self.amount <= 0:
            print("You have run out of the item.")


class Armor(Item):
    def __init__(self, name, value, durability, isweapon, isgun):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.durability = durability
        self.isweapon = isweapon
        self.isgun = isgun


class Consumables(Item):
    def __init__(self, name, value, amount, isweapon, health, isgun):
        super(Item, self).__init__()
        self.name = name
        self.value = value
        self.amount = amount
        self.isweapon = isweapon
        self.health = health
        self.isgun = isgun

    def consume(self, target):
        if self.amount > 0:
            print("%s takes in the item." % target.name)
            self.amount -= 1
            if target.health < 100:
                target.health += self.health
        if self.amount <= 0:
            print("You have run out of the item.")


class HealthPotion(Consumables):
    def __init__(self, name, value, amount, isweapon, health, isgun):
        super(HealthPotion, self).__init__(name, value, amount, isweapon, health, isgun)
        self.isweapon = isweapon
        self.health = health
        self.isgun = isgun

    def consume(self, target):
        if self.amount > 0:
            print("%s takes in the item." % target.name)
            self.amount -= 1
            if target.health < 100:
                target.health += self.health
        if self.amount <= 0:
            print("You have run out of the item.")


edw = HealthPotion("Weak Health Potion", 25, 3, False, 20, False)
cookie = Food("Cookie", 15, 20, False, 2, False)
glo = Pistol("The Glock", 15, 40, True, 1, True)
swo = Sword('El Dorito', 10, 30, True, False)
ird = Dagger('Irrelevant Dagger', 5, 25, True, False)
ban = Food('Banana', 10, 10, False, 2, False)
ri = Pistol ('Hunting Rifle', 20, 50, True, 1, True)
m4 = Pistol('M4 Carbine', 200, 75, True, 1, True)
mhp = HealthPotion('Medium Health Potion', 2, 2, False, 35, False)
kk = Dagger('Kitchen Knife', 2, 10, True, False)
shp = HealthPotion('Strong Health Potion', 2, 1, False, 50, False)
uhp = HealthPotion('Ultra Health Potion', 2, 3, False, 100, False)
ic = Food('Ice Cream', 2, 15, False, 1, False)



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

    def consume(self, consumable):
        if consumable.amount > 0:
            print("%s takes in the item." % self.name)
            consumable.amount -= 1
            if self.health < 100:
                self.health += consumable.health
        if consumable.amount <= 0:
            ed.bag.pop(command)
            print("You have run out of the item.")

orc1 = Character('The First Orc', 100, 20, 2, 0)
orc2 = Character('The Second Orc', 100, 25, 2, 0)
ed = Character('Edwin Burgos', 100, 25, 1, 100)
rob = Character('Roberto Moreno', 100, 25, 2, 0)
bob = Character('Bobby Vixathep', 100, 20, 2, 0)
la = Character('Senor Wiebe', 100, 75, 2, 125)
g = Character('Gloria', 100, 30, 2, 25)
Hli = Character('Hli', 100, 50, 2, 25)
gi = Character('Giant', 100, 50, 2, 50)
gl = Character('Eric', 100, 50, 2, 75)
ja = Character('Jacinto', 100, 50, 2, 100)
ro = Character('Gun Guardian', 100, 40, 2, 50)
wiebe = Character('Larry', 100, 35, 3, 0)
rc = Character('Stranger', 100, 25, 3, 25)

class Room:
    def __init__(self, the_name, N, W, E, S, U, D, the_description, items, npc=None, hli=None):
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
        self.hli = hli

    def move(self, direction):
        ##This function allows movement to a different node.
        global node
        node = globals()[getattr(self, direction)]


# Room1
mentr = Room('Mall Entrance', 'hw', 'food', 'elev', None, None, None, ' You\
 are in the front mall entrance. Behind you are the\
 mall front doors, but they are nailed shut.', [cookie], orc1, None)

# Room2
hw = Room('Hallway', 'ftl', 'jail', 'hw2', 'mentr', None, None, ' It\'s a long \
hallway.', None, None, None)

# Room3
food = Room('Foodcourt', None, 'wfr', 'mentr', 'bath', None, None, ' There are\
tons of empty tables. The light is flickering.', None, None, None)

# Room4
elev = Room('Elevator', None, 'mentr', None, None, None, None, ' It\'s \
an elevator. The power is down.', [mhp, kk], None, None)

# Room5
wfr = Room('Wet Floor', None, None, 'food', None, None, None, ' The floor is \
significantly moist.', [edw, ic], None, None)

# Room6
bath = Room('Bathroom', 'food', None, None, None, None, None, ' It\'s a \
bathroom. The stalls are locked and the mirrors are shattered.', [edw], orc2, None)

# Room7
jail = Room('Mall Jail', None, None, 'hw', None, None, None, ' This is \
the mall jail. It is extremely cold, and a badge is gleaming on the desk.', [glo, mhp], rc, None)

# Room8
ftl = Room('Footlocker', None, None, None, 'hw', None, None, ' It\'s a \
store. There are shoes thrown all over the ground and fairly large footprints,', [shp], rob, None)

# Room9
hw2 = Room('Hallway', 'pp', 'hw', 'pa', 'hg', None, None, ' It\'s a \
long hallway.', None, None, None)

# Room10
pp = Room('Pretzel Palace', 'kc', None, None, 'hw2', None, None, 'There is a cold\
 pretzel on the counter, and the cash register is empty. There is a sword stabbed into the ground.', [swo], None, None)

# Room11
kc = Room('Kitchen', 'frz', None, None, 'pp', None, None, "It's a kitchen. There\
 is a freezer towards the back and pans on the ground.", [edw], None, None)

# Room12
hg = Room('Hunting Goods', 'hw2', None, None, 'ws', None, None, "It's a hunting shop. \
There are firearms hung on the walls and on the counters.", None, None, None)

# Room13
ws = Room('Weapon Storage', 'hg', None, None, None, None, None, "There are\
 racks of weapons on the walls and aligned on shelves, and stacks of\
 ammunition in the corner of the room.", [ri, mhp], ro, None)

# Room14
pa = Room('Play Area', 'ts', 'hw2', 'hw3', 'jwr', None, None, "There are\
 multiple obstacle courses for children, but a few are broken in half\
 and most have spider webs.", [mhp], g, None)

# Room15
frz = Room('Freezer', None, None, None, 'kc', None, None, "It is extremely\
 cold (obviously, it's a freezer) and to your right there are frozen\
 water bottles.", [ird, mhp], None, None)

# Room16
ts = Room('Toy Store', None, None, None, 'pa', None, None, "This room seems to\
 be oddly clean, compared to the rest. Although some shelves are still snapped.", [edw], None, None)

# Room17
jwr = Room('Jewelry Store', 'pa', None, None, None, None, None, "There are\
 diamond rings in the glass cases, and a sparkling diamond necklace\
 sitting alone on a counter top.", [ban, shp], None, None)

# Room18
hw3 = Room('Hallway', 'hw4', 'pa', 'hbp', 'co', None, None, "It's \
the end of a hall, the hall continues ahead.", [ban], None, None)

# Room19
hbp = Room('Hli\'s Beauty Products', None, 'hw3', None, None, None, None, "A\
 very neat beauty store, with makeup products on  the shelves,\
 and clothing hanging on racks organized by color. A name tag reading 'Hli'\
 is lying on the counter. You must find Hli.", [m4, shp], wiebe, None)

# Room20
co = Room('Clothing Outlet', 'hw3', None, None, None, None, None, "There is \
tons of clothes thrown on the ground, and all the metal racks are flipped over.", [edw], bob, None)

# Room21
hw4 = Room('Hallway', 'Dr', None, None, 'hw3', None, None, "There is nothing to the left or the right. Ahead are two big closed doors \
There's a sign which reads 'She's in here'. Something doesn't seem right.", [shp], None, None)

# Room22
Dr = Room('Dark Room', 'r23', None, None, 'hw4', None, None, "It is very dark, but a flickering light makes the room \
barely visible.", None, gi, None)

# Room23
r23 = Room('Light Room', 'r24', None, 'Dr', None, None, "The exact opposite of the last room, it is extremely bright \
as the walls grow a bright white.", None, gl, None)
# Room24
r24 = Room('Mirror Room', 'r25', None, None, 'r23', None, None, "The room is full of mirrors. All around you the only \
the only visible thing is your reflectio.", None, ja, None)

# Room25
r25 = Room('Restroom', 'r26', None, None, 'r24', None, None, "There are two pouches on the ground. A sign reads 'Go north \
when ready.", [edw, mhp, shp], None, None)

# Room26
r26 = Room('Final Room', 'r27', None, None, 'r25', None, None, "There is another set of bulky doors. A sign reads \
'If you've made it this far go ahead just one more time.'", None, la, None)

# Room27
r27 = Room('Backroom', None, None, None, 'r26', None, None, "In the corner is a girl... Hli?", None, None, Hli)

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
    if node.hli is None:
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
                for num, consumable in enumerate(ed.bag):
                    print(str(num + 1) + ": " + consumable.name)
                print()
                command = int(input('>')) - 1
                if ed.bag[command].isweapon is False:
                    if ed.bag[command].amount > 0:
                        ed.bag[command].consume(ed)
                        if ed.health > 100:
                            ed.health = 100
                            print("You now have %d health." % ed.health)
                        print()
                    if ed.bag[command].amount <= 0:
                        print('You have run out of this item.')
                        ed.bag.pop(command)
                        print()
                elif ed.bag[command].isweapon is not False:
                    print('Item is not consumable;')
                    print()
            else:
                if command in health:
                    if ed.armor <= 0:
                        print('You have 0 armor left.')
                        print('You have %d health left.' % ed.health)
                    elif ed.armor > 0:
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
    else:
        print(node.name)
        print(node.description)
        print()
        print('You have found Hli! She is safe!')
        print('Game Over')
        sys.exit(0)