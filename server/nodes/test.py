from state import State


def test(state: State) -> State:
    state['messages'] = "Hey" + state['messages']

    return state
