class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        Default local initialization varaibles
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self)-> None:
        '''
        Method to power the tv.
        '''
        if self.__status == True:
            self.__status = False
        elif self.__status == False:
            self.__status = True


    def mute(self) -> None:
        '''
        Method to mute the tv volume.
        '''
        if self.__status == False:
            pass
        elif self.__muted == True:
            self.__muted = False
        elif self.__muted == False:
            self.__muted = True

    def channel_up(self) -> None:
        '''
        Method to increase the tv channel.
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self)-> None:
        '''
        Method to decrease the tv channel.
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Method to increase the tv volume.
        '''
        if self.__status:
            if self.__muted:
                if self.__volume < Television.MAX_VOLUME:
                    self.__muted = False
                    self.__volume += 1
            else:
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to decrease the tv volume.
        '''
        if self.__status:
            if self.__muted:
                if self.__volume > Television.MIN_VOLUME:
                    self.__muted = False
                    self.__volume -= 1
            else:
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to show the tv status
        :return: tv status
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

