from lib.config import create_app

import gflags


FLAGS = gflags.FLAGS

gflags.DEFINE_enum('env', None,
                   ['local', 'prod', 'qa', 'dev'],
                   'Zhibogame environment to use',
                   short_name='e')

create_app()


def main(argv, run_func):
    try:
        argv = FLAGS(argv)
    except gflags.FlagsError as e:
        print '\n%s\nUsage: %s ARGS\n%s' % (e, argv[0], FLAGS)
        return 1
    if len(FLAGS(argv)) > 1:
        run_func(argv[1:])
    else:
        run_func()
