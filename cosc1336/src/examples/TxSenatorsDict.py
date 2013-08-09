
def ProcessFile( fn ):
    senatorFile = open( fn, "r" )

    partyAffiliation = {}
    for line in senatorFile:
        line = line.strip()
        words = line.split( "$" )
        party = words[1]
        senator = words[0]
        if party in partyAffiliation:               # Is there a list there?
            nameAsIs = partyAffiliation[party]
            nameAsIs += [ senator ]
            partyAffiliation[party] = nameAsIs
        else:
            partyAffiliation[party] = [ senator ]
        print( partyAffiliation )

    senatorFile.close()

def main():
    ProcessFile( "C:\\workspaces\\workspace_python\\TexasSenate\src\\TexasSenate.txt" )

main()
