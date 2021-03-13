# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer0 = 'Ruud Gullit'
scorer1 = 'Marco van Basten'
goal0 = 32
goal1 = 54
scorers = 'Ruud Gullit' + '32',  'Marco van Basten' + '54'
report = f'{scorer0} scored in the {goal0}nd minute' + f'\n{scorer1} scored in the {goal1}th minute'
player = 'Ruud Gullit'
first_name =  player[0:4]
last_name_len = len(player[5:11])
name_short = player[0] + '. ' + player [5:11]
chant = (first_name + '!')
good_chant = (first_name + '!') != chant
print(good_chant)
