from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1400   ._SN',
        MapName             = 'Bose',
        Location            = 'T1400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Sentry',                               # 9
        'Sentry',                               # 10
        'Royal Army Soldier',                   # 11
        'Royal Army Soldier',                   # 12
        'Carlos',                               # 13
        'Lyndon',                               # 14
        'Sting',                                # 15
        'Royal Army Soldier',                   # 16
        'Royal Army Soldier',                   # 17
        'Royal Army Soldier',                   # 18
        'Royal Army Soldier',                   # 19
        'Royal Army Soldier',                   # 20
        'Royal Army Soldier',                   # 21
        'Royal Army Officer',                   # 22
        'Royal Army Soldier',                   # 23
        'Royal Army Soldier',                   # 24
        'Royal Army Soldier',                   # 25
        'Royal Army Soldier',                   # 26
        'Royal Army Soldier',                   # 27
        'Royal Army Soldier',                   # 28
        'Royal Army Soldier',                   # 29
        'Royal Army Soldier',                   # 30
        'Royal Army Soldier',                   # 31
        'Royal Army Soldier',                   # 32
        'Royal Army Soldier',                   # 33
        'Royal Army Soldier',                   # 34
        'Royal Army Soldier',                   # 35
        'Royal Army Soldier',                   # 36
        'Royal Army Soldier',                   # 37
        'Royal Army Soldier',                   # 38
        'Royal Army Soldier',                   # 39
        'Royal Army Soldier',                   # 40
        'Royal Army Soldier',                   # 41
        'Royal Army Soldier',                   # 42
        'Royal Army Soldier',                   # 43
        'Royal Army Soldier',                   # 44
        'Royal Army Soldier',                   # 45
        'Royal Army Soldier',                   # 46
        'Royal Army Soldier',                   # 47
        'Royal Army Soldier',                   # 48
        'Royal Army Soldier',                   # 49
        'Royal Army Soldier',                   # 50
        'Royal Army Soldier',                   # 51
        'Royal Army Soldier',                   # 52
        'Royal Army Soldier',                   # 53
        'Royal Army Soldier',                   # 54
        'Royal Army Soldier',                   # 55
        'Royal Army Soldier',                   # 56
        'Royal Army Soldier',                   # 57
        'Royal Army Soldier',                   # 58
        'Royal Army Soldier',                   # 59
        'Royal Army Soldier',                   # 60
        'Royal Army Soldier',                   # 61
        'Royal Army Soldier',                   # 62
        'Royal Army Soldier',                   # 63
        'Royal Army Soldier',                   # 64
        'Royal Army Soldier',                   # 65
        'Royal Army Soldier',                   # 66
        'Royal Army Soldier',                   # 67
        'Royal Army Soldier',                   # 68
        'Royal Army Soldier',                   # 69
        'Royal Army Soldier',                   # 70
        'Royal Army Soldier',                   # 71
        'Royal Army Officer',                   # 72
        'Royal Army Officer',                   # 73
        'Royal Army Officer',                   # 74
        'Royal Army Officer',                   # 75
        'Royal Army Officer',                   # 76
        'Royal Army Officer',                   # 77
        'Cassius',                              # 78
        'General Morgan',                       # 79
        'Eisen Road',                           # 80
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01660 ._CH',             # 02
        'ED6_DT27/CH03790 ._CH',             # 03
        'ED6_DT07/CH01310 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01660P._CP',             # 02
        'ED6_DT27/CH03790P._CP',             # 03
        'ED6_DT07/CH01310P._CP',             # 04
    )

    DeclNpc(
        X                   = 9100,
        Z                   = 0,
        Y                   = -10190,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2400,
        Z                   = 0,
        Y                   = -7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2100,
        Z                   = 0,
        Y                   = -20100,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 7620,
        Z                   = 10,
        Y                   = -18860,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 0,
        Y                   = -26140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -4570,
        Z                   = 0,
        Y                   = -8880,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 80,
        Z                   = 0,
        Y                   = -10570,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 1900,
        Z                   = 0,
        Y                   = -9630,
        Direction           = 303,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -2620,
        Z                   = 0,
        Y                   = -11290,
        Direction           = 27,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4010,
        Z                   = 0,
        Y                   = -9180,
        Direction           = 303,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 2430,
        Z                   = 0,
        Y                   = -11400,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        X                   = 11890,
        Z                   = 40,
        Y                   = -60460,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_9D2",          # 00, 0
        "Function_1_B01",          # 01, 1
        "Function_2_B68",          # 02, 2
        "Function_3_CE5",          # 03, 3
        "Function_4_D09",          # 04, 4
        "Function_5_D56",          # 05, 5
        "Function_6_DA3",          # 06, 6
        "Function_7_1270",         # 07, 7
        "Function_8_14F5",         # 08, 8
        "Function_9_1AF3",         # 09, 9
        "Function_10_20F7",        # 0A, 10
        "Function_11_27C6",        # 0B, 11
        "Function_12_2C3F",        # 0C, 12
        "Function_13_300D",        # 0D, 13
        "Function_14_3221",        # 0E, 14
        "Function_15_33CA",        # 0F, 15
        "Function_16_3585",        # 10, 16
        "Function_17_3913",        # 11, 17
        "Function_18_3A75",        # 12, 18
        "Function_19_3D40",        # 13, 19
        "Function_20_402B",        # 14, 20
        "Function_21_49EC",        # 15, 21
    )


    def Function_0_9D2(): pass

    label("Function_0_9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A84")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_A81")
    SetChrPos(0xF, -1400, 0, -12000, 0)
    SetChrPos(0x10, 0, 0, -12000, 0)
    SetChrPos(0x11, 1400, 0, -12000, 0)
    SetChrPos(0x12, -1400, 0, -13400, 0)
    SetChrPos(0x13, 0, 0, -13400, 0)
    SetChrPos(0x14, 1400, 0, -13400, 0)

    label("loc_A81")

    Jump("loc_AC5")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_A98")
    SetChrChipByIndex(0xC, 1)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_AC5")

    label("loc_A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_AA7")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_AC5")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC5")
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC5")
    SetChrFlags(0xE, 0x10)

    label("loc_AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_AE4")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 20)
    Jump("loc_B00")

    label("loc_AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_B00")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 21)

    label("loc_B00")

    Return()

    # Function_0_9D2 end

    def Function_1_B01(): pass

    label("Function_1_B01")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFE0430, 0x230045)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3A")
    OP_72(0x3, 0x10)
    OP_6F(0x3, 560)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)

    label("loc_B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4E")
    OP_72(0x3, 0x10)
    OP_6F(0x3, 0)

    label("loc_B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B67")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B67")

    Return()

    # Function_1_B01 end

    def Function_2_B68(): pass

    label("Function_2_B68")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CCF")

    label("loc_B8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CCF")

    label("loc_BA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBF")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CCF")

    label("loc_BBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD8")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CCF")

    label("loc_BD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF1")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CCF")

    label("loc_BF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CCF")

    label("loc_C0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C23")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CCF")

    label("loc_C23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CCF")

    label("loc_C3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CCF")

    label("loc_C55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CCF")

    label("loc_C6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C87")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CCF")

    label("loc_C87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CCF")

    label("loc_CA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB9")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CCF")

    label("loc_CB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCF")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CCF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CE4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CCF")

    label("loc_CE4")

    Return()

    # Function_2_B68 end

    def Function_3_CE5(): pass

    label("Function_3_CE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D08")
    OP_8D(0xFE, -7000, -13000, 3500, -25300, 2000)
    Jump("Function_3_CE5")

    label("loc_D08")

    Return()

    # Function_3_CE5 end

    def Function_4_D09(): pass

    label("Function_4_D09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D55")
    OP_8E(0xFE, 0xFFFFDCD8, 0x2DE6, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFF63C, 0x2DE6, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_4_D09")

    label("loc_D55")

    Return()

    # Function_4_D09 end

    def Function_5_D56(): pass

    label("Function_5_D56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA2")
    OP_8E(0xFE, 0x2328, 0x2DE6, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x9C4, 0x2DE6, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_5_D56")

    label("loc_DA2")

    Return()

    # Function_5_D56 end

    def Function_6_DA3(): pass

    label("Function_6_DA3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_E27")

    ChrTalk(    #0
        0xFE,
        (
            "There's been an emergency call-up of\x01",
            "the border garrison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "But what do they expect anyone to do\x01",
            "without guns?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1000")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F60")

    ChrTalk(    #2
        0xFE,
        (
            "The problem started just as we were letting\x01",
            "some Imperial freight through the gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "So, as you can see, the gate's currently\x01",
            "jammed open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "This is just a little TOO defenseless for\x01",
            "comfort, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "We wouldn't last five seconds against the\x01",
            "Imperial Army at the moment!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_FFD")

    label("loc_F60")


    ChrTalk(    #6
        0xFE,
        (
            "The problem started just as we were letting\x01",
            "some Imperial freight through the gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "This is just a little TOO defenseless for\x01",
            "comfort, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFD")

    Jump("loc_126C")

    label("loc_1000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1072")

    ChrTalk(    #8
        0xFE,
        (
            "Looks like that dragon business is\x01",
            "done with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I'm glad we weren't sortied in force\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_1072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_10E7")

    ChrTalk(    #10
        0xFE,
        "The general is on board the Arseille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "He's taking personal command of the\x01",
            "capture of the dragon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_10E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_126C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11C7")

    ChrTalk(    #12
        0xFE,
        (
            "General Morgan's finally back from the\x01",
            "signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "That means it's time to get back to\x01",
            "business for real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "If we let up our guard for even a moment,\x01",
            "he'll come down on us like lightning!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_11C7")


    ChrTalk(    #15
        0xFE,
        (
            "General Morgan's finally back from the\x01",
            "signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "He's only just returned and is\x01",
            "already back on full-time duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Talk about a man of steel!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_126C")

    TalkEnd(0x8)
    Return()

    # Function_6_DA3 end

    def Function_7_1270(): pass

    label("Function_7_1270")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_138E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12F6")

    ChrTalk(    #18
        0xFE,
        (
            "Alert status has finally, FINALLY been\x01",
            "called off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Phew! Things haven't been this tense\x01",
            "since the coup!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138B")

    label("loc_12F6")


    ChrTalk(    #20
        0xFE,
        "Welcome to the Haken Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Alert status has finally, FINALLY been\x01",
            "called off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Phew! Things haven't been this tense\x01",
            "since the coup!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_138B")

    Jump("loc_14F1")

    label("loc_138E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1409")

    ChrTalk(    #23
        0xFE,
        (
            "Haken Gate is currently on alert because\x01",
            "of the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I hope the Air Force can take care of it\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F1")

    label("loc_1409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_14F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1466")

    ChrTalk(    #25
        0xFE,
        "Welcome to the Haken Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Beyond here lies the Erebonian Empire.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14F1")

    label("loc_1466")


    ChrTalk(    #27
        0xFE,
        "Welcome to the Haken Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Beyond here lies the Erebonian Empire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I'm afraid you'll need Liberlian passports\x01",
            "to proceed.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_14F1")

    TalkEnd(0x9)
    Return()

    # Function_7_1270 end

    def Function_8_14F5(): pass

    label("Function_8_14F5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_16CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(    #30
        0xFE,
        (
            "Our guns are a problem, sure, but what's\x01",
            "really causing everyone to lose sleep is\x01",
            "the loss of the Air Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "A huge part of the country's modern defense\x01",
            "strategy relies on the Air Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Losing it makes us all feel pretty exposed\x01",
            "before a cruel, hostile world...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_16C7")

    label("loc_1623")


    ChrTalk(    #33
        0xFE,
        (
            "A huge part of the country's modern defense\x01",
            "strategy relies on the Air Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Losing it makes us all feel pretty exposed\x01",
            "before a cruel, hostile world...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C7")

    Jump("loc_1AEF")

    label("loc_16CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_177C")

    ChrTalk(    #35
        0xFE,
        (
            "Having the gate hanging open like\x01",
            "this is like having a hole in our wall--\x01",
            "a HUGE one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "The responsibility of us gate-watchers\x01",
            "is greater than it's ever been.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AEF")

    label("loc_177C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_18BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_180C")

    ChrTalk(    #37
        0xFE,
        (
            "Apparently the Bracer Guild took care\x01",
            "of the dragon problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Kinda feels like we had the spotlight\x01",
            "snatched from us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B8")

    label("loc_180C")


    ChrTalk(    #39
        0xFE,
        "This is just what I've heard, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Apparently the Bracer Guild took care\x01",
            "of the dragon problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Kinda feels like we had the spotlight\x01",
            "snatched from us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_18B8")

    Jump("loc_1AEF")

    label("loc_18BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(    #42
        0xFE,
        (
            "Apparently the dragon-capturing plan\x01",
            "isn't going so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I didn't think the Air Force would have\x01",
            "such a hard time of it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A43")

    label("loc_1950")


    ChrTalk(    #44
        0xFE,
        (
            "Apparently the dragon-capturing plan\x01",
            "isn't going so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "It's gotten to the point where they're\x01",
            "going to try fighting the dragon on land.\x01",
            "Yikes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "It's just gossip, though. You probably shouldn't\x01",
            "pay too much attention to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1A43")

    Jump("loc_1AEF")

    label("loc_1A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1AEF")

    ChrTalk(    #47
        0xFE,
        (
            "The non-aggression pact being signed\x01",
            "doesn't just make our worries go away\x01",
            "like magic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "We're going to be keeping as close\x01",
            "an eye on the border as ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEF")

    TalkEnd(0xA)
    Return()

    # Function_8_14F5 end

    def Function_9_1AF3(): pass

    label("Function_9_1AF3")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1BAD")

    ChrTalk(    #49
        0xFE,
        (
            "Even in an emergency like this, General\x01",
            "Morgan is the epitome of calmness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Just what you'd expect from one of the\x01",
            "greatest generals in Liberlian history,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F3")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C91")

    ChrTalk(    #51
        0xFE,
        (
            "This is the first major troop summons\x01",
            "in a while. Since the dragon appeared,\x01",
            "in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "But now it seems like things are\x01",
            "REALLY serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "These events might change the fate\x01",
            "of the whole kingdom.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1CE8")

    label("loc_1C91")


    ChrTalk(    #54
        0xFE,
        "Things have really hit the fan now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "It's all gonna come down to us soldiers.\x02",
    )

    CloseMessageWindow()

    label("loc_1CE8")

    Jump("loc_20F3")

    label("loc_1CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D77")

    ChrTalk(    #56
        0xFE,
        (
            "The general had this real unpleasant\x01",
            "look on his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Everything should be all right now.\x01",
            "I wonder what's up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E46")

    label("loc_1D77")


    ChrTalk(    #58
        0xFE,
        (
            "I saw the general just a little while\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Even though everything's been settled,\x01",
            "he still had this real unpleasant look\x01",
            "on his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I guess it might've just been my\x01",
            "imagination. Maybe...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1E46")

    Jump("loc_20F3")

    label("loc_1E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F0B")

    ChrTalk(    #61
        0xFE,
        (
            "The border garrison's on alert status,\x01",
            "but as a practical matter, we're not\x01",
            "taking any direct action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "After all, this is the cornerstone\x01",
            "of Liberl's national defense!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFF")

    label("loc_1F0B")


    ChrTalk(    #63
        0xFE,
        (
            "It's mostly the Royal Guard and Air\x01",
            "Force handling the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "The border garrison's on alert status,\x01",
            "but as a practical matter, we're not\x01",
            "taking any direct action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "As always, it falls to us to keep a\x01",
            "close eye on the border.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1FFF")

    Jump("loc_20F3")

    label("loc_2002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_20F3")

    ChrTalk(    #66
        0xFE,
        (
            "Ten years ago, the Empire broke through\x01",
            "this gate, and moved through this pass\x01",
            "to invade Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Guess that's why I always feel a little\x01",
            "tense when I look out and see the friggin'\x01",
            "Erebonian Empire spread out in front of me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F3")

    TalkEnd(0xB)
    Return()

    # Function_9_1AF3 end

    def Function_10_20F7(): pass

    label("Function_10_20F7")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2477")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 5)), scpexpr(EXPR_END)), "loc_2211")

    NpcTalk(    #68
        0xFE,
        "Carlos",
        (
            "And that's it. I'm no longer an army man.\x01",
            "Time to say goodbye to the uniform.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #69
        0xFE,
        "Carlos",
        (
            "It wasn't for long, but life in the army\x01",
            "was more fun than I expected.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #70
        0xFE,
        "Carlos",
        (
            "Yeah, from traveling, to the army, and\x01",
            "back to the road... This is the life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2474")

    label("loc_2211")


    NpcTalk(    #71
        0xFE,
        "Carlos",
        (
            "And that's it. I'm no longer an army man.\x01",
            "Time to say goodbye to the uniform.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #72
        0xFE,
        "Carlos",
        (
            "Oh, yeah, to mark the occasion, let me\x01",
            "give you guys this.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #73
        "\x07\x00Received #578i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x242, 1)
    OP_A2(0x10BD)
    OP_0D()

    NpcTalk(    #74
        0xFE,
        "Carlos",
        (
            "That book was my secret pleasure during\x01",
            "the more boring parts of base life.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0xFE,
        "Carlos",
        (
            "Still, though, looking back on it, it wasn't\x01",
            "for all that long, but life in the army was\x01",
            "more fun than I expected.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0xFE,
        "Carlos",
        "All right, time to finish my discharge.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0xFE,
        "Carlos",
        (
            "It's been quite the run-around getting\x01",
            "here, but it's finally time for my trip\x01",
            "to the Empire!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2474")

    Jump("loc_27C2")

    label("loc_2477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_251E")

    ChrTalk(    #78
        0xFE,
        (
            "You'd be surprised how much you can save\x01",
            "up with a soldier's salary!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Once I'm discharged from the army,\x01",
            "I'm going to be going on that trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2604")

    label("loc_251E")


    ChrTalk(    #80
        0xFE,
        (
            "I've got enough money to travel on now,\x01",
            "so I think it's about time I left the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "My discharge has been deferred, though,\x01",
            "since we're on alert status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "Well, all I gotta do now is get through\x01",
            "this in one piece.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2604")

    Jump("loc_27C2")

    label("loc_2607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_27C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_26A4")

    ChrTalk(    #83
        0xFE,
        (
            "I originally came out here to travel to\x01",
            "Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I ran out of money part way, though,\x01",
            "and had no choice but to become a\x01",
            "soldier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C2")

    label("loc_26A4")


    ChrTalk(    #85
        0xFE,
        (
            "I originally came out here to travel to\x01",
            "Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I ran out of money part way, though,\x01",
            "and had no choice but to become a\x01",
            "soldier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Military life is hard, but the soldiers\x01",
            "here are nice people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "And hey, livin' life one step at a time\x01",
            "ain't such a bad thing, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_27C2")

    TalkEnd(0xC)
    Return()

    # Function_10_20F7 end

    def Function_11_27C6(): pass

    label("Function_11_27C6")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2A39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_28A7")

    ChrTalk(    #89
        0xFE,
        (
            "The dragon apparently fled without being\x01",
            "seriously injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I still wish I knew why this dragon was\x01",
            "acting so...so wildly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "It contradicts everything we know about\x01",
            "dragons. Such a mystery...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A36")

    label("loc_28A7")


    ChrTalk(    #92
        0xFE,
        (
            "The dragon apparently fled without being\x01",
            "seriously injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "As unpopular as I know our dragon 'friend'\x01",
            "is right now, as a researcher of ancient\x01",
            "life, I have to admit I'm relieved it got away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I can make quite a bit of progress with\x01",
            "just the photos we took...if I can keep them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "How much I'll be able to publish will be\x01",
            "up to my negotiating skills now, not my\x01",
            "scientific ones.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2A36")

    Jump("loc_2C3B")

    label("loc_2A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B01")

    ChrTalk(    #96
        0xFE,
        (
            "I do hope the army is very careful\x01",
            "with this capture plan of theirs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "It may be causing a great deal of trouble\x01",
            "now, but a real, live dragon is irreplaceable\x01",
            "scientifically.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C3B")

    label("loc_2B01")


    ChrTalk(    #98
        0xFE,
        "I heard the dragon fled into Nebel Valley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "I tried coming here, thinking I might\x01",
            "be able to get a look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Anyway, I do hope the army is very\x01",
            "careful with this capture plan of theirs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "It may be causing a great deal of trouble\x01",
            "now, but a real, live dragon is irreplaceable\x01",
            "scientifically.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2C3B")

    TalkEnd(0xD)
    Return()

    # Function_11_27C6 end

    def Function_12_2C3F(): pass

    label("Function_12_2C3F")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_2C4C")
    OP_A2(0x6)

    label("loc_2C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD5")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Sting previously\x01",               # 0
            "Set as did not meet Sting previously\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CC9"),
        (1, "loc_2CCF"),
        (SWITCH_DEFAULT, "loc_2CD5"),
    )


    label("loc_2CC9")

    OP_A2(0x6)
    Jump("loc_2CD5")

    label("loc_2CCF")

    OP_A3(0x6)
    Jump("loc_2CD5")

    label("loc_2CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_2D27")

    ChrTalk(    #102
        0xFE,
        "Grant and Anelace are both out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "We're counting on you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3009")

    label("loc_2D27")


    ChrTalk(    #104
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2E17")

    ChrTalk(    #105
        0x101,
        (
            "#1011FOh, hey, you're, um...\x02\x03",

            "Sting, right? With the Bose branch?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #106
        0xFE,
        (
            "That's right.\x01",
            "And you're that rookie from a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "No, that's right, you were promoted recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1016FYeah, somehow!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E6A")

    label("loc_2E17")


    ChrTalk(    #109
        0x101,
        (
            "#1015F(Huh? Hey, this guy...)\x02\x03",

            "(Now that I look, he's got a guild emblem on!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E6A")


    ChrTalk(    #110
        0x106,
        (
            "#050FSup, Sting? Been a while.\x02\x03",

            "You out here on the hunt for these\x01",
            "crazy monsters, too?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #111
        0xFE,
        "Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "Working in Bose again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x106,
        (
            "#050FYeah, for the moment, anyway.\x02\x03",

            "We're mostly just helpin' with those\x01",
            "weird monsters on the road right now,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Got'cha. There've been a lot of\x01",
            "those these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "We'll be counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x106,
        "#051FJust leave it to us.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A53)

    label("loc_3009")

    TalkEnd(0xE)
    Return()

    # Function_12_2C3F end

    def Function_13_300D(): pass

    label("Function_13_300D")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_316D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E9")

    ChrTalk(    #117
        0xFE,
        (
            "When you think about it, the Imperials\x01",
            "can't use guns either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "There's no way they'd try to attack us\x01",
            "with just hand weapons or whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "...Well, that's what I tell myself,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_316A")

    label("loc_30E9")


    ChrTalk(    #120
        0xFE,
        (
            "Nobody can use orbal guns around here,\x01",
            "so there's no way the Imperials will attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "That's what I tell myself, anyway.\x02",
    )

    CloseMessageWindow()

    label("loc_316A")

    Jump("loc_321D")

    label("loc_316D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_321D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E5")

    ChrTalk(    #122
        0xFE,
        "This whole thing is completely crazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Damn it!\x01",
            "Today was supposed to be my day off, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_321D")

    label("loc_31E5")


    ChrTalk(    #124
        0xFE,
        (
            "Damn it!\x01",
            "Today was supposed to be my day off, too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321D")

    TalkEnd(0xF)
    Return()

    # Function_13_300D end

    def Function_14_3221(): pass

    label("Function_14_3221")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D3")

    ChrTalk(    #125
        0xFE,
        (
            "Damn you, Imperial Army! What are you doing?!\x01",
            "Come and take a shot at me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I can't kick ass and run out of gum if there\x01",
            "isn't a war, now can I?!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3322")

    label("loc_32D3")


    ChrTalk(    #127
        0xFE,
        (
            "Damn you, Imperial Army! What are you doing?!\x01",
            "Come and take a shot at me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3322")

    Jump("loc_33C6")

    label("loc_3325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_33C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339A")

    ChrTalk(    #128
        0xFE,
        (
            "Heheheheh!\x01",
            "At last, the time has come!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Come on, Imperial Army!\x01",
            "I'll send you packing!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_33C6")

    label("loc_339A")


    ChrTalk(    #130
        0xFE,
        (
            "Heheheheh!\x01",
            "At last, the time has come!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C6")

    TalkEnd(0x10)
    Return()

    # Function_14_3221 end

    def Function_15_33CA(): pass

    label("Function_15_33CA")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_343E")

    ChrTalk(    #131
        0xFE,
        (
            "Th-The guy next to me is seriously\x01",
            "kind of crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I'm just gonna pretend I can't hear\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3581")

    label("loc_343E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350E")

    ChrTalk(    #133
        0xFE,
        (
            "I think the guy next to me's lost it.\x01",
            "He keeps mumbling stuff about his\x01",
            "rifle and how it's his best friend...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "I'm trying to stay away from him in\x01",
            "case he actually starts a war!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3581")

    label("loc_350E")


    ChrTalk(    #135
        0xFE,
        (
            "I think the guy next to me's lost it.\x01",
            "He keeps mumbling stuff about his\x01",
            "rifle and how it's his best friend...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3581")

    TalkEnd(0x11)
    Return()

    # Function_15_33CA end

    def Function_16_3585(): pass

    label("Function_16_3585")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_37D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370B")

    ChrTalk(    #136
        0xFE,
        (
            "I honestly don't think the Erebonians\x01",
            "are going to take a shot at us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "They can't use any orbal-powered weapons\x01",
            "either, first of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Besides, no matter what else, they did\x01",
            "just sign the non-aggression pact.\x01",
            "Not even Osborne would go against that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "Not without a really good chance of\x01",
            "winning quickly, at least. I don't think\x01",
            "they'll try anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_37D0")

    label("loc_370B")


    ChrTalk(    #140
        0xFE,
        (
            "I honestly don't think the Erebonians\x01",
            "are going to take a shot at us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Unless they have some miraculous way of\x01",
            "defeating us instantly, they wouldn't\x01",
            "risk the wrath of the whole continent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D0")

    Jump("loc_390F")

    label("loc_37D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_390F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A0")

    ChrTalk(    #142
        0xFE,
        (
            "I was prepared for this to happen from\x01",
            "the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "No way I'm not going to stand up now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "Having enlisted as a soldier in Her\x01",
            "Majesty's army, it's time to do my duty.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_390F")

    label("loc_38A0")


    ChrTalk(    #145
        0xFE,
        (
            "I was prepared for this to happen from\x01",
            "the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "There's no way I'm going to shirk my\x01",
            "duty now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390F")

    TalkEnd(0x12)
    Return()

    # Function_16_3585 end

    def Function_17_3913(): pass

    label("Function_17_3913")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_39CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3994")

    ChrTalk(    #147
        0xFE,
        (
            "I don't see anything on the plains\x01",
            "to the north.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "I just hope this ends with nothing\x01",
            "happening.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_39CA")

    label("loc_3994")


    ChrTalk(    #149
        0xFE,
        (
            "I don't see anything on the plains\x01",
            "to the north.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CA")

    Jump("loc_3A71")

    label("loc_39CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A46")

    ChrTalk(    #150
        0xFE,
        "So just ahead of us is Imperial territory...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "J-Just looking at it makes me feel uneasy...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_3A71")

    label("loc_3A46")


    ChrTalk(    #152
        0xFE,
        "Mmmmm... I'm gettin' kind of nervous!\x02",
    )

    CloseMessageWindow()

    label("loc_3A71")

    TalkEnd(0x13)
    Return()

    # Function_17_3913 end

    def Function_18_3A75(): pass

    label("Function_18_3A75")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B49")

    ChrTalk(    #153
        0xFE,
        (
            "There's no sign of the Imperial Army\x01",
            "moving at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "They're gonna be just as stuck with their\x01",
            "tanks not working, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "Hah, I think we're getting a bit paranoid.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_3BD5")

    label("loc_3B49")


    ChrTalk(    #156
        0xFE,
        (
            "There's no sign of the Imperial Army\x01",
            "moving at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "They're gonna be just as stuck with their\x01",
            "tanks not working, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD5")

    Jump("loc_3D3C")

    label("loc_3BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB1")

    ChrTalk(    #158
        0xFE,
        (
            "Of course the gate just HAD to stop working\x01",
            "in the middle of a caravan moving through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "I gotta admit, the timing seems almost\x01",
            "too perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "Isn't it just a little bit suspicious...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_3D3C")

    label("loc_3CB1")


    ChrTalk(    #161
        0xFE,
        (
            "Of course the gate just HAD to stop working\x01",
            "in the middle of a caravan moving through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "Isn't it just a little bit suspicious...?\x02",
    )

    CloseMessageWindow()

    label("loc_3D3C")

    TalkEnd(0x14)
    Return()

    # Function_18_3A75 end

    def Function_19_3D40(): pass

    label("Function_19_3D40")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3E22")

    ChrTalk(    #163
        0xFE,
        (
            "We're continuing the alert, just in case,\x01",
            "but I don't think we have much to worry\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "Their weapons are just as unusable as ours.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "And even if they wanted to mobilize,\x01",
            "how would they move troops?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4027")

    label("loc_3E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F77")

    ChrTalk(    #166
        0xFE,
        (
            "Having the gate jammed wide open is\x01",
            "certainly a problem, but it's not the end\x01",
            "of the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "That gate is pure steel and designed to\x01",
            "withstand large projectiles. There's no\x01",
            "way we can move it by hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "Until orbments start working again,\x01",
            "it's stuck like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "All we can do is be as alert as possible.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_4027")

    label("loc_3F77")


    ChrTalk(    #170
        0xFE,
        (
            "That gate is pure steel and designed to\x01",
            "withstand large projectiles. There's no\x01",
            "way we can move it by hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Until orbments start working again,\x01",
            "it's stuck like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4027")

    TalkEnd(0x15)
    Return()

    # Function_19_3D40 end

    def Function_20_402B(): pass

    label("Function_20_402B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
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
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x47, -4520, 0, -11180, 180)
    SetChrPos(0x16, -5920, 0, -13010, 0)
    SetChrPos(0x17, -4880, 0, -13070, 0)
    SetChrPos(0x18, -3760, 0, -13080, 0)
    SetChrPos(0x19, -6040, 0, -14600, 0)
    SetChrPos(0x1A, -4880, -10, -14630, 0)
    SetChrPos(0x1B, -3730, 0, -14620, 0)
    SetChrPos(0x2E, -5930, 0, -16510, 0)
    SetChrPos(0x2F, -4820, 0, -16500, 0)
    SetChrPos(0x30, -3620, 0, -16520, 0)
    SetChrPos(0x48, -1050, 0, -11060, 180)
    SetChrPos(0x1C, -2210, 0, -13070, 0)
    SetChrPos(0x1D, -1050, 0, -13020, 0)
    SetChrPos(0x1E, -10, 0, -13090, 0)
    SetChrPos(0x1F, -2180, 0, -14600, 0)
    SetChrPos(0x20, -1060, 0, -14610, 0)
    SetChrPos(0x21, 0, 0, -14650, 0)
    SetChrPos(0x31, -2150, 0, -16530, 0)
    SetChrPos(0x32, -1020, 0, -16510, 0)
    SetChrPos(0x33, 80, 0, -16500, 0)
    SetChrPos(0x49, 2240, 0, -11070, 180)
    SetChrPos(0x22, 1170, 0, -12720, 0)
    SetChrPos(0x23, 2150, 0, -12770, 0)
    SetChrPos(0x24, 3180, 0, -12700, 0)
    SetChrPos(0x25, 1140, 0, -14640, 0)
    SetChrPos(0x26, 2180, 0, -14620, 0)
    SetChrPos(0x27, 3210, 0, -14600, 0)
    SetChrPos(0x34, 1210, 0, -16570, 0)
    SetChrPos(0x35, 2200, 0, -16530, 0)
    SetChrPos(0x36, 3260, 0, -16590, 0)
    SetChrPos(0x4A, 5410, 0, -11150, 180)
    SetChrPos(0x28, 4290, 0, -13090, 0)
    SetChrPos(0x29, 5340, 0, -13070, 0)
    SetChrPos(0x2A, 6390, 0, -13060, 0)
    SetChrPos(0x2B, 4370, 0, -14630, 0)
    SetChrPos(0x2C, 5370, 0, -14640, 0)
    SetChrPos(0x2D, 6390, 0, -14610, 0)
    SetChrPos(0x37, 4390, 0, -16570, 0)
    SetChrPos(0x38, 5310, 0, -16510, 0)
    SetChrPos(0x39, 6420, 0, -16530, 0)
    SetChrPos(0x15, -2900, 0, -18790, 180)
    SetChrPos(0x8, -4150, 0, -20160, 0)
    SetChrPos(0x9, -2970, 0, -20180, 0)
    SetChrPos(0xA, -1750, -10, -20160, 0)
    SetChrPos(0xB, -4100, 0, -22060, 0)
    SetChrPos(0xC, -2920, 0, -22000, 0)
    SetChrPos(0xF, -1710, 10, -22060, 0)
    SetChrPos(0x10, -4110, -10, -23710, 0)
    SetChrPos(0x11, -2930, 10, -23790, 0)
    SetChrPos(0x12, -1760, 0, -23740, 0)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x4B, 870, -10, -18600, 180)
    SetChrPos(0x13, -360, -30, -20250, 0)
    SetChrPos(0x14, 690, -30, -20200, 0)
    SetChrPos(0x3A, 1960, 0, -20330, 0)
    SetChrPos(0x3B, -370, 10, -22080, 0)
    SetChrPos(0x3C, 780, 10, -22010, 0)
    SetChrPos(0x3D, 1970, 10, -22010, 0)
    SetChrPos(0x3E, -290, 0, -23840, 0)
    SetChrPos(0x3F, 820, 0, -23860, 0)
    SetChrPos(0x40, 1970, 10, -23820, 0)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    SetChrPos(0x4C, 4560, 30, -18680, 180)
    SetChrPos(0x41, 3390, 20, -20080, 0)
    SetChrPos(0x42, 4570, 0, -20160, 0)
    SetChrPos(0x43, 5840, 30, -20190, 0)
    SetChrPos(0x44, 3430, 10, -22080, 0)
    SetChrPos(0x45, 4630, 10, -22040, 0)
    SetChrPos(0x46, 5900, 0, -22070, 0)
    SetChrPos(0xE, 3410, 10, -23910, 0)
    SetChrPos(0x4D, 4640, -10, -23920, 0)
    SetChrPos(0x4E, 5860, 0, -23900, 0)
    SetChrChipByIndex(0xE, 0)
    SetChrChipByIndex(0x4D, 0)
    SetChrChipByIndex(0x4E, 0)
    OP_4A(0x47, 255)
    OP_4A(0x48, 255)
    OP_4A(0x49, 255)
    OP_4A(0x4A, 255)
    OP_4A(0x4B, 255)
    OP_4A(0x4C, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_4A(0x23, 255)
    OP_4A(0x24, 255)
    OP_4A(0x25, 255)
    OP_4A(0x26, 255)
    OP_4A(0x27, 255)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    OP_4A(0x2C, 255)
    OP_4A(0x2D, 255)
    OP_4A(0x2E, 255)
    OP_4A(0x2F, 255)
    OP_4A(0x30, 255)
    OP_4A(0x31, 255)
    OP_4A(0x32, 255)
    OP_4A(0x33, 255)
    OP_4A(0x34, 255)
    OP_4A(0x35, 255)
    OP_4A(0x36, 255)
    OP_4A(0x37, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    OP_4A(0x3A, 255)
    OP_4A(0x3B, 255)
    OP_4A(0x3C, 255)
    OP_4A(0x3D, 255)
    OP_4A(0x3E, 255)
    OP_4A(0x3F, 255)
    OP_4A(0x40, 255)
    OP_4A(0x41, 255)
    OP_4A(0x42, 255)
    OP_4A(0x43, 255)
    OP_4A(0x44, 255)
    OP_4A(0x45, 255)
    OP_4A(0x46, 255)
    OP_4A(0xE, 255)
    OP_4A(0x4D, 255)
    OP_4A(0x4E, 255)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    SetChrFlags(0x47, 0x40)
    SetChrFlags(0x48, 0x40)
    SetChrFlags(0x49, 0x40)
    SetChrFlags(0x4A, 0x40)
    SetChrFlags(0x4B, 0x40)
    SetChrFlags(0x4C, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x2A, 0x40)
    SetChrFlags(0x2B, 0x40)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x2E, 0x40)
    SetChrFlags(0x2F, 0x40)
    SetChrFlags(0x30, 0x40)
    SetChrFlags(0x31, 0x40)
    SetChrFlags(0x32, 0x40)
    SetChrFlags(0x33, 0x40)
    SetChrFlags(0x34, 0x40)
    SetChrFlags(0x35, 0x40)
    SetChrFlags(0x36, 0x40)
    SetChrFlags(0x37, 0x40)
    SetChrFlags(0x38, 0x40)
    SetChrFlags(0x39, 0x40)
    SetChrFlags(0x3A, 0x40)
    SetChrFlags(0x3B, 0x40)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3D, 0x40)
    SetChrFlags(0x3E, 0x40)
    SetChrFlags(0x3F, 0x40)
    SetChrFlags(0x40, 0x40)
    SetChrFlags(0x41, 0x40)
    SetChrFlags(0x42, 0x40)
    SetChrFlags(0x43, 0x40)
    SetChrFlags(0x44, 0x40)
    SetChrFlags(0x45, 0x40)
    SetChrFlags(0x46, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0x4D, 0x40)
    SetChrFlags(0x4E, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    OP_6D(0, -500, -17000, 0)
    OP_67(0, 4980, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(334000, 0)
    OP_6E(538, 0)

    def lambda_4975():
        OP_6D(-3500, 1000, -3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4975)

    def lambda_498D():
        OP_67(0, 3500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_498D)

    def lambda_49A5():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49A5)

    def lambda_49B5():
        OP_6E(550, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_49B5)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_402B end

    def Function_21_49EC(): pass

    label("Function_21_49EC")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_D2(0x2701E6, 0x2701EB, 0x5)
    OP_D2(0x70150, 0x70154, 0x6)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x4D, 5)
    SetChrChipByIndex(0x4E, 6)
    SetChrPos(0x4E, -500, 11750, -3000, 180)
    SetChrPos(0x4D, 500, 11750, -3000, 180)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    OP_6D(630, 11750, -1740, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #172
        0x4D,
        "#1128F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x4E, 90, 400)
    Sleep(500)

    ChrTalk(    #173
        0x4E,
        (
            "#166F#6PAre you sure, Cassius?\x02\x03",

            "If you're that worried, you could\x01",
            "have gone with them, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x4D, 270, 400)
    Sleep(400)

    ChrTalk(    #174
        0x4D,
        (
            "#1125F#4PNo, it's fine.\x02\x03",

            "#1122FWeissmann is even more dangerous\x01",
            "than I thought he would be.\x02\x03",

            "If I accompanied them, I would simply\x01",
            "be painting a target on their heads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x4E,
        (
            "#163F#6PYes, if you were out in the open,\x01",
            "he'd strike at your ankle like the\x01",
            "snake he is...\x02\x03",

            "#165FThe price of fame, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x4D,
        (
            "#1123F#4PAnd it is maddeningly frustrating,\x01",
            "let me tell you.\x02\x03",

            "#1120FOf course, this is also what\x01",
            "gives us a chance to strike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x4E,
        (
            "#163F#6PA game of truth and lies as the two\x01",
            "of you try to read the other, eh?\x02\x03",

            "#160FSpeaking of lies, do you think the\x01",
            "Blood and Iron Chancellor will really\x01",
            "hold back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x4D,
        (
            "#1122F#4PAs powerful as he is, he can't gainsay\x01",
            "an oath from Prince Olivert easily.\x02\x03",

            "#1125FAs long as we don't give them any more\x01",
            "of an opening, I think we'll be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x4E,
        (
            "#166F#6PHmph. I hope so.\x02\x03",

            "#163FEverything rests on the team\x01",
            "aboard the Arseille, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x4D,
        "#1128F#4PYes...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x4D, 180, 400)

    def lambda_4EC8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_4EC8)
    Sleep(500)

    ChrTalk(    #181
        0x4D,
        (
            "#1122F#6P(Lena...and great, benevolent\x01",
            "Aidios of the sky...)\x02\x03",

            "(Shine down where your children\x01",
            "must walk... Please...)\x02\x03",

            "#1125F(That beneath this enormous sky...\x01",
            "they might find the path they seek.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x208F)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400B5, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_6D(-162160, 0, -33060, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_EA(0x15, 0x0, 0x0, 0x0)

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5025")
    ShowSaveMenu()

    label("loc_5025")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    OP_20(0x1388)
    Sleep(2000)
    OP_21()
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    AddParty(0x1, 0xF7, 0xFF)
    OP_A3(0x208F)
    ClearMapFlags(0x100000)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_49EC end

    SaveToFile()

Try(main)
