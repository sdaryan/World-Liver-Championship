## World Liver Championship

Officials of the country's Liver Federation are preparing teams to participate in the World Liver Championship. According to the rules of the World Liver Championship, each person can only participate in 5 world liver competitions. The head of the federation has gathered all the athletes in this field, and each player has participated several times in world competitions to date. Liver teams consist of exactly 3 members. Now Mr. Shaygan Ariamehr, the head of the federation, wants to form teams that can participate together in the World Liver Championships for at least 3 years if selected (meaning each member of a team can have participated a maximum of 2 times in the World Liver Championships).

The first input line contains the number n, which is the number of desired liver players. The next input line contains n numbers separated by spaces, indicating how many times each player has participated in the World Liver Championship. Print a number in the output that represents the maximum number of teams that can be formed under the conditions mentioned.

## Input:
```python
6
5 0 4 2 1 0
```

## Output:
```python
1
```

## Input:
```python
41
5 3 3 1 1 2 5 0 1 3 1 1 4 2 0 3 1 3 3 4 4 1 2 0 5 3 3 1 0 5 0 1 2 2 1 0 2 5 0 4 2
```
## Output:
```python
8
```

In the sample input, players with 5 and 4 games cannot be in a group according to the question; therefore, only 4 players who have had 0, 2, 1, and 0 games can be in groups. With 4 people, only one 3-person group can be formed. Note that there is no need to calculate the number of permutations.

------------------------------------------------------------------------------
## مسابقات جهانی کبدی

مسئولین فدراسیون کبدی کشور در حال آماده سازی تیم هایی برای شرکت در مسابقات جهانی کبدی هستند. طبق قوانین مسابقات جهانی کبدی هر شخص فقط در ۵ مسابقه ی جهانی کبدی می تواند شرکت کند. رئیس فدراسیون تمامی ورزشکاران این رشته را دور هم جمع کرده است، هر بازیکن تا امروز تعدادی بار در مسابقات جهانی شرکت کرده است. تیم های کبدی دقیقا از ۳ نفر تشکیل می شود. حال آقای شایگان آریامهر، رئیس فدراسیون می خواهد تیم هایی تشکیل دهد که در صورت انتخاب شدن هرکدام از آن تیم ها، حداقل بتوانند 3 سال با هم در مسابقات جهانی شرکت کنند (یعنی هرکدام از اعضای یک تیم حداکثر ۲بار در مسابقات جهانی شرکت کرده باشند)

خط اول ورودی شامل عدد n یعنی تعداد بازیکنان کبدی مد نظر است. خط بعدی ورودی شامل n عدد که با space از هم جدا شده اند می باشد که نمایانگر این است که هر بازیکن چندبار در مسابقات جهانی شرکت کرده است. در خروجی یک عدد چاپ کنید که نمایانگر حداکثر تیم های تشکیل شده با شرایط گفته شده می باشد.
