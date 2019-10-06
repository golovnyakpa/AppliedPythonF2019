#!/usr/bin/env python
# coding: utf-8


class HashMap:
    """
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    """
    class Entry:
        def __init__(self, key, value):
            """
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            """
            self.pair = (key, value)

        def get_key(self):
            # TODO возвращаем ключ
            return self.pair[0]

        def get_value(self):
            # TODO возвращаем значение
            return self.pair[1]

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            return self.pair[0] == other.pair[0]

    def __init__(self, bucket_num=64):
        """
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        """
        self.map = [[] for i in range(bucket_num)]
        self.bucket_num = bucket_num
        self.entries_num = 0
        self.full_buckets = 0

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        # если оно присутствует, иначе default_value
        idx = self._get_index(self._get_hash(key))
        if self.map[idx]:
            for entry in self.map[idx]:
                if entry.get_key() == key:
                    return entry.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        self._resize()
        idx = self._get_index(self._get_hash(key))
        if (len(self.map[idx])) == 0:
            self.full_buckets += 1
        for i in range(len(self.map[idx])):
            if self.map[idx][i].get_key() == key:
                del self.map[idx][i]
                self.entries_num -= 1
                break
        self.map[idx].append(HashMap.Entry(key, value))
        self.entries_num += 1

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.entries_num

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.bucket_num

    def values(self):
        # TODO Должен возвращать итератор значений
        for lst in self.map:
            for entry in lst:
                yield entry.get_value()

    def keys(self):
        # TODO Должен возвращать итератор ключей
        for lst in self.map:
            for entry in lst:
                yield entry.get_key()

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        for lst in self.map:
            for entry in lst:
                yield (entry.get_key(), entry.get_value())

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        if self.full_buckets / self.bucket_num > 0.8:
            self.bucket_num *= 2
            new_map = [[] for i in range(self.bucket_num)]
            for lst in self.map:
                for entry in lst:
                    idx = self._get_index(self._get_hash(entry.get_key()))
                    new_map[idx].append(entry)
            self.map = new_map

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        return f'buckets: {self.bucket_num}, items: {len(self)}'

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        # raise NotImplementedError
        for lst in self.map:
            for entry in lst:
                if item == entry.get_key():
                    return True
        return False
