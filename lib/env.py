import gflags

FLAGS = gflags.FLAGS

gflags.DEFINE_enum('env', None,
                   ['local', 'prod', 'qa', 'dev'],
                   'Zhibogame environment to use',
                   short_name='e')