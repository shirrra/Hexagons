import sys
sys.path.append('../src')
from hexagons_classes import HexagonsGame, _Vec, _Hexagon, Tile, Shape, Line, Circle, Triangle

def func(pr = False):
  HexagonsGame.start()
  
  # Solution
  # 1.
  start_tile = Tile(2, 2)
  ring = start_tile.neighbors()
  ring.draw('purple')
  start_tile.draw('white')
  
  # 2.
  for i in range(4):
      ring = ring.copy_paste('right', 2)
      ring.draw('purple')

  if pr:
    HexagonsGame.plot()

  return HexagonsGame.board_state

if __name__ == '__main__':
  func(pr=True)
