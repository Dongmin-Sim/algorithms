from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    play_map = defaultdict(list)
    best_map = defaultdict(int)
    temp = []
    
    for idx, items in enumerate(zip(genres, plays)):
        temp.append((items[0], items[1], idx))
        
    temp.sort(key= lambda x: x[1], reverse=True)
    
    for genre, play, idx in temp:
        play_map[genre].append((play, idx))
        best_map[genre] += play
    
    best_map = sorted(best_map.items(), key=lambda x:-x[1])
    
    
    for key, val in best_map:
        songs = play_map[key]
        songs.sort(key=lambda x:(-x[0], x[1]))
        answer += [i for play, i in songs[:2]]
            

    return answer