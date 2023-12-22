import pandas as pd
import datetime as DT
import time


def input_data():
    data, firsttime, lasttime = None, None, None

    for i in range(3):
        try:
            data_str = input("Введите дату в формате дд/мм/гггг: ").strip()
            firsttime_str = input("Введите время начала отдыха в формате чч:mm: ").strip()
            lasttime_str = input("Введите время окончания отдыха в формате чч:mm: ").strip()

            data = DT.datetime.strptime(data_str, '%d/%m/%Y').date()
            firsttime = DT.datetime.strptime(firsttime_str, '%H:%M').time()
            lasttime = DT.datetime.strptime(lasttime_str, '%H:%M').time()

            break
        except ValueError:
            print(f'Вы ввели некорректные данные. Проверьте правильность ввода. Осталось попыток: {2 - i}')
            time.sleep(3)

    if data is not None and firsttime is not None and lasttime is not None:
        df = pd.DataFrame([[data, firsttime, lasttime]],
                          columns=['Дата', 'Время начала отдыха', 'Время окончания отдыха'])
        return df
    else:
        return None


# its_freetime()
df = input_data()
if df is not None:
    print(df)
else:
    print("Не удалось получить данные.")