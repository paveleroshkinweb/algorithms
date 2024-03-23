def find_best_songs(songs):
    best = songs[0]
    for s in songs:
        best = best & s
    return sorted(list(best))


if __name__ == '__main__':
    songs = []
    for _ in range(int(input())):
        _ = input()
        songs.append(set(input().split()))
    best_songs = find_best_songs(songs)
    print(len(best_songs))
    print(*best_songs)
