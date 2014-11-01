mypairs
========================================

- fork of https://pypi.python.org/pypi/AllPairs
- python3 support


Demo of the basic functionality - just getting pairwise/n-wise combinations

::

    from mypairs import all_pairs2 as all_pairs

    # sample parameters are is taken from 
    # http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


    parameters = [ [ "Brand X", "Brand Y" ]
                 , [ "98", "NT", "2000", "XP"]
                 , [ "Internal", "Modem" ]
                 , [ "Salaried", "Hourly", "Part-Time", "Contr." ]
                 , [ 6, 10, 15, 30, 60 ]
                 ]

    pairwise = all_pairs( parameters )

    print("PAIRWISE:")
    for i, v in enumerate(pairwise):
        print("%i:\t%s" % (i, str(v)))

output

::

    PAIRWISE:
    0:	['Brand X', '98', 'Internal', 'Salaried', 6]
    1:	['Brand Y', 'NT', 'Modem', 'Hourly', 6]
    2:	['Brand Y', '2000', 'Internal', 'Part-Time', 10]
    3:	['Brand X', 'XP', 'Modem', 'Contr.', 10]
    4:	['Brand X', '2000', 'Modem', 'Part-Time', 15]
    5:	['Brand Y', 'XP', 'Internal', 'Hourly', 15]
    6:	['Brand Y', '98', 'Modem', 'Salaried', 30]
    7:	['Brand X', 'NT', 'Internal', 'Contr.', 30]
    8:	['Brand X', '98', 'Internal', 'Hourly', 60]
    9:	['Brand Y', '2000', 'Modem', 'Contr.', 60]
    10:	['Brand Y', 'NT', 'Modem', 'Salaried', 60]
    11:	['Brand Y', 'XP', 'Modem', 'Part-Time', 60]
    12:	['Brand Y', '2000', 'Modem', 'Hourly', 30]
    13:	['Brand Y', '98', 'Modem', 'Contr.', 15]
    14:	['Brand Y', 'XP', 'Modem', 'Salaried', 15]
    15:	['Brand Y', 'NT', 'Modem', 'Part-Time', 15]
    16:	['Brand Y', 'XP', 'Modem', 'Part-Time', 30]
    17:	['Brand Y', '98', 'Modem', 'Part-Time', 6]
    18:	['Brand Y', '2000', 'Modem', 'Salaried', 6]
    19:	['Brand Y', '98', 'Modem', 'Salaried', 10]
    20:	['Brand Y', 'XP', 'Modem', 'Contr.', 6]
    21:	['Brand Y', 'NT', 'Modem', 'Hourly', 10]
