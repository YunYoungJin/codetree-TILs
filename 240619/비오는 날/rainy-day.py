class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
        
# 변수 선언 및 입력
n = int(input())
arr = [input().split() for _ in range(n)]
forecasts = [Forecast(date, day, weather) for date, day, weather in arr]

# 비오는 날 중 가장 빠른 날 찾기
target = 0
forecasts.sort(key = lambda x : x.date)
for i, forecast in enumerate(forecasts):
    if forecast.weather == "Rain":
        target = i
        break

# 결과 출력
print(f"{forecasts[i].date} {forecasts[i].day} {forecasts[i].weather}")