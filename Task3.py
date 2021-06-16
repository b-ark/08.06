# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one,
# turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N
# or 'name' exists in the list, or "No" - in the other case.

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.valid_channels()
        self.currentChannel = channels[0]

    def valid_channels(self):
        """Проверка передаваемых в класс данных"""
        if not isinstance(self.channels, list):
            raise ValueError('Каналы определены неправильно! Передайте названия каналов в списке')
        if not self.channels:
            raise ValueError('Список каналов пустой! Для корректной работы контроллера, введите как минимум 1 канал')

    def current_channel(self):
        """Возвращет значение текущего канала"""
        print(f'Текущий канал: {self.currentChannel}')
        return self.currentChannel

    def first_channel(self):
        """Переключение на первый канал"""
        self.currentChannel = self.channels[0]
        self.current_channel()

    def last_channel(self):
        """Переключение на последний канал"""
        self.currentChannel = self.channels[-1]
        self.current_channel()

    def turn_channel(self, n):
        """Переключение на канал по номеру"""
        if n < 1 or n > len(self.channels):
            raise ValueError(f'Канала по номеру {n} не существует')
        else:
            self.currentChannel = self.channels[n-1]
            self.current_channel()

    def next_channel(self):
        """Переключение на следующий канал"""
        if self.channels[-1] == self.currentChannel:
            self.currentChannel = self.channels[0]
        else:
            self.currentChannel = self.channels[self.channels.index(self.currentChannel) + 1]
        self.current_channel()

    def previous_channel(self):
        """Переключение на предыдущий канал"""
        if self.channels[0] == self.currentChannel:
            self.currentChannel = self.channels[-1]
        else:
            self.currentChannel = self.channels[self.channels.index(self.currentChannel) - 1]
        self.current_channel()

    def is_exist(self, key):
        """Проверка: существует ли канал по номеру/названию"""
        if isinstance(key, str):
            if key in self.channels:
                print(f'Канал {key} существует')
            else:
                print(f'Канала {key} не существует')
        elif isinstance(key, int):
            if key < 1 or key > len(self.channels):
                print(f'Канала по номеру {key} не существует')
            else:
                print(f'Канал по номеру {key} существует. Его название: \'{self.channels[key]}\'')
        else:
            raise ValueError('Необходимый канал задан неверно. Используйте целочисленные или буквенные значения')


def main():
    CHANNELS = ["BBC", "Discovery", "TV1000"]
    controller = TVController(CHANNELS)
    controller.first_channel()
    controller.last_channel()
    controller.turn_channel(1)
    controller.next_channel()
    controller.previous_channel()
    controller.current_channel()
    controller.is_exist(4)
    controller.is_exist("BBC")


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
