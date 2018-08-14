from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0044   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '4250 约修亚 待机',                     # 9
        '4251 约修亚 移动',                     # 10
        '4252 约修亚 攻击',                     # 11
        '4253 约修亚 被弹开',                   # 12
        '4254 约修亚 倒下',                     # 13
        '4255 约修亚 魔法咏唱',                 # 14
        '4256 约修亚 魔法发动',                 # 15
        '4257 约修亚 胜利',                     # 16
        '4240 雪拉 待机',                       # 17
        '4241 雪拉 移动',                       # 18
        '4242 雪拉 攻击',                       # 19
        '4243 雪拉 被弹开',                     # 20
        '4244 雪拉 倒下',                       # 21
        '4245 雪拉 魔法咏唱',                   # 22
        '4246 雪拉 魔法发动',                   # 23
        '4247 雪拉 胜利',                       # 24
        '4260 奥利维尔 待机',                   # 25
        '4261 奥利维尔 移动',                   # 26
        '4262 奥利维尔 攻击',                   # 27
        '4263 奥利维尔 被弹开',                 # 28
        '4264 奥利维尔 倒下',                   # 29
        '4265 奥利维尔 魔法咏唱',               # 30
        '4266 奥利维尔 魔法发动',               # 31
        '4267 奥利维尔 胜利',                   # 32
        '4230 雪拉18岁 待机',                   # 33
        '4231 雪拉18岁 移动',                   # 34
        '4232 雪拉18岁 攻击',                   # 35
        '4233 雪拉18岁 被弹开',                 # 36
        '4234 雪拉18岁 倒下',                   # 37
        '4235 雪拉18岁 魔法咏唱',               # 38
        '4236 雪拉18岁 魔法发动',               # 39
        '4237 雪拉18岁 胜利',                   # 40
        '4270 乔丝特 待机',                     # 41
        '4271 乔丝特 移动',                     # 42
        '4272 乔丝特 攻击',                     # 43
        '4273 乔丝特 被弹开',                   # 44
        '4274 乔丝特 倒下',                     # 45
        '4275 乔丝特 魔法咏唱',                 # 46
        '4276 乔丝特 魔法发动',                 # 47
        '4277 乔丝特 胜利',                     # 48
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH04250 ._CH',             # 00
        'ED6_DT27/CH04251 ._CH',             # 01
        'ED6_DT27/CH04252 ._CH',             # 02
        'ED6_DT27/CH04253 ._CH',             # 03
        'ED6_DT27/CH04254 ._CH',             # 04
        'ED6_DT27/CH04255 ._CH',             # 05
        'ED6_DT27/CH04256 ._CH',             # 06
        'ED6_DT27/CH04257 ._CH',             # 07
        'ED6_DT27/CH04253 ._CH',             # 08
        'ED6_DT27/CH04253 ._CH',             # 09
        'ED6_DT27/CH04253 ._CH',             # 0A
        'ED6_DT27/CH04253 ._CH',             # 0B
        'ED6_DT27/CH04240 ._CH',             # 0C
        'ED6_DT27/CH04241 ._CH',             # 0D
        'ED6_DT27/CH04242 ._CH',             # 0E
        'ED6_DT27/CH04243 ._CH',             # 0F
        'ED6_DT27/CH04244 ._CH',             # 10
        'ED6_DT27/CH04245 ._CH',             # 11
        'ED6_DT27/CH04246 ._CH',             # 12
        'ED6_DT27/CH04247 ._CH',             # 13
        'ED6_DT27/CH04243 ._CH',             # 14
        'ED6_DT27/CH04243 ._CH',             # 15
        'ED6_DT27/CH04243 ._CH',             # 16
        'ED6_DT27/CH04243 ._CH',             # 17
        'ED6_DT27/CH04260 ._CH',             # 18
        'ED6_DT27/CH04261 ._CH',             # 19
        'ED6_DT27/CH04262 ._CH',             # 1A
        'ED6_DT27/CH04263 ._CH',             # 1B
        'ED6_DT27/CH04264 ._CH',             # 1C
        'ED6_DT27/CH04265 ._CH',             # 1D
        'ED6_DT27/CH04266 ._CH',             # 1E
        'ED6_DT27/CH04267 ._CH',             # 1F
        'ED6_DT27/CH04263 ._CH',             # 20
        'ED6_DT27/CH04263 ._CH',             # 21
        'ED6_DT27/CH04263 ._CH',             # 22
        'ED6_DT27/CH04263 ._CH',             # 23
        'ED6_DT27/CH04230 ._CH',             # 24
        'ED6_DT27/CH04231 ._CH',             # 25
        'ED6_DT27/CH04232 ._CH',             # 26
        'ED6_DT27/CH04233 ._CH',             # 27
        'ED6_DT27/CH04234 ._CH',             # 28
        'ED6_DT27/CH04235 ._CH',             # 29
        'ED6_DT27/CH04236 ._CH',             # 2A
        'ED6_DT27/CH04237 ._CH',             # 2B
        'ED6_DT27/CH04233 ._CH',             # 2C
        'ED6_DT27/CH04233 ._CH',             # 2D
        'ED6_DT27/CH04233 ._CH',             # 2E
        'ED6_DT27/CH04233 ._CH',             # 2F
        'ED6_DT27/CH04270 ._CH',             # 30
        'ED6_DT27/CH04271 ._CH',             # 31
        'ED6_DT27/CH04272 ._CH',             # 32
        'ED6_DT27/CH04273 ._CH',             # 33
        'ED6_DT27/CH04274 ._CH',             # 34
        'ED6_DT27/CH04275 ._CH',             # 35
        'ED6_DT27/CH04276 ._CH',             # 36
        'ED6_DT27/CH04277 ._CH',             # 37
        'ED6_DT27/CH04273 ._CH',             # 38
        'ED6_DT27/CH04273 ._CH',             # 39
        'ED6_DT27/CH04273 ._CH',             # 3A
        'ED6_DT27/CH04273 ._CH',             # 3B
    )

    AddCharChipPat(
        'ED6_DT27/CH04250P._CP',             # 00
        'ED6_DT27/CH04251P._CP',             # 01
        'ED6_DT27/CH04252P._CP',             # 02
        'ED6_DT27/CH04253P._CP',             # 03
        'ED6_DT27/CH04254P._CP',             # 04
        'ED6_DT27/CH04255P._CP',             # 05
        'ED6_DT27/CH04256P._CP',             # 06
        'ED6_DT27/CH04257P._CP',             # 07
        'ED6_DT27/CH04253P._CP',             # 08
        'ED6_DT27/CH04253P._CP',             # 09
        'ED6_DT27/CH04253P._CP',             # 0A
        'ED6_DT27/CH04253P._CP',             # 0B
        'ED6_DT27/CH04240P._CP',             # 0C
        'ED6_DT27/CH04241P._CP',             # 0D
        'ED6_DT27/CH04242P._CP',             # 0E
        'ED6_DT27/CH04243P._CP',             # 0F
        'ED6_DT27/CH04244P._CP',             # 10
        'ED6_DT27/CH04245P._CP',             # 11
        'ED6_DT27/CH04246P._CP',             # 12
        'ED6_DT27/CH04247P._CP',             # 13
        'ED6_DT27/CH04243P._CP',             # 14
        'ED6_DT27/CH04243P._CP',             # 15
        'ED6_DT27/CH04243P._CP',             # 16
        'ED6_DT27/CH04243P._CP',             # 17
        'ED6_DT27/CH04260P._CP',             # 18
        'ED6_DT27/CH04261P._CP',             # 19
        'ED6_DT27/CH04262P._CP',             # 1A
        'ED6_DT27/CH04263P._CP',             # 1B
        'ED6_DT27/CH04264P._CP',             # 1C
        'ED6_DT27/CH04265P._CP',             # 1D
        'ED6_DT27/CH04266P._CP',             # 1E
        'ED6_DT27/CH04267P._CP',             # 1F
        'ED6_DT27/CH04263P._CP',             # 20
        'ED6_DT27/CH04263P._CP',             # 21
        'ED6_DT27/CH04263P._CP',             # 22
        'ED6_DT27/CH04263P._CP',             # 23
        'ED6_DT27/CH04230P._CP',             # 24
        'ED6_DT27/CH04231P._CP',             # 25
        'ED6_DT27/CH04232P._CP',             # 26
        'ED6_DT27/CH04233P._CP',             # 27
        'ED6_DT27/CH04234P._CP',             # 28
        'ED6_DT27/CH04235P._CP',             # 29
        'ED6_DT27/CH04236P._CP',             # 2A
        'ED6_DT27/CH04237P._CP',             # 2B
        'ED6_DT27/CH04233P._CP',             # 2C
        'ED6_DT27/CH04233P._CP',             # 2D
        'ED6_DT27/CH04233P._CP',             # 2E
        'ED6_DT27/CH04233P._CP',             # 2F
        'ED6_DT27/CH04270P._CP',             # 30
        'ED6_DT27/CH04271P._CP',             # 31
        'ED6_DT27/CH04272P._CP',             # 32
        'ED6_DT27/CH04273P._CP',             # 33
        'ED6_DT27/CH04274P._CP',             # 34
        'ED6_DT27/CH04275P._CP',             # 35
        'ED6_DT27/CH04276P._CP',             # 36
        'ED6_DT27/CH04277P._CP',             # 37
        'ED6_DT27/CH04273P._CP',             # 38
        'ED6_DT27/CH04273P._CP',             # 39
        'ED6_DT27/CH04273P._CP',             # 3A
        'ED6_DT27/CH04273P._CP',             # 3B
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 16,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 17,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 18,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 19,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 20,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 21,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 22,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 23,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 24,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 25,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 26,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 52,
        ChipIndex           = 0x34,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 53,
        ChipIndex           = 0x35,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 27,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 54,
        ChipIndex           = 0x36,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 28,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 29,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )


    ScpFunction(
        "Function_0_78A",          # 00, 0
        "Function_1_78B",          # 01, 1
        "Function_2_78C",          # 02, 2
        "Function_3_7A2",          # 03, 3
        "Function_4_80F",          # 04, 4
        "Function_5_825",          # 05, 5
        "Function_6_83B",          # 06, 6
        "Function_7_856",          # 07, 7
        "Function_8_871",          # 08, 8
        "Function_9_88C",          # 09, 9
        "Function_10_8B0",         # 0A, 10
        "Function_11_98D",         # 0B, 11
        "Function_12_9A3",         # 0C, 12
        "Function_13_9DA",         # 0D, 13
        "Function_14_9FA",         # 0E, 14
        "Function_15_A15",         # 0F, 15
        "Function_16_A2B",         # 10, 16
        "Function_17_A62",         # 11, 17
        "Function_18_A82",         # 12, 18
        "Function_19_A9D",         # 13, 19
        "Function_20_AB3",         # 14, 20
        "Function_21_AEA",         # 15, 21
        "Function_22_B05",         # 16, 22
        "Function_23_B20",         # 17, 23
        "Function_24_B36",         # 18, 24
        "Function_25_B6D",         # 19, 25
        "Function_26_B8D",         # 1A, 26
        "Function_27_BA8",         # 1B, 27
        "Function_28_BBE",         # 1C, 28
        "Function_29_BF5",         # 1D, 29
        "Function_30_C15",         # 1E, 30
        "Function_31_C33",         # 1F, 31
        "Function_32_C4C",         # 20, 32
        "Function_33_C65",         # 21, 33
        "Function_34_C7E",         # 22, 34
        "Function_35_C97",         # 23, 35
    )


    def Function_0_78A(): pass

    label("Function_0_78A")

    Return()

    # Function_0_78A end

    def Function_1_78B(): pass

    label("Function_1_78B")

    Return()

    # Function_1_78B end

    def Function_2_78C(): pass

    label("Function_2_78C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A1")
    OP_99(0xFE, 0x0, 0x7, 0x708)
    Jump("Function_2_78C")

    label("loc_7A1")

    Return()

    # Function_2_78C end

    def Function_3_7A2(): pass

    label("Function_3_7A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_80E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_3_7A2")

    label("loc_80E")

    Return()

    # Function_3_7A2 end

    def Function_4_80F(): pass

    label("Function_4_80F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_824")
    OP_99(0xFE, 0x0, 0xB, 0x708)
    Jump("Function_4_80F")

    label("loc_824")

    Return()

    # Function_4_80F end

    def Function_5_825(): pass

    label("Function_5_825")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_83A")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_5_825")

    label("loc_83A")

    Return()

    # Function_5_825 end

    def Function_6_83B(): pass

    label("Function_6_83B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_855")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Sleep(500)
    Jump("Function_6_83B")

    label("loc_855")

    Return()

    # Function_6_83B end

    def Function_7_856(): pass

    label("Function_7_856")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_870")
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Sleep(500)
    Jump("Function_7_856")

    label("loc_870")

    Return()

    # Function_7_856 end

    def Function_8_871(): pass

    label("Function_8_871")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88B")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_8_871")

    label("loc_88B")

    Return()

    # Function_8_871 end

    def Function_9_88C(): pass

    label("Function_9_88C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8AF")
    OP_8D(0xFE, 4000, 20000, 24000, 28000, 1500)
    Jump("Function_9_88C")

    label("loc_8AF")

    Return()

    # Function_9_88C end

    def Function_10_8B0(): pass

    label("Function_10_8B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(90)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(40)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(70)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    Jump("Function_10_8B0")

    label("loc_98C")

    Return()

    # Function_10_8B0 end

    def Function_11_98D(): pass

    label("Function_11_98D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A2")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_11_98D")

    label("loc_9A2")

    Return()

    # Function_11_98D end

    def Function_12_9A3(): pass

    label("Function_12_9A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D9")
    SetChrChipByIndex(0xFE, 5)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 6)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_12_9A3")

    label("loc_9D9")

    Return()

    # Function_12_9A3 end

    def Function_13_9DA(): pass

    label("Function_13_9DA")

    SetChrFlags(0xFE, 0x2)

    label("loc_9DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F9")
    OP_99(0xFE, 0x0, 0x21, 0x7D0)
    Sleep(500)
    Jump("loc_9DF")

    label("loc_9F9")

    Return()

    # Function_13_9DA end

    def Function_14_9FA(): pass

    label("Function_14_9FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A14")
    OP_99(0xFE, 0x0, 0x8, 0x7D0)
    Sleep(500)
    Jump("Function_14_9FA")

    label("loc_A14")

    Return()

    # Function_14_9FA end

    def Function_15_A15(): pass

    label("Function_15_A15")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A2A")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_15_A15")

    label("loc_A2A")

    Return()

    # Function_15_A15 end

    def Function_16_A2B(): pass

    label("Function_16_A2B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A61")
    SetChrChipByIndex(0xFE, 17)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 18)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_16_A2B")

    label("loc_A61")

    Return()

    # Function_16_A2B end

    def Function_17_A62(): pass

    label("Function_17_A62")

    SetChrFlags(0xFE, 0x2)

    label("loc_A67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A81")
    OP_99(0xFE, 0x0, 0xD, 0x7D0)
    Sleep(500)
    Jump("loc_A67")

    label("loc_A81")

    Return()

    # Function_17_A62 end

    def Function_18_A82(): pass

    label("Function_18_A82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9C")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_18_A82")

    label("loc_A9C")

    Return()

    # Function_18_A82 end

    def Function_19_A9D(): pass

    label("Function_19_A9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB2")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_19_A9D")

    label("loc_AB2")

    Return()

    # Function_19_A9D end

    def Function_20_AB3(): pass

    label("Function_20_AB3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE9")
    SetChrChipByIndex(0xFE, 29)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 30)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_20_AB3")

    label("loc_AE9")

    Return()

    # Function_20_AB3 end

    def Function_21_AEA(): pass

    label("Function_21_AEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B04")
    OP_99(0xFE, 0x0, 0xE, 0x7D0)
    Sleep(500)
    Jump("Function_21_AEA")

    label("loc_B04")

    Return()

    # Function_21_AEA end

    def Function_22_B05(): pass

    label("Function_22_B05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B1F")
    OP_99(0xFE, 0x0, 0x8, 0x7D0)
    Sleep(500)
    Jump("Function_22_B05")

    label("loc_B1F")

    Return()

    # Function_22_B05 end

    def Function_23_B20(): pass

    label("Function_23_B20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B35")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_23_B20")

    label("loc_B35")

    Return()

    # Function_23_B20 end

    def Function_24_B36(): pass

    label("Function_24_B36")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B6C")
    SetChrChipByIndex(0xFE, 41)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 42)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_24_B36")

    label("loc_B6C")

    Return()

    # Function_24_B36 end

    def Function_25_B6D(): pass

    label("Function_25_B6D")

    SetChrFlags(0xFE, 0x2)

    label("loc_B72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B8C")
    OP_99(0xFE, 0x0, 0xD, 0x7D0)
    Sleep(500)
    Jump("loc_B72")

    label("loc_B8C")

    Return()

    # Function_25_B6D end

    def Function_26_B8D(): pass

    label("Function_26_B8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA7")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_26_B8D")

    label("loc_BA7")

    Return()

    # Function_26_B8D end

    def Function_27_BA8(): pass

    label("Function_27_BA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBD")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_27_BA8")

    label("loc_BBD")

    Return()

    # Function_27_BA8 end

    def Function_28_BBE(): pass

    label("Function_28_BBE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF4")
    SetChrChipByIndex(0xFE, 53)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 54)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_28_BBE")

    label("loc_BF4")

    Return()

    # Function_28_BBE end

    def Function_29_BF5(): pass

    label("Function_29_BF5")

    SetChrFlags(0xFE, 0x2)

    label("loc_BFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C14")
    OP_99(0xFE, 0x0, 0xD, 0x7D0)
    Sleep(500)
    Jump("loc_BFA")

    label("loc_C14")

    Return()

    # Function_29_BF5 end

    def Function_30_C15(): pass

    label("Function_30_C15")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "你好。\x02",
    )

    Jump("loc_C2E")

    label("loc_C2E")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_C15 end

    def Function_31_C33(): pass

    label("Function_31_C33")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "#1500F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_C33 end

    def Function_32_C4C(): pass

    label("Function_32_C4C")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "#1520F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_C4C end

    def Function_33_C65(): pass

    label("Function_33_C65")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        "#1540F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_C65 end

    def Function_34_C7E(): pass

    label("Function_34_C7E")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "#1640F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_C7E end

    def Function_35_C97(): pass

    label("Function_35_C97")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "#1560F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_C97 end

    SaveToFile()

Try(main)
