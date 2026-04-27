import pandas as pd
import numpy as np
import random
import argparse
import sys

#parsing user given constants
parser = argparse.ArgumentParser(description='Information about length of region and sample size')
parser.add_argument('-pedigrees', dest = 'pedigrees', action='store', nargs = 1, type = str, help = 'path to pedigree file')
parser.add_argument('-outFile', dest = 'outFile', action='store', nargs = 1, type = str, help = 'path to store output files')
parser.add_argument('-samples', dest = 'samples', action='store', nargs = 1, type = int, help = 'no. of samples required')

args = parser.parse_args()
samples = args.samples[0]
pedigrees = args.pedigrees[0]
outFile = args.outFile[0]

df = pd.read_csv(pedigrees, sep='\t', names=['id', 'pedigreeID', 'parent1', 'parent2', 'sex'])
#Separate males and females
df1 = df[df.sex=="F"].copy()
df2 = df[df.sex=="M"].copy()

#Check if sample is chimeric by identifying duplicates (ie same parents non-identical twins)
m1 = df1.duplicated(['parent1','parent2'], keep=False)
#Assign chimeric status and then remove duplicates (ie keep just one twin for lists of parent IDs)
df1['chimerism'] = np.select([m1],[1], default=0)
tdf = df1[df1.chimerism==1].drop_duplicates(['parent1', 'parent2'])
p1 = list(tdf['parent1'])
p2 = list(tdf['parent2'])
#Randomly sample
lst = random.sample(range(0, len(p1)-1), samples)
l1 = [p1[i] for i in lst]
l2 = [p2[i] for i in lst]
#Create df of sampled parent IDs
u = pd.DataFrame({"parent1":l1,"parent2":l2})
#Merge with df of all individuals of that sex, leaving just sampling twins
fdf = df1.merge(u)

#Repeat for males
#Check if sample is chimeric by identifying duplicates (ie same parents non-identical twins)
m1 = df2.duplicated(['parent1','parent2'], keep=False)
#Assign chimeric status and then remove duplicates (ie keep just one twin for lists of parent IDs)
df2['chimerism'] = np.select([m1],[1], default=0)
tdf = df2[df2.chimerism==1].drop_duplicates(['parent1', 'parent2'])
p1 = list(tdf['parent1'])
p2 = list(tdf['parent2'])
#Randomly sample
lst = random.sample(range(0, len(p1)-1), samples)
l1 = [p1[i] for i in lst]
l2 = [p2[i] for i in lst]
#Create df of sampled parent IDs
u = pd.DataFrame({"parent1":l1,"parent2":l2})
#Merge with df of all individuals of that sex, leaving just sampling twins
mdf = df2.merge(u)

#Combine dfs
rdf = pd.concat([fdf, mdf])

#Output only IDs
rdf[['id']].to_csv(outFile + "_chimeric.txt", header=False, index=False)
