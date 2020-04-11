Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> data.pollster.unique()
array(['Morning Consult', 'Gallup', 'Ipsos', 'Quinnipiac University',
       'Rasmussen Reports/Pulse Opinion Research',
       'Public Policy Polling', 'YouGov', 'SurveyMonkey', 'IBD/TIPP',
       'CNN/Opinion Research Corp.', 'CBS News', 'Zogby Analytics',
       'McLaughlin & Associates', 'Emerson College',
       'Pew Research Center', 'Fox News', 'Harris Poll',
       'Kaiser Family Foundation', 'Marist College',
       'American Research Group', 'NBC News/Wall Street Journal',
       'Suffolk University', 'Monmouth University',
       'Garin-Hart-Yang/Global Strategy Group', 'Saint Leo University',
       'icitizen', 'AP-NORC',
       'CNBC/Hart Research/Public Opinion Strategies',
       'USC Dornsife/LA Times', 'ABC News/Washington Post',
       'Gravis Marketing', 'GQR Research', 'Selzer & Co.', 'SurveyUSA',
       'CNN/SSRS', 'George Washington University/Battleground',
       'Opinion Savvy', 'Lucid',
       'Cards Against Humanity/Survey Sampling International',
       'University of Maryland/Washington Post',
       'Public Religion Research Institute', 'Tarrance Group',
       'America First Policies', 'Global Strategy Group/GBAO',
       'Washington Post/George Mason University', 'HarrisX',
       'Vox Populi Polling', 'Civiqs', 'Heart+Mind Strategies',
       'The Washington Post', 'Civis Analytics', 'Research Co.',
       'Public Opinion Strategies', 'D-CYFOR', 'GBAO', 'PSB Research',
       'Georgetown University/Battleground', 'Climate Nexus',
       'Hart Research Associates', 'Cygnal',
       'YouGov Blue/Data for Progress', 'Basswood Research',
       'Washington Post/Kaiser Family Foundation', 'YouGov Blue',
       'Marquette Law School', 'Hofstra University',
       'RealClear Opinion Research', 'AtlasIntel', 'Change Research',
       'RMG Research', 'Echelon Insights'], dtype=object)
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
9980     Fox News
2927     Fox News
8737     Fox News
1425     Fox News
11321    Fox News
Name: pollster, dtype: object
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
9980     Fox News
2927     Fox News
8737     Fox News
1425     Fox News
11321    Fox News
           ...   
10939    Fox News
2337     Fox News
9459     Fox News
963      Fox News
8438     Fox News
Name: pollster, Length: 70, dtype: object
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
          president   subgroup  ... createddate             timestamp
9980   Donald Trump     Voters  ...   1/23/2019  14:20:52 10 Apr 2020
2927   Donald Trump  All polls  ...   1/23/2019  14:18:27 10 Apr 2020
8737   Donald Trump     Voters  ...   1/24/2018  14:20:52 10 Apr 2020
1425   Donald Trump  All polls  ...   1/24/2018  14:18:27 10 Apr 2020
11321  Donald Trump     Voters  ...   1/26/2020  14:20:52 10 Apr 2020
...             ...        ...  ...         ...                   ...
10939  Donald Trump     Voters  ...   9/19/2019  14:20:52 10 Apr 2020
2337   Donald Trump  All polls  ...   9/23/2018  14:18:27 10 Apr 2020
9459   Donald Trump     Voters  ...   9/23/2018  14:20:52 10 Apr 2020
963    Donald Trump  All polls  ...   9/27/2017  14:18:27 10 Apr 2020
8438   Donald Trump     Voters  ...   9/27/2017  14:20:52 10 Apr 2020

[70 rows x 22 columns]
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
          president   subgroup  ... createddate             timestamp
9980   Donald Trump     Voters  ...   1/23/2019  14:20:52 10 Apr 2020
2927   Donald Trump  All polls  ...   1/23/2019  14:18:27 10 Apr 2020
8737   Donald Trump     Voters  ...   1/24/2018  14:20:52 10 Apr 2020
1425   Donald Trump  All polls  ...   1/24/2018  14:18:27 10 Apr 2020
11321  Donald Trump     Voters  ...   1/26/2020  14:20:52 10 Apr 2020
...             ...        ...  ...         ...                   ...
10939  Donald Trump     Voters  ...   9/19/2019  14:20:52 10 Apr 2020
2337   Donald Trump  All polls  ...   9/23/2018  14:18:27 10 Apr 2020
9459   Donald Trump     Voters  ...   9/23/2018  14:20:52 10 Apr 2020
963    Donald Trump  All polls  ...   9/27/2017  14:18:27 10 Apr 2020
8438   Donald Trump     Voters  ...   9/27/2017  14:20:52 10 Apr 2020

[70 rows x 22 columns]
Traceback (most recent call last):
  File "/Users/kelseywu/Desktop/testing1.py", line 14, in <module>
    plt.plot(createddate, approve)
NameError: name 'createddate' is not defined
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
          president   subgroup  ... createddate             timestamp
9980   Donald Trump     Voters  ...   1/23/2019  14:20:52 10 Apr 2020
2927   Donald Trump  All polls  ...   1/23/2019  14:18:27 10 Apr 2020
8737   Donald Trump     Voters  ...   1/24/2018  14:20:52 10 Apr 2020
1425   Donald Trump  All polls  ...   1/24/2018  14:18:27 10 Apr 2020
11321  Donald Trump     Voters  ...   1/26/2020  14:20:52 10 Apr 2020
...             ...        ...  ...         ...                   ...
10939  Donald Trump     Voters  ...   9/19/2019  14:20:52 10 Apr 2020
2337   Donald Trump  All polls  ...   9/23/2018  14:18:27 10 Apr 2020
9459   Donald Trump     Voters  ...   9/23/2018  14:20:52 10 Apr 2020
963    Donald Trump  All polls  ...   9/27/2017  14:18:27 10 Apr 2020
8438   Donald Trump     Voters  ...   9/27/2017  14:20:52 10 Apr 2020

[70 rows x 22 columns]
Traceback (most recent call last):
  File "/Users/kelseywu/Desktop/testing1.py", line 14, in <module>
    data_fox.plt.plot(createddate, approve)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'plt'
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
          president   subgroup  ... createddate             timestamp
9980   Donald Trump     Voters  ...   1/23/2019  14:20:52 10 Apr 2020
2927   Donald Trump  All polls  ...   1/23/2019  14:18:27 10 Apr 2020
8737   Donald Trump     Voters  ...   1/24/2018  14:20:52 10 Apr 2020
1425   Donald Trump  All polls  ...   1/24/2018  14:18:27 10 Apr 2020
11321  Donald Trump     Voters  ...   1/26/2020  14:20:52 10 Apr 2020
...             ...        ...  ...         ...                   ...
10939  Donald Trump     Voters  ...   9/19/2019  14:20:52 10 Apr 2020
2337   Donald Trump  All polls  ...   9/23/2018  14:18:27 10 Apr 2020
9459   Donald Trump     Voters  ...   9/23/2018  14:20:52 10 Apr 2020
963    Donald Trump  All polls  ...   9/27/2017  14:18:27 10 Apr 2020
8438   Donald Trump     Voters  ...   9/27/2017  14:20:52 10 Apr 2020

[70 rows x 22 columns]
Traceback (most recent call last):
  File "/Users/kelseywu/Desktop/testing1.py", line 14, in <module>
    plt.plot(data_fox[createddate], data_fox[approve])
NameError: name 'createddate' is not defined
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
          president   subgroup  ... createddate             timestamp
9980   Donald Trump     Voters  ...   1/23/2019  14:20:52 10 Apr 2020
2927   Donald Trump  All polls  ...   1/23/2019  14:18:27 10 Apr 2020
8737   Donald Trump     Voters  ...   1/24/2018  14:20:52 10 Apr 2020
1425   Donald Trump  All polls  ...   1/24/2018  14:18:27 10 Apr 2020
11321  Donald Trump     Voters  ...   1/26/2020  14:20:52 10 Apr 2020
...             ...        ...  ...         ...                   ...
10939  Donald Trump     Voters  ...   9/19/2019  14:20:52 10 Apr 2020
2337   Donald Trump  All polls  ...   9/23/2018  14:18:27 10 Apr 2020
9459   Donald Trump     Voters  ...   9/23/2018  14:20:52 10 Apr 2020
963    Donald Trump  All polls  ...   9/27/2017  14:18:27 10 Apr 2020
8438   Donald Trump     Voters  ...   9/27/2017  14:20:52 10 Apr 2020

[70 rows x 22 columns]
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
          president   subgroup  ... createddate             timestamp
9980   Donald Trump     Voters  ...   1/23/2019  14:20:52 10 Apr 2020
2927   Donald Trump  All polls  ...   1/23/2019  14:18:27 10 Apr 2020
8737   Donald Trump     Voters  ...   1/24/2018  14:20:52 10 Apr 2020
1425   Donald Trump  All polls  ...   1/24/2018  14:18:27 10 Apr 2020
11321  Donald Trump     Voters  ...   1/26/2020  14:20:52 10 Apr 2020
...             ...        ...  ...         ...                   ...
10939  Donald Trump     Voters  ...   9/19/2019  14:20:52 10 Apr 2020
2337   Donald Trump  All polls  ...   9/23/2018  14:18:27 10 Apr 2020
9459   Donald Trump     Voters  ...   9/23/2018  14:20:52 10 Apr 2020
963    Donald Trump  All polls  ...   9/27/2017  14:18:27 10 Apr 2020
8438   Donald Trump     Voters  ...   9/27/2017  14:20:52 10 Apr 2020

[70 rows x 22 columns]
Traceback (most recent call last):
  File "/Users/kelseywu/Desktop/testing1.py", line 17, in <module>
    fig.autofmt_xdate()
AttributeError: 'list' object has no attribute 'autofmt_xdate'
>>> 
================================ RESTART: Shell ================================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
          president   subgroup  ... createddate             timestamp
9980   Donald Trump     Voters  ...   1/23/2019  14:20:52 10 Apr 2020
2927   Donald Trump  All polls  ...   1/23/2019  14:18:27 10 Apr 2020
8737   Donald Trump     Voters  ...   1/24/2018  14:20:52 10 Apr 2020
1425   Donald Trump  All polls  ...   1/24/2018  14:18:27 10 Apr 2020
11321  Donald Trump     Voters  ...   1/26/2020  14:20:52 10 Apr 2020
...             ...        ...  ...         ...                   ...
10939  Donald Trump     Voters  ...   9/19/2019  14:20:52 10 Apr 2020
2337   Donald Trump  All polls  ...   9/23/2018  14:18:27 10 Apr 2020
9459   Donald Trump     Voters  ...   9/23/2018  14:20:52 10 Apr 2020
963    Donald Trump  All polls  ...   9/27/2017  14:18:27 10 Apr 2020
8438   Donald Trump     Voters  ...   9/27/2017  14:20:52 10 Apr 2020

[70 rows x 22 columns]
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
          president   subgroup  ... createddate             timestamp
9980   Donald Trump     Voters  ...   1/23/2019  14:20:52 10 Apr 2020
2927   Donald Trump  All polls  ...   1/23/2019  14:18:27 10 Apr 2020
8737   Donald Trump     Voters  ...   1/24/2018  14:20:52 10 Apr 2020
1425   Donald Trump  All polls  ...   1/24/2018  14:18:27 10 Apr 2020
11321  Donald Trump     Voters  ...   1/26/2020  14:20:52 10 Apr 2020
...             ...        ...  ...         ...                   ...
10939  Donald Trump     Voters  ...   9/19/2019  14:20:52 10 Apr 2020
2337   Donald Trump  All polls  ...   9/23/2018  14:18:27 10 Apr 2020
9459   Donald Trump     Voters  ...   9/23/2018  14:20:52 10 Apr 2020
963    Donald Trump  All polls  ...   9/27/2017  14:18:27 10 Apr 2020
8438   Donald Trump     Voters  ...   9/27/2017  14:20:52 10 Apr 2020

[70 rows x 22 columns]
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> print(data_cnn)
         president   subgroup  ... createddate             timestamp
4820  Donald Trump     Adults  ...    2/3/2017  14:19:25 10 Apr 2020
40    Donald Trump  All polls  ...    2/3/2017  14:18:27 10 Apr 2020
156   Donald Trump  All polls  ...    3/6/2017  14:18:27 10 Apr 2020
4902  Donald Trump     Adults  ...    3/6/2017  14:19:25 10 Apr 2020
363   Donald Trump  All polls  ...   4/27/2017  14:18:27 10 Apr 2020
5047  Donald Trump     Adults  ...   4/27/2017  14:19:25 10 Apr 2020

[6 rows x 22 columns]
>>> print(data_rev)
          president   subgroup  ... createddate             timestamp
2809   Donald Trump  All polls  ...    1/1/2019  14:18:27 10 Apr 2020
9879   Donald Trump     Voters  ...    1/1/2019  14:20:52 10 Apr 2020
9876   Donald Trump     Voters  ...    1/1/2019  14:20:52 10 Apr 2020
9850   Donald Trump     Voters  ...    1/1/2019  14:20:52 10 Apr 2020
2807   Donald Trump  All polls  ...    1/1/2019  14:18:27 10 Apr 2020
...             ...        ...  ...         ...                   ...
5421   Donald Trump     Adults  ...    9/9/2017  14:19:25 10 Apr 2020
3991   Donald Trump  All polls  ...    9/9/2019  14:18:27 10 Apr 2020
3985   Donald Trump  All polls  ...    9/9/2019  14:18:27 10 Apr 2020
10907  Donald Trump     Voters  ...    9/9/2019  14:20:52 10 Apr 2020
10901  Donald Trump     Voters  ...    9/9/2019  14:20:52 10 Apr 2020

[11575 rows x 22 columns]
>>> data[createddate]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data[createddate]
NameError: name 'createddate' is not defined
>>> data['createddate']
0        1/23/2017
1        1/23/2017
2        1/24/2017
3         3/1/2017
4        1/26/2017
           ...    
11570    4/10/2020
11571     4/9/2020
11572    4/10/2020
11573    4/10/2020
11574    4/10/2020
Name: createddate, Length: 11575, dtype: object
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/tools/datetimes.py", line 432, in _convert_listlike_datetimes
    values, tz = conversion.datetime_to_datetime64(arg)
  File "pandas/_libs/tslibs/conversion.pyx", line 200, in pandas._libs.tslibs.conversion.datetime_to_datetime64
TypeError: Unrecognized value type: <class 'str'>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/kelseywu/Desktop/testing1.py", line 9, in <module>
    data['createddate'] =  pd.to_datetime(data['createddate'], format='%d/%m/%Y')
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/tools/datetimes.py", line 724, in to_datetime
    cache_array = _maybe_cache(arg, format, cache, convert_listlike)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/tools/datetimes.py", line 152, in _maybe_cache
    cache_dates = convert_listlike(unique_dates, format)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/tools/datetimes.py", line 435, in _convert_listlike_datetimes
    raise e
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/tools/datetimes.py", line 399, in _convert_listlike_datetimes
    result, timezones = array_strptime(
  File "pandas/_libs/tslibs/strptime.pyx", line 142, in pandas._libs.tslibs.strptime.array_strptime
ValueError: time data '1/23/2017' does not match format '%d/%m/%Y' (match)
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> print(data_cnn)
         president   subgroup  ... createddate             timestamp
40    Donald Trump  All polls  ...  2017-02-03  14:18:27 10 Apr 2020
4820  Donald Trump     Adults  ...  2017-02-03  14:19:25 10 Apr 2020
156   Donald Trump  All polls  ...  2017-03-06  14:18:27 10 Apr 2020
4902  Donald Trump     Adults  ...  2017-03-06  14:19:25 10 Apr 2020
363   Donald Trump  All polls  ...  2017-04-27  14:18:27 10 Apr 2020
5047  Donald Trump     Adults  ...  2017-04-27  14:19:25 10 Apr 2020

[6 rows x 22 columns]
>>> print(data_cnn[disapprove, createddate])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(data_cnn[disapprove, createddate])
NameError: name 'disapprove' is not defined
>>> print(data_cnn['disapprove', 'createddate'])
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('disapprove', 'createddate')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(data_cnn['disapprove', 'createddate'])
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('disapprove', 'createddate')
>>> print(data_cnn[['disapprove]])
		
SyntaxError: EOL while scanning string literal
>>> print(data_cnn[['disapprove']])
      disapprove
40          53.0
4820        53.0
156         52.0
4902        52.0
363         54.0
5047        54.0
>>> print(data_cnn[['disapprove'], ['createddate']])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(data_cnn[['disapprove'], ['createddate']])
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 116, in pandas._libs.index.IndexEngine.get_loc
TypeError: '(['disapprove'], ['createddate'])' is an invalid key
>>> print(data_cnn[['disapprove','createddate']])
      disapprove createddate
40          53.0  2017-02-03
4820        53.0  2017-02-03
156         52.0  2017-03-06
4902        52.0  2017-03-06
363         54.0  2017-04-27
5047        54.0  2017-04-27
>>> print(data_cnn[['approve','createddate']])
      approve createddate
40       44.0  2017-02-03
4820     44.0  2017-02-03
156      45.0  2017-03-06
4902     45.0  2017-03-06
363      44.0  2017-04-27
5047     44.0  2017-04-27
>>> print(data_fox[['approve','createddate']])
       approve createddate
80        48.0  2017-02-14
7878      48.0  2017-02-14
197       43.0  2017-03-15
7951      43.0  2017-03-15
366       45.0  2017-04-26
...        ...         ...
4617      47.0  2020-02-28
4717      48.0  2020-03-26
11509     48.0  2020-03-26
11566     49.0  2020-04-09
4780      49.0  2020-04-09

[70 rows x 2 columns]
>>> data.pollster.unique()
array(['Morning Consult', 'Gallup', 'Ipsos', 'Quinnipiac University',
       'Rasmussen Reports/Pulse Opinion Research',
       'Public Policy Polling', 'YouGov', 'SurveyMonkey', 'IBD/TIPP',
       'CNN/Opinion Research Corp.', 'CBS News', 'Zogby Analytics',
       'McLaughlin & Associates', 'Emerson College',
       'Pew Research Center', 'Fox News', 'Harris Poll',
       'Kaiser Family Foundation', 'Marist College',
       'American Research Group', 'NBC News/Wall Street Journal',
       'Suffolk University', 'Monmouth University',
       'Garin-Hart-Yang/Global Strategy Group', 'Saint Leo University',
       'icitizen', 'AP-NORC',
       'CNBC/Hart Research/Public Opinion Strategies',
       'USC Dornsife/LA Times', 'ABC News/Washington Post',
       'Gravis Marketing', 'GQR Research', 'Selzer & Co.', 'SurveyUSA',
       'CNN/SSRS', 'George Washington University/Battleground',
       'Opinion Savvy', 'Lucid',
       'Cards Against Humanity/Survey Sampling International',
       'University of Maryland/Washington Post',
       'Public Religion Research Institute', 'Tarrance Group',
       'America First Policies', 'Global Strategy Group/GBAO',
       'Washington Post/George Mason University', 'HarrisX',
       'Vox Populi Polling', 'Civiqs', 'Heart+Mind Strategies',
       'The Washington Post', 'Civis Analytics', 'Research Co.',
       'Public Opinion Strategies', 'D-CYFOR', 'GBAO', 'PSB Research',
       'Georgetown University/Battleground', 'Climate Nexus',
       'Hart Research Associates', 'Cygnal',
       'YouGov Blue/Data for Progress', 'Basswood Research',
       'Washington Post/Kaiser Family Foundation', 'YouGov Blue',
       'Marquette Law School', 'Hofstra University',
       'RealClear Opinion Research', 'AtlasIntel', 'Change Research',
       'RMG Research', 'Echelon Insights'], dtype=object)
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
No handles with labels found to put in legend.
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
Traceback (most recent call last):
  File "/Users/kelseywu/Desktop/testing1.py", line 41, in <module>
    plt.set_title("Comparing Trump Disapproval Percentages Across Polls from Fox, Gallup, and CBS")
AttributeError: module 'matplotlib.pyplot' has no attribute 'set_title'
>>> 
================================ RESTART: Shell ================================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 
================= RESTART: /Users/kelseywu/Desktop/testing1.py =================
>>> 