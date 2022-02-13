def getHint(secret: str, guess: str) -> str:
  bulls = 0
  bucket = [0] * 10 #create a bucket with 10 places with 0. Use 10, since the highest digit is 9 (0-9). This bucket will represent each number by it's index and we will add and remove values for each match.
  
  for s, g in zip(secret, guess): #use zip function for parallel iteration.
    if s == g: #check if the number in the secret is equal to the number in the guess.
        bulls += 1
    else: #if not, add 1 on the index of s and remove 1 in the index of g. That way we will be able to count the bulls and cows.
        bucket[int(s)] += 1
        bucket[int(g)] -= 1

  if bulls == len(secret):
    print(f'You guessed the correct secret!')
  else:
    print(f'{bulls} Bulls and {len(secret) - bulls - sum(x for x in bucket if x > 0)} Cows.')

getHint('4518', '3524')