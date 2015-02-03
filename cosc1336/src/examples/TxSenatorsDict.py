
def process_file(fn):
    senator_file = open(fn, "r")

    party_affiliation = {}
    for line in senator_file:
        line = line.strip()
        words = line.split("$")
        party = words[1]
        senator = words[0]
        if party in party_affiliation:               # Is there a list there?
            name_as_is = party_affiliation[party]
            name_as_is += [senator]
            party_affiliation[party] = name_as_is
        else:
            party_affiliation[party] = [senator]
        print(party_affiliation)

    senator_file.close()


def main():
    process_file("C:\\workspaces\\workspace_python\\TexasSenate\src\\TexasSenate.txt")

main()
