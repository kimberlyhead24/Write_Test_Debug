def lengthOfLongestSubstring(self, s: str) -> int:
  last_seen = {}
  start = 0
  best = 0
  for i, letter in enumerate(s):
      if letter in last_seen and last_seen[letter] >= start:
          start = last_seen[letter] + 1
      last_seen[letter]= i
      best = max(best, i - start + 1)
        
  return best
