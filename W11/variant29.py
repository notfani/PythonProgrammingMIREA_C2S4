from contextlib import suppress


class FSMException(Exception):
    pass


class FSM:
    def __init__(self):
        self.state = 'C4'
        self.outputs = {
            'C0': 'y0',
            'C1': 'y3',
            'C2': 'y1',
            'C3': 'y1',
            'C4': 'y4',
            'C5': 'y2',
        }
        self.transitions = {
            'C4': {'hop': self._to_C0},
            'C0': {'crawl': self._to_C5, 'drag': self._to_C1},
            'C1': {'drag': self._stay_C1, 'crawl': self._to_C2},
            'C2': {'glare': self._to_C3},
            'C5': {'hop': self._hop_from_C5},
        }
        self.vars = {}

    def _to_C0(self):
        self.state = 'C0'

    def _to_C1(self):
        self.state = 'C1'

    def _to_C2(self):
        self.state = 'C2'

    def _to_C3(self):
        self.state = 'C3'

    def _to_C4(self):
        self.state = 'C4'

    def _to_C5(self):
        self.state = 'C5'

    def _stay_C1(self):
        self.state = 'C1'

    def _hop_from_C5(self):
        if 'w' not in self.vars:
            raise FSMException('unsupported')
        if self.vars['w'] == 0:
            self._to_C2()
        elif self.vars['w'] == 1:
            self._to_C1()
        else:
            raise FSMException('unsupported')

    def store_w(self, value):
        self.vars['w'] = value

    def get_output(self):
        return self.outputs[self.state]

    def has_max_out_edges(self):
        all_out_counts = [2, 2, 2, 1, 1, 1]
        max_out = max(all_out_counts)
        current_out = len(self.transitions.get(self.state, {}))
        return current_out == max_out

    def part_of_loop(self):
        loops = {'C0', 'C1', 'C2', 'C5'}
        return self.state in loops

    def __getattr__(self, name):
        if name.startswith('store_'):
            return self._make_store_func(name)
        if self._is_known_transition(name):
            return lambda: self._handle_transition(name)
        raise FSMException('unknown')

    def _make_store_func(self, name):
        var_name = name.split('_', 1)[1]

        def store_func(value):
            self.vars[var_name] = value

        return store_func

    def _is_known_transition(self, name):
        return any(name in transitions for transitions
                   in self.transitions.values())

    def _handle_transition(self, name):
        state_transitions = self.transitions.get(self.state, {})
        if name not in state_transitions:
            raise FSMException('unsupported')
        state_transitions[name]()


def main():
    return FSM()


def check_state(obj, expected_state):
    outputs = {
        'C0': 'y0', 'C1': 'y3', 'C2': 'y1',
        'C3': 'y1', 'C4': 'y4', 'C5': 'y2'
    }
    assert obj.state == expected_state,\
        f"state: expected {expected_state}, got {obj.state}"
    assert obj.get_output() == outputs[expected_state]
    current_out = len(obj.transitions.get(obj.state, {}))
    max_out = max([2, 2, 2, 1, 1, 1])
    assert obj.has_max_out_edges() == (current_out == max_out)
    assert obj.part_of_loop() == (obj.state in {'C0', 'C1', 'C2', 'C5'})


def expect_exception(func, message):
    try:
        func()
        assert False, "Expected FSMException"
    except Exception as e:
        assert str(e) == message,\
            f"Expected message '{message}', got '{str(e)}'"


def test():
    test_initial_state()
    test_transition_hop_to_C0()
    test_crawl_from_C0_to_C5()
    test_hop_from_C5_with_all_w_values()
    test_glare_from_C2_to_C3()
    test_invalid_transition()
    test_store_x_and_check_value()
    test_invalid_w_in_hop_from_C5()
    test_stay_C1_on_drag()
    test_missing_w_raises_exception()
    test_invalid_w_raises_exception()
    test_unknown_method_raises_FSMException()
    test_all_states_get_output()
    test_has_max_out_edges_and_part_of_loop()
    test_nonexistent_transition()
    test_drag_from_C0_to_C1()
    test_store_y()
    test_direct_state_changes()
    test_store_long_var_name()
    test_direct_call_stay_C1()
    test_all_possible_exceptions()


def test_invalid_w_raises_exception():
    obj = main()
    obj.hop()           # C4 -> C0
    obj.crawl()         # C0 -> C5
    obj.store_w(2)      # invalid value for w
    expect_exception(lambda: obj.hop(), 'unsupported')


def test_initial_state():
    obj = main()
    check_state(obj, 'C4')


def test_transition_hop_to_C0():
    obj = main()
    obj.hop()
    check_state(obj, 'C0')


def test_crawl_from_C0_to_C5():
    obj = main()
    obj.hop()
    obj.crawl()
    check_state(obj, 'C5')


def test_hop_from_C5_with_all_w_values():
    obj = main()
    obj.hop()  # C4 -> C0
    obj.crawl()  # C0 -> C5

    # Case 1: w is missing
    expect_exception(lambda: obj.hop(), 'unsupported')

    # Case 2: w = 0
    obj.store_w(0)
    obj.hop()
    check_state(obj, 'C2')

    # Case 3: w = 1
    obj._to_C5()  # Вернуться в C5
    obj.store_w(1)
    obj.hop()
    check_state(obj, 'C1')

    # Case 4: w = invalid value (e.g., 2)
    obj._to_C5()  # Вернуться в C5
    obj.store_w(2)
    expect_exception(lambda: obj.hop(), 'unsupported')


def test_glare_from_C2_to_C3():
    obj = main()
    obj.hop()
    obj.crawl()
    obj.store_w(0)
    obj.hop()
    obj.glare()
    check_state(obj, 'C3')


def test_direct_call_stay_C1():
    obj = main()
    obj._to_C1()
    obj._stay_C1()
    check_state(obj, 'C1')


def test_invalid_transition():
    obj = main()
    obj.hop()
    obj.crawl()
    obj.store_w(0)
    obj.hop()
    expect_exception(lambda: obj.drag(), 'unsupported')


def test_store_x_and_check_value():
    obj = main()
    obj._to_C4()
    obj.store_x(10)
    assert obj.vars['x'] == 10


def test_invalid_w_in_hop_from_C5():
    obj = main()
    obj.hop()
    obj.crawl()
    obj.store_w(2)
    expect_exception(lambda: obj.hop(), 'unsupported')


def test_stay_C1_on_drag():
    obj = main()
    obj.hop()
    obj.drag()
    check_state(obj, 'C1')
    obj.drag()
    check_state(obj, 'C1')  # stay_C1


def test_missing_w_raises_exception():
    obj = main()
    obj.hop()
    obj.crawl()
    expect_exception(lambda: obj.hop(), 'unsupported')


def test_unknown_method_raises_FSMException():
    obj = main()
    expect_exception(lambda: getattr(obj, 'stare')(), 'unknown')


def test_all_states_get_output():
    obj = main()
    for state in ['C0', 'C1', 'C2', 'C3', 'C4', 'C5']:
        obj.state = state
        out = obj.get_output()
        assert out in ('y0', 'y1', 'y2', 'y3', 'y4')


def test_has_max_out_edges_and_part_of_loop():
    obj = main()
    for state in ['C0', 'C1', 'C2', 'C3', 'C4', 'C5']:
        obj.state = state
        assert obj.has_max_out_edges() == (state in {'C0', 'C1'})
        assert obj.part_of_loop() == (state in {'C0', 'C1', 'C2', 'C5'})


def test_nonexistent_transition():
    obj = main()
    obj.hop()
    obj.crawl()
    obj.store_w(1)
    obj.hop()
    obj.crawl()
    obj.glare()
    check_state(obj, 'C3')
    expect_exception(lambda: obj.stare(), 'unknown')


def test_drag_from_C0_to_C1():
    obj = main()
    obj.hop()
    obj.drag()
    check_state(obj, 'C1')


def test_store_y():
    obj = main()
    obj._to_C1()
    obj.drag()
    check_state(obj, 'C1')
    obj.store_y(99)
    assert obj.vars['y'] == 99


def test_direct_state_changes():
    obj = main()
    for state in ['C0', 'C1', 'C2', 'C3', 'C4', 'C5']:
        setattr(obj, f"_to_{state[1:]}", lambda: None)  # Примерный шаблон
        obj.state = state
        assert obj.state == state


def test_store_long_var_name():
    obj = main()
    obj.store_some_long_var_name(42)
    assert obj.vars['some_long_var_name'] == 42


def test_all_possible_exceptions():
    obj = main()

    # Test unsupported method in current state
    obj.hop()  # C4 -> C0
    # В C0 метод 'glare' не определён
    expect_exception(lambda: obj.glare(), 'unsupported')

    # Test unknown method
    expect_exception(lambda: getattr(obj, 'stare')(), 'unknown')

    # Test missing variable 'w' in C5
    obj._to_C5()  # Перейти в C5 без вызова hop()
    expect_exception(lambda: obj.hop(), 'unsupported')  # w не задан

    # Test invalid value for 'w'
    obj.store_w(2)
    expect_exception(lambda: obj.hop(), 'unsupported')
