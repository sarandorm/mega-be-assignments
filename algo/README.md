# Algorithm part

## How to run the project

Simply run the file ` solve.py ` and then type list of word with comma as a seperator. Finally, type in targeted word. The result will be printed via terminal

```
python solve.py
Enter list of word : ab,bc,cd
Enter target word : abcd
('ab', 'cd')
```

## Time and space complexity analysis

In the function, on the 3rd line, you can see that it is a set creation. Set creation time and space complexity is at O(n). In the 4th line, there is a for loop. which time complexity is O(n). Now, within the loop. There is a set lookup, which cost O(1).

Outside the loop is O(n) and the loop part is O(n). Resulting in O(2n), which is O(n). So does the space complexity, we have list of n element and set of n element. Resulting in O(2n), which is O(n)