screen_positions = {
    'range_percent': {
        5: {
            0: (1881, 72, 100, 16),
            1: (2014, 72, 100, 16),
            2: (2144, 72, 100, 16),
            3: (2277, 72, 100, 16),
            4: (2407, 72, 100, 16)
        },

        4: {
            0: (1881, 72, 100, 16),
            1: (2044, 72, 100, 16),
            2: (2209, 72, 100, 16),
            3: (2375, 72, 100, 16)
        }
    },

    'responses': {
        0: (41, 1444),
        1: (111, 1444),
        2: (173, 1444),
        3: (234, 1444),
        4: (292, 1444),
        5: (350, 1444)
    },

    'load_sim': (903, 101),
    'load_one_street': (1300, 1086)
}

sims = {
    'sb_bn_3bp': {
        'type': 'HU 3bp',
        'run_time': '8in reset at 4in',
        'saved_runs_dir': 'C:\\Users\\sted9\\Desktop\\MonkerSolver\\savedRuns\\3bp_sb_bn_0',
        'saved_tree': 'C:\\Users\\sted9\\Desktop\\MonkerSolver\\trees\\3bp_25_50_75_100.tree',
        'save_screenshots': './screenshots',
        'flops': ['Ks7s6d', 'Ks7s2d', 'Ks7d6c', 'QsJs6c', 'Qs7s2d'],
        'stacks': 177,
        'pot_size': 48,
        'tree_structure': [
            ['25,50,75,100;50,100', 'Flop'],
            ['40,100;100', 'Turn and River']
        ],
        'steps': [
            {
                'title': 'OP (first acton)',
                'setup': None,
                'captures': ['check', '25', '50', '75', '100'],
                'ss_prefix': 'sb_0',
                'trim': True
            },
            {
                'title': 'IP vs Check',
                'setup': [('response', 1)],
                'captures': ['check', '25', '50', '75', '100'],
                'ss_prefix': 'bn_0',
                'trim': True
            },
            {
                'title': 'IP vs 25',
                'setup': [('response', 0), ('response', 2)],
                'captures': ['fold', 'call', '40', '100'],
                'ss_prefix': 'bn_1',
                'trim': False
            },
            {
                'title': 'IP vs 50',
                'setup': [('response', 0), ('response', 3)],
                'captures': ['fold', 'call', '40', '100'],
                'ss_prefix': 'bn_2',
                'trim': False
            },
            {
                'title': 'IP vs 75',
                'setup': [('response', 0), ('response', 4)],
                'captures': ['fold', 'call', '40', '100'],
                'ss_prefix': 'bn_3',
                'trim': False
            },
            {
                'title': 'IP vs 100',
                'setup': [('response', 0), ('response', 5)],
                'captures': ['fold', 'call', '40', '100'],
                'ss_prefix': 'bn_4',
                'trim': False
            }
        ]
    }
}
