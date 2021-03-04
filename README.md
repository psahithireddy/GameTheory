# PSNE, Dominant Strategies
Run

 - python3 13.py


## About
Given a n-Player Game the code lists all Pure Strategy Nash Equilibria and  all Very Weakly Dominant Strategies for each player.

## Input Format
The input is a n-Player Game with the payoffs listed in the NFG Format (as described in the [Gambit Project](http://www.gambit-project.org/)).
   - First line contains the number of players n.
   - The second line contains n space-separated numbers, the i th number corresponding to the number of strategies available to the i th player. (S <sub>i</sub>)
   - The third line contains the list of payoffs in the NFG Format.

## Output Format
 - First line should contain the number of PSNE. (n psne )
 - Followed by n psne lines, the i th line containing n space-separated numbers corresponding to the equilibrium strategies for each player respectively.
 - Next, you should output n lines, with the i th line listing the number of very weakly dominant strategies for the i th player followed by the dominant strategies.

## Sample
### Input 1
2<br></br>
2 2<br></br>
-2 -2 -2 -10 -10 -2 -5 -5

### Output 1
2 <br></br>
1 1<br></br>
2 2<br></br>
1 2<br></br>
1 2  
