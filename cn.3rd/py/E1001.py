from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E1001   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4166.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
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
        '充满活力的女主持人',                   # 9
        '神秘绅士',                             # 10
        '对战对手①',                           # 11
        '对战对手②',                           # 12
        '对战对手③',                           # 13
        '对战对手④',                           # 14
        '对战对手⑤',                           # 15
        '对战对手⑥',                           # 16
        '对战对手⑦',                           # 17
        '对战对手⑧',                           # 18
        '观众',                                 # 19
        '观众',                                 # 20
        '观众',                                 # 21
        '观众',                                 # 22
        '观众',                                 # 23
        '观众',                                 # 24
        '观众',                                 # 25
        '观众',                                 # 26
        '观众',                                 # 27
        '观众',                                 # 28
        '观众',                                 # 29
        '观众',                                 # 30
        '观众',                                 # 31
        '观众',                                 # 32
        '观众',                                 # 33
        '观众',                                 # 34
        '观众',                                 # 35
        '观众',                                 # 36
        '观众',                                 # 37
        '观众',                                 # 38
        '观众',                                 # 39
        '观众',                                 # 40
        '观众',                                 # 41
        '观众',                                 # 42
        '观众',                                 # 43
        '观众',                                 # 44
        '观众',                                 # 45
        '观众',                                 # 46
        '观众',                                 # 47
        '观众',                                 # 48
        '观众',                                 # 49
        '观众',                                 # 50
        '观众',                                 # 51
        '观众',                                 # 52
        '观众',                                 # 53
        '观众',                                 # 54
        '观众',                                 # 55
        '观众',                                 # 56
        '观众',                                 # 57
        '观众',                                 # 58
        '目标用照相机',                         # 59
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
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03930 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01230 ._CH',             # 05
        'ED6_DT07/CH01180 ._CH',             # 06
        'ED6_DT07/CH01490 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03930P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01230P._CP',             # 05
        'ED6_DT07/CH01180P._CP',             # 06
        'ED6_DT07/CH01490P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14660,
        Z                   = 4700,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15770,
        Z                   = 4950,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16860,
        Z                   = 5200,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17850,
        Z                   = 5450,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14670,
        Z                   = 4700,
        Y                   = 1910,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15910,
        Z                   = 4950,
        Y                   = 1830,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16760,
        Z                   = 5200,
        Y                   = 1830,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17780,
        Z                   = 5450,
        Y                   = 1990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = 1830,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14660,
        Z                   = 4700,
        Y                   = 3340,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15770,
        Z                   = 4950,
        Y                   = 3350,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16860,
        Z                   = 5200,
        Y                   = 3310,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17850,
        Z                   = 5450,
        Y                   = 3330,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = 3330,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14660,
        Z                   = 4700,
        Y                   = 4530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15770,
        Z                   = 4950,
        Y                   = 4510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16860,
        Z                   = 5200,
        Y                   = 4540,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17850,
        Z                   = 5450,
        Y                   = 4550,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = 4330,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14660,
        Z                   = 4700,
        Y                   = -17600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15770,
        Z                   = 4950,
        Y                   = -17600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16860,
        Z                   = 5200,
        Y                   = -17600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17850,
        Z                   = 5450,
        Y                   = -17600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = -17600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14670,
        Z                   = 4700,
        Y                   = -16320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15910,
        Z                   = 4950,
        Y                   = -16329,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16760,
        Z                   = 5200,
        Y                   = -16379,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17780,
        Z                   = 5450,
        Y                   = -16290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = -16360,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14660,
        Z                   = 4700,
        Y                   = -14960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15770,
        Z                   = 4950,
        Y                   = -14990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16860,
        Z                   = 5200,
        Y                   = -14940,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17850,
        Z                   = 5450,
        Y                   = -14950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = -14930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14660,
        Z                   = 4700,
        Y                   = -13320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15770,
        Z                   = 4950,
        Y                   = -13310,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16860,
        Z                   = 5200,
        Y                   = -13310,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17850,
        Z                   = 5450,
        Y                   = -13290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = -13280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_74A",          # 00, 0
        "Function_1_756",          # 01, 1
        "Function_2_760",          # 02, 2
        "Function_3_8DD",          # 03, 3
        "Function_4_FC9",          # 04, 4
        "Function_5_1732",         # 05, 5
        "Function_6_3659",         # 06, 6
        "Function_7_4061",         # 07, 7
        "Function_8_40CE",         # 08, 8
        "Function_9_40E3",         # 09, 9
        "Function_10_4178",        # 0A, 10
        "Function_11_41F9",        # 0B, 11
        "Function_12_42EC",        # 0C, 12
        "Function_13_430B",        # 0D, 13
        "Function_14_441C",        # 0E, 14
        "Function_15_452D",        # 0F, 15
        "Function_16_46B6",        # 10, 16
        "Function_17_4727",        # 11, 17
        "Function_18_48B0",        # 12, 18
        "Function_19_4A15",        # 13, 19
        "Function_20_4B1F",        # 14, 20
        "Function_21_4B5A",        # 15, 21
        "Function_22_4C64",        # 16, 22
        "Function_23_4CEE",        # 17, 23
        "Function_24_4DEF",        # 18, 24
        "Function_25_4E4C",        # 19, 25
        "Function_26_4F5D",        # 1A, 26
        "Function_27_506E",        # 1B, 27
        "Function_28_524F",        # 1C, 28
        "Function_29_52A4",        # 1D, 29
        "Function_30_545B",        # 1E, 30
        "Function_31_5624",        # 1F, 31
        "Function_32_5805",        # 20, 32
        "Function_33_5876",        # 21, 33
        "Function_34_59C7",        # 22, 34
        "Function_35_5B1D",        # 23, 35
        "Function_36_5BBF",        # 24, 36
        "Function_37_5BDE",        # 25, 37
        "Function_38_5C8F",        # 26, 38
        "Function_39_5D40",        # 27, 39
        "Function_40_5EDB",        # 28, 40
        "Function_41_5EDC",        # 29, 41
        "Function_42_6077",        # 2A, 42
        "Function_43_6109",        # 2B, 43
        "Function_44_61AC",        # 2C, 44
        "Function_45_61C1",        # 2D, 45
        "Function_46_6252",        # 2E, 46
        "Function_47_62E3",        # 2F, 47
        "Function_48_6374",        # 30, 48
        "Function_49_6389",        # 31, 49
        "Function_50_641A",        # 32, 50
        "Function_51_64AB",        # 33, 51
        "Function_52_6B5F",        # 34, 52
        "Function_53_814A",        # 35, 53
        "Function_54_82B5",        # 36, 54
    )


    def Function_0_74A(): pass

    label("Function_0_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_755")
    Event(0, 3)

    label("loc_755")

    Return()

    # Function_0_74A end

    def Function_1_756(): pass

    label("Function_1_756")

    OP_B1("U4166_2")
    Return()

    # Function_1_756 end

    def Function_2_760(): pass

    label("Function_2_760")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_785")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8C7")

    label("loc_785")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8C7")

    label("loc_79E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8C7")

    label("loc_7B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8C7")

    label("loc_7D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8C7")

    label("loc_7E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_802")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8C7")

    label("loc_802")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8C7")

    label("loc_81B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8C7")

    label("loc_834")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8C7")

    label("loc_84D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_866")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8C7")

    label("loc_866")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8C7")

    label("loc_87F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_898")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8C7")

    label("loc_898")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8C7")

    label("loc_8B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8C7")

    label("loc_8DC")

    Return()

    # Function_2_760 end

    def Function_3_8DD(): pass

    label("Function_3_8DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(0, 80000, 1000, 0)
    OP_67(0, 9300, -10000, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(665, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 80000, 0, 180)
    SetChrFlags(0x11, 0x2000)
    FadeToBright(3000, 0)
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 3)), scpexpr(EXPR_END)), "loc_CA1")

    ChrTalk(    #0
        0x11,
        (
            "#5P……哎呀，欢迎各位。\x01",
            "我从心底感谢大家再次来访。\x02\x03",

            "#5P那么，大家今晚\x01",
            "也愿意陪我们一起开心吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_B46")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B43")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B43")
    OP_28(0x23, 0x4, 0x8)

    ChrTalk(    #1
        0x11,
        (
            "#5P……啊呀，\x01",
            "这不是『里·武术大会\x01",
            "参加许可证』吗？\x02\x03",

            "#5P嗯……\x01",
            "那就交给我吧。\x02",
        )
    )

    Jump("loc_A7B")

    label("loc_A7B")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_3F(0x33D, 1)
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "\x1F\x3D\x03\x07\x00交出。\x02",
    )

    Jump("loc_AB1")

    label("loc_AB1")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(    #3
        0x11,
        (
            "#5P……恩，确实收到了。\x02\x03",

            "从此刻开始，\x01",
            "各位已经获得了\x01",
            "『噩梦模式』的挑战权。\x02\x03",

            "怎么样，\x01",
            "要参加大会吗？\x02",
        )
    )

    Jump("loc_B40")

    label("loc_B40")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_B43")

    Jump("loc_C9E")

    label("loc_B46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_C9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9E")
    OP_28(0x22, 0x4, 0x8)

    ChrTalk(    #4
        0x11,
        (
            "#5P……啊呀，\x01",
            "这不是『里·武术大会\x01",
            "参加许可证』吗？\x02\x03",

            "#5P嗯……\x01",
            "那就交给我吧。\x02",
        )
    )

    Jump("loc_BD6")

    label("loc_BD6")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_3F(0x33D, 1)
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #5
        "\x1F\x3D\x03\x07\x00交出。\x02",
    )

    Jump("loc_C0C")

    label("loc_C0C")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(    #6
        0x11,
        (
            "#5P……恩，确实收到了。\x02\x03",

            "从此刻开始，\x01",
            "各位已经获得了\x01",
            "『困难模式』的挑战权。\x02\x03",

            "怎么样，\x01",
            "要参加大会吗？\x02",
        )
    )

    Jump("loc_C9B")

    label("loc_C9B")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_C9E")

    Jump("loc_E9E")

    label("loc_CA1")

    OP_A2(0x2F13)

    ChrTalk(    #7
        0x11,
        (
            "#5P……哎呀，\x01",
            "欢迎各位大驾光临。\x02\x03",

            "#5P接下来，\x01",
            "我要带领大家前往\x01",
            "身经百战的勇士们聚集的地方……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)

    ChrTalk(    #8
        0x11,
        (
            "#5P顺带一提，\x01",
            "为了配合各位的兴趣\x01",
            "我们准备了某项计划。\x02\x03",

            "#5P要给它起个名字的话……\x01",
            "『里』武术大会――\x01",
            "就这么称呼好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)

    ChrTalk(    #9
        0x11,
        (
            "#5P规则简单明了……\x01",
            "目前在场的各位\x01",
            "将会组成四个人的队伍――\x02\x03",

            "#5P与我们所准备的三支强队\x01",
            "进行连续作战，仅此而已……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)

    ChrTalk(    #10
        0x11,
        (
            "#5P没关系啦，详细情况\x01",
            "只要参加马上就会明白的。\x02\x03",

            "#5P……怎么样？\x01",
            "能不能稍微\x01",
            "陪我们玩玩呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_E9E")

    Sleep(300)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #11
        "\x18\x07\x05参加里·武术大会吗？\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC8")

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【参加】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    Jump("loc_F1B")

    label("loc_F1B")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F38"),
        (1, "loc_F3F"),
        (SWITCH_DEFAULT, "loc_FC5"),
    )


    label("loc_F38")

    Call(0, 4)
    Jump("loc_FC5")

    label("loc_F3F")

    OP_5F(0x0)
    OP_56(0x0)

    ChrTalk(    #12
        0x11,
        (
            "#5P是这样吗……\x01",
            "那可真是遗憾。\x02\x03",

            "#5P那么，\x01",
            "衷心期待各位再次光临……\x02",
        )
    )

    Jump("loc_FA0")

    label("loc_FA0")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_FC5")

    label("loc_FC5")

    Jump("loc_EDB")

    label("loc_FC8")

    Return()

    # Function_3_8DD end

    def Function_4_FC9(): pass

    label("Function_4_FC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_11CC")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C9")

    Menu(
        1,
        380,
        330,
        1,
        (
            "★【普通模式】\x01",      # 0
            "★【困难模式】\x01",      # 1
            "★【噩梦模式】\x01",      # 2
        )
    )

    MenuEnd(0x2)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1047"),
        (1, "loc_10C1"),
        (2, "loc_113B"),
        (SWITCH_DEFAULT, "loc_11B9"),
    )


    label("loc_1047")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #13
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_1098")

    label("loc_1098")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11C6")

    label("loc_10C1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #14
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_1112")

    label("loc_1112")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11C6")

    label("loc_113B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #15
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_118C")

    label("loc_118C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11C6")

    label("loc_11B9")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11C6")

    label("loc_11C6")

    Jump("loc_FE6")

    label("loc_11C9")

    Jump("loc_1731")

    label("loc_11CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D6")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D3")

    Menu(
        1,
        380,
        330,
        1,
        (
            "★【普通模式】\x01",      # 0
            "★【困难模式】\x01",      # 1
            "  【噩梦模式】\x01",      # 2
        )
    )

    MenuEnd(0x2)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1251"),
        (1, "loc_12CB"),
        (2, "loc_1345"),
        (SWITCH_DEFAULT, "loc_13C3"),
    )


    label("loc_1251")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #16
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_12A2")

    label("loc_12A2")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D0")

    label("loc_12CB")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #17
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_131C")

    label("loc_131C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D0")

    label("loc_1345")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #18
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_1396")

    label("loc_1396")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D0")

    label("loc_13C3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D0")

    label("loc_13D0")

    Jump("loc_11F0")

    label("loc_13D3")

    Jump("loc_1731")

    label("loc_13D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1548")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1545")

    Menu(
        1,
        380,
        330,
        1,
        (
            "★【普通模式】\x01",      # 0
            "★【困难模式】\x01",      # 1
        )
    )

    MenuEnd(0x2)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1441"),
        (1, "loc_14BB"),
        (SWITCH_DEFAULT, "loc_1535"),
    )


    label("loc_1441")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #19
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_1492")

    label("loc_1492")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1542")

    label("loc_14BB")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #20
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_150C")

    label("loc_150C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1542")

    label("loc_1535")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1542")

    label("loc_1542")

    Jump("loc_13F3")

    label("loc_1545")

    Jump("loc_1731")

    label("loc_1548")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16C1")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_156C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BE")

    Menu(
        1,
        380,
        330,
        1,
        (
            "★【普通模式】\x01",      # 0
            "  【困难模式】\x01",      # 1
        )
    )

    MenuEnd(0x2)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_15BA"),
        (1, "loc_1634"),
        (SWITCH_DEFAULT, "loc_16AE"),
    )


    label("loc_15BA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #21
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_160B")

    label("loc_160B")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16BB")

    label("loc_1634")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #22
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_1685")

    label("loc_1685")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16BB")

    label("loc_16AE")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16BB")

    label("loc_16BB")

    Jump("loc_156C")

    label("loc_16BE")

    Jump("loc_1731")

    label("loc_16C1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x0)

    ChrTalk(    #23
        0x11,
        (
            "#5P呵呵，明白了。\x02\x03",

            "那么，\x01",
            "我立刻为各位带路。\x02",
        )
    )

    Jump("loc_1715")

    label("loc_1715")

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)

    label("loc_1731")

    Return()

    # Function_4_FC9 end

    def Function_5_1732(): pass

    label("Function_5_1732")

    EventBegin(0x0)
    FadeToDark(2000, 0, -1)
    Sleep(2000)
    OP_1E()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1820")
    OP_AD(0x240141, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1767")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_181D")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17CE"),
        (1, "loc_17DB"),
        (2, "loc_17F0"),
        (SWITCH_DEFAULT, "loc_181A"),
    )


    label("loc_17CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_181A")

    label("loc_17DB")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 53)
    Jump("loc_181A")

    label("loc_17F0")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_181A")

    label("loc_181A")

    Jump("loc_1767")

    label("loc_181D")

    Jump("loc_19D5")

    label("loc_1820")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FC")
    OP_AD(0x240142, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1843")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F9")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18AA"),
        (1, "loc_18B7"),
        (2, "loc_18CC"),
        (SWITCH_DEFAULT, "loc_18F6"),
    )


    label("loc_18AA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F6")

    label("loc_18B7")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 53)
    Jump("loc_18F6")

    label("loc_18CC")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18F6")

    label("loc_18F6")

    Jump("loc_1843")

    label("loc_18F9")

    Jump("loc_19D5")

    label("loc_18FC")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D5")
    OP_AD(0x240143, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_191F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D5")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1986"),
        (1, "loc_1993"),
        (2, "loc_19A8"),
        (SWITCH_DEFAULT, "loc_19D2"),
    )


    label("loc_1986")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D2")

    label("loc_1993")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 54)
    Jump("loc_19D2")

    label("loc_19A8")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19D2")

    label("loc_19D2")

    Jump("loc_191F")

    label("loc_19D5")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A3D")
    OP_6D(18700, 7000, -6450, 0)
    OP_67(0, 2340, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    Jump("loc_1A7A")

    label("loc_1A3D")

    OP_6D(2690, 0, -6500, 0)
    OP_67(0, 17470, -27990, 0)
    OP_6B(730, 0)
    OP_6C(90000, 0)
    OP_6E(554, 0)

    label("loc_1A7A")

    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 11990, 9750, -6500, 270)
    ClearChrFlags(0x11, 0x2000)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 6410, 0, -6500, 270)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    Call(0, 7)
    Sleep(100)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C45")
    Call(0, 11)
    Jump("loc_1CED")

    label("loc_1C45")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C58")
    Call(0, 15)
    Jump("loc_1CED")

    label("loc_1C58")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6B")
    Call(0, 19)
    Jump("loc_1CED")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7E")
    Call(0, 23)
    Jump("loc_1CED")

    label("loc_1C7E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C91")
    Call(0, 27)
    Jump("loc_1CED")

    label("loc_1C91")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA4")
    Call(0, 31)
    Jump("loc_1CED")

    label("loc_1CA4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB7")
    Call(0, 35)
    Jump("loc_1CED")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CCA")
    Call(0, 39)
    Jump("loc_1CED")

    label("loc_1CCA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CDD")
    Call(0, 43)
    Jump("loc_1CED")

    label("loc_1CDD")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CED")
    Call(0, 47)

    label("loc_1CED")

    Sleep(1000)
    OP_22(0xAE, 0x0, 0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2192")
    Sleep(500)

    def lambda_1D2A():
        OP_6D(12830, 1710, -6480, 6000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1D2A)

    def lambda_1D42():
        OP_67(0, 12200, -21480, 6000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1D42)

    def lambda_1D5A():
        OP_6B(2130, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1D5A)
    WaitChrThread(0x10, 0x2)
    Sleep(1000)
    Fade(1000)
    OP_6D(2690, 0, -6500, 0)
    OP_67(0, 17470, -27990, 0)
    OP_6B(730, 0)
    OP_6C(90000, 0)
    OP_6E(554, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E49")

    ChrTalk(    #24
        0x10,
        "#5P好了，大家久等了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#5P今晚将有四位勇士\x01",
            "前来挑战普通模式！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "#5P那么，我马上介绍一下各支队伍！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F6E")

    label("loc_1E49")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDD")

    ChrTalk(    #27
        0x10,
        "#5P好了，大家久等了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#5P今晚将有四位勇士\x01",
            "前来挑战困难模式！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#5P那么，我马上介绍一下双方队伍！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F6E")

    label("loc_1EDD")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6E")

    ChrTalk(    #30
        0x10,
        "#5P好了，大家久等了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#5P今晚将有四位勇士\x01",
            "前来挑战噩梦模式！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        "#5P那么，我马上介绍一下双方队伍！！\x02",
    )

    CloseMessageWindow()

    label("loc_1F6E")

    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Call(0, 51)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FCD")

    ChrTalk(    #33
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "其真面目完全不明。\x01",
            "黑衣人队！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2074")

    label("loc_1FCD")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2022")

    ChrTalk(    #34
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "其真面目完全不明。\x01",
            "黑色猎兵团队！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2074")

    label("loc_2022")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2074")

    ChrTalk(    #35
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "守卫公爵的老练盾牌。\x01",
            "终生现役队！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2074")


    ChrTalk(    #36
        0x10,
        (
            "#5P那么这就开始第１回合！\x01",
            "大家鼓足劲上吧！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#5P现在请两队成员\x01",
            "取出武器摆好架势！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2105")
    OP_43(0x0, 0x0, 0x0, 0xC)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_213C")

    label("loc_2105")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2122")
    OP_43(0x0, 0x0, 0x0, 0x18)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_213C")

    label("loc_2122")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213C")
    OP_43(0x0, 0x0, 0x0, 0x24)
    OP_43(0x0, 0x1, 0x0, 0x8)

    label("loc_213C")

    Sleep(2000)

    ChrTalk(    #38
        0x10,
        "#5P Ready～～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        "#5P#4S Fight！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_283F")

    label("loc_2192")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2412")

    ChrTalk(    #40
        0x10,
        "#5P来吧，英勇地作战吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#5P接下来是第２回合！\x01",
            "在此重新介绍一下双方队伍！！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Call(0, 51)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2280")

    ChrTalk(    #42
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "软绵绵毛茸茸可爱军团。\x01",
            "猿羊队！\x02",
        )
    )

    Jump("loc_227C")

    label("loc_227C")

    CloseMessageWindow()
    Jump("loc_232D")

    label("loc_2280")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22DB")

    ChrTalk(    #43
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "全部为『十三工房』制造。\x01",
            "Rhein Gold队！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232D")

    label("loc_22DB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232D")

    ChrTalk(    #44
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "回归的暴走战车。\x01",
            "奥尔杰尤ＭＫⅡ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232D")


    ChrTalk(    #45
        0x10,
        (
            "#5P现在请两队成员\x01",
            "取出武器摆好架势！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2385")
    OP_43(0x0, 0x0, 0x0, 0x10)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_23BC")

    label("loc_2385")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A2")
    OP_43(0x0, 0x0, 0x0, 0x1C)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_23BC")

    label("loc_23A2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23BC")
    OP_43(0x0, 0x0, 0x0, 0x28)
    OP_43(0x0, 0x1, 0x0, 0x8)

    label("loc_23BC")

    Sleep(2000)

    ChrTalk(    #46
        0x10,
        "#5P Ready～～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#5P#4S Fight！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_283F")

    label("loc_2412")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2593")

    ChrTalk(    #48
        0x10,
        "#5P来吧，英勇地作战吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#5P接下来是第３回合！\x01",
            "在此重新介绍一下双方队伍！！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Call(0, 51)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E7")

    ChrTalk(    #50
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "『泰斗流』的达人组合。\x01",
            "雾香＆瓦鲁特队！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E7")

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "#5P现在请两队成员\x01",
            "取出武器摆好架势！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253D")
    OP_43(0x0, 0x0, 0x0, 0x2C)
    OP_43(0x0, 0x1, 0x0, 0x8)

    label("loc_253D")

    Sleep(2000)

    ChrTalk(    #52
        0x10,
        "#5P Ready～～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        "#5P#4S Fight！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_283F")

    label("loc_2593")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_283F")

    ChrTalk(    #54
        0x10,
        "#5P好，终于到了最终决战！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#5P挑战者队到底能否\x01",
            "获得最后的胜利呢！？！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        "#5P那么来介绍一下最后的队伍！！\x02",
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Call(0, 51)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A7")

    ChrTalk(    #57
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "『噬身之蛇』所属。\x01",
            "基尔巴特＆人形兵器队！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275C")

    label("loc_26A7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2702")

    ChrTalk(    #58
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "其真面目是古代龙！？\x01",
            "神秘小龙宝宝队！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275C")

    label("loc_2702")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275C")

    ChrTalk(    #59
        0x10,
        (
            "#5P对手是西边的红组──\x01",
            "最强最凶恶的二人组！\x01",
            "卡西乌斯＆莱维队！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275C")

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#5P现在请两队成员\x01",
            "取出武器摆好架势！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B5")
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_27EC")

    label("loc_27B5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D2")
    OP_43(0x0, 0x0, 0x0, 0x20)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_27EC")

    label("loc_27D2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27EC")
    OP_43(0x0, 0x0, 0x0, 0x30)
    OP_43(0x0, 0x1, 0x0, 0x8)

    label("loc_27EC")

    Sleep(2000)

    ChrTalk(    #61
        0x10,
        "#5P Ready～～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        "#5P#4S Fight！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    label("loc_283F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2864")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x390, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_2864")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2889")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_2889")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AE")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x392, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_28AE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D3")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_28D3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F8")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x395, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_28F8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291D")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_291D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2942")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_2942")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2967")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_2967")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298C")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x399, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29AE")

    label("loc_298C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29AE")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x39B, 0x0, 0x0, 0x0, 0xFF)

    label("loc_29AE")

    FadeToDark(0, 0, -1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3658")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_29E8"),
        (1, "loc_29F5"),
        (SWITCH_DEFAULT, "loc_2A02"),
    )


    label("loc_29E8")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A02")

    label("loc_29F5")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A02")

    label("loc_2A02")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2A13"),
        (1, "loc_2C6C"),
        (SWITCH_DEFAULT, "loc_3655"),
    )


    label("loc_2A13")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(2690, 0, -6500, 0)
    OP_67(0, 17470, -27990, 0)
    OP_6B(730, 0)
    OP_6C(90000, 0)
    OP_6E(554, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 6410, 0, -6500, 270)
    Call(0, 9)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A89")
    Call(0, 14)
    Jump("loc_2B31")

    label("loc_2A89")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9C")
    Call(0, 18)
    Jump("loc_2B31")

    label("loc_2A9C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AAF")
    Call(0, 22)
    Jump("loc_2B31")

    label("loc_2AAF")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC2")
    Call(0, 26)
    Jump("loc_2B31")

    label("loc_2AC2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD5")
    Call(0, 30)
    Jump("loc_2B31")

    label("loc_2AD5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE8")
    Call(0, 34)
    Jump("loc_2B31")

    label("loc_2AE8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFB")
    Call(0, 38)
    Jump("loc_2B31")

    label("loc_2AFB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0E")
    Call(0, 42)
    Jump("loc_2B31")

    label("loc_2B0E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B21")
    Call(0, 46)
    Jump("loc_2B31")

    label("loc_2B21")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B31")
    Call(0, 50)

    label("loc_2B31")

    Sleep(1000)
    OP_22(0xAE, 0x0, 0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Call(0, 52)
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6B")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B83")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2B83")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B9B")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2B9B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB3")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2BB3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BCB")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2BCB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE3")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2BE3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BFB")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2BFB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C13")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2C13")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2B")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C40")

    label("loc_2C2B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C40")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C40")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3655")

    label("loc_2C6C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(2690, 0, -6500, 0)
    OP_67(0, 17470, -27990, 0)
    OP_6B(730, 0)
    OP_6C(90000, 0)
    OP_6E(554, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 6410, 0, -6500, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 11950, 9750, -6450, 270)
    Call(0, 10)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF8")
    Call(0, 13)
    Jump("loc_2DA0")

    label("loc_2CF8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D0B")
    Call(0, 17)
    Jump("loc_2DA0")

    label("loc_2D0B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1E")
    Call(0, 21)
    Jump("loc_2DA0")

    label("loc_2D1E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D31")
    Call(0, 25)
    Jump("loc_2DA0")

    label("loc_2D31")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D44")
    Call(0, 29)
    Jump("loc_2DA0")

    label("loc_2D44")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D57")
    Call(0, 33)
    Jump("loc_2DA0")

    label("loc_2D57")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6A")
    Call(0, 37)
    Jump("loc_2DA0")

    label("loc_2D6A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7D")
    Call(0, 41)
    Jump("loc_2DA0")

    label("loc_2D7D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D90")
    Call(0, 45)
    Jump("loc_2DA0")

    label("loc_2D90")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DA0")
    Call(0, 49)

    label("loc_2DA0")

    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E3B")

    ChrTalk(    #63
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——终生现役队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#5P……哎呀呀，真遗憾。\x01",
            "挑战者队伍\x01",
            "在第１回合中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_2E3B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EBF")

    ChrTalk(    #65
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——猿羊队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#5P……嗯～很遗憾，\x01",
            "挑战者队伍\x01",
            "在第２回合中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_2EBF")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F53")

    ChrTalk(    #67
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——基尔巴特＆人形兵器队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        (
            "#5P……嗯～非常遗憾，\x01",
            "挑战者队伍\x01",
            "在最终决战中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_2F53")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE1")

    ChrTalk(    #69
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——黑色猎兵团队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "#5P……哎呀呀，真遗憾。\x01",
            "挑战者队伍\x01",
            "在第１回合中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_2FE1")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306A")

    ChrTalk(    #71
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——RheinGold队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#5P……嗯～很遗憾，\x01",
            "挑战者队伍\x01",
            "在第２回合中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_306A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30F8")

    ChrTalk(    #73
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——神秘小龙宝宝队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#5P……嗯～非常遗憾，\x01",
            "挑战者队伍\x01",
            "在最终决战中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_30F8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3182")

    ChrTalk(    #75
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——黑衣人队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#5P……哎呀呀，真遗憾。\x01",
            "挑战者队伍\x01",
            "在第１回合中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_3182")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_320E")

    ChrTalk(    #77
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——奥尔杰尤ＭＫⅡ胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "#5P……嗯～很遗憾，\x01",
            "挑战者队伍\x01",
            "在第２回合中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_320E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_329A")

    ChrTalk(    #79
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——雾香＆瓦鲁特队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "#5P……嗯～很遗憾，\x01",
            "挑战者队伍\x01",
            "在第３回合中败退～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3327")

    label("loc_329A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3327")

    ChrTalk(    #81
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "红组——卡西乌斯＆莱维队胜利～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "#5P……嗯～非常遗憾，\x01",
            "挑战者队伍\x01",
            "在最终决战中败退～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3327")

    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_20(0xBB8)
    Sleep(3000)
    OP_0D()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(0, 80000, 1000, 0)
    OP_67(0, 9300, -10000, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(665, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 80000, 0, 180)
    FadeToBright(4000, 0)
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_347B")

    ChrTalk(    #83
        0x11,
        "#5P……唔，只有这种程度吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        (
            "#5P我觉得各位\x01",
            "应该还能战得更勇猛一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x11,
        (
            "#5P唉，也罢……\x01",
            "衷心期待\x01",
            "各位再次前来参加。\x02",
        )
    )

    Jump("loc_3477")

    label("loc_3477")

    CloseMessageWindow()
    Jump("loc_35FB")

    label("loc_347B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_353F")

    ChrTalk(    #86
        0x11,
        "#5P唔，到此为止了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x11,
        (
            "#5P我觉得各位\x01",
            "应该还能战得更勇猛一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        (
            "#5P唉，也罢……\x01",
            "衷心期待\x01",
            "各位再次前来参加。\x02",
        )
    )

    Jump("loc_353B")

    label("loc_353B")

    CloseMessageWindow()
    Jump("loc_35FB")

    label("loc_353F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35FB")

    ChrTalk(    #89
        0x11,
        (
            "#5P唔，真可惜呢……\x01",
            "只差一步就能成功了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x11,
        (
            "#5P不过，\x01",
            "我相信各位下次\x01",
            "一定能渡过难关。\x02",
        )
    )

    Jump("loc_35D0")

    label("loc_35D0")

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#5P衷心期待\x01",
            "各位再次前来参加。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3655")

    label("loc_3655")

    Jump("loc_29CB")

    label("loc_3658")

    Return()

    # Function_5_1732 end

    def Function_6_3659(): pass

    label("Function_6_3659")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(860, 0, -6420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 930, 0, -6580, 90)
    SetChrPos(0x1, -1310, 0, -5190, 90)
    SetChrPos(0x2, -1310, 0, -6120, 90)
    SetChrPos(0x3, -1310, 0, -7920, 90)
    SetChrPos(0x11, 2500, 0, -6550, 270)
    SetChrPos(0x10, 3500, 0, -5190, 270)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3902")

    ChrTalk(    #92
        0x11,
        "#5P恭喜恭喜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x11,
        (
            "#5P哎呀呀，各位真是\x01",
            "让我们体验到了充分的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x11,
        (
            "#5P这是我的\x01",
            "一点小小心意。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x2E5, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #95
        "\x07\x00得到了\x1F\xE5\x02\x07\x00。\x02",
    )

    Jump("loc_384B")

    label("loc_384B")

    CloseMessageWindow()
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #96
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_3876")

    label("loc_3876")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #97
        0x11,
        (
            "#5P各位已经获得了\x01",
            "挑战『困难模式』的资格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x11,
        (
            "#5P如果找到参加大会的『证明』后，\x01",
            "就请再到这里来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A8")

    label("loc_3902")


    ChrTalk(    #99
        0x11,
        "#5P恭喜恭喜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x11,
        (
            "#5P哎呀呀，各位真是\x01",
            "让我们体验到了充分的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "#5P如果愿意的话，\x01",
            "随时都可以再来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x11,
        "#5P那么，各位贵安……\x02",
    )

    CloseMessageWindow()

    label("loc_39A8")

    Jump("loc_3E15")

    label("loc_39AB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2A")

    ChrTalk(    #103
        0x11,
        "#5P恭喜恭喜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        (
            "#5P哎呀呀，各位真是\x01",
            "让我们体验到了充分的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "#5P这是我的\x01",
            "一点小小心意。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x2E6, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #106
        "\x07\x00得到了\x1F\xE6\x02\x07\x00。\x02",
    )

    Jump("loc_3A71")

    label("loc_3A71")

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #107
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_3A9E")

    label("loc_3A9E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #108
        0x11,
        (
            "#5P各位已经获得了\x01",
            "挑战『噩梦模式』的资格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x11,
        (
            "#5P如果找到参加大会的『证明』后，\x01",
            "就请再到这里来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD0")

    label("loc_3B2A")


    ChrTalk(    #110
        0x11,
        "#5P恭喜恭喜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x11,
        (
            "#5P哎呀呀，各位真是\x01",
            "让我们体验到了充分的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x11,
        (
            "#5P如果愿意的话，\x01",
            "随时都可以再来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x11,
        "#5P那么，各位贵安……\x02",
    )

    CloseMessageWindow()

    label("loc_3BD0")

    Jump("loc_3E15")

    label("loc_3BD3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E15")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D6F")

    ChrTalk(    #114
        0x11,
        "#5P恭喜恭喜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x11,
        (
            "#5P话说回来，\x01",
            "没想到你们竟然能打败那些人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x11,
        (
            "#5P哎呀呀，各位真是\x01",
            "让我大开眼界。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x11,
        "#5P请收下这个。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x2E7, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #118
        "\x07\x00得到了\x1F\xE7\x02\x07\x00。\x02",
    )

    Jump("loc_3CBA")

    label("loc_3CBA")

    CloseMessageWindow()
    AddMira(20000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #119
        "\x07\x00得到了\x07\x02２００００米拉\x07\x00。\x02",
    )

    Jump("loc_3CE7")

    label("loc_3CE7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #120
        0x11,
        (
            "#5P虽然没有更高级的模式了，\x01",
            "不过如果愿意的话，\x01",
            "随时都可以再来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x11,
        "#5P那么，各位贵安……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E15")

    label("loc_3D6F")


    ChrTalk(    #122
        0x11,
        "#5P恭喜恭喜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        (
            "#5P哎呀呀，各位真是\x01",
            "让我们体验到了充分的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x11,
        (
            "#5P如果愿意的话，\x01",
            "随时都可以再来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x11,
        "#5P那么，各位贵安……\x02",
    )

    CloseMessageWindow()

    label("loc_3E15")

    Sleep(600)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_24(0xAE, 0x5A)
    Sleep(300)
    OP_24(0xAE, 0x50)
    Sleep(300)
    OP_24(0xAE, 0x46)
    Sleep(300)
    OP_24(0xAE, 0x3C)
    Sleep(300)
    OP_24(0xAE, 0x32)
    Sleep(300)
    OP_24(0xAE, 0x28)
    Sleep(300)
    OP_24(0xAE, 0x1E)
    Sleep(300)
    OP_24(0xAE, 0x14)
    Sleep(300)
    OP_23(0xAE)
    OP_21()
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #126
        "\x07\x00Episode『里·武术大会』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F89")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F86")
    Sleep(1000)
    OP_28(0x21, 0x4, 0x10)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x22, 0x4, 0x2)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #127
        "\x07\x05已获得『困难模式』的挑战资格。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #128
        (
            "\x07\x05持有某个道具进入『门』\x01",
            "即可进行挑战。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_3F86")

    Jump("loc_4046")

    label("loc_3F89")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4025")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4022")
    Sleep(1000)
    OP_28(0x22, 0x4, 0x10)
    OP_28(0x22, 0x4, 0x20)
    OP_28(0x23, 0x4, 0x2)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #129
        "\x07\x05已获得『噩梦模式』的挑战资格。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #130
        (
            "\x07\x05持有某个道具进入『门』\x01",
            "即可进行挑战。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_4022")

    Jump("loc_4046")

    label("loc_4025")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4046")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4046")
    OP_28(0x23, 0x4, 0x10)
    OP_28(0x23, 0x4, 0x20)

    label("loc_4046")

    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_3659 end

    def Function_7_4061(): pass

    label("Function_7_4061")

    OP_E0(0, 0x48, 0x2)
    OP_E0(1, 0x49, 0x2)
    OP_E0(2, 0x4A, 0x2)
    OP_E0(3, 0x4B, 0x2)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 1020, 0, -11320, 0)
    SetChrPos(0x1, -350, 0, -12560, 0)
    SetChrPos(0x2, 2580, 0, -12560, 0)
    SetChrPos(0x3, 1030, 0, -13650, 0)
    Return()

    # Function_7_4061 end

    def Function_8_40CE(): pass

    label("Function_8_40CE")

    SetChrChipByIndex(0x0, 8)
    SetChrChipByIndex(0x1, 9)
    SetChrChipByIndex(0x2, 10)
    SetChrChipByIndex(0x3, 11)
    Return()

    # Function_8_40CE end

    def Function_9_40E3(): pass

    label("Function_9_40E3")

    OP_E0(0, 0x48, 0x2)
    OP_E0(1, 0x49, 0x2)
    OP_E0(2, 0x4A, 0x2)
    OP_E0(3, 0x4B, 0x2)
    SetChrChipByIndex(0x0, 8)
    SetChrChipByIndex(0x1, 9)
    SetChrChipByIndex(0x2, 10)
    SetChrChipByIndex(0x3, 11)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 1020, 0, -11320, 0)
    SetChrPos(0x1, -350, 0, -12560, 0)
    SetChrPos(0x2, 2580, 0, -12560, 0)
    SetChrPos(0x3, 1030, 0, -13650, 0)
    Return()

    # Function_9_40E3 end

    def Function_10_4178(): pass

    label("Function_10_4178")

    OP_E0(0, 0x48, 0x5)
    OP_E0(1, 0x49, 0x5)
    OP_E0(2, 0x4A, 0x5)
    OP_E0(3, 0x4B, 0x5)
    SetChrSubChip(0x0, 3)
    SetChrSubChip(0x1, 3)
    SetChrSubChip(0x2, 3)
    SetChrSubChip(0x3, 3)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 1020, 0, -11320, 0)
    SetChrPos(0x1, -350, 0, -12560, 0)
    SetChrPos(0x2, 2580, 0, -12560, 0)
    SetChrPos(0x3, 1030, 0, -13650, 0)
    Return()

    # Function_10_4178 end

    def Function_11_41F9(): pass

    label("Function_11_41F9")

    OP_D2(0x270028, 0x27002C, 0xC)
    OP_D2(0x27002A, 0x27002E, 0xD)
    OP_D2(0x2704A2, 0x2704AB, 0xE)
    OP_D2(0x27057C, 0x270583, 0xF)
    OP_D2(0x270028, 0x27002C, 0x10)
    OP_D2(0x27002A, 0x27002E, 0x11)
    OP_D2(0x2704A2, 0x2704AB, 0x12)
    OP_D2(0x27057C, 0x270583, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 13)
    SetChrChipByIndex(0x15, 13)
    SetChrChipByIndex(0x16, 13)
    SetChrChipByIndex(0x17, 13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -1500, 0, -1000, 180)
    SetChrPos(0x15, 3500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    Return()

    # Function_11_41F9 end

    def Function_12_42EC(): pass

    label("Function_12_42EC")

    SetChrChipByIndex(0x12, 14)
    SetChrChipByIndex(0x13, 14)
    SetChrChipByIndex(0x14, 15)
    SetChrChipByIndex(0x15, 15)
    SetChrChipByIndex(0x16, 15)
    SetChrChipByIndex(0x17, 15)
    Return()

    # Function_12_42EC end

    def Function_13_430B(): pass

    label("Function_13_430B")

    OP_D2(0x2704A2, 0x2704AB, 0xC)
    OP_D2(0x27057C, 0x270583, 0xD)
    OP_D2(0x2704A2, 0x2704AB, 0xE)
    OP_D2(0x27057C, 0x270583, 0xF)
    OP_D2(0x270028, 0x27002C, 0x10)
    OP_D2(0x27002A, 0x27002E, 0x11)
    OP_D2(0x2704A2, 0x2704AB, 0x12)
    OP_D2(0x27057C, 0x270583, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 13)
    SetChrChipByIndex(0x15, 13)
    SetChrChipByIndex(0x16, 13)
    SetChrChipByIndex(0x17, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -1500, 0, -1000, 180)
    SetChrPos(0x15, 3500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    Return()

    # Function_13_430B end

    def Function_14_441C(): pass

    label("Function_14_441C")

    OP_D2(0x2704A6, 0x2704AF, 0xC)
    OP_D2(0x270580, 0x270587, 0xD)
    OP_D2(0x2704A6, 0x2704AF, 0xE)
    OP_D2(0x270580, 0x270587, 0xF)
    OP_D2(0x270028, 0x27002C, 0x10)
    OP_D2(0x27002A, 0x27002E, 0x11)
    OP_D2(0x2704A2, 0x2704AB, 0x12)
    OP_D2(0x27057C, 0x270583, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 13)
    SetChrChipByIndex(0x15, 13)
    SetChrChipByIndex(0x16, 13)
    SetChrChipByIndex(0x17, 13)
    SetChrSubChip(0x12, 3)
    SetChrSubChip(0x13, 3)
    SetChrSubChip(0x14, 3)
    SetChrSubChip(0x15, 3)
    SetChrSubChip(0x16, 3)
    SetChrSubChip(0x17, 3)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -1500, 0, -1000, 180)
    SetChrPos(0x15, 3500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    Return()

    # Function_14_441C end

    def Function_15_452D(): pass

    label("Function_15_452D")

    OP_D2(0x9047E, 0x90482, 0xC)
    OP_D2(0x290046, 0x29004A, 0xD)
    OP_D2(0x9008C, 0x90090, 0xE)
    OP_D2(0x90480, 0x90484, 0xF)
    OP_D2(0x290048, 0x29004C, 0x10)
    OP_D2(0x9008E, 0x90092, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 14)
    SetChrChipByIndex(0x15, 14)
    SetChrChipByIndex(0x16, 14)
    SetChrChipByIndex(0x17, 14)
    SetChrChipByIndex(0x18, 14)
    SetChrChipByIndex(0x19, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -500, 0, -1000, 180)
    SetChrPos(0x15, 2500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    SetChrPos(0x18, 500, 0, -1000, 180)
    SetChrPos(0x19, 1500, 0, -1000, 180)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Return()

    # Function_15_452D end

    def Function_16_46B6(): pass

    label("Function_16_46B6")

    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    SetChrChipByIndex(0x12, 15)
    SetChrChipByIndex(0x13, 16)
    SetChrChipByIndex(0x14, 17)
    SetChrChipByIndex(0x15, 17)
    SetChrChipByIndex(0x16, 17)
    SetChrChipByIndex(0x17, 17)
    SetChrChipByIndex(0x18, 17)
    SetChrChipByIndex(0x19, 17)
    SetChrSubChip(0x12, 1)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 1)
    SetChrSubChip(0x15, 1)
    SetChrSubChip(0x16, 1)
    SetChrSubChip(0x17, 1)
    SetChrSubChip(0x18, 1)
    SetChrSubChip(0x19, 1)
    Return()

    # Function_16_46B6 end

    def Function_17_4727(): pass

    label("Function_17_4727")

    OP_D2(0x9047E, 0x90482, 0xC)
    OP_D2(0x290046, 0x29004A, 0xD)
    OP_D2(0x9008C, 0x90090, 0xE)
    OP_D2(0x9008C, 0x90090, 0xF)
    OP_D2(0x9008C, 0x90090, 0x10)
    OP_D2(0x9008C, 0x90090, 0x11)
    OP_D2(0x9008C, 0x90090, 0x12)
    OP_D2(0x9008C, 0x90090, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 14)
    SetChrChipByIndex(0x15, 14)
    SetChrChipByIndex(0x16, 14)
    SetChrChipByIndex(0x17, 14)
    SetChrChipByIndex(0x18, 14)
    SetChrChipByIndex(0x19, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -500, 0, -1000, 180)
    SetChrPos(0x15, 2500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    SetChrPos(0x18, 500, 0, -1000, 180)
    SetChrPos(0x19, 1500, 0, -1000, 180)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Return()

    # Function_17_4727 end

    def Function_18_48B0(): pass

    label("Function_18_48B0")

    OP_D2(0x90486, 0x90487, 0xC)
    OP_D2(0x29004E, 0x29004F, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x9008C, 0x90090, 0xF)
    OP_D2(0x9008C, 0x90090, 0x10)
    OP_D2(0x9008C, 0x90090, 0x11)
    OP_D2(0x9008C, 0x90090, 0x12)
    OP_D2(0x9008C, 0x90090, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 14)
    SetChrChipByIndex(0x15, 14)
    SetChrChipByIndex(0x16, 14)
    SetChrChipByIndex(0x17, 14)
    SetChrChipByIndex(0x18, 14)
    SetChrChipByIndex(0x19, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -500, 0, -1000, 180)
    SetChrPos(0x15, 2500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    SetChrPos(0x18, 500, 0, -1000, 180)
    SetChrPos(0x19, 1500, 0, -1000, 180)
    Return()

    # Function_18_48B0 end

    def Function_19_4A15(): pass

    label("Function_19_4A15")

    OP_D2(0x290779, 0x29077D, 0xC)
    OP_D2(0x29040B, 0x29040F, 0xD)
    OP_D2(0x29040A, 0x29040E, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x12, 1000, 0, 1000, 180)
    SetChrPos(0x13, 0, 0, -2000, 180)
    SetChrPos(0x14, 2000, 0, -2000, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Return()

    # Function_19_4A15 end

    def Function_20_4B1F(): pass

    label("Function_20_4B1F")

    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 14)
    SetChrChipByIndex(0x14, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    Return()

    # Function_20_4B1F end

    def Function_21_4B5A(): pass

    label("Function_21_4B5A")

    OP_D2(0x290779, 0x29077D, 0xC)
    OP_D2(0x29040B, 0x29040F, 0xD)
    OP_D2(0x29040A, 0x29040E, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x12, 1000, 0, 1000, 180)
    SetChrPos(0x13, 0, 0, -2000, 180)
    SetChrPos(0x14, 2000, 0, -2000, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Return()

    # Function_21_4B5A end

    def Function_22_4C64(): pass

    label("Function_22_4C64")

    OP_D2(0x2703AC, 0x2703B6, 0xC)
    OP_D2(0x29040B, 0x29040F, 0xD)
    OP_D2(0x29040A, 0x29040E, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrSubChip(0x12, 3)
    SetChrPos(0x12, 1000, 0, -1000, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x12, 0xFF)
    Return()

    # Function_22_4C64 end

    def Function_23_4CEE(): pass

    label("Function_23_4CEE")

    OP_D2(0x29014C, 0x290150, 0xC)
    OP_D2(0x270029, 0x27002D, 0xD)
    OP_D2(0x29014C, 0x290150, 0xE)
    OP_D2(0x2704C6, 0x2704CF, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 13)
    SetChrChipByIndex(0x15, 13)
    SetChrChipByIndex(0x16, 13)
    SetChrChipByIndex(0x17, 13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -1500, 0, -1000, 180)
    SetChrPos(0x15, 3500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    Return()

    # Function_23_4CEE end

    def Function_24_4DEF(): pass

    label("Function_24_4DEF")

    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    SetChrChipByIndex(0x12, 14)
    SetChrChipByIndex(0x13, 14)
    SetChrChipByIndex(0x14, 15)
    SetChrChipByIndex(0x15, 15)
    SetChrChipByIndex(0x16, 15)
    SetChrChipByIndex(0x17, 15)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    Return()

    # Function_24_4DEF end

    def Function_25_4E4C(): pass

    label("Function_25_4E4C")

    OP_D2(0x29014C, 0x290150, 0xC)
    OP_D2(0x2704C6, 0x2704CF, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 13)
    SetChrChipByIndex(0x15, 13)
    SetChrChipByIndex(0x16, 13)
    SetChrChipByIndex(0x17, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -1500, 0, -1000, 180)
    SetChrPos(0x15, 3500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    Return()

    # Function_25_4E4C end

    def Function_26_4F5D(): pass

    label("Function_26_4F5D")

    OP_D2(0x290154, 0x290155, 0xC)
    OP_D2(0x2704CA, 0x2704D3, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 13)
    SetChrChipByIndex(0x15, 13)
    SetChrChipByIndex(0x16, 13)
    SetChrChipByIndex(0x17, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 3)
    SetChrSubChip(0x15, 3)
    SetChrSubChip(0x16, 3)
    SetChrSubChip(0x17, 3)
    SetChrPos(0x12, 0, 0, -2000, 180)
    SetChrPos(0x13, 2000, 0, -2000, 180)
    SetChrPos(0x14, -1500, 0, -1000, 180)
    SetChrPos(0x15, 3500, 0, -1000, 180)
    SetChrPos(0x16, 0, 0, 0, 180)
    SetChrPos(0x17, 2000, 0, 0, 180)
    Return()

    # Function_26_4F5D end

    def Function_27_506E(): pass

    label("Function_27_506E")

    OP_D2(0x29093B, 0x29093F, 0xC)
    OP_D2(0x290931, 0x290935, 0xD)
    OP_D2(0x29093D, 0x290941, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 12)
    SetChrChipByIndex(0x15, 12)
    SetChrChipByIndex(0x16, 12)
    SetChrChipByIndex(0x17, 12)
    SetChrChipByIndex(0x18, 13)
    SetChrChipByIndex(0x19, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x12, -500, 0, -3000, 180)
    SetChrPos(0x13, 2500, 0, -3000, 180)
    SetChrPos(0x14, -3500, 0, -500, 180)
    SetChrPos(0x15, 5500, 0, -500, 180)
    SetChrPos(0x16, -500, 0, 2000, 180)
    SetChrPos(0x17, 2500, 0, 2000, 180)
    SetChrPos(0x18, -500, 0, -500, 180)
    SetChrPos(0x19, 2500, 0, -500, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Return()

    # Function_27_506E end

    def Function_28_524F(): pass

    label("Function_28_524F")

    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    SetChrChipByIndex(0x12, 14)
    SetChrChipByIndex(0x13, 14)
    SetChrChipByIndex(0x14, 14)
    SetChrChipByIndex(0x15, 14)
    SetChrChipByIndex(0x16, 14)
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    Return()

    # Function_28_524F end

    def Function_29_52A4(): pass

    label("Function_29_52A4")

    OP_D2(0x29093B, 0x29093F, 0xC)
    OP_D2(0x290931, 0x290935, 0xD)
    OP_D2(0x29093D, 0x290941, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 14)
    SetChrChipByIndex(0x13, 14)
    SetChrChipByIndex(0x14, 14)
    SetChrChipByIndex(0x15, 14)
    SetChrChipByIndex(0x16, 14)
    SetChrChipByIndex(0x17, 14)
    SetChrChipByIndex(0x18, 13)
    SetChrChipByIndex(0x19, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x12, -500, 0, -3000, 180)
    SetChrPos(0x13, 2500, 0, -3000, 180)
    SetChrPos(0x14, -3500, 0, -500, 180)
    SetChrPos(0x15, 5500, 0, -500, 180)
    SetChrPos(0x16, -500, 0, 2000, 180)
    SetChrPos(0x17, 2500, 0, 2000, 180)
    SetChrPos(0x18, -500, 0, -500, 180)
    SetChrPos(0x19, 2500, 0, -500, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Return()

    # Function_29_52A4 end

    def Function_30_545B(): pass

    label("Function_30_545B")

    OP_D2(0x29093B, 0x29093F, 0xC)
    OP_D2(0x290931, 0x290935, 0xD)
    OP_D2(0x29093D, 0x290941, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 12)
    SetChrChipByIndex(0x15, 12)
    SetChrChipByIndex(0x16, 12)
    SetChrChipByIndex(0x17, 12)
    SetChrChipByIndex(0x18, 13)
    SetChrChipByIndex(0x19, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x12, -500, 0, -3000, 180)
    SetChrPos(0x13, 2500, 0, -3000, 180)
    SetChrPos(0x14, -3500, 0, -500, 180)
    SetChrPos(0x15, 5500, 0, -500, 180)
    SetChrPos(0x16, -500, 0, 2000, 180)
    SetChrPos(0x17, 2500, 0, 2000, 180)
    SetChrPos(0x18, -500, 0, -500, 180)
    SetChrPos(0x19, 2500, 0, -500, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    Return()

    # Function_30_545B end

    def Function_31_5624(): pass

    label("Function_31_5624")

    OP_D2(0x290909, 0x29090D, 0xC)
    OP_D2(0x29090B, 0x29090F, 0xD)
    OP_D2(0x90244, 0x90248, 0xE)
    OP_D2(0x90246, 0x9024A, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 14)
    SetChrChipByIndex(0x14, 14)
    SetChrChipByIndex(0x15, 14)
    SetChrChipByIndex(0x16, 14)
    SetChrChipByIndex(0x17, 14)
    SetChrChipByIndex(0x18, 14)
    SetChrChipByIndex(0x19, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x12, 1000, 0, -1000, 180)
    SetChrPos(0x13, -500, 0, -2500, 180)
    SetChrPos(0x14, 2500, 0, -2500, 180)
    SetChrPos(0x15, -2000, 0, -500, 180)
    SetChrPos(0x16, 4000, 0, -500, 180)
    SetChrPos(0x17, -500, 0, 1000, 180)
    SetChrPos(0x18, 2500, 0, 1000, 180)
    SetChrPos(0x19, 1000, 0, 1500, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Return()

    # Function_31_5624 end

    def Function_32_5805(): pass

    label("Function_32_5805")

    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 15)
    SetChrChipByIndex(0x14, 15)
    SetChrChipByIndex(0x15, 15)
    SetChrChipByIndex(0x16, 15)
    SetChrChipByIndex(0x17, 15)
    SetChrChipByIndex(0x18, 15)
    SetChrChipByIndex(0x19, 15)
    SetChrSubChip(0x12, 3)
    SetChrSubChip(0x13, 3)
    SetChrSubChip(0x14, 3)
    SetChrSubChip(0x15, 3)
    SetChrSubChip(0x16, 3)
    SetChrSubChip(0x17, 3)
    SetChrSubChip(0x18, 3)
    SetChrSubChip(0x19, 3)
    Return()

    # Function_32_5805 end

    def Function_33_5876(): pass

    label("Function_33_5876")

    OP_D2(0x290909, 0x29090D, 0xC)
    OP_D2(0x29090B, 0x29090F, 0xD)
    OP_D2(0x90244, 0x90248, 0xE)
    OP_D2(0x90246, 0x9024A, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 15)
    SetChrChipByIndex(0x14, 15)
    SetChrChipByIndex(0x15, 15)
    SetChrChipByIndex(0x16, 15)
    SetChrChipByIndex(0x17, 15)
    SetChrChipByIndex(0x18, 15)
    SetChrChipByIndex(0x19, 15)
    SetChrSubChip(0x12, 3)
    SetChrSubChip(0x13, 3)
    SetChrSubChip(0x14, 3)
    SetChrSubChip(0x15, 3)
    SetChrSubChip(0x16, 3)
    SetChrSubChip(0x17, 3)
    SetChrSubChip(0x18, 3)
    SetChrSubChip(0x19, 3)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x12, 1000, 0, -1000, 180)
    SetChrPos(0x13, -500, 0, -2500, 180)
    SetChrPos(0x14, 2500, 0, -2500, 180)
    SetChrPos(0x15, -2000, 0, -500, 180)
    SetChrPos(0x16, 4000, 0, -500, 180)
    SetChrPos(0x17, -500, 0, 1000, 180)
    SetChrPos(0x18, 2500, 0, 1000, 180)
    SetChrPos(0x19, 1000, 0, 1500, 180)
    Return()

    # Function_33_5876 end

    def Function_34_59C7(): pass

    label("Function_34_59C7")

    OP_D2(0x260324, 0x260329, 0xC)
    OP_D2(0x9024C, 0x9024D, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 13)
    SetChrChipByIndex(0x15, 13)
    SetChrChipByIndex(0x16, 13)
    SetChrChipByIndex(0x17, 13)
    SetChrChipByIndex(0x18, 13)
    SetChrChipByIndex(0x19, 13)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x12, 1000, 0, -1000, 180)
    SetChrPos(0x13, -500, 0, -2500, 180)
    SetChrPos(0x14, 2500, 0, -2500, 180)
    SetChrPos(0x15, -2000, 0, -500, 180)
    SetChrPos(0x16, 4000, 0, -500, 180)
    SetChrPos(0x17, -500, 0, 1000, 180)
    SetChrPos(0x18, 2500, 0, 1000, 180)
    SetChrPos(0x19, 1000, 0, 1500, 180)
    SetChrFlags(0x12, 0x800)
    Return()

    # Function_34_59C7 end

    def Function_35_5B1D(): pass

    label("Function_35_5B1D")

    OP_D2(0x70150, 0x70154, 0xC)
    OP_D2(0x7035C, 0x70361, 0xD)
    OP_D2(0x7015A, 0x7015E, 0xE)
    OP_D2(0x2704B4, 0x2704BD, 0xF)
    OP_D2(0x270490, 0x270499, 0x10)
    OP_D2(0x7015A, 0x7015E, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 14)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x12, 2420, 0, -1930, 180)
    SetChrPos(0x13, -340, 0, -1880, 180)
    SetChrPos(0x14, 1120, 0, -320, 180)
    Return()

    # Function_35_5B1D end

    def Function_36_5BBF(): pass

    label("Function_36_5BBF")

    SetChrChipByIndex(0x12, 15)
    SetChrChipByIndex(0x13, 16)
    SetChrChipByIndex(0x14, 17)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    Return()

    # Function_36_5BBF end

    def Function_37_5BDE(): pass

    label("Function_37_5BDE")

    OP_D2(0x2704B4, 0x2704BD, 0xC)
    OP_D2(0x270490, 0x270499, 0xD)
    OP_D2(0x7015A, 0x7015E, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x12, 2420, 0, -1930, 180)
    SetChrPos(0x13, -340, 0, -1880, 180)
    SetChrPos(0x14, 1120, 0, -320, 180)
    Return()

    # Function_37_5BDE end

    def Function_38_5C8F(): pass

    label("Function_38_5C8F")

    OP_D2(0x2704B8, 0x2704C1, 0xC)
    OP_D2(0x270494, 0x27049D, 0xD)
    OP_D2(0x600AE, 0x600B3, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 14)
    SetChrSubChip(0x12, 3)
    SetChrSubChip(0x13, 3)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x12, 2420, 0, -1930, 180)
    SetChrPos(0x13, -340, 0, -1880, 180)
    SetChrPos(0x14, 1120, 0, -320, 180)
    Return()

    # Function_38_5C8F end

    def Function_39_5D40(): pass

    label("Function_39_5D40")

    OP_D2(0x90094, 0x90095, 0xC)
    OP_D2(0x90094, 0x90095, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    OP_A1(0x19, 0x7)
    ClearChrFlags(0x19, 0x100)
    OP_72(0x407, 0x0)
    ExitThread()
    OP_71(0x2007, 0x0)
    ExitThread()
    OP_6F(0x7, 1)
    OP_70(0x7, 0x14)
    OP_D1(25, 0, 180000, 0, 0)
    LoadEffect(0x0, "monster\\ms30600a.eff")
    LoadEffect(0x1, "monster\\ms30600b.eff")
    PlayEffect(0x1, 0x1, 0x19, 950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x19, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x19, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0x19, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x19, 1000, 0, -1000, 180)
    Return()

    # Function_39_5D40 end

    def Function_40_5EDB(): pass

    label("Function_40_5EDB")

    Return()

    # Function_40_5EDB end

    def Function_41_5EDC(): pass

    label("Function_41_5EDC")

    OP_D2(0x90094, 0x90095, 0xC)
    OP_D2(0x90094, 0x90095, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    OP_A1(0x19, 0x7)
    ClearChrFlags(0x19, 0x100)
    OP_72(0x407, 0x0)
    ExitThread()
    OP_71(0x2007, 0x0)
    ExitThread()
    OP_6F(0x7, 1)
    OP_70(0x7, 0x14)
    OP_D1(25, 0, 180000, 0, 0)
    LoadEffect(0x0, "monster\\ms30600a.eff")
    LoadEffect(0x1, "monster\\ms30600b.eff")
    PlayEffect(0x1, 0x1, 0x19, 950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x19, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x19, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0x19, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x19, 1000, 0, -1000, 180)
    Return()

    # Function_41_5EDC end

    def Function_42_6077(): pass

    label("Function_42_6077")

    OP_D2(0x90094, 0x90095, 0xC)
    OP_D2(0x90094, 0x90095, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    OP_A1(0x19, 0x7)
    ClearChrFlags(0x19, 0x100)
    OP_72(0x407, 0x0)
    ExitThread()
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_6F(0x7, 1)
    OP_D1(25, 0, 180000, 0, 0)
    SetChrPos(0x19, 1000, 0, -1000, 180)
    Return()

    # Function_42_6077 end

    def Function_43_6109(): pass

    label("Function_43_6109")

    OP_71(0x407, 0x0)
    ExitThread()
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_D2(0x70379, 0x7037E, 0xC)
    OP_D2(0x27047E, 0x270487, 0xD)
    OP_D2(0x2701C6, 0x2701CB, 0xE)
    OP_D2(0x27022A, 0x270234, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, -340, 0, -1880, 180)
    SetChrPos(0x13, 2420, 0, -1930, 180)
    Return()

    # Function_43_6109 end

    def Function_44_61AC(): pass

    label("Function_44_61AC")

    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    Return()

    # Function_44_61AC end

    def Function_45_61C1(): pass

    label("Function_45_61C1")

    OP_D2(0x70379, 0x7037E, 0xC)
    OP_D2(0x27047E, 0x270487, 0xD)
    OP_D2(0x2701C6, 0x2701CB, 0xE)
    OP_D2(0x27022A, 0x270234, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, -340, 0, -1880, 180)
    SetChrPos(0x13, 2420, 0, -1930, 180)
    Return()

    # Function_45_61C1 end

    def Function_46_6252(): pass

    label("Function_46_6252")

    OP_D2(0x270482, 0x27048B, 0xC)
    OP_D2(0x27022E, 0x270238, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrSubChip(0x12, 3)
    SetChrSubChip(0x13, 3)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, -340, 0, -1880, 180)
    SetChrPos(0x13, 2420, 0, -1930, 180)
    Return()

    # Function_46_6252 end

    def Function_47_62E3(): pass

    label("Function_47_62E3")

    OP_D2(0x2701E6, 0x2701EB, 0xC)
    OP_D2(0x27046C, 0x270475, 0xD)
    OP_D2(0x70148, 0x7014C, 0xE)
    OP_D2(0x27027A, 0x270284, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 14)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x12, -340, 0, -1880, 180)
    SetChrPos(0x13, 2420, 0, -1930, 180)
    Return()

    # Function_47_62E3 end

    def Function_48_6374(): pass

    label("Function_48_6374")

    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    Return()

    # Function_48_6374 end

    def Function_49_6389(): pass

    label("Function_49_6389")

    OP_D2(0x2701E6, 0x2701EB, 0xC)
    OP_D2(0x27046C, 0x270475, 0xD)
    OP_D2(0x70148, 0x7014C, 0xE)
    OP_D2(0x27027A, 0x270284, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x12, -340, 0, -1880, 180)
    SetChrPos(0x13, 2420, 0, -1930, 180)
    Return()

    # Function_49_6389 end

    def Function_50_641A(): pass

    label("Function_50_641A")

    OP_D2(0x270470, 0x270479, 0xC)
    OP_D2(0x27027E, 0x270288, 0xD)
    OP_D2(0x90094, 0x90095, 0xE)
    OP_D2(0x90094, 0x90095, 0xF)
    OP_D2(0x90094, 0x90095, 0x10)
    OP_D2(0x90094, 0x90095, 0x11)
    OP_D2(0x90094, 0x90095, 0x12)
    OP_D2(0x90094, 0x90095, 0x13)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrSubChip(0x12, 3)
    SetChrSubChip(0x13, 3)
    SetChrPos(0x12, -340, 0, -1880, 180)
    SetChrPos(0x13, 2420, 0, -1930, 180)
    Return()

    # Function_50_641A end

    def Function_51_64AB(): pass

    label("Function_51_64AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6527")

    ChrTalk(    #131
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "恋爱暴风乱舞。\x01",
            "约修亚选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6527")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_658A")

    ChrTalk(    #132
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "七耀教会，星杯骑士团所属。\x01",
            "凯文神父等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_658A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65ED")

    ChrTalk(    #133
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "七耀教会，星杯骑士团所属。\x01",
            "莉丝修女等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_65ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6648")

    ChrTalk(    #134
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "蔡斯中央工房所属。\x01",
            "提妲选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6648")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66AF")

    ChrTalk(    #135
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "利贝尔王国，王室亲卫队所属。\x01",
            "尤莉亚上尉等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_66AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6710")

    ChrTalk(    #136
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "帝国军第７机甲师团所属。\x01",
            "穆拉少校等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6710")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6779")

    ChrTalk(    #137
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "运输公司『卡普亚特急便』所属。\x01",
            "乔丝特选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6779")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67E0")

    ChrTalk(    #138
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "杰尼丝王立学院，击剑部所属。\x01",
            "科洛丝选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_67E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6841")

    ChrTalk(    #139
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "游击士协会，正游击士。\x01",
            "约修亚选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6841")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_689E")

    ChrTalk(    #140
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "游击士协会，正游击士。\x01",
            "金选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_689E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6909")

    ChrTalk(    #141
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "漂泊的诗人、稀世之天才演奏家。\x01",
            "奥利维尔选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6909")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_696C")

    ChrTalk(    #142
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "游击士协会，柏斯支部。\x01",
            "亚妮拉丝选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_696C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D1")

    ChrTalk(    #143
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "游击士协会，洛连特支部。\x01",
            "雪拉扎德选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_69D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A32")

    ChrTalk(    #144
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "游击士协会，正游击士。\x01",
            "阿加特选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6A32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A95")

    ChrTalk(    #145
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "游击士协会，正游击士。\x01",
            "艾丝蒂尔选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6A95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B00")

    ChrTalk(    #146
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "王国军旧情报部，原司令、原上校。\x01",
            "理查德选手等四人组！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5E")

    label("loc_6B00")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B5E")

    ChrTalk(    #147
        0x10,
        (
            "#5P东边，苍之挑战者──\x01",
            "『噬身之蛇』的执行者。\x01",
            "歼灭天使玲等四人组！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B5E")

    Return()

    # Function_51_64AB end

    def Function_52_6B5F(): pass

    label("Function_52_6B5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CCC")

    ChrTalk(    #148
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——约修亚队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1E")

    ChrTalk(    #149
        0x10,
        (
            "#5P挑战者——约修亚队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_6C1A")

    label("loc_6C1A")

    CloseMessageWindow()
    Jump("loc_6CC9")

    label("loc_6C1E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C75")

    ChrTalk(    #150
        0x10,
        (
            "#5P挑战者——约修亚队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_6C71")

    label("loc_6C71")

    CloseMessageWindow()
    Jump("loc_6CC9")

    label("loc_6C75")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC9")

    ChrTalk(    #151
        0x10,
        (
            "#5P挑战者——约修亚队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_6CC8")

    label("loc_6CC8")

    CloseMessageWindow()

    label("loc_6CC9")

    Jump("loc_8149")

    label("loc_6CCC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0E")

    ChrTalk(    #152
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——凯文队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D64")

    ChrTalk(    #153
        0x10,
        (
            "#5P挑战者——凯文队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_6D60")

    label("loc_6D60")

    CloseMessageWindow()
    Jump("loc_6E0B")

    label("loc_6D64")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DB9")

    ChrTalk(    #154
        0x10,
        (
            "#5P挑战者——凯文队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_6DB5")

    label("loc_6DB5")

    CloseMessageWindow()
    Jump("loc_6E0B")

    label("loc_6DB9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0B")

    ChrTalk(    #155
        0x10,
        (
            "#5P挑战者——凯文队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_6E0A")

    label("loc_6E0A")

    CloseMessageWindow()

    label("loc_6E0B")

    Jump("loc_8149")

    label("loc_6E0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F50")

    ChrTalk(    #156
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——莉丝队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EA6")

    ChrTalk(    #157
        0x10,
        (
            "#5P挑战者——莉丝队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_6EA2")

    label("loc_6EA2")

    CloseMessageWindow()
    Jump("loc_6F4D")

    label("loc_6EA6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EFB")

    ChrTalk(    #158
        0x10,
        (
            "#5P挑战者——莉丝队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_6EF7")

    label("loc_6EF7")

    CloseMessageWindow()
    Jump("loc_6F4D")

    label("loc_6EFB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F4D")

    ChrTalk(    #159
        0x10,
        (
            "#5P挑战者——莉丝队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_6F4C")

    label("loc_6F4C")

    CloseMessageWindow()

    label("loc_6F4D")

    Jump("loc_8149")

    label("loc_6F50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7092")

    ChrTalk(    #160
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——提妲队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FE8")

    ChrTalk(    #161
        0x10,
        (
            "#5P挑战者——提妲队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_6FE4")

    label("loc_6FE4")

    CloseMessageWindow()
    Jump("loc_708F")

    label("loc_6FE8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_703D")

    ChrTalk(    #162
        0x10,
        (
            "#5P挑战者——提妲队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_7039")

    label("loc_7039")

    CloseMessageWindow()
    Jump("loc_708F")

    label("loc_703D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_708F")

    ChrTalk(    #163
        0x10,
        (
            "#5P挑战者——提妲队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_708E")

    label("loc_708E")

    CloseMessageWindow()

    label("loc_708F")

    Jump("loc_8149")

    label("loc_7092")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71DC")

    ChrTalk(    #164
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——尤莉亚队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712E")

    ChrTalk(    #165
        0x10,
        (
            "#5P挑战者——尤莉亚队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_712A")

    label("loc_712A")

    CloseMessageWindow()
    Jump("loc_71D9")

    label("loc_712E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7185")

    ChrTalk(    #166
        0x10,
        (
            "#5P挑战者——尤莉亚队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_7181")

    label("loc_7181")

    CloseMessageWindow()
    Jump("loc_71D9")

    label("loc_7185")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71D9")

    ChrTalk(    #167
        0x10,
        (
            "#5P挑战者——尤莉亚队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_71D8")

    label("loc_71D8")

    CloseMessageWindow()

    label("loc_71D9")

    Jump("loc_8149")

    label("loc_71DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_731E")

    ChrTalk(    #168
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——穆拉队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7274")

    ChrTalk(    #169
        0x10,
        (
            "#5P挑战者——穆拉队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_7270")

    label("loc_7270")

    CloseMessageWindow()
    Jump("loc_731B")

    label("loc_7274")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C9")

    ChrTalk(    #170
        0x10,
        (
            "#5P挑战者——穆拉队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_72C5")

    label("loc_72C5")

    CloseMessageWindow()
    Jump("loc_731B")

    label("loc_72C9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_731B")

    ChrTalk(    #171
        0x10,
        (
            "#5P挑战者——穆拉队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_731A")

    label("loc_731A")

    CloseMessageWindow()

    label("loc_731B")

    Jump("loc_8149")

    label("loc_731E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7468")

    ChrTalk(    #172
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——乔丝特队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73BA")

    ChrTalk(    #173
        0x10,
        (
            "#5P挑战者——乔丝特队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_73B6")

    label("loc_73B6")

    CloseMessageWindow()
    Jump("loc_7465")

    label("loc_73BA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7411")

    ChrTalk(    #174
        0x10,
        (
            "#5P挑战者——乔丝特队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_740D")

    label("loc_740D")

    CloseMessageWindow()
    Jump("loc_7465")

    label("loc_7411")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7465")

    ChrTalk(    #175
        0x10,
        (
            "#5P挑战者——乔丝特队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_7464")

    label("loc_7464")

    CloseMessageWindow()

    label("loc_7465")

    Jump("loc_8149")

    label("loc_7468")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75B2")

    ChrTalk(    #176
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——科洛丝队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7504")

    ChrTalk(    #177
        0x10,
        (
            "#5P挑战者——科洛丝队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_7500")

    label("loc_7500")

    CloseMessageWindow()
    Jump("loc_75AF")

    label("loc_7504")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_755B")

    ChrTalk(    #178
        0x10,
        (
            "#5P挑战者——科洛丝队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_7557")

    label("loc_7557")

    CloseMessageWindow()
    Jump("loc_75AF")

    label("loc_755B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75AF")

    ChrTalk(    #179
        0x10,
        (
            "#5P挑战者——科洛丝队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_75AE")

    label("loc_75AE")

    CloseMessageWindow()

    label("loc_75AF")

    Jump("loc_8149")

    label("loc_75B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76FC")

    ChrTalk(    #180
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——约修亚队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_764E")

    ChrTalk(    #181
        0x10,
        (
            "#5P挑战者——约修亚队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_764A")

    label("loc_764A")

    CloseMessageWindow()
    Jump("loc_76F9")

    label("loc_764E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76A5")

    ChrTalk(    #182
        0x10,
        (
            "#5P挑战者——约修亚队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_76A1")

    label("loc_76A1")

    CloseMessageWindow()
    Jump("loc_76F9")

    label("loc_76A5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76F9")

    ChrTalk(    #183
        0x10,
        (
            "#5P挑战者——约修亚队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_76F8")

    label("loc_76F8")

    CloseMessageWindow()

    label("loc_76F9")

    Jump("loc_8149")

    label("loc_76FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7836")

    ChrTalk(    #184
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——金队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7790")

    ChrTalk(    #185
        0x10,
        (
            "#5P挑战者——金队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_778C")

    label("loc_778C")

    CloseMessageWindow()
    Jump("loc_7833")

    label("loc_7790")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77E3")

    ChrTalk(    #186
        0x10,
        (
            "#5P挑战者——金队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_77DF")

    label("loc_77DF")

    CloseMessageWindow()
    Jump("loc_7833")

    label("loc_77E3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7833")

    ChrTalk(    #187
        0x10,
        (
            "#5P挑战者——金队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_7832")

    label("loc_7832")

    CloseMessageWindow()

    label("loc_7833")

    Jump("loc_8149")

    label("loc_7836")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7988")

    ChrTalk(    #188
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——奥利维尔队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78D6")

    ChrTalk(    #189
        0x10,
        (
            "#5P挑战者——奥利维尔队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_78D2")

    label("loc_78D2")

    CloseMessageWindow()
    Jump("loc_7985")

    label("loc_78D6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_792F")

    ChrTalk(    #190
        0x10,
        (
            "#5P挑战者——奥利维尔队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_792B")

    label("loc_792B")

    CloseMessageWindow()
    Jump("loc_7985")

    label("loc_792F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7985")

    ChrTalk(    #191
        0x10,
        (
            "#5P挑战者——奥利维尔队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_7984")

    label("loc_7984")

    CloseMessageWindow()

    label("loc_7985")

    Jump("loc_8149")

    label("loc_7988")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ADA")

    ChrTalk(    #192
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——亚妮拉丝队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A28")

    ChrTalk(    #193
        0x10,
        (
            "#5P挑战者——亚妮拉丝队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_7A24")

    label("loc_7A24")

    CloseMessageWindow()
    Jump("loc_7AD7")

    label("loc_7A28")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A81")

    ChrTalk(    #194
        0x10,
        (
            "#5P挑战者——亚妮拉丝队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_7A7D")

    label("loc_7A7D")

    CloseMessageWindow()
    Jump("loc_7AD7")

    label("loc_7A81")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD7")

    ChrTalk(    #195
        0x10,
        (
            "#5P挑战者——亚妮拉丝队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_7AD6")

    label("loc_7AD6")

    CloseMessageWindow()

    label("loc_7AD7")

    Jump("loc_8149")

    label("loc_7ADA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C2C")

    ChrTalk(    #196
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——雪拉扎德队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B7A")

    ChrTalk(    #197
        0x10,
        (
            "#5P挑战者——雪拉扎德队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_7B76")

    label("loc_7B76")

    CloseMessageWindow()
    Jump("loc_7C29")

    label("loc_7B7A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BD3")

    ChrTalk(    #198
        0x10,
        (
            "#5P挑战者——雪拉扎德队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_7BCF")

    label("loc_7BCF")

    CloseMessageWindow()
    Jump("loc_7C29")

    label("loc_7BD3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C29")

    ChrTalk(    #199
        0x10,
        (
            "#5P挑战者——雪拉扎德队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_7C28")

    label("loc_7C28")

    CloseMessageWindow()

    label("loc_7C29")

    Jump("loc_8149")

    label("loc_7C2C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D76")

    ChrTalk(    #200
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——阿加特队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CC8")

    ChrTalk(    #201
        0x10,
        (
            "#5P挑战者——阿加特队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_7CC4")

    label("loc_7CC4")

    CloseMessageWindow()
    Jump("loc_7D73")

    label("loc_7CC8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D1F")

    ChrTalk(    #202
        0x10,
        (
            "#5P挑战者——阿加特队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_7D1B")

    label("loc_7D1B")

    CloseMessageWindow()
    Jump("loc_7D73")

    label("loc_7D1F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D73")

    ChrTalk(    #203
        0x10,
        (
            "#5P挑战者——阿加特队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_7D72")

    label("loc_7D72")

    CloseMessageWindow()

    label("loc_7D73")

    Jump("loc_8149")

    label("loc_7D76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EC8")

    ChrTalk(    #204
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——艾丝蒂尔队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E16")

    ChrTalk(    #205
        0x10,
        (
            "#5P挑战者——艾丝蒂尔队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_7E12")

    label("loc_7E12")

    CloseMessageWindow()
    Jump("loc_7EC5")

    label("loc_7E16")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E6F")

    ChrTalk(    #206
        0x10,
        (
            "#5P挑战者——艾丝蒂尔队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_7E6B")

    label("loc_7E6B")

    CloseMessageWindow()
    Jump("loc_7EC5")

    label("loc_7E6F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EC5")

    ChrTalk(    #207
        0x10,
        (
            "#5P挑战者——艾丝蒂尔队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_7EC4")

    label("loc_7EC4")

    CloseMessageWindow()

    label("loc_7EC5")

    Jump("loc_8149")

    label("loc_7EC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8012")

    ChrTalk(    #208
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——理查德队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F64")

    ChrTalk(    #209
        0x10,
        (
            "#5P挑战者——理查德队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_7F60")

    label("loc_7F60")

    CloseMessageWindow()
    Jump("loc_800F")

    label("loc_7F64")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FBB")

    ChrTalk(    #210
        0x10,
        (
            "#5P挑战者——理查德队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_7FB7")

    label("loc_7FB7")

    CloseMessageWindow()
    Jump("loc_800F")

    label("loc_7FBB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_800F")

    ChrTalk(    #211
        0x10,
        (
            "#5P挑战者——理查德队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_800E")

    label("loc_800E")

    CloseMessageWindow()

    label("loc_800F")

    Jump("loc_8149")

    label("loc_8012")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8149")

    ChrTalk(    #212
        0x10,
        (
            "#5P比赛结束～！！\x01",
            "挑战者——玲队获胜～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A6")

    ChrTalk(    #213
        0x10,
        (
            "#5P挑战者——玲队～\x01",
            "在此称霸\x01",
            "普通模式～！！\x02",
        )
    )

    Jump("loc_80A2")

    label("loc_80A2")

    CloseMessageWindow()
    Jump("loc_8149")

    label("loc_80A6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80F9")

    ChrTalk(    #214
        0x10,
        (
            "#5P挑战者——玲队～\x01",
            "在此称霸\x01",
            "困难模式～！！\x02",
        )
    )

    Jump("loc_80F5")

    label("loc_80F5")

    CloseMessageWindow()
    Jump("loc_8149")

    label("loc_80F9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8149")

    ChrTalk(    #215
        0x10,
        (
            "#5P挑战者——玲队～\x01",
            "在此称霸\x01",
            "噩梦模式～！！\x02",
        )
    )

    Jump("loc_8148")

    label("loc_8148")

    CloseMessageWindow()

    label("loc_8149")

    Return()

    # Function_52_6B5F end

    def Function_53_814A(): pass

    label("Function_53_814A")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #216
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　第１回合、第２回合、最终决战——\x01",
            "　与各自的三个小组对战，并力争胜出。\x01",
            "　战斗败北的话，大会就此宣告结束。\x01",
            "　\x01",
            "　每场比赛结束之后，\x01",
            "　ＨＰ和ＥＰ会完全回复，请务必全力以赴出战。\x01",
            "　（※ＣＰ会维持原状。）\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_82A8")

    label("loc_82A8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_53_814A end

    def Function_54_82B5(): pass

    label("Function_54_82B5")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #217
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　与阻挡在自己面前的小组对战，\x01",
            "　请力争大获全胜。\x01",
            "　战斗败北的话，大会就此宣告结束。\x01",
            "　\x01",
            "　每场比赛结束之后，\x01",
            "　ＨＰ和ＥＰ会完全回复，请务必全力以赴出战。\x01",
            "　（※ＣＰ会维持原状。）\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_83FD")

    label("loc_83FD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_54_82B5 end

    SaveToFile()

Try(main)
