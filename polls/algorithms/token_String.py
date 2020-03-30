# vreau sa iau doar cuvintele cheie dintr-o propozitie, alaturi de nume de chestii
import mysql.connector


def initializare():
    interzis = []
    interzis.append('I')
    interzis.append('You')
    interzis.append('We')
    interzis.append('They')
    interzis.append('i')
    interzis.append('you')
    interzis.append('we')
    interzis.append('they')
    interzis.append('He')
    interzis.append('he')
    interzis.append('she')
    interzis.append('She')
    interzis.append('want')
    interzis.append('need')
    interzis.append('wish')
    interzis.append('crave')
    interzis.append('demand')
    interzis.append('am')
    interzis.append('are')
    interzis.append('is')
    interzis.append('look')
    interzis.append('require')
    interzis.append('must')
    interzis.append('have')
    interzis.append('more')
    interzis.append('movie')
    interzis.append('film')
    interzis.append('less')
    interzis.append('but')
    interzis.append('to')
    interzis.append('lack')
    interzis.append('request')
    interzis.append('urge')
    interzis.append('a')
    interzis.append('in')
    interzis.append('an')
    interzis.append('that')
    interzis.append('than')
    interzis.append('the')
    interzis.append('which')
    interzis.append('who')
    interzis.append('might')
    interzis.append('may')
    interzis.append('for')
    interzis.append('by')
    interzis.append('with')
    interzis.append('act')
    interzis.append('play')
    interzis.append('featurring')
    interzis.append('features')
    interzis.append('perform')
    interzis.append('acts')
    interzis.append('plays')
    interzis.append('features')
    interzis.append('performs')
    interzis.append('more')
    interzis.append('bigger')
    interzis.append('lower')
    interzis.append('rating')
    interzis.append('degree')
    interzis.append('level')
    interzis.append('rank')
    interzis.append('score')
    interzis.append('tier')
    interzis.append('reputation')
    interzis.append('position')
    interzis.append('note')
    interzis.append('tag')
    interzis.append('made')
    interzis.append('and')
    interzis.append('produced')
    interzis.append('built')
    interzis.append('finished')
    interzis.append('created')
    interzis.append('manufactured')
    interzis.append('formed')
    interzis.append('launched')
    interzis.append('prepared')
    interzis.append('see')
    interzis.append('can')
    interzis.append('could')
    interzis.append('have')
    interzis.append('where')
    interzis.append('view')
    interzis.append('having')
    interzis.append('wanna')
    interzis.append('rating')
    interzis.append('a')
    interzis.append('over')
    interzis.append('looking')

    return interzis

#print(interzis)

def tokenizer(string):

    tokens = []
    interzis = initializare()
    ok = False
    string = string.replace("," , "")
    string = string.split(" ")
    for i in range(0,len(string)):
        if ok == False:
            if string[i] not in interzis:

                words = " "
                count = 0
                print(string[i])
                if string[i][0].isupper()==True:
                    j = i+1
                    words = (string[i]) 
                    
                    words = words + " " + (string[j])
                    #j = j + 1
                    ok = True

                    c = []
                    c.append(words)
                    c.append("n")
                    tokens.append(c)

                else:
                    if string[i].isnumeric() == True:
                        if int(string[i]) > 10:
                            x = float(int(string[i])/10)
                        else:
                            x = float(int(string[i]))

                        c = []
                        c.append(x)
                        c.append("r")
                        tokens.append(c)
                    else:
                        if len(string[i])==3 and string[i][1] == ".":
                            first = int(string[i][0]) * 10
                            second = int(string[i][2])
                            x = float((first+second)/10)

                            c = []
                            c.append(x)
                            c.append("r")
                            tokens.append(c)
                        else:
                            c = []
                            c.append(string[i])
                            c.append("a")
                            tokens.append(c)

        else:
                ok = False
    return tokens


#for testing the function

# tokens = tokenizer("i want a movie with princesses Studio Ghibli")
# # # tokens contine perechi token, type ; type apartine {n-nume, a-altceva}
# for t in tokens:
#     print(t)    # t[0] - token, t[1] - type














