from copy import copy, deepcopy


def memento(obj: object, deep: object = True):
    """Memento Design Pattern
    Remembers the current state of an object and can be called to reset the object to that state.
    :param obj: Object to remember the state of.
    :param deep: Deep copy (for immutable variables).
    :return: Callable that can be called to reset the object to the saved state.
    """
    # copy the current state
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        """Restore the previously saved state"""
        obj.__dict__.clear()
        obj.__dict__.update(state)

    # return function to restore the object to the copied state
    return restore


class Memento:
    """Memento Design Pattern"""
    _state = None

    def save_current_state(self):
        # Create a memento of the current state
        self._state = memento(self, True)

    def reset(self):
        # Reset the object to the saved state
        # todo: support multiple states
        self._state()
