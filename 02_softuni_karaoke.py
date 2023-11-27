participants = {participant: {'songs':[], 'awards': []} for participant in input().split(', ')}
songs = [song for song in input().split(", ")]

while True:
    current_stage = input()
    if current_stage == 'dawn':
        break

    participant = current_stage.split(', ')[0]
    song = current_stage.split(', ')[1]
    award = current_stage.split(', ')[2]

    if participant in participants:
        if song in songs:
            participants[participant]['songs'].append(song)
            if award not in participants[participant]['awards']:
                participants[participant]['awards'].append(award)

sorted_participants = dict(sorted(participants.items(), key=lambda participant: participant))
for participant, values in participants.items():
    if len(values['awards']) != 0:
        print(f"{participant}: {len(values['awards'])} awards")
        for award in values['awards']:
            print(f"--{award}")
    else:
        print("No awards")
#
# print(participants)
# print(sorted_participants)




