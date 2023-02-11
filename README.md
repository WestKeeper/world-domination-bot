# Бот автоматизации роли ведущего в игре "Мировое Господство"

## Роли

1. Host - создаёт сессию. Имеет права на настройку параметров игры перед запуском.
2. Member - подключается к сессии. Не имеет прав на настройку параметров игры.

## Запуск бота

1. Запуск бота осуществляется стандартной командой /start.
2. Возможные команды бота:
    1. /start - сбросить бота. Необходимо, чтобы стали доступны обновления.
    2. /help - получить описания списка доступных команд
    3. /create_united_nations - Создать ООН (лобби)
    4. /connect_to_united_nations - Подключиться к созданному ООН (лобби)
3. Создателю ООН (Хосту) при подключении нового человека (включая себя) высвечиваются
    сообщения следующего формата:
    - Подключился новый национальный лидер <username>. Всего лидеров: <N>.

## Настройка параметров игры

- После того, как host нажимает "Создать Игру", ему предполагается сконфигурировать игру
- Автоматически подсчитывается количество игроков (N), включая Хоста,
    и выводится N случайных заранее сконфигурированных стран
- Хост может согласиться, перегенерировать страны или не согласиться
- Если Хост не согласен, ему потребуется ввести N сообщений в следующем формате:
    - <Название_Страны>: Город_1, Город_2, Город_3, Город_4
    - США: Вашингтон Нью-Йорк Лос-Анджелес Сан-Франциско
- Названия городов идут от наибольшего к наименьшему
- Далее требуется назначить страны игрокам. Высвечиваются вопросы по типу:
    - Кто будет главой страны Китай?
- У Хоста есть клавиатура с именами игроков, с помощью которой он отвечает на вопросы.
- Далее Хосту предлагается выбор временных ограничений
- В начале выводятся ограничений по умолчанию:
    - Первое собрание ООН: 1 мин/страна
    - Другое заседание ООН: 1 мин/страна + 3 мин общие
    - Свободные переговоры в Лобби: 10 мин
- Хост может согласиться или не согласиться. Если нет - настраивает временные ограничения
    числовыми значениями, отвечая на соответствующие вопросы
- Далее Хосту отправляется список итоговых настроек, и он либо соглашается,
    либо сбрасывает создание игры и начинает заново.

## Ход игры

- Бот выводит сообщение: Первое собрание оон, 1 минута на страну
- Бот  по порядку отправляет сообщение по типу: “Китай, ваша минута пошла”
- Бот отправляет: “Время заседания окончено, просьба разойтись по странам”
- “Этап дипломатии, 10 минут”
- Здесь бот является координатором взаимодействий стран.
    - Чтобы попросить другую страну о переговорах, надо отправить запрос боту на конкретную страну. Другая страна получает сообщение о запросе, и может принять или отклонить его (InlineButtons?).
    - В случае если она занята, сообщение она не получает, страна-запроситель получает сообщение “Требуемая страна сейчас занята”.
    - После того, как страны закончили переговоры, нужно тыкнуть “свободен для переговоров”
- Формирование приказа происходит походу этапа дипломатии. Прайс доступен сразу:
    - Разработать ядерную технологию
    - Построить ракету (нельзя построить, если не разработана технология)
    - Передать деньги (не больше, чем есть)
    - Развить город 1,2,3,4
    - Поставить щит на город 1,2,3,4 (На одном городе, максимум 1 щит)
    - Развить экологию
    - Разбомбить какой–то город какой-то страны (Нельзя бомбить, если нет ракет)
- Предупреждения о таймингах:
    - Осталось 5 мин
    - 2 минуты
    - 1 минута
    - просрочил 30 сек - Отправляй сообщение!
    - Просрочил 1 минуту - конец
- Когда все приказы отправлены, или истекло время дипломатии, отправляется сводка по мировой ситуации. Жесткий режим: если приказ недозаполнен, отправляется то, что заполнено:
    - Уровень экологии в мире
    - Уровни жизни каждой страны (barchart)
    - Уровни жизни в каждом городе (таблицы)
- Индивидуальная статистика страны:
    - В приложении
- Повторение собрания ООН, только + время на обсуждение
- Зацикливаем на 6 раундов.
- Итоговая статистика:
    - В приложении
- Выдаются звания:
    - Главный агрессор
    - Миротворец
    - Интриган
    - Эколог
- Внутренние механики:
    - Ужесточить убывание экологии: допустим, если 3 раунда подряд никто не вкладывается, то она точно по нулям
- Как развитие:
    - Бот как автономный игрок
    - Прилетают анимации ракет, если твои города взорвали, вместе с индивидуальной статистикой
    - Локальная экология: твоя экология сильнее растет, мировая чуть медленнее
    - Материковая экология: экология соседа растет чуть быстрее, чем мировая
    - Завязать экологию на бомбление: там где бомбануло, там экология падает
    - МБ что-то кроме щита добавить

## Примечания

- Диалоги реализовать с помощью состояния? (FSMContext)
- Как реализовывать общие состояния для всех? AppScheduler? Состояния в БД?
- Разделение ролей реализовать с помощью MiddleWare и замыкания? Нет, лучше прописы
- Использовать Appscheduler для таймингов?
- БД: в RAM? SQLite? Redis?

## Приложения
- Все приложения (некоторые шаблоны сообщений) доступны [здесь](https://docs.google.com/document/d/1yT7HXiv8WFPXGPJRs9FgIYt1yvzAjAVVEuHLa6oIrZA/edit#)

## План
1. Механизм сессий
