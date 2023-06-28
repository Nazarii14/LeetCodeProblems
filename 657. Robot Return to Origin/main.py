# def judgeCircle(moves):
#      position = [0, 0]
#      for i in moves:
#          if i == "U":
#              position[1] += 1
#          if i == "D":
#              position[1] -= 1
#          if i == "L":
#              position[0] -= 1
#          if i == "R":
#              position[0] += 1
#      return position == [0, 0]
def judgeCircle(moves):
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")

print(judgeCircle("UD"))
print(judgeCircle("LL"))
