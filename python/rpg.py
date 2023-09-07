def main():
  yoshihiko = RpgHero(_atk = 50, _hp = 100)

  print("ATK:", yoshihiko.atk)
  print("HP:", yoshihiko.hp)

  yoshihiko.powerup(10)
  yoshihiko.recover(25)

  print("ATK:", yoshihiko.atk)
  print("HP:", yoshihiko.hp)


  print("=== Level up ===")

  yoshihiko = RpgMaster(_atk = 50, _hp = 100, _mp = 20)
  yoshihiko.enhance()
  print("ATK:", yoshihiko.atk)

class RpgHero:

  def __init__(self, _atk=0, _hp=0):
    self.atk = _atk
    self.hp = _hp

  def powerup(self, i):
    self.atk = self.atk + i

  def recover(self, j):
    self.hp = self.hp + j


class RpgMaster(RpgHero):

  def __init__(self, _atk=0, _hp=0, _mp = 0):
    super().__init__(_atk, _hp)
    self.mp = _mp

  def enhance(self):
    super().powerup(self.mp)


if __name__ == "__main__":
  main()
