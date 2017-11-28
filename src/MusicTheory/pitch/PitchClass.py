import collections
from Framework.ConstMeta import ConstMeta
"""
半音数からピッチクラスと相対オクターブを取得する。
"""
class PitchClass(metaclass=ConstMeta):
    _PitchClass = collections.namedtuple('PitchClass', ['PitchClass', 'RelativeOctave'])
    MaxPitchClass = 11
    MinPitchClass = 0
    @classmethod
    def Get(cls, halfToneNum:int):
        pitchClass = halfToneNum % (cls.MaxPitchClass+1)
        relativeOctave = halfToneNum // (cls.MaxPitchClass+1)
        if pitchClass < cls.MinPitchClass:
            pitchClass += (cls.MaxPitchClass+1)
        return cls._PitchClass(pitchClass, relativeOctave)


if __name__ == '__main__':
    pc = PitchClass.Get(9)
    print(pc)
    print(tuple(pc))
    print(pc.PitchClass, pc.RelativeOctave)
#    pc.PitchClass += 2#AttributeError: can't set attribute

    for halfToneNum in range(12*3):
        print(halfToneNum, PitchClass.Get(halfToneNum))
    for halfToneNum in range(-12*3, 0):
        print(halfToneNum, PitchClass.Get(halfToneNum))
    
    print(PitchClass.MinPitchClass)
    print(PitchClass.MaxPitchClass)
