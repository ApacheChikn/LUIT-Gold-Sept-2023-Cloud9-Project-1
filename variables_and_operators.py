'''
FULL DISCLOSURE:
I copied this answer from the lesson: Python PCEP Become Certified Entry-Level Python Programmer.
I could have retyped what was in the LUIT video: LUIT Recorded Coaching Calls - Self Paced (Section 4: Python, Session 2)
but I couldn't see all the tiny print on the screen.
'''

income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
 
print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 'income tax in Ripoffland. You would save', income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')
