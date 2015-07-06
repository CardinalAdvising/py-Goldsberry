import requests

class Transactions:
    """
    """
    def __init__(self):
        self._url = "http://stats.nba.com/feeds/NBAPlayerTransactions-559107/json.js"
        self._pull = requests.get(self._url)
    def Transactions(self):
        return self._pull.json()['ListItems']

class DailyStandings:
    """
    """
    def __init__(self, date, LeagueID = 00, offset = 0):
        self.url = "http://stats.nba.com/stats/scoreboard?"
        # Add Logic to test if date matches patter mm-dd-yyyy
        self._api_param = {'LeagueID':LeagueID,
                           'gameDate':date,
                           'DayOffset':offset
        }
        self._pull = requests.get(self._url, params=self._api_param)
    def GameHeader(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def LineScore(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeriesStandings(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def LastMeeting(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def EastConfStandingsByDay(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WestConfStandingsByDay(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Available(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerList:
    """
    """
    def __init__(self, CurrentSeason='1', LeagueID='00', Season='2014-15'):
        self._url = "http://stats.nba.com/stats/commonallplayers?"
        self._api_param = {'IsOnlyCurrentSeason':CurrentSeason,
                           'LeagueID':LeagueID,
                           'Season': Season
        }
        self._pull = requests.get(self._url, params=self._api_param)
    def Players(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class FranchiseHistory:
    """
    """
    def __init__(self, LeagueID='00'):
        self._url = "http://stats.nba.com/stats/franchisehistory?"
        self._api_param = {'LeagueID':LeagueID
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def FranchiseHistory(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def DefunctTeams(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayoffPicture:
    """
    """
    def __init__(self, LeagueID='00', SeasonID='22014'):
        self._url = "http://stats.nba.com/stats/franchisehistory?"
        self._api_param = {'LeagueID':LeagueID,
                           'SeasonID':SeasonID
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def EastConfPlayoffPicture(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WestConfPlayoffPicture(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def EastConfStandings(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WestConfStandings(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def EastConfRemainingGames(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WestConfRemainingGames(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class LeagueLeaders:
    def __init__(self, LeagueID='00', permode='PerGame', scope='S', season='All Time',
        seasontype='Regular Season', statcategory='PTS'):
        self._url = "http://stats.nba.com/stats/leagueleaders?"
        self._api_param = {'LeagueID':LeagueID,
                           'Scope':scope,
                           'PerMode':permode,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StatCategory':statcategory
                           }
        #Scope: (RS)|(S)|(Rookies) one of these options
        self._pull = requests.get(self._url, params=self._api_param)
    def Leaders(self):
        _headers = self._pull.json()['resultSet']['headers']
        _values = self._pull.json()['resultSet']['rowSet']
        return [dict(zip(_headers, value)) for value in _values]