people, party = map(int, input().split())
inspector_list = list(map(int,input().split()))
inspectors = set(inspector_list[1:])
party_list = []
for i in range(party):
    attendee = list(map(int,input().split()))[1:]
    party_list.append(attendee)

if not inspectors:
    result = party
    print(result)
else:
    for i in range(party):
        for j in range(party):
            for k in party_list[j]:
                if k in inspectors:
                    inspectors.update(party_list[j])
                    party_list[j] = []
                    break
    result = 0
    for i in party_list:
        if i :
            result += 1
    print(result)
