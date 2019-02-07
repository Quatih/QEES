
import pandas as pd
import numpy as np
from sys import exit
import os
import sys
from parse_trace import parse

if __name__== "__main__":
  df = parse(str(sys.argv[1]))
  df.to_csv("out.csv")
  a = df[['time', 'B.load']]
  a.drop_duplicates(subset = 'time',keep='last').to_csv("kibam.csv",header=False, index=False)
  
  start_times = [5367, 11204, 16951, 22674, 28430, 34307, 40374, 46421, 52289, 58049, 63772, 69513, 75349, 81376, 87459, 93369, 99149, 104876, 110608, 116414, 122392, 128487, 134437, 140238, 145971, 151696, 157475, 163402, 169496, 175495, 181325, 187070, 192792, 198552, 204435, 210504, 216541, 222402,
  2707, 8521, 14261, 19986, 25756, 31664, 37749, 43768, 49614, 55366, 61090, 66845, 72711, 78765, 84817, 90695, 96462, 102187, 107928, 113757, 119768, 125851, 131771, 137558, 143288, 149021, 154821, 160786, 166875, 172835, 178644, 184381, 190108, 195884, 201800, 207883, 213889, 219727, 225477,
  6837, 23916, 29751, 60592, 65340, 66202, 70973, 71954, 77737, 83484, 89215, 95054, 106372, 112047, 148622, 153366, 154327, 159207, 160108, 165873, 171604, 177362, 194425, 200321,
  60917, 66429, 72087, 77787, 83507, 89317, 148887, 154504, 160190, 165900, 171645]
  stop_times = [10937, 16774, 22521, 28244, 34000, 39877, 45944, 51991, 57859, 63619, 69342, 75083, 80919, 86946, 93029, 98939, 104719, 110446, 116178, 121984, 127962, 134057, 140007, 145808, 151541, 157266, 163045, 168972, 175066, 181065, 186895, 192640, 198362, 204122, 210005, 216074, 222111, 227972,
  8277, 14091, 19831, 25556, 31326, 37234, 43319, 49338, 55184, 60936, 66660, 72415, 78281, 84335, 90387, 96265, 102032, 107757, 113498, 119327, 125338, 131421, 137341, 143128, 148858, 154591, 160391, 166356, 172445, 178405, 184214, 189951, 195678, 201454, 207370, 213453, 219459, 225297, 231047,
  7354, 24504, 30099, 61025, 65751, 66803, 71549, 72532, 78291, 84075, 89800, 95322, 106842, 112605, 149188, 153954, 154924, 159559, 160664, 166444, 172208, 177852, 195021, 200556,
  61141, 66947, 72667, 78366, 84023, 89530, 149330, 155067, 160775, 166457, 172058]
  jobs = ['Jb0','Jb1','Jb2','Jb3']
  emptydict = {
    'Start time (s)' :[], 
    'Stop time (s)' : [],
    'Duration (s)' : [],
    'Scheduled' : []
  }
  ind = df[["offsets["+str(x)+"]" for x in range(len(jobs))]] 
  of = [pd.DataFrame(emptydict) for x in jobs]
  for i in range(len(jobs)):
    states = df[jobs[i]]
    for j in range(len(states)):
      if "Schedule" in states[j]:
        index = ind.loc[j][i]
        add = {
            'Start time (s)' : [start_times[index]],
            'Stop time (s)' : [stop_times[index]],
            'Duration (s)' : [stop_times[index]-start_times[index]],
            'Scheduled' : ['Y']
          }
        addf = pd.DataFrame(add)
        of[i] = of[i].append(addf,ignore_index=True)
      elif "Skip" in states[j]:
        index = ind.loc[j][i]
        add = {
            'Start time (s)' : [start_times[index]], 
            'Stop time (s)' : [stop_times[index]],
            'Duration (s)' : [stop_times[index]-start_times[index]],
            'Scheduled' : ['N']
          }
        addf = pd.DataFrame(add)
        of[i] = of[i].append(addf,ignore_index=True)
  for i in range(len(of)):
    lis = [x for x in range(1, len(of[i])+1)]
    AccDict = {
      'Access' : lis
    }
    of[i].iloc[:,0:3] = of[i].iloc[:,0:3].astype(int)
    outp = pd.concat([pd.DataFrame(AccDict),of[i]],sort =False,axis=1)
    outp.to_csv(jobs[i] + ".csv",index=False)