# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#part1_greet_template

def greet(name, greeting = 'Hello, <name>!') :
    if '<name>' in greeting:
        greeting = greeting.replace('<name>', name)
        print(f'{greeting}')
    return print

print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))
print(greet('Dan', 'How are you <name>?'))

#part2_force
def force (mass, body='earth') :
    gravity = {'sun' : 274,
                'jupiter' : 24.92,
                'neptune' : 11.15,
                'saturn' : 10.44,
                'earth' : 9.798,
                'uranus' : 8.87,
                'venus' : 8.87,
                'mars' : 3.71,
                'mercury' : 3.7,
                'moon' : 1.62,
                'pluto' : 0.58,
                }
    print(mass * round(gravity[body], 1))
    return print

print(force(1,'earth'))

# Part 3: Gravity
def pull(m1, m2 , d):
    G = 6.674  * (10 ** -11)
    print(G*((m1 * m2) / d ** 2))
    return print

print(pull(800, 1500, 3))