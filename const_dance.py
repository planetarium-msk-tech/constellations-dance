import datetime as dt

print('Файл const.txt со списком созвездий'
      ' должен находиться в этой же директории\n')
print('Результаты работы скрипта сохраняются в папку "uni_files"\n')

print('ENTER FADE_IN TIME IN SECONDS')
FADE_IN = int(input().strip())
print('ENTER FADE_OUT TIME IN SECONDS')
FADE_OUT = int(input().strip())
print('ENTER ACTIVE TIME IN SECONDS')
ACTIVE_TIME = int(input().strip())
print('ENTER DELTA BETWEEN CONSTELLATIONS IN SECONDS')
DELTA = int(input().strip())
print('ENTER MAX BRIGHTNESS')
MAX_BRIGHT = int(input().strip())

FADE_IN = dt.timedelta(seconds=FADE_IN)
FADE_OUT = dt.timedelta(seconds=FADE_OUT)
ACTIVE_TIME = dt.timedelta(seconds=ACTIVE_TIME)
DELTA = dt.timedelta(seconds=DELTA)

constellations_names = []

with open('const.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line != '\n':
            constellations_names.append(line.strip())

result_list = []
start = dt.time(minute=1, second=1)
for name in constellations_names:
    tmp_start = dt.datetime.combine(dt.date(1, 1, 1), start)
    end = (tmp_start + (FADE_IN + ACTIVE_TIME)).time()
    result_list.append(
        (f'{start}', f'{name} #{MAX_BRIGHT} T{FADE_IN.seconds}')
    )
    result_list.append(
        (f'{end}', f'{name} #0 T{FADE_OUT.seconds}')
    )
    start = (tmp_start + DELTA).time()

result_list.sort()

print('ENTER SCRIPT SUFFIX. NO SPACES. USE "_"')
print('FILE NAME WILL BE LIKE THIS: "constellations_dance_SUFFIX"')
suffix = input().strip()

with open(f'uni_files/constellations_dance_{suffix}.uni', 'w') as f:
    f.write(
        (f'00:01:00.0\tREM {f.name} fade_in:{FADE_IN.seconds},'
         f' fade_out:{FADE_OUT.seconds}, active_time:{ACTIVE_TIME.seconds},'
         f' delta:{DELTA.seconds}\n')
    )
    f.write('00:01:00.2\tTIME #2022/6/22 L06.27\n')
    for result in result_list:
        f.write(f'{result[0]}.0\t{result[1]}\n')
