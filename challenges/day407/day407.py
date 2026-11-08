'''
Initialize my name:

Some people just have a first name; some people have first and last names and some people have first, middle and last names.

You task is to initialize the middle names (if there is any).

Examples
'Jack Ryan'                   => 'Jack Ryan'
'Lois Mary Lane'              => 'Lois M. Lane'
'Dimitri'                     => 'Dimitri'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis'
'''
def initialize_names(name):
    return ' '.join([n if i ==1 or i == len(name.split()) else f'{n[0]}.' for i, n in enumerate(name.split(), 1)])
# old
#def initialize_names(name):
#    return ' '.join([n for n in name.split()]) if len(name.split()) < 3 else ' '.join([name.split()[0]+ ' ' + ' '.join([f'{n[0]}.' for n in name.split()[1:-1]]) + ' ' + name.split()[-1]])