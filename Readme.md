There are 4 mini-challenges from CodeOp:

- Assemble furniture
- Proper Burguer
- Potatoes (Patatas bravas)
- Longest run



Description of all challenges:

>> Assemble furniture <<

"""In this challenge, you will write a maximumGuests function that receives two arguments. The first argument is the number of wooden boards, and the second argument is the number of wooden legs.
The arguments represent the pieces we can use to assemble dining tables and chairs.

For example, if we have four wooden boards and ten wooden legs, the function could be invoked like:

maximumGuests(4, 10)
Your function should return the number of people that will be able to sit around the tables, once the furniture is assembled.
For someone to be able to sit around a table, there has to be a chair for them to sit on, and a space in the table for them to sit in front of. Here's what you need to know about the furniture:
To assemble a table, you will need four wooden boards and four wooden legs. Each table is big enough to seat four people around them.
To assemble a chair, you will need one wooden board and three wooden legs. Each chair can sit one person, provided there's space for them in a table."""



>> Proper burguer <<

"""In this challenge, you will write a isProperBurger function that receives a list (array) as an argument. Each element of the list is a string containing the name of an ingredient. Together, the list represents the whole stack of ingredients in the burger, ordered from bottom to top -- in the order you'd put them on the plate.

For example, for a simple cheese burger, your function could be invoked like:

isProperBurger(
  ["bread", "patty", "cheese", "bread"])
Your function should return a boolean (true or false) that represents whether the burger is properly made. Here's all you need to know about the art of making proper burgers:

A burger always starts and ends with "bread". There should not be bread anywhere else in the burger.
There has to be at least one "patty" in between the two pieces of bread. If there's no patty, then it's not a burger, it's just a pile of bread.
There cannot be "cheese" under the patties. Cheese always goes on top (that is, on the list, it must appear after the patties)
Our burgers really are simple -- you can be assured that every element in the list of ingredients will be one of the ingredients mentioned above."""



>> Potatoes (Patatas bravas) <<

"""In this challenge, you will write a makeBravas function that receives a list (array) as an argument. Each element of the list is a string containing the word "small", "medium" or "large", representing a potato of that size.

For example, if there is one large potato, one small potato and two medium potatoes, your function could be invoked like:

makeBravas(
  ["medium", "large", "small", "medium"])
Your function should return the amount of complete portions of patatas bravas that can be made with the given potatoes. Here's all you need to know about making bravas, the "secret recipe", if you will:

A small potato can only be chopped into four potato chips.
A medium potato can be chopped into eight potato chips.
A large potato can be chopped into twenty-four potato chips!
To make a portion of patatas bravas, you need twenty potato chips.
Any potato chips that remain after the complete portions are made are discarded. For example, given one large potato, your function should return exactly one (1), as you can only make one portion."""



>> Longest run <<

"""In this challenge, you will write a longestRun function that receives a list (array) as an argument. Each element in the list is a string containing a color. The list represents the colors of the different cars you see running down the road.

For example, if you see a red car, then two blue cars and then a yellow car, your function would be invoked like:

longestRun(["red", "blue", "blue", "yellow"])
Your function should return the name of the color that has the longest run. That is, the color that appears the most times in a row, next to itself, without other colors in between.

For example, if you see two blue cars, then four red cars, and then three blue cars, the red cars are the ones that had the longest run, as there was a run of four red cars. Even if there were more blue cars in total, the blue cars appeared in two shorter runs.

You can assume that the list will not be empty, and that a single color appears the most times in a row."""