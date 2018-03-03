from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Cheerful Host',                        # 9
        'Mysterious Gentlefriend',              # 10
        'Opponent 1',                           # 11
        'Opponent 2',                           # 12
        'Opponent 3',                           # 13
        'Opponent 4',                           # 14
        'Opponent 5',                           # 15
        'Opponent 6',                           # 16
        'Opponent 7',                           # 17
        'Opponent 8',                           # 18
        'Audience Member',                      # 19
        'Audience Member',                      # 20
        'Audience Member',                      # 21
        'Audience Member',                      # 22
        'Audience Member',                      # 23
        'Audience Member',                      # 24
        'Audience Member',                      # 25
        'Audience Member',                      # 26
        'Audience Member',                      # 27
        'Audience Member',                      # 28
        'Audience Member',                      # 29
        'Audience Member',                      # 30
        'Audience Member',                      # 31
        'Audience Member',                      # 32
        'Audience Member',                      # 33
        'Audience Member',                      # 34
        'Audience Member',                      # 35
        'Audience Member',                      # 36
        'Audience Member',                      # 37
        'Audience Member',                      # 38
        'Audience Member',                      # 39
        'Audience Member',                      # 40
        'Audience Member',                      # 41
        'Audience Member',                      # 42
        'Audience Member',                      # 43
        'Audience Member',                      # 44
        'Audience Member',                      # 45
        'Audience Member',                      # 46
        'Audience Member',                      # 47
        'Audience Member',                      # 48
        'Audience Member',                      # 49
        'Audience Member',                      # 50
        'Audience Member',                      # 51
        'Audience Member',                      # 52
        'Audience Member',                      # 53
        'Audience Member',                      # 54
        'Audience Member',                      # 55
        'Audience Member',                      # 56
        'Audience Member',                      # 57
        'Audience Member',                      # 58
        'Target Camera',                        # 59
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
        "Function_4_10B1",         # 04, 4
        "Function_5_17E0",         # 05, 5
        "Function_6_3C17",         # 06, 6
        "Function_7_4A92",         # 07, 7
        "Function_8_4AFF",         # 08, 8
        "Function_9_4B14",         # 09, 9
        "Function_10_4BA9",        # 0A, 10
        "Function_11_4C2A",        # 0B, 11
        "Function_12_4D1D",        # 0C, 12
        "Function_13_4D3C",        # 0D, 13
        "Function_14_4E4D",        # 0E, 14
        "Function_15_4F5E",        # 0F, 15
        "Function_16_50E7",        # 10, 16
        "Function_17_5158",        # 11, 17
        "Function_18_52E1",        # 12, 18
        "Function_19_5446",        # 13, 19
        "Function_20_5550",        # 14, 20
        "Function_21_558B",        # 15, 21
        "Function_22_5695",        # 16, 22
        "Function_23_571F",        # 17, 23
        "Function_24_5820",        # 18, 24
        "Function_25_587D",        # 19, 25
        "Function_26_598E",        # 1A, 26
        "Function_27_5A9F",        # 1B, 27
        "Function_28_5C80",        # 1C, 28
        "Function_29_5CD5",        # 1D, 29
        "Function_30_5E8C",        # 1E, 30
        "Function_31_6055",        # 1F, 31
        "Function_32_6236",        # 20, 32
        "Function_33_62A7",        # 21, 33
        "Function_34_63F8",        # 22, 34
        "Function_35_654E",        # 23, 35
        "Function_36_65F0",        # 24, 36
        "Function_37_660F",        # 25, 37
        "Function_38_66C0",        # 26, 38
        "Function_39_6771",        # 27, 39
        "Function_40_690C",        # 28, 40
        "Function_41_690D",        # 29, 41
        "Function_42_6AA8",        # 2A, 42
        "Function_43_6B3A",        # 2B, 43
        "Function_44_6BDD",        # 2C, 44
        "Function_45_6BF2",        # 2D, 45
        "Function_46_6C83",        # 2E, 46
        "Function_47_6D14",        # 2F, 47
        "Function_48_6DA5",        # 30, 48
        "Function_49_6DBA",        # 31, 49
        "Function_50_6E4B",        # 32, 50
        "Function_51_6EDC",        # 33, 51
        "Function_52_761F",        # 34, 52
        "Function_53_8CD6",        # 35, 53
        "Function_54_8E7E",        # 36, 54
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
    OP_C4(0x0, 0x20000000)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 3)), scpexpr(EXPR_END)), "loc_C65")

    ChrTalk(    #0
        0x11,
        (
            "#5PAh! Good day. It's nice to see you.\x02\x03",

            "#5PSo, would you like to participate again?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_B22")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1F")
    OP_28(0x23, 0x4, 0x8)

    ChrTalk(    #1
        0x11,
        (
            "#5P...Oh? Is that an invitation I see?\x02\x03",

            "#5PCould I trouble you to hand it over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_3F(0x33D, 1)
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "\x07\x05The \x1F\x3D\x03\x07\x05 was carefully inspected.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(    #3
        0x11,
        (
            "#5PThank you.\x02\x03",

            "You may now challenge the nightmare arena\x01",
            "whenever you see fit.\x02\x03",

            "Well, what would you like to do now?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_B1F")

    Jump("loc_C62")

    label("loc_B22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_C62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C62")
    OP_28(0x22, 0x4, 0x8)

    ChrTalk(    #4
        0x11,
        (
            "#5P...Oh? Is that an invitation I see?\x02\x03",

            "#5PCould I trouble you to hand it over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_3F(0x33D, 1)
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #5
        "\x07\x05The \x1F\x3D\x03\x07\x05 was carefully inspected.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(    #6
        0x11,
        (
            "#5PThank you.\x02\x03",

            "You may now challenge the hard arena\x01",
            "whenever you see fit.\x02\x03",

            "Well, what would you like to do now?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_C62")

    Jump("loc_F58")

    label("loc_C65")

    OP_A2(0x2F13)

    ChrTalk(    #7
        0x11,
        (
            "#5PAh! Good day to you all.\x02\x03",

            "#5PThe place you're about to enter is an arena\x01",
            "where history's strongest warriors gather and\x01",
            "eagerly await new challengers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)

    ChrTalk(    #8
        0x11,
        (
            "#5PAnd today, you will have the opportunity to BE\x01",
            "those challengers. Do what you can to emerge\x01",
            "victorious!\x02\x03",

            "#5PI feel I must warn you, however, that this is a\x01",
            "martial arts tournament like no other--only the\x01",
            "best may compete.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)

    ChrTalk(    #9
        0x11,
        (
            "#5PThe rules are simple. First, the four of you will\x01",
            "form one team and step into the arena.\x02\x03",

            "#5PThere, your team will face off against three\x01",
            "others one after another, with no breaks in\x01",
            "between.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)

    ChrTalk(    #10
        0x11,
        (
            "#5PAs for the rest...I'm sure you'll pick it up as you\x01",
            "go along. Heehee.\x02\x03",

            "#5PSo, what do you say? Would you be interested\x01",
            "in joining us?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F58")

    OP_C4(0x1, 0x20000000)
    Sleep(300)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #11
        "\x18\x07\x05Participate in the Tournament?\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B0")

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Join\x01",      # 0
            "Quit\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FE0"),
        (1, "loc_FE7"),
        (SWITCH_DEFAULT, "loc_10AD"),
    )


    label("loc_FE0")

    Call(0, 4)
    Jump("loc_10AD")

    label("loc_FE7")

    OP_5F(0x0)
    OP_56(0x0)

    ChrTalk(    #12
        0x11,
        (
            "#5PIs that so? Well, that is a shame...\x02\x03",

            "#5PStill, should you change your mind, you know\x01",
            "where to find us. We will be eagerly awaiting\x01",
            "your next visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_10AD")

    label("loc_10AD")

    Jump("loc_FA3")

    label("loc_10B0")

    Return()

    # Function_3_8DD end

    def Function_4_10B1(): pass

    label("Function_4_10B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_12A6")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A3")

    Menu(
        1,
        380,
        330,
        1,
        (
            "★ Normal Arena\x01",         # 0
            "★ Hard Arena\x01",           # 1
            "★ Nightmare Arena\x01",      # 2
        )
    )

    MenuEnd(0x2)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1133"),
        (1, "loc_11A7"),
        (2, "loc_121B"),
        (SWITCH_DEFAULT, "loc_1293"),
    )


    label("loc_1133")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #13
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A0")

    label("loc_11A7")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #14
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A0")

    label("loc_121B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #15
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A0")

    label("loc_1293")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A0")

    label("loc_12A0")

    Jump("loc_10CE")

    label("loc_12A3")

    Jump("loc_17DF")

    label("loc_12A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A2")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149F")

    Menu(
        1,
        380,
        330,
        1,
        (
            "★ Normal Arena\x01",         # 0
            "★ Hard Arena\x01",           # 1
            "   Nightmare Arena\x01",      # 2
        )
    )

    MenuEnd(0x2)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_132F"),
        (1, "loc_13A3"),
        (2, "loc_1417"),
        (SWITCH_DEFAULT, "loc_148F"),
    )


    label("loc_132F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #16
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_149C")

    label("loc_13A3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #17
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_149C")

    label("loc_1417")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #18
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_149C")

    label("loc_148F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_149C")

    label("loc_149C")

    Jump("loc_12CA")

    label("loc_149F")

    Jump("loc_17DF")

    label("loc_14A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1608")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1605")

    Menu(
        1,
        380,
        330,
        1,
        (
            "★ Normal Arena\x01",      # 0
            "★ Hard Arena\x01",        # 1
        )
    )

    MenuEnd(0x2)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_150D"),
        (1, "loc_1581"),
        (SWITCH_DEFAULT, "loc_15F5"),
    )


    label("loc_150D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #19
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1602")

    label("loc_1581")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #20
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1602")

    label("loc_15F5")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1602")

    label("loc_1602")

    Jump("loc_14BF")

    label("loc_1605")

    Jump("loc_17DF")

    label("loc_1608")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1775")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_162C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1772")

    Menu(
        1,
        380,
        330,
        1,
        (
            "★ Normal Arena\x01",      # 0
            "   Hard Arena\x01",        # 1
        )
    )

    MenuEnd(0x2)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_167A"),
        (1, "loc_16EE"),
        (SWITCH_DEFAULT, "loc_1762"),
    )


    label("loc_167A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #21
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_176F")

    label("loc_16EE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)

    ChrTalk(    #22
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_176F")

    label("loc_1762")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_176F")

    label("loc_176F")

    Jump("loc_162C")

    label("loc_1772")

    Jump("loc_17DF")

    label("loc_1775")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x0)

    ChrTalk(    #23
        0x11,
        (
            "#5PSplendid!\x02\x03",

            "Well, then, if you don't mind following me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Call(0, 5)
    Call(0, 5)
    Call(0, 6)

    label("loc_17DF")

    Return()

    # Function_4_10B1 end

    def Function_5_17E0(): pass

    label("Function_5_17E0")

    EventBegin(0x0)
    FadeToDark(2000, 0, -1)
    Sleep(2000)
    OP_1E()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B8")
    OP_AD(0x240141, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1815")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B5")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1866"),
        (1, "loc_1873"),
        (2, "loc_1888"),
        (SWITCH_DEFAULT, "loc_18B2"),
    )


    label("loc_1866")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18B2")

    label("loc_1873")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 53)
    Jump("loc_18B2")

    label("loc_1888")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18B2")

    label("loc_18B2")

    Jump("loc_1815")

    label("loc_18B5")

    Jump("loc_1A41")

    label("loc_18B8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197E")
    OP_AD(0x240142, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197B")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_192C"),
        (1, "loc_1939"),
        (2, "loc_194E"),
        (SWITCH_DEFAULT, "loc_1978"),
    )


    label("loc_192C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1978")

    label("loc_1939")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 53)
    Jump("loc_1978")

    label("loc_194E")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1978")

    label("loc_1978")

    Jump("loc_18DB")

    label("loc_197B")

    Jump("loc_1A41")

    label("loc_197E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A41")
    OP_AD(0x240143, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A41")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19F2"),
        (1, "loc_19FF"),
        (2, "loc_1A14"),
        (SWITCH_DEFAULT, "loc_1A3E"),
    )


    label("loc_19F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A3E")

    label("loc_19FF")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 54)
    Jump("loc_1A3E")

    label("loc_1A14")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A3E")

    label("loc_1A3E")

    Jump("loc_19A1")

    label("loc_1A41")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AA9")
    OP_6D(18700, 7000, -6450, 0)
    OP_67(0, 2340, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    Jump("loc_1AE6")

    label("loc_1AA9")

    OP_6D(2690, 0, -6500, 0)
    OP_67(0, 17470, -27990, 0)
    OP_6B(730, 0)
    OP_6C(90000, 0)
    OP_6E(554, 0)

    label("loc_1AE6")

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
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB1")
    Call(0, 11)
    Jump("loc_1D59")

    label("loc_1CB1")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC4")
    Call(0, 15)
    Jump("loc_1D59")

    label("loc_1CC4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD7")
    Call(0, 19)
    Jump("loc_1D59")

    label("loc_1CD7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEA")
    Call(0, 23)
    Jump("loc_1D59")

    label("loc_1CEA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFD")
    Call(0, 27)
    Jump("loc_1D59")

    label("loc_1CFD")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D10")
    Call(0, 31)
    Jump("loc_1D59")

    label("loc_1D10")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D23")
    Call(0, 35)
    Jump("loc_1D59")

    label("loc_1D23")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D36")
    Call(0, 39)
    Jump("loc_1D59")

    label("loc_1D36")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D49")
    Call(0, 43)
    Jump("loc_1D59")

    label("loc_1D49")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D59")
    Call(0, 47)

    label("loc_1D59")

    Sleep(1000)
    OP_22(0xAE, 0x0, 0x64)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C4(0x0, 0x20000000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2356")
    Sleep(500)

    def lambda_1D9C():
        OP_6D(12830, 1710, -6480, 6000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1D9C)

    def lambda_1DB4():
        OP_67(0, 12200, -21480, 6000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1DB4)

    def lambda_1DCC():
        OP_6B(2130, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1DCC)
    WaitChrThread(0x10, 0x2)
    Sleep(1000)
    Fade(1000)
    OP_6D(2690, 0, -6500, 0)
    OP_67(0, 17470, -27990, 0)
    OP_6B(730, 0)
    OP_6C(90000, 0)
    OP_6E(554, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F1F")

    ChrTalk(    #24
        0x10,
        "#5PIt is now the moment you've all been waiting for!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#5PTonight, four new warriors will be stepping up to\x01",
            "the plate and challenging the normal arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#5PSo let's get right to introducing our fierce fighters,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210D")

    label("loc_1F1F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2015")

    ChrTalk(    #27
        0x10,
        "#5PIt is now the moment you've all been waiting for!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#5PTonight, four new warriors will be stepping up to\x01",
            "the plate and challenging the hard arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#5PSo let's get right to introducing our fierce fighters,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210D")

    label("loc_2015")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_210D")

    ChrTalk(    #30
        0x10,
        "#5PIt is now the moment you've all been waiting for!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#5PTonight, four new warriors will be stepping up to\x01",
            "the plate and challenging the nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "#5PSo let's get right to introducing our fierce fighters,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210D")

    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Call(0, 51)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2186")

    ChrTalk(    #33
        0x10,
        (
            "#5PStanding against them in the red corner, we have \x01",
            "the mysterious Team Men in Black!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2269")

    label("loc_2186")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F1")

    ChrTalk(    #34
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "the mysterious Team Black Jaegers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2269")

    label("loc_21F1")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2269")

    ChrTalk(    #35
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "the aged defenders of the duke, Team Old Toughies!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2269")


    ChrTalk(    #36
        0x10,
        "#5PLet the first round begiiiiiin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        "#5PStep on up and ready your weapons!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E3")
    OP_43(0x0, 0x0, 0x0, 0xC)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_231A")

    label("loc_22E3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2300")
    OP_43(0x0, 0x0, 0x0, 0x18)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_231A")

    label("loc_2300")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231A")
    OP_43(0x0, 0x0, 0x0, 0x24)
    OP_43(0x0, 0x1, 0x0, 0x8)

    label("loc_231A")

    Sleep(2000)

    ChrTalk(    #38
        0x10,
        "#5PReady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        "#5P#4SFIGHT!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_2AF4")

    label("loc_2356")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2624")

    ChrTalk(    #40
        0x10,
        "#5PLet's keep up this momentum!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#5PFirst, allow me to introduce who will be fighting in\x01",
            "the second round!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Call(0, 51)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2469")

    ChrTalk(    #42
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "the adorable-but-deadly Team Creepy Sheep!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_2469")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E4")

    ChrTalk(    #43
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "the Thirteen Factories-manufactured Team Reingold!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_24E4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_255F")

    ChrTalk(    #44
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "the back and deadlier than ever Team Orgueille Mk.II!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255F")


    ChrTalk(    #45
        0x10,
        "#5PStep on up and ready your weapons!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B1")
    OP_43(0x0, 0x0, 0x0, 0x10)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_25E8")

    label("loc_25B1")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25CE")
    OP_43(0x0, 0x0, 0x0, 0x1C)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_25E8")

    label("loc_25CE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E8")
    OP_43(0x0, 0x0, 0x0, 0x28)
    OP_43(0x0, 0x1, 0x0, 0x8)

    label("loc_25E8")

    Sleep(2000)

    ChrTalk(    #46
        0x10,
        "#5PReady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#5P#4SFIGHT!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_2AF4")

    label("loc_2624")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27AB")

    ChrTalk(    #48
        0x10,
        "#5PLet's keep up this momentum!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#5PFirst, allow me to introduce who will be fighting in\x01",
            "the third round!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Call(0, 51)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271F")

    ChrTalk(    #50
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "the deadly martial arts duo, Team Taito!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_271F")

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "#5PStep on up and ready your weapons!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_276F")
    OP_43(0x0, 0x0, 0x0, 0x2C)
    OP_43(0x0, 0x1, 0x0, 0x8)

    label("loc_276F")

    Sleep(2000)

    ChrTalk(    #52
        0x10,
        "#5PReady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        "#5P#4SFIGHT!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_2AF4")

    label("loc_27AB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AF4")

    ChrTalk(    #54
        0x10,
        (
            "#5PThe moment is upon us at last! It is time for the\x01",
            "final round to begiiiin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#5PWill our challengers emerge victorious one last\x01",
            "time? You won't have to wait long to find out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        "#5PWell, allow me to introduce our final teams!\x02",
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Call(0, 51)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2935")

    ChrTalk(    #57
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "the Ouroboros-affiliated Team Gilbert!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A31")

    label("loc_2935")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29AE")

    ChrTalk(    #58
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "what may be an ancient dragon: Team Baby Dragon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A31")

    label("loc_29AE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A31")

    ChrTalk(    #59
        0x10,
        (
            "#5PStanding against them in the red corner, we have\x01",
            "the strongest and deadliest tag team in history:\x01",
            "Team Blades!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A31")

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        "#5PStep on up and ready your weapons!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A84")
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_2ABB")

    label("loc_2A84")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA1")
    OP_43(0x0, 0x0, 0x0, 0x20)
    OP_43(0x0, 0x1, 0x0, 0x8)
    Jump("loc_2ABB")

    label("loc_2AA1")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABB")
    OP_43(0x0, 0x0, 0x0, 0x30)
    OP_43(0x0, 0x1, 0x0, 0x8)

    label("loc_2ABB")

    Sleep(2000)

    ChrTalk(    #61
        0x10,
        "#5PReady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        "#5P#4SFIGHT!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    label("loc_2AF4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B19")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x390, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2B19")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3E")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2B3E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B63")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x392, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2B63")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B88")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2B88")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BAD")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x395, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2BAD")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD2")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2BD2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF7")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2BF7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C1C")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2C1C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C41")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x399, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C63")

    label("loc_2C41")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C63")
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x39B, 0x0, 0x0, 0x0, 0xFF)

    label("loc_2C63")

    FadeToDark(0, 0, -1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C16")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2C9D"),
        (1, "loc_2CAA"),
        (SWITCH_DEFAULT, "loc_2CB7"),
    )


    label("loc_2C9D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CB7")

    label("loc_2CAA")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CB7")

    label("loc_2CB7")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2CC8"),
        (1, "loc_2F21"),
        (SWITCH_DEFAULT, "loc_3C13"),
    )


    label("loc_2CC8")

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
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3E")
    Call(0, 14)
    Jump("loc_2DE6")

    label("loc_2D3E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D51")
    Call(0, 18)
    Jump("loc_2DE6")

    label("loc_2D51")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D64")
    Call(0, 22)
    Jump("loc_2DE6")

    label("loc_2D64")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D77")
    Call(0, 26)
    Jump("loc_2DE6")

    label("loc_2D77")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D8A")
    Call(0, 30)
    Jump("loc_2DE6")

    label("loc_2D8A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9D")
    Call(0, 34)
    Jump("loc_2DE6")

    label("loc_2D9D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB0")
    Call(0, 38)
    Jump("loc_2DE6")

    label("loc_2DB0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC3")
    Call(0, 42)
    Jump("loc_2DE6")

    label("loc_2DC3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DD6")
    Call(0, 46)
    Jump("loc_2DE6")

    label("loc_2DD6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE6")
    Call(0, 50)

    label("loc_2DE6")

    Sleep(1000)
    OP_22(0xAE, 0x0, 0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Call(0, 52)
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E20")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2E20")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E38")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2E38")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E50")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2E50")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E68")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2E68")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E80")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2E80")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E98")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2E98")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB0")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2EB0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC8")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2EC8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EE0")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF5")

    label("loc_2EE0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF5")
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EF5")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C13")

    label("loc_2F21")

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
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FAD")
    Call(0, 13)
    Jump("loc_3055")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC0")
    Call(0, 17)
    Jump("loc_3055")

    label("loc_2FC0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD3")
    Call(0, 21)
    Jump("loc_3055")

    label("loc_2FD3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE6")
    Call(0, 25)
    Jump("loc_3055")

    label("loc_2FE6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF9")
    Call(0, 29)
    Jump("loc_3055")

    label("loc_2FF9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300C")
    Call(0, 33)
    Jump("loc_3055")

    label("loc_300C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_301F")
    Call(0, 37)
    Jump("loc_3055")

    label("loc_301F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3032")
    Call(0, 41)
    Jump("loc_3055")

    label("loc_3032")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3045")
    Call(0, 45)
    Jump("loc_3055")

    label("loc_3045")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3055")
    Call(0, 49)

    label("loc_3055")

    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311D")

    ChrTalk(    #63
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Team Men in Black!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#5POh, what a pity! It looks like our challengers are\x01",
            "going to have to go home on the first round!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_311D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D7")

    ChrTalk(    #65
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Team Creepy Sheep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#5POh, what a pity! It looks like our challengers are\x01",
            "going to have to go home on the second round!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_31D7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3295")

    ChrTalk(    #67
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Team Gilbert!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        (
            "#5POh, what a pity! Our challengers were so close, \x01",
            "but winning the final round was just out of their\x01",
            "reach!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_3295")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_334F")

    ChrTalk(    #69
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Team Black Jaegers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "#5POh, what a pity! It looks like our challengers are\x01",
            "going to have to go home on the first round!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_334F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3405")

    ChrTalk(    #71
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Team Reingold!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#5POh, what a pity! It looks like our challengers are\x01",
            "going to have to go home on the second round!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_3405")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34C7")

    ChrTalk(    #73
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Team Baby Dragon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#5POh, what a pity! Our challengers were so close, \x01",
            "but winning the final round was just out of their\x01",
            "reach!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_34C7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3580")

    ChrTalk(    #75
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Team Old Toughies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#5POh, what a pity! It looks like our challengers are\x01",
            "going to have to go home on the first round!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_3580")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363C")

    ChrTalk(    #77
        0x10,
        (
            "#5PThe match is decided! The winner is ...\x01",
            "Team Orgueille Mk2!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "#5POh, what a pity! It looks like our challengers are\x01",
            "going to have to go home on the second round!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_363C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36ED")

    ChrTalk(    #79
        0x10,
        (
            "#5PThe match is decided! The winner is..\x01",
            "Team Taito!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "#5POh, what a pity! It looks like our challengers are\x01",
            "going to have to go home on the third round!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_36ED")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A7")

    ChrTalk(    #81
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Team Blades!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "#5POh, what a pity! Our challengers were so close, \x01",
            "but winning the final round was just out of their\x01",
            "reach!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A7")

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
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3955")

    ChrTalk(    #83
        0x11,
        "#5P...Oh, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        (
            "#5PI was honestly expecting that you might be able\x01",
            "to put up a little more of a fight, but alas! I was\x01",
            "mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x11,
        (
            "#5PStill, if you ever feel up for having another attempt,\x01",
            "do come back. You will be very much welcomed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB9")

    label("loc_3955")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A7A")

    ChrTalk(    #86
        0x11,
        "#5PWhat a shame...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x11,
        (
            "#5PI was honestly expecting that you might be able\x01",
            "to put up a little more of a fight, but alas! I was\x01",
            "mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        (
            "#5PStill, if you ever feel up for having another attempt,\x01",
            "do come back. You will be very much welcomed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB9")

    label("loc_3A7A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BB9")

    ChrTalk(    #89
        0x11,
        (
            "#5PThis nearly brings a tear to my eye... You were so\x01",
            "close to glory, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x11,
        (
            "#5PStill, I believe you will be able to use what you've\x01",
            "learned here in order to claim victory next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#5PSo by all means come back and take another crack\x01",
            "at it. We'd love to see what you can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB9")

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
    Jump("loc_3C13")

    label("loc_3C13")

    Jump("loc_2C80")

    label("loc_3C16")

    Return()

    # Function_5_17E0 end

    def Function_6_3C17(): pass

    label("Function_6_3C17")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x1, 0x20000000)
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
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4079")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F61")

    ChrTalk(    #92
        0x11,
        "#5PCongratulations on your victory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x11,
        (
            "#5PThat was quite a show of skill! Your matches\x01",
            "were a joy to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x11,
        (
            "#5PThese are but a small token of my appreciation\x01",
            "for making this such a fine tournament.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x2E5, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #95
        "\x07\x05Received \x1F\xE5\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #96
        "\x07\x05Received \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #97
        0x11,
        (
            "#5PYou've now earned the right to challenge the\x01",
            "hard arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x11,
        (
            "#5PYou will still need to find an invitation in order\x01",
            "to do so, however. Should you find one, please\x01",
            "do come back here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4076")

    label("loc_3F61")


    ChrTalk(    #99
        0x11,
        "#5PCongratulations to all of you on your victory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x11,
        (
            "#5PThat was really quite the display of skill. \x01",
            "Your matches were a pleasure to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "#5PIf you feel like fighting here again, please come\x01",
            "back. We will welcome you with open arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x11,
        "#5PUntil then, farewell.\x02",
    )

    CloseMessageWindow()

    label("loc_4076")

    Jump("loc_4731")

    label("loc_4079")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A6")

    ChrTalk(    #103
        0x11,
        "#5PCongratulations to all of you on your victory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        (
            "#5PThat really was quite a show of skill. \x01",
            "Your matches were a joy to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "#5PThese are but a small token of my appreciation\x01",
            "for putting on such a fine show.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x2E6, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #106
        "\x07\x05Received \x1F\xE6\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #107
        "\x07\x05Received \x07\x0210,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #108
        0x11,
        (
            "#5PYou've now earned the right to challenge the\x01",
            "nightmare arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x11,
        (
            "#5PYou will still need to find an invitation in order\x01",
            "to do so, however. Should you find one, please\x01",
            "do come back here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43BB")

    label("loc_42A6")


    ChrTalk(    #110
        0x11,
        "#5PCongratulations to all of you on your victory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x11,
        (
            "#5PThat was really quite the display of skill. \x01",
            "Your matches were a pleasure to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x11,
        (
            "#5PIf you feel like fighting here again, please come\x01",
            "back. We will welcome you with open arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x11,
        "#5PUntil then, farewell.\x02",
    )

    CloseMessageWindow()

    label("loc_43BB")

    Jump("loc_4731")

    label("loc_43BE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4731")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_461C")

    ChrTalk(    #114
        0x11,
        "#5PCongratulations to all of you on your victory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x11,
        (
            "#5PI'm not sure that I expected anyone to ever be\x01",
            "able to defeat those two, but you exceeded even\x01",
            "my most optimistic expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x11,
        "#5PI am astounded, to say the least!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x11,
        "#5PPlease, do accept these.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x2E7, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #118
        "\x07\x05Received \x1F\xE7\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(20000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #119
        "\x07\x05Received \x07\x0220,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #120
        0x11,
        (
            "#5PI'm afraid there are no more arenas for you to \x01",
            "challenge, but should you wish to test your mettle\x01",
            "against the existing ones again, do come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x11,
        "#5PWell, until next time...good day to you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4731")

    label("loc_461C")


    ChrTalk(    #122
        0x11,
        "#5PCongratulations to all of you on your victory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        (
            "#5PThat was really quite the display of skill. \x01",
            "Your matches were a pleasure to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x11,
        (
            "#5PIf you feel like fighting here again, please come\x01",
            "back. We will welcome you with open arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x11,
        "#5PUntil then, farewell.\x02",
    )

    CloseMessageWindow()

    label("loc_4731")

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
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47CD")
    OP_F7(0xB, 0x3, 0x0)
    Jump("loc_47F2")

    label("loc_47CD")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E1")
    OP_F7(0xB, 0x3, 0x1)
    Jump("loc_47F2")

    label("loc_47E1")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47F2")
    OP_F7(0xB, 0x3, 0x2)

    label("loc_47F2")

    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #126
        "\x07\x00Side Story [The Arena] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_490A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4907")
    Sleep(1000)
    OP_28(0x21, 0x4, 0x10)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x22, 0x4, 0x2)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #127
        "\x07\x05It is now possible to take on the hard arena.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #128
        (
            "\x07\x05Entering the door with the required item will\x01",
            "allow you to challenge it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_4907")

    Jump("loc_49FA")

    label("loc_490A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D6")
    Sleep(1000)
    OP_28(0x22, 0x4, 0x10)
    OP_28(0x22, 0x4, 0x20)
    OP_28(0x23, 0x4, 0x2)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #129
        "\x07\x05It is now possible to take on the nightmare arena.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #130
        (
            "\x07\x05Entering the door with the required item will\x01",
            "allow you to challenge it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_49D6")

    Jump("loc_49FA")

    label("loc_49D9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FA")
    OP_28(0x23, 0x4, 0x10)
    OP_28(0x23, 0x4, 0x20)

    label("loc_49FA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x587, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x590, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A77")
    Sleep(1000)
    OP_3F(0x590, 1)
    OP_3E(0x591, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #131
        "\x07\x02Jinu\x07\x05's power has increased.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_A2(0x2C38)

    label("loc_4A77")

    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_3C17 end

    def Function_7_4A92(): pass

    label("Function_7_4A92")

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

    # Function_7_4A92 end

    def Function_8_4AFF(): pass

    label("Function_8_4AFF")

    SetChrChipByIndex(0x0, 8)
    SetChrChipByIndex(0x1, 9)
    SetChrChipByIndex(0x2, 10)
    SetChrChipByIndex(0x3, 11)
    Return()

    # Function_8_4AFF end

    def Function_9_4B14(): pass

    label("Function_9_4B14")

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

    # Function_9_4B14 end

    def Function_10_4BA9(): pass

    label("Function_10_4BA9")

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

    # Function_10_4BA9 end

    def Function_11_4C2A(): pass

    label("Function_11_4C2A")

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

    # Function_11_4C2A end

    def Function_12_4D1D(): pass

    label("Function_12_4D1D")

    SetChrChipByIndex(0x12, 14)
    SetChrChipByIndex(0x13, 14)
    SetChrChipByIndex(0x14, 15)
    SetChrChipByIndex(0x15, 15)
    SetChrChipByIndex(0x16, 15)
    SetChrChipByIndex(0x17, 15)
    Return()

    # Function_12_4D1D end

    def Function_13_4D3C(): pass

    label("Function_13_4D3C")

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

    # Function_13_4D3C end

    def Function_14_4E4D(): pass

    label("Function_14_4E4D")

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

    # Function_14_4E4D end

    def Function_15_4F5E(): pass

    label("Function_15_4F5E")

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

    # Function_15_4F5E end

    def Function_16_50E7(): pass

    label("Function_16_50E7")

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

    # Function_16_50E7 end

    def Function_17_5158(): pass

    label("Function_17_5158")

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

    # Function_17_5158 end

    def Function_18_52E1(): pass

    label("Function_18_52E1")

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

    # Function_18_52E1 end

    def Function_19_5446(): pass

    label("Function_19_5446")

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

    # Function_19_5446 end

    def Function_20_5550(): pass

    label("Function_20_5550")

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

    # Function_20_5550 end

    def Function_21_558B(): pass

    label("Function_21_558B")

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

    # Function_21_558B end

    def Function_22_5695(): pass

    label("Function_22_5695")

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

    # Function_22_5695 end

    def Function_23_571F(): pass

    label("Function_23_571F")

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

    # Function_23_571F end

    def Function_24_5820(): pass

    label("Function_24_5820")

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

    # Function_24_5820 end

    def Function_25_587D(): pass

    label("Function_25_587D")

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

    # Function_25_587D end

    def Function_26_598E(): pass

    label("Function_26_598E")

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

    # Function_26_598E end

    def Function_27_5A9F(): pass

    label("Function_27_5A9F")

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

    # Function_27_5A9F end

    def Function_28_5C80(): pass

    label("Function_28_5C80")

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

    # Function_28_5C80 end

    def Function_29_5CD5(): pass

    label("Function_29_5CD5")

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

    # Function_29_5CD5 end

    def Function_30_5E8C(): pass

    label("Function_30_5E8C")

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

    # Function_30_5E8C end

    def Function_31_6055(): pass

    label("Function_31_6055")

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

    # Function_31_6055 end

    def Function_32_6236(): pass

    label("Function_32_6236")

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

    # Function_32_6236 end

    def Function_33_62A7(): pass

    label("Function_33_62A7")

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

    # Function_33_62A7 end

    def Function_34_63F8(): pass

    label("Function_34_63F8")

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

    # Function_34_63F8 end

    def Function_35_654E(): pass

    label("Function_35_654E")

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

    # Function_35_654E end

    def Function_36_65F0(): pass

    label("Function_36_65F0")

    SetChrChipByIndex(0x12, 15)
    SetChrChipByIndex(0x13, 16)
    SetChrChipByIndex(0x14, 17)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    Return()

    # Function_36_65F0 end

    def Function_37_660F(): pass

    label("Function_37_660F")

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

    # Function_37_660F end

    def Function_38_66C0(): pass

    label("Function_38_66C0")

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

    # Function_38_66C0 end

    def Function_39_6771(): pass

    label("Function_39_6771")

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

    # Function_39_6771 end

    def Function_40_690C(): pass

    label("Function_40_690C")

    Return()

    # Function_40_690C end

    def Function_41_690D(): pass

    label("Function_41_690D")

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

    # Function_41_690D end

    def Function_42_6AA8(): pass

    label("Function_42_6AA8")

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

    # Function_42_6AA8 end

    def Function_43_6B3A(): pass

    label("Function_43_6B3A")

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

    # Function_43_6B3A end

    def Function_44_6BDD(): pass

    label("Function_44_6BDD")

    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    Return()

    # Function_44_6BDD end

    def Function_45_6BF2(): pass

    label("Function_45_6BF2")

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

    # Function_45_6BF2 end

    def Function_46_6C83(): pass

    label("Function_46_6C83")

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

    # Function_46_6C83 end

    def Function_47_6D14(): pass

    label("Function_47_6D14")

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

    # Function_47_6D14 end

    def Function_48_6DA5(): pass

    label("Function_48_6DA5")

    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    Return()

    # Function_48_6DA5 end

    def Function_49_6DBA(): pass

    label("Function_49_6DBA")

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

    # Function_49_6DBA end

    def Function_50_6E4B(): pass

    label("Function_50_6E4B")

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

    # Function_50_6E4B end

    def Function_51_6EDC(): pass

    label("Function_51_6EDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F57")

    ChrTalk(    #132
        0x10,
        (
            "#5PIn the blue corner, we have Joshua Bright\x01",
            "and his lovely ladies!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_6F57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FC9")

    ChrTalk(    #133
        0x10,
        (
            "#5PIn the blue corner, we are led by Father Kevin\x01",
            "Graham of the Septian Church's Gralsritter!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_6FC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_703A")

    ChrTalk(    #134
        0x10,
        (
            "#5PIn the blue corner, we are led by Sister Ries\x01",
            "Argent of the Septian Church's Gralsritter!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_703A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_709A")

    ChrTalk(    #135
        0x10,
        (
            "#5PIn the blue corner, we are led by Tita Russell\x01",
            "of Zeiss Central Factory!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_709A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7102")

    ChrTalk(    #136
        0x10,
        (
            "#5PIn the blue corner, we are led by Captain Julia\x01",
            "Schwarz of Liberl's Royal Guard!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_7102")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_717D")

    ChrTalk(    #137
        0x10,
        (
            "#5PIn the blue corner, we are led by Major Mueller\x01",
            "Vander of the Imperial Army's 7th Armored Division!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_717D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E3")

    ChrTalk(    #138
        0x10,
        (
            "#5PIn the blue corner, we are led by Josette\x01",
            "Capua of the Capua Delivery Service!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_71E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724D")

    ChrTalk(    #139
        0x10,
        (
            "#5PIn the blue corner, we are led by Kloe Rinz\x01",
            "of Jenis Royal Academy's Fencing Club!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_724D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B7")

    ChrTalk(    #140
        0x10,
        (
            "#5PIn the blue corner, we are led by senior bracer\x01",
            "Joshua Bright of the Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_72B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_731E")

    ChrTalk(    #141
        0x10,
        (
            "#5PIn the blue corner, we are led by senior bracer\x01",
            "Zin Vathek of the Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_731E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_738B")

    ChrTalk(    #142
        0x10,
        (
            "#5PIn the blue corner, we are led by wandering poet\x01",
            "and genius musician Olivier Lenheim!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_738B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73FC")

    ChrTalk(    #143
        0x10,
        (
            "#5PIn the blue corner, we are led by an ace of the\x01",
            "Bose Bracer Guild branch, Anelace Elfead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_73FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7472")

    ChrTalk(    #144
        0x10,
        (
            "#5PIn the blue corner, we are led by an ace of the\x01",
            "Rolent Bracer Guild branch, Scherazard Harvey!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_7472")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74DC")

    ChrTalk(    #145
        0x10,
        (
            "#5PIn the blue corner, we are led by senior bracer\x01",
            "Agate Crosner of the Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_74DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7547")

    ChrTalk(    #146
        0x10,
        (
            "#5PIn the blue corner, we are led by senior bracer\x01",
            "Estelle Bright of the Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_7547")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C2")

    ChrTalk(    #147
        0x10,
        (
            "#5PIn the blue corner, we are led by former colonel\x01",
            "Richard of the Royal Army's Intelligence Division!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761E")

    label("loc_75C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_761E")

    ChrTalk(    #148
        0x10,
        (
            "#5PIn the blue corner, we are led by Ouroboros'\x01",
            "Angel of Slaughter, Renne!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_761E")

    Return()

    # Function_51_6EDC end

    def Function_52_761F(): pass

    label("Function_52_761F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7791")

    ChrTalk(    #149
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Joshua's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76E3")

    ChrTalk(    #150
        0x10,
        (
            "#5PThey've done it! Joshua's team has conquered the \x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_778E")

    label("loc_76E3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7737")

    ChrTalk(    #151
        0x10,
        (
            "#5PThey've done it! Joshua's team has conquered the\x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_778E")

    label("loc_7737")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_778E")

    ChrTalk(    #152
        0x10,
        (
            "#5PThey've done it! Joshua's team has conquered the \x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_778E")

    Jump("loc_8CD5")

    label("loc_7791")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78FA")

    ChrTalk(    #153
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Father Graham's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_783F")

    ChrTalk(    #154
        0x10,
        (
            "#5PThey've done it! Father Graham's team has\x01",
            "conquered the normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78F7")

    label("loc_783F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_789A")

    ChrTalk(    #155
        0x10,
        (
            "#5PThey've done it! Father Graham's team has\x01",
            "conquered the hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78F7")

    label("loc_789A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78F7")

    ChrTalk(    #156
        0x10,
        (
            "#5PThey've done it! Father Graham's team has\x01",
            "conquered the nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78F7")

    Jump("loc_8CD5")

    label("loc_78FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A57")

    ChrTalk(    #157
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Sister Ries' team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A2")

    ChrTalk(    #158
        0x10,
        (
            "#5PThey've done it! Sister Ries' team has conquered\x01",
            "the normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A54")

    label("loc_79A2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79FA")

    ChrTalk(    #159
        0x10,
        (
            "#5PThey've done it! Sister Ries' team has conquered\x01",
            "the hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A54")

    label("loc_79FA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A54")

    ChrTalk(    #160
        0x10,
        (
            "#5PThey've done it! Sister Ries' team has conquered\x01",
            "the nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A54")

    Jump("loc_8CD5")

    label("loc_7A57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B9F")

    ChrTalk(    #161
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Tita's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AF4")

    ChrTalk(    #162
        0x10,
        (
            "#5PThey've done it! Tita's team has conquered the \x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B9C")

    label("loc_7AF4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B47")

    ChrTalk(    #163
        0x10,
        (
            "#5PThey've done it! Tita's team has conquered the \x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B9C")

    label("loc_7B47")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B9C")

    ChrTalk(    #164
        0x10,
        (
            "#5PThey've done it! Tita's team has conquered the \x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B9C")

    Jump("loc_8CD5")

    label("loc_7B9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D10")

    ChrTalk(    #165
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Captain Schwarz's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C51")

    ChrTalk(    #166
        0x10,
        (
            "#5PThey've done it! Captain Schwarz's team has\x01",
            "conquered the normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D0D")

    label("loc_7C51")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CAE")

    ChrTalk(    #167
        0x10,
        (
            "#5PThey've done it! Captain Schwarz's team has\x01",
            "conquered the hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D0D")

    label("loc_7CAE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D0D")

    ChrTalk(    #168
        0x10,
        (
            "#5PThey've done it! Captain Schwarz's team has\x01",
            "conquered the nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D0D")

    Jump("loc_8CD5")

    label("loc_7D10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E75")

    ChrTalk(    #169
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Major Vander's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DBC")

    ChrTalk(    #170
        0x10,
        (
            "#5PThey've done it! Major Vander's team has conquered\x01",
            "the normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E72")

    label("loc_7DBC")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E16")

    ChrTalk(    #171
        0x10,
        (
            "#5PThey've done it! Major Vander's team has conquered\x01",
            "the hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E72")

    label("loc_7E16")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E72")

    ChrTalk(    #172
        0x10,
        (
            "#5PThey've done it! Major Vander's team has conquered\x01",
            "the nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E72")

    Jump("loc_8CD5")

    label("loc_7E75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC9")

    ChrTalk(    #173
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Josette's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F18")

    ChrTalk(    #174
        0x10,
        (
            "#5PThey've done it! Josette's team has conquered the \x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FC6")

    label("loc_7F18")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F6E")

    ChrTalk(    #175
        0x10,
        (
            "#5PThey've done it! Josette's team has conquered the \x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FC6")

    label("loc_7F6E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC6")

    ChrTalk(    #176
        0x10,
        (
            "#5PThey've done it! Josette's team has conquered the \x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC6")

    Jump("loc_8CD5")

    label("loc_7FC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8111")

    ChrTalk(    #177
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Kloe's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8066")

    ChrTalk(    #178
        0x10,
        (
            "#5PThey've done it! Kloe's team has conquered the \x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_810E")

    label("loc_8066")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80B9")

    ChrTalk(    #179
        0x10,
        (
            "#5PThey've done it! Kloe's team has conquered the \x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_810E")

    label("loc_80B9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810E")

    ChrTalk(    #180
        0x10,
        (
            "#5PThey've done it! Kloe's team has conquered the \x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_810E")

    Jump("loc_8CD5")

    label("loc_8111")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8261")

    ChrTalk(    #181
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Joshua's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B2")

    ChrTalk(    #182
        0x10,
        (
            "#5PThey've done it! Joshua's team has conquered the \x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_825E")

    label("loc_81B2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8207")

    ChrTalk(    #183
        0x10,
        (
            "#5PThey've done it! Joshua's team has conquered the \x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_825E")

    label("loc_8207")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_825E")

    ChrTalk(    #184
        0x10,
        (
            "#5PThey've done it! Joshua's team has conquered the \x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_825E")

    Jump("loc_8CD5")

    label("loc_8261")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83A5")

    ChrTalk(    #185
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Zin's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82FC")

    ChrTalk(    #186
        0x10,
        (
            "#5PThey've done it! Zin's team has conquered the \x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83A2")

    label("loc_82FC")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834E")

    ChrTalk(    #187
        0x10,
        (
            "#5PThey've done it! Zin's team has conquered the \x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83A2")

    label("loc_834E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83A2")

    ChrTalk(    #188
        0x10,
        (
            "#5PThey've done it! Zin's team has conquered the \x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83A2")

    Jump("loc_8CD5")

    label("loc_83A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84F6")

    ChrTalk(    #189
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Olivier's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8447")

    ChrTalk(    #190
        0x10,
        (
            "#5PThey've done it! Olivier's team has conquered the\x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84F3")

    label("loc_8447")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_849C")

    ChrTalk(    #191
        0x10,
        (
            "#5PThey've done it! Olivier's team has conquered the\x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84F3")

    label("loc_849C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84F3")

    ChrTalk(    #192
        0x10,
        (
            "#5PThey've done it! Olivier's team has conquered the\x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84F3")

    Jump("loc_8CD5")

    label("loc_84F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8647")

    ChrTalk(    #193
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Anelace's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8598")

    ChrTalk(    #194
        0x10,
        (
            "#5PThey've done it! Anelace's team has conquered the\x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8644")

    label("loc_8598")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85ED")

    ChrTalk(    #195
        0x10,
        (
            "#5PThey've done it! Anelace's team has conquered the\x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8644")

    label("loc_85ED")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8644")

    ChrTalk(    #196
        0x10,
        (
            "#5PThey've done it! Anelace's team has conquered the\x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8644")

    Jump("loc_8CD5")

    label("loc_8647")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87A4")

    ChrTalk(    #197
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Scherazard's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86EF")

    ChrTalk(    #198
        0x10,
        (
            "#5PThey've done it! Scherazard's team has conquered\x01",
            "the normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87A1")

    label("loc_86EF")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8747")

    ChrTalk(    #199
        0x10,
        (
            "#5PThey've done it! Scherazard's team has conquered\x01",
            "the hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87A1")

    label("loc_8747")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87A1")

    ChrTalk(    #200
        0x10,
        (
            "#5PThey've done it! Scherazard's team has conquered\x01",
            "the nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87A1")

    Jump("loc_8CD5")

    label("loc_87A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88ED")

    ChrTalk(    #201
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Agate's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8842")

    ChrTalk(    #202
        0x10,
        (
            "#5PThey've done it! Agate's team has conquered the\x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88EA")

    label("loc_8842")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8895")

    ChrTalk(    #203
        0x10,
        (
            "#5PThey've done it! Agate's team has conquered the\x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88EA")

    label("loc_8895")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88EA")

    ChrTalk(    #204
        0x10,
        (
            "#5PThey've done it! Agate's team has conquered the\x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88EA")

    Jump("loc_8CD5")

    label("loc_88ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A3E")

    ChrTalk(    #205
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Estelle's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_898F")

    ChrTalk(    #206
        0x10,
        (
            "#5PThey've done it! Estelle's team has conquered the\x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A3B")

    label("loc_898F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E4")

    ChrTalk(    #207
        0x10,
        (
            "#5PThey've done it! Estelle's team has conquered the\x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A3B")

    label("loc_89E4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A3B")

    ChrTalk(    #208
        0x10,
        (
            "#5PThey've done it! Estelle's team has conquered the\x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A3B")

    Jump("loc_8CD5")

    label("loc_8A3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8F")

    ChrTalk(    #209
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Richard's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AE0")

    ChrTalk(    #210
        0x10,
        (
            "#5PThey've done it! Richard's team has conquered the\x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B8C")

    label("loc_8AE0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B35")

    ChrTalk(    #211
        0x10,
        (
            "#5PThey've done it! Richard's team has conquered the\x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B8C")

    label("loc_8B35")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8C")

    ChrTalk(    #212
        0x10,
        (
            "#5PThey've done it! Richard's team has conquered the\x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B8C")

    Jump("loc_8CD5")

    label("loc_8B8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CD5")

    ChrTalk(    #213
        0x10,
        (
            "#5PThe match is decided! The winner is...\x01",
            "Renne's team!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C2D")

    ChrTalk(    #214
        0x10,
        (
            "#5PThey've done it! Renne's team has conquered the\x01",
            "normal arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CD5")

    label("loc_8C2D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C80")

    ChrTalk(    #215
        0x10,
        (
            "#5PThey've done it! Renne's team has conquered the\x01",
            "hard arena!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CD5")

    label("loc_8C80")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CD5")

    ChrTalk(    #216
        0x10,
        (
            "#5PThey've done it! Renne's team has conquered the\x01",
            "nightmare arena!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CD5")

    Return()

    # Function_52_761F end

    def Function_53_8CD6(): pass

    label("Function_53_8CD6")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #217
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "In this game, you will compete against three teams in three rounds,\x01",
            "and you must defeat all of them to win. Losing any of the battles results\x01",
            "in you losing the tournament as a whole.\x01\x01",
            "At the end of each round, your HP and EP will be fully restored.\x01",
            "Your CP, however, will not.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_53_8CD6 end

    def Function_54_8E7E(): pass

    label("Function_54_8E7E")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #218
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "In this game, you will compete against three teams in three rounds,\x01",
            "and you must defeat all of them to win. Losing any of the battles results\x01",
            "in you losing the tournament as a whole.\x01\x01",
            "At the end of each round, your HP and EP will be fully restored.\x01",
            "Your CP, however, will not.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_54_8E7E end

    SaveToFile()

Try(main)
