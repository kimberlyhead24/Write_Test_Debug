class Solution:
  def romanVal(self, string: str) -> int:
    roman_table = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }

    total = 0
    prev_val = 0
    for character in reversed(string):
      val = roman_table[character]
      if val < prev_val:
        total -= val
      else:
        total += val
      prev_val = val
    return total

if __name__ == "__main__":
  sol = Solution()
  tests = [
    ("III", 3),
    ("IV", 4),
    ("XIV", 14),
    ("XXIX", 29),
    ("LX", 60),
    ("XCIX", 99),
    ("DCCC", 800),
    ("CMXCIX", 999),
    ("MCMXCIX", 1999),
    ("MIV", 1004),
  ]
  results = {}
  for string, expected in tests:
    result = sol.romanVal(string)
    results[string] = {"status": "PASS" if result == expected else "FAIL", "expected": expected, "result": result, }
  for test, info in results.items(): 
    print(f"{test}: {info['status']} | expected={info['expected']} | got={info['result']}")
  
    
                   
