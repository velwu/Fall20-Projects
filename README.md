# Fantastic Chess Variants and How to Play Them
A student final project for the Fall 2020 semester of Data Structure & Algorithm at iSchool, UIUC

(yes, the title is a reference to [this other fantastic thing](https://harrypotter.fandom.com/wiki/Fantastic_Beasts_and_Where_to_Find_Them_(film)), in case you've noticed. I am a proud Rowling fanboy~)


## What is this project and why is it important??

As a cornerstone for myself to build a Python chess AI (probably as an extra-curricular personal project) sometime in the future, this project involves analyses of many existing games in the [Minichess family](https://en.wikipedia.org/wiki/Minichess), including writing my own Minimax AI to play them.

Instead of relying on any mainstream chess libraries out there, **all chess pieces movement mechanisms are written in Python in their originality by myself**. This is an important element to demonstrate my own data structuring capabilities.

## What the current program covers:

- 1. 3x3 Boards 
  - Chess variants on a 3×3 board are not clearly defined, so it is not written in stone what pieces are involved or where they each start. These are largely solved games, however, so provide a good place to conduct simpler and quicker analyses.
  - This part will also likely involve some variants I created out of thin air because magic (alright, it's done on my laptop, but you get it).
 
- 2. 3x? Boards 
  - I came up with these variants, bending the rules a little. The victory is earned not by taking the opponent's King, but by eliminating all his/her pieces.
  
  - **The House of Commoners**: 
    - A 3x4 or 3x5 board with only non-royal pieces are present.
    
  ![Snapshot Image 5](https://github.com/velwu/Fall20-Projects/blob/main/3x4%20THoC.PNG)
    
  - **Queen's Gauntlet**: 
    - A 3x5 board with both players' Queens and their Knights in position to deliver cross shots against the Kings.
    
  ![Snapshot Image 4](https://github.com/velwu/Fall20-Projects/blob/main/3x5%20QueensGlt.PNG)
 
- 3. 4x? Boards
  - **Silverman 4x5**
    - While Silverman 4x4 is known to be solved in favor of White player, Silverman recently proposed a 4x5 that is more playable.
    
  ![Snapshot Image 0](https://github.com/velwu/Fall20-Projects/blob/main/Silverman%204x5.PNG)
  
  - **Alternate Thai**
    - Inspired by Thai Chess, also called [Makruk](https://en.wikipedia.org/wiki/Makruk)
    
  ![Snapshot Image Thai](https://github.com/velwu/Fall20-Projects/blob/main/4x8%20AltThai.PNG)
  
    
- 4. 5x5 Boards
  - The only variant that is solved in this family is the Gardner minichess (with White player having an obvious advantage). This project will attempt to prove it mathematically and demonstrate it programmatically, while also analyzing the following variants:
    - **Jacobs–Meirovitz**
    - **Mallett**
    
Because Gardner is a solved and is an unbalanced (potentially unfun) game, the inclusion of the other two is important in making this project valuable.
For now, 3x4 customized boards and Silverman 4x5 (as screenshot below describes) are the main targets of analysis, while the Jacobs–Meirovitz variant is the ultimate goal of this analysis as I find it the most balanced and fun among the 3. It is also, unlike Gardner's, an unsolved game. Mallet is also unsolved though it is argued by some to be unbalanced, thanks to the Bishop/Knight exclusivity on both sides.

![Snapshot Image 1](https://github.com/velwu/Fall20-Projects/blob/main/5x5%20Gardner%20variant.PNG)
![Snapshot Image 2](https://github.com/velwu/Fall20-Projects/blob/main/5x5%20JM%20variant.PNG)
![Snapshot Image 3](https://github.com/velwu/Fall20-Projects/blob/main/5x5%20Mallett%20variant.PNG)


## Gameplay Snapshots:
- 1. THOC 3x4 (match just starting out)

![Snapshot Image game_play1](https://github.com/velwu/Fall20-Projects/blob/main/gameplay_snapshot_THOC_3x4.png)

- 2. THOC 3x5 (match near conclusion)

![Snapshot Image game_play2](https://github.com/velwu/Fall20-Projects/blob/main/gameplay_snapshot_THOC_3x5.png)

- 3. Alt Thai 4x8 (Black player submits, White player wins)

![Snapshot Image game_play3](https://github.com/velwu/Fall20-Projects/blob/main/gameplay_snapshot_Thai_4x8.png)


## Match Results:
- 1. THOC_3x5

![Snapshot Image results1](https://github.com/velwu/Fall20-Projects/blob/main/match_results_THOC_3x5.png)

- 2. Queen's Gauntlet 3x5

![Snapshot Image results2](https://github.com/velwu/Fall20-Projects/blob/main/match_results_QueensGlt_3x5.png)

- 3. Alt Thai 4x8 

![Snapshot Image results2](https://github.com/velwu/Fall20-Projects/blob/main/match_results_AltThai_4x8.png)
