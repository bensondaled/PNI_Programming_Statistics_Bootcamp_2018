## non-normal
A = (45-np.random.gamma(3.4, 3.3, size=200))*19
B = (45-np.random.gamma(3.2, 3.4, size=120))*21

A = A[A>0]
B = B[B>0]

pl.hist(A, bins=60, normed=True)
pl.hist(B, bins=60, normed=True)

np.save('sampleA', A)
np.save('sampleB', B)

## normal

a = np.random.normal(1207, 121, size=200)
b = np.random.normal(1376, 131, size=220)

np.save('sample_a.npy', a)
np.save('sample_b.npy', b)

## sample and population

samp = np.random.normal(30, 30, size=120)
pop = np.random.normal(30, 120, size=10000)

np.save('sample.npy', samp)
np.save('population.npy', pop)

##
