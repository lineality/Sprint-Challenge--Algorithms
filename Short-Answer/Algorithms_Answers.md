#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0
    while (a < n * n * n):
      a = a + n * n
'''
a = 0                                       O(1) simple attribution
    while (a < n * n * n):                  O(1) checking single value
      a = a + n * n                         O(1) simple attribution
                                            Total: dominant feature is...
                                            O(1)


'''
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
'''
b)  sum = 0                                 O(1) simple attribution
    for i in range(n):                      0(n) iterates through all of n one time (for)
      j = 1                                     O(1) simple attribution
      while j < n:                              O(1) checking single value (while)
        j *= 2                                  O(1) simple attribution
        sum += 1                                O(1) simple attribution
                                            Total: this contains a nested for-while, but the while is O(1)
                                            O(n)
'''
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
'''
c)  def bunnyEars(bunnies):                 O(1) simple attribution
      if bunnies == 0:                      O(1) simple check
        return 0                            O(1) simple print

      return 2 + bunnyEars(bunnies-1)       guess: O(n^2) because while bunnies-1 is less than bunnies, it's not bunnies//2 (log)
                                            the final output is just input * 2, but beyond 1000 input the memory breaks
                                            seems to be between nlogn and n^2...
                                            but for very large numbers that may be too slow a decrease to associate with log

                                            (n-1^2 ?)

                                            total:
                                            O(n^2)


'''


## Exercise II

avg. time complexity of O(log n)
basically the same as binary search, which has an average time
complexity of O(log n)
because each iteration searches .5 (half) the previous slice of n,
so increasing N only somewhat increases runtime (less that proportional to n).


see working binary search with instructional printout made by me here:
https://colab.research.google.com/drive/1CxahSeHcwrAuG1c51wQ2ks3s_dhfw4BD

similar to binary search
but you are looking for a threshold between two states
rather than a single value match.

# 0 check for solution:
check: if egg breaks && floor_range is zero
then solution is current value

if egg no_breaks && floor_range is zero
then solution is current_floor+1

# 1. half the list (building stories):
start in the middle of the list
location_observed = "middle floor" (of given range)

# 2. check the state: break or not_break

# 3. if search_target is higher (if the egg doesn't break)
shift the search frame: so that your current search becomes the
new bottom (so the next middle will be half way to the top)
e.g. from .5 to .75

# 4. if search_target is lower (if the egg does break),
shift the search frame: so that your current search becomes the
new bottom (so the next middle will be half way to the top)
e.g. from .5 to .25

# 5. repeat (goes back to top of while loop)
continue looking until the the search target matches the location observed
in the target sorted list
