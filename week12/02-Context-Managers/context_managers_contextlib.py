from contextlib import contextmanager

@contextmanager
def welcome_message(name):
    print("Hello, {} ".format(name))
    yield
    print("Bye, {}".format(name))

with welcome_message("Rosi"):
    print("Hiiii")



@contextmanager
def working_with_file(filename):
    fn = open(filename)
    yield fn
    fn.close()

with working_with_file('some_file.txt') as f:
    print(f.read())



@contextmanager
def make_context():
    print('entering')
    try:
        yield "Yielding......."
    except RuntimeError as err:
        print('ERROR: {0}'.format(err))
    finally:
        print('exiting')

with make_context() as value:
    print('inside with statement: {}'.format(value))
