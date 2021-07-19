from input_module import take_input
from process_module import process
from output_module import output
from greetings_module import greet_user

greet_user()

while True:
    i = take_input()
    o = process(i)
    output(o)
