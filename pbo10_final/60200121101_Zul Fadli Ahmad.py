# Nama Zul Fadli Ahmad
# NIM 60200121101

# Main class
class Character:
    def __init__(self, nama, hp, mana, stamina, phsy, armor, crtChance, crtDamage):
        self.nama = nama
        self.hp = hp
        self.mana = mana
        self.stamina = stamina
        self.phsy = phsy
        self.armor = armor
        self.crtChance = crtChance
        self.crtDamage = crtDamage
        self.infoCharacter()

    def infoCharacter(self):
        print("New Character\n=========================")
        print("Nama: " + str(self.nama))
        print("HP: " + str(self.hp))
        print("Mana: " + str(self.mana))
        print("Stamina: " + str(self.stamina))
        print("Phsy: " + str(self.phsy))
        print("Armor: " + str(self.armor))
        print("Crt Change: " + str(self.crtChance))
        print("Crt Damage: " + str(self.crtDamage))
        print("\n")

# Sub class
class Hero(Character):
    def __init__(self, nama, hp, mana, stamina, phsy, armor, crtChance, crtDamage):
        super().__init__(nama, hp, mana, stamina, phsy, armor, crtChance, crtDamage)

class Enemy(Character):
    def __init__(self, nama, hp, mana, stamina, phsy, armor, crtChance, crtDamage):
        super().__init__(nama, hp, mana, stamina, phsy, armor, crtChance, crtDamage)


# another class
class Battle:
    def attack(self, attacker, target):
        if(attacker.phsy > target.armor):
            self.demage = attacker.phsy - target.armor
            target.hp = target.hp - self.demage
            
        self.__infoBattle(attacker, target)

    def skill(self, multyplayDing, attacker, target):
        attacker.phsy = attacker.phsy + multyplayDing;
        self.attack(attacker, target)


    def __infoBattle(self, attacker, target):
        print("!!! Penyerangan Terjadi !!!\n----------------------------")
        print("=> " + attacker.nama + " Menyerang " + target.nama);
        print("Demage pada " + target.nama + ": " + str(self.demage))
        print("HP " + target.nama + " tersisa : " + str(target.hp) + "\n")




# Instansiasi Objek
# nama    =          nama     hp       mana  stamina phsy armor ...
barbarian = Hero("Barbarian", 120, "Si paling barbar", 400, 20, 4, 20, 20)
giant = Enemy("Giant", 100, "Si paling besar", 300, 30, 6, 10, 5)


battle = Battle()
#       attacker, target

# Barbarian VS Giant
battle.attack(barbarian, giant)
battle.attack(giant, barbarian)
battle.skill(2, barbarian, giant)