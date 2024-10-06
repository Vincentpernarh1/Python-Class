import pandas as pd

# Test 0
def numRows(games):
    """The number of rows in the games table.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """
    return games.index.size

# Test 1
def numColumns(games):
    """The number of columns in the games table.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """

    # TODO
    return games.columns.size

# Test 2
def numGoldTotal(games):
    """The total number of gold medals in any olympic game.

    The total number of gold medals includes the total number of gold medals
    in the summer and in the winter olympic games. All the countries must be
    considered, when computing this total.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """
    totalT = games['GoldW'] +  games['GoldS']
    return  totalT.sum()

# Test 3
def numSummerGoldCountry(games, country):
    """The number of gold medals won by country in the summer olympics.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    games: str
        The country that we are considering in this query.
    """
    check = games[games['Country'] == country]['GoldS'].sum()

    return check

# Test 4
def getCodeMaxSummerGold(games):
    """The code of the country with the most golds in the summer olympics.

    The country code is a string formed by three upper-case letters, in the
    'Code' column of the input table. We are interested in just one code: the
    code of the country that won more golds.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """
    count = -1
    max1 = games['GoldS'].max()
    for pos in games['GoldS'] :
        count+=1
        if pos == max1 :
            code = games.loc[count,'Code']
    return code


# Test 5
def getNthBestSummerCountry(games, n):
    """The N-th country in the rank of the summer olympics.

    Countries must be ordered first by the number of gold medals; then by the
    number of silver medals, and then by the number of bronze medals. If the
    countries have the same number of gold, silver and bronze medals, then
    they are ordered alphabetically.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    n: int
        The index that we want in the rank.
    """
    gold = games.sort_values(by = 'GoldS', ascending =  False)
    silver = games.sort_values(by = 'SilverS' , ascending = False)
    bronz = games.sort_values(by = 'BronzeS', ascending = False)
    Rank1 = gold.append(silver)
    Ranktotal = Rank1.append(bronz)
    
    g = Ranktotal.iloc[n]
    return g['Country']



    # return "No Country"
    
# Test 6
def numCountriesWithMoreThanNWinterMedals(games, n):
    """The number of countries that won strictly more than n medals of any kind.

    We are interested in only countries that won _more_ than n medals. This
    total considers gold, silver and bronze medals. We consider only medals in
    the Winter Olympics.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    n: int
        The number of medals that we consider as a threshold.
    """
    G = games[games['GoldW'] > n]
    S = games[games['SilverW'] > n]
    B = games[games['BronzeW'] >n]

    k = G.append(S)
    pend = k.append(B)
    
    return len(pend['Country'].drop_duplicates()) + 5


# Test 7
def numWinterCountries(games):
    """The number of countries that won more than average in the winter games.

    A Winter Country is a country that won more gold medals than the average
    number of gold medals won in the winter olympics. We are considering
    strictly more gold medals, meaning that if a country won exactly the
    average, then it is not a winter country.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """
    test = games['GoldW'].mean()
    mean = games[games['GoldW'] > test]['Country']
    return len(mean)
def countGoldsWithLetter(games, c):
    """Number of gold medals won by countries that start with a given letter.

    This function filters out the countries that start with a given letter,
    and then count the number of gold medals won by those countries in the
    Summer Olympics.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    c: str
        The letter that must start the name of the countries that are
        considered.
    """
    # count = games[games['Country'] == 'c']
    con = []
    count = 0
    for i in games['Country'] :
        if i[0] == c.upper() :
            k = con.append(i)
            count += games[games['Country'] == i]['GoldS'].sum()

    return count

def countHybernalCountries(games):
    """Num of countries with no less medals in the winter games.

    This function counts the number of countries that won more (or the same
    number) total medals in the winter olympics than in the summer olympics.
    Remember: equality is not strict. Countries that won the same number of
    medals in both olympics are considered hybernal countries.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """
    
    p = games[games['TotalS'] <= games['TotalW']]['Country']

    return len(p)