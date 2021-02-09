

def compute_tweets(a, b):

    # Check if file exists

    try:

        # Declaring Variables

        rawTweet = []
        latitude = []
        longitude = []
        timeZone = []
        date = []
        time = []
        tweet = []
        keywords = []
        keyValues = []

        sentValsC = 0
        sentVals = 0
        keyWordTweets = []
        happinessScore = []

        Eastern = []
        count_of_tweetsE = 0
        count_of_keyword_tweetsE = 0
        averageE = 0
        totalHappinessE = 0

        Central = []
        count_of_tweetsC = 0
        count_of_keyword_tweetsC = 0
        averageC = 0
        totalHappinessC = 0

        Mountain = []
        count_of_tweetsM = 0
        count_of_keyword_tweetsM = 0
        averageM = 0
        totalHappinessM = 0

        Pacific = []
        count_of_tweetsP = 0
        count_of_keyword_tweetsP = 0
        averageP = 0
        totalHappinessP = 0

        # Tweet Format Isolation

        fileA = open(a, encoding='utf-8', errors='ignore')
        rawTweet = fileA.readlines()

        for n in range(len(rawTweet)):
            lat, long, _, d, t, text = rawTweet[n].split(' ', 5)
            latitude.append(float(lat[1:-1]))
            longitude.append(float(long[:-1]))
            date.append(d)
            time.append(t)
            tweet.append(text)

        fileA.close()

        # Keyword and Value Extraction

        fileB = open(b, encoding='utf-8', errors='ignore')
        rawKeys = fileB.readlines()

        for n in range(len(rawKeys)):
            keys, vals = rawKeys[n].split(',')
            keywords.append(keys)
            keyValues.append(int(vals))

        fileB.close()

        # Main Processing

        for n in range(len(tweet)):

            # This breaks up each tweet into words for analysis

            tweet[n] = tweet[n].translate(str.maketrans('', '', "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"))
            tweet[n] = tweet[n].lower()
            words = tweet[n].split()

            # This analyses the tweet for keywords and calculates happiness (needs to be fixed)

            for x in range(len(words)):
                for i in range(len(keywords)):
                    if words[x] == keywords[i]:
                        print(n, x)
                        sentVals += keyValues[i]
                        sentValsC += 1
            if sentValsC != 0:
                happinessScore.append(sentVals/sentValsC)
                sentVals = 0
                sentValsC = 0
            else:
                happinessScore.append(0)

            if happinessScore[n] != 0:
                keyWordTweets.append(1)
            else:
                keyWordTweets.append(0)
            print(happinessScore[n])

            # This checks what timezone it is in

            if (latitude[n] > 49.189787) or (latitude[n] < 24.660845):
                timeZone.append("None")
            elif (longitude[n] < -125.242264) or (longitude[n] > -67.444574):
                timeZone.append("None")
            elif -67.444574 >= longitude[n] >= -87.518395:
                timeZone.append("Eastern")
            elif -87.518395 >= longitude[n] >= -101.998892:
                timeZone.append("Central")
            elif -101.998892 >= longitude[n] >= -115.236428:
                timeZone.append("Mountain")
            elif -115.236428 >= longitude[n] >= -125.242264:
                timeZone.append("Pacific")

            # Forming the tuple (average, count_of_keyword_tweets, count_of_tweets)

            if timeZone[n] == "Eastern":
                count_of_tweetsE += 1
                if keyWordTweets[n] == 1:
                    count_of_keyword_tweetsE += 1
                    totalHappinessE += happinessScore[n]
            elif timeZone[n] == "Central":
                count_of_tweetsC +=1
                if keyWordTweets[n] == 1:
                    count_of_keyword_tweetsC += 1
                    totalHappinessC += happinessScore[n]
            elif timeZone[n] == "Mountain":
                count_of_tweetsM +=1
                if keyWordTweets[n] == 1:
                    count_of_keyword_tweetsM += 1
                    totalHappinessM += happinessScore[n]
            elif timeZone[n] == "Pacific":
                count_of_tweetsP +=1
                if keyWordTweets[n] == 1:
                    count_of_keyword_tweetsP += 1
                    totalHappinessP += happinessScore[n]
            else:
                pass

            if count_of_keyword_tweetsE != 0:
                averageE = totalHappinessE/count_of_keyword_tweetsE
            else:
                averageE = 0
            if count_of_keyword_tweetsC != 0:
                averageC = totalHappinessC/count_of_keyword_tweetsC
            else:
                averageC = 0
            if count_of_keyword_tweetsM != 0:
                averageM = totalHappinessM/count_of_keyword_tweetsM
            else:
                averageM = 0
            if count_of_keyword_tweetsP != 0:
                averageP= totalHappinessP/count_of_keyword_tweetsP
            else:
                averageP = 0

        Eastern.append(averageE)
        Eastern.append(count_of_keyword_tweetsE)
        Eastern.append(count_of_tweetsE)

        Central.append(averageC)
        Central.append(count_of_keyword_tweetsC)
        Central.append(count_of_tweetsC)

        Mountain.append(averageM)
        Mountain.append(count_of_keyword_tweetsM)
        Mountain.append(count_of_tweetsM)

        Pacific.append(averageP)
        Pacific.append(count_of_keyword_tweetsP)
        Pacific.append(count_of_tweetsP)

    except FileNotFoundError:
        print("One of the files does not exist.")
        return []
    else:
        return [Eastern, Central, Mountain, Pacific]
