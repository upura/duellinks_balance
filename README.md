Investigation of Randomness of Duellinks skill "Balance"
===
In the update on November 6, 2017, the effect of the skill "balance" was adjusted, and it seems that certain randomness was given. The aim of this investigation is to reveal the randomness by using python script that automatically counts the number of monsters, magic and trap from the screenshot of the initial hand.

# Description
Deck contains 10 monsters, 5 magic and 5 traps (Total 20 cards). Duels are manually repeated and in each deul a screenshot of the initial hand is taken.

By executing "duellinks_balance.py", the number of monster, magic and trap are automatically counted for all images placed in the "img" folder, and the distribution is automatically calculated.

# Method of Image Process
1. Extract area of 4 cards from each image
1. Difine an average of the RGB values in each region as a feature amount
1. Categorize all data into monster, magic and trap by using K-means
1. Calculation and show graph

The process can be seen in the following link.

https://github.com/upura/duellinks_balance/blob/master/demo_duellinks_balance.ipynb

# Japanese Blog
日本語でのブログはこちら/Japanese version blog
https://upura.hatenablog.com/entry/2017/11/10/081635
