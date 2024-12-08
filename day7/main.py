###############*###############
#           PART 1            #
###############*###############
def check(tval, eqs):
  if len(eqs) == 1: return tval == eqs[0]
  return (tval % eqs[-1] == 0 and check(tval // eqs[-1], eqs[:-1])) or \
         (tval > eqs[-1] and check(tval - eqs[-1], eqs[:-1]))


###############*###############
#           PART 2            #
###############*###############
def check2(tval, eqs):
  if len(eqs) == 1: return tval == eqs[0]
  s_tval, s_eqs = str(tval), str(eqs[-1])
  return (tval % eqs[-1] == 0 and check2(tval // eqs[-1], eqs[:-1])) or \
         (tval > eqs[-1] and check2(tval - eqs[-1], eqs[:-1])) or \
         (len(s_tval) > len(s_eqs) and s_tval.endswith(s_eqs) and check2(int(s_tval[:-len(s_eqs)]), eqs[:-1]))


res1, res2 = 0, 0
for line in open("input.txt", "r"):
  test, *eqs = map(int, line[:-1].replace(":", "").split())
  res1 += int(check(test, eqs)) * test
  res2 += int(check2(test, eqs)) * test

print(res1)
print(res2)
