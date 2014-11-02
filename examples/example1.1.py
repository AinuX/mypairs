from mypairs import AllPairs

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""


# sample parameters are is taken from 
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [ [ "Brand X", "Brand Y" ]
             , [ "98", "NT", "2000", "XP"]
             , [ "Internal", "Modem" ]
             , [ "Salaried", "Hourly", "Part-Time", "Contr." ]
             , [ 6, 10, 15, 30, 60 ]
             ]

pairwise = AllPairs( parameters )

print("PAIRWISE:")
for i, v in enumerate(pairwise):
    print("%i:\t%s" % (i, str(v)))
