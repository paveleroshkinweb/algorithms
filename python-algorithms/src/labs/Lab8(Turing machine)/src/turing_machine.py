def turing_machine(tape, state_table, initial_state):
    i = 0
    while True:
        current_element = tape[i]
        