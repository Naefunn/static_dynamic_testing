### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # needs double equals. Single equals is assignment operator, not equality.
    if card.value = 1:
      return True
    # missing colon after else.
    else
      return False
   
  # incorrect spelling of def, not dif. No comma between function parameters card1 and card2 in the highest_card functiion.
  dif highest_card(self, card1 card2):
  # no indentation of the if statement.
  if card1.value > card2.value:
    #incorrect variable name. Missing the 1 on card1.
    return card
  else:
    return card2
  

# cards_total function not indented withing the class.
def cards_total(self, cards):
  # total variable not assigned to anything. Should be set to 0.
  total
  for card in cards:
    total += card.value
    # return statement not outside the loop so will kill the loop on the first interation.
    # cannot concatonate a string with an integer
    return "You have a total of" + total
  
```
