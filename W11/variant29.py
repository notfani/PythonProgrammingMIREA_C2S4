class FSMException(Exception):
    pass


class FSM:
    _outputs = {
        'c0': 'y0',
        'c1': 'y3',
        'c2': 'y1',
        'c3': 'y1',
        'c4': 'y4',
        'c5': 'y2',
    }

    _transitions = {
        'c4': {'hop': 'c0'},
        'c0': {'crawl': 'c5', 'drag': 'c1'},
        'c5': {'hop': lambda self: 'c2' if self.w == 0 else 'c1'},
        'c1': {'drag': 'c1', 'cast': 'c4', 'crawl': 'c2'},
        'c2': {'glare': 'c3'},
        'c3': {},
    }

    _out_edges = {k: len(v) for k, v in _transitions.items()}
    _loop_states = {'c4', 'c0', 'c5', 'c1'}

    def __init__(self):
        self.state = 'c4'
        self.w = 0

    def store_w(self, value):
        self.w = value

    def _transition(self, action):
        if self.state not in self._transitions:
            raise FSMException('unsupported')
        transitions = self._transitions[self.state]
        if action not in transitions:
            raise FSMException('unsupported')
        target = transitions[action]
        self.state = target(self) if callable(target) else target

    def hop(self):
        self._transition('hop')

    def crawl(self):
        self._transition('crawl')

    def drag(self):
        self._transition('drag')

    def cast(self):
        self._transition('cast')

    def glare(self):
        self._transition('glare')

    def get_output(self):
        return self._outputs[self.state]

    def has_max_out_edges(self):
        return (self._out_edges[self.state] ==
                max(self._out_edges.values()))

    def part_of_loop(self):
        return self.state in self._loop_states

    def __getattr__(self, name):
        raise FSMException('unknown')


def main():
    return FSM()


def test():
    fsm = main()
    assert isinstance(fsm, FSM)
    assert fsm.state == 'c4'
    assert fsm.get_output() == 'y4'
    assert fsm.part_of_loop()
    assert not fsm.has_max_out_edges()

    fsm.hop()
    assert fsm.state == 'c0'
    assert fsm.get_output() == 'y0'
    assert fsm.part_of_loop()
    assert not fsm.has_max_out_edges()

    try:
        fsm.hop()
    except FSMException as e:
        assert str(e) == 'unsupported'

    fsm.drag()
    assert fsm.state == 'c1'
    assert fsm.get_output() == 'y3'
    assert fsm.part_of_loop()
    assert fsm.has_max_out_edges()

    try:
        fsm.hop()
    except FSMException as e:
        assert str(e) == 'unsupported'

    fsm.crawl()
    assert fsm.state == 'c2'
    assert fsm.get_output() == 'y1'
    assert not fsm.part_of_loop()
    assert not fsm.has_max_out_edges()

    try:
        fsm.drive()
    except FSMException as e:
        assert str(e) == 'unknown'

    fsm.glare()
    assert fsm.state == 'c3'
    assert fsm.get_output() == 'y1'
    assert not fsm.part_of_loop()
    assert not fsm.has_max_out_edges()

    test_unknown_methods()
    test_invalid_transitions()
    test_invalid_state_raises()


def test_unknown_methods():
    fsm = FSM()
    unknown_methods = ['stare', 'drive', 'jump', 'fly']
    for method in unknown_methods:
        try:
            getattr(fsm, method)()
        except FSMException as e:
            assert str(e) == 'unknown'


def test_invalid_transitions():
    cases = [
        ('c4', 'crawl'),
        ('c4', 'drag'),
        ('c0', 'hop'),
        ('c0', 'cast'),
        ('c0', 'glare'),
        ('c1', 'hop'),
        ('c1', 'glare'),
        ('c2', 'hop'),
        ('c2', 'cast'),
        ('c2', 'drag'),
        ('c3', 'hop'),
        ('c3', 'crawl'),
        ('c3', 'cast'),
        ('c3', 'drag'),
        ('c3', 'glare'),
    ]

    for state, method in cases:
        fsm = prepare_fsm_to_state(state)
        try:
            getattr(fsm, method)()
        except FSMException as e:
            assert str(e) == 'unsupported'


def prepare_fsm_to_state(state):
    fsm = FSM()
    if state == 'c0':
        fsm.hop()
    elif state == 'c1':
        fsm.hop()
        fsm.drag()
    elif state == 'c2':
        fsm.hop()
        fsm.crawl()
        fsm.store_w(0)
        fsm.hop()
    elif state == 'c3':
        fsm.hop()
        fsm.crawl()
        fsm.store_w(0)
        fsm.hop()
        fsm.glare()
    return fsm


def test_invalid_state_raises():
    fsm = FSM()
    fsm.state = 'invalid'
    try:
        fsm.hop()
    except FSMException as e:
        assert str(e) == 'unsupported'
