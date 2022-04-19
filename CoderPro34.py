import heapq
from collections import defaultdict

def meeting_rooms(meetings):
    md = defaultdict(list)    # Way less code than Java.        Grab: meetings.sort(key=lambda x: x[0])

    for m in meetings:
        md[m[0]].append(1)
        md[m[1]].append(-1)

    keys = list(md.keys())
    keys.sort()

    (mCur,mMax) = (0,0)
    for k in keys:
        mCur += sum(md[k])
        if mCur>mMax:
            mMax = mCur

    return mMax

# print(meeting_rooms([[20, 30], [10, 21], [0, 50]]))
print(meeting_rooms([[20, 30], [20, 21], [0, 50]]))
