from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3105   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3105.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Major Cid',                            # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Soldier',                              # 18
        'Soldier',                              # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Soldier',                              # 23
        'Soldier',                              # 24
        'Soldier',                              # 25
        'Soldier',                              # 26
        'Soldier',                              # 27
        'Soldier',                              # 28
        'Soldier',                              # 29
        'Soldier',                              # 30
        'Soldier',                              # 31
        'Soldier',                              # 32
        'Soldier',                              # 33
        'Soldier',                              # 34
        'Soldier',                              # 35
        'Soldier',                              # 36
        'Soldier',                              # 37
        'Soldier',                              # 38
        'Soldier',                              # 39
        'Soldier',                              # 40
        'Soldier',                              # 41
        'Soldier',                              # 42
        'Soldier',                              # 43
        'Soldier',                              # 44
        'Soldier',                              # 45
        'Soldier',                              # 46
        'Soldier',                              # 47
        'Soldier',                              # 48
        'Soldier',                              # 49
        'Soldier',                              # 50
        'Soldier',                              # 51
        'Soldier',                              # 52
        'Soldier',                              # 53
        'Soldier',                              # 54
        'Soldier',                              # 55
        'Soldier',                              # 56
        'Soldier',                              # 57
        'Soldier',                              # 58
        'Soldier',                              # 59
        'Soldier',                              # 60
        'Soldier',                              # 61
        'Soldier',                              # 62
        'Soldier',                              # 63
        'Soldier',                              # 64
        'Soldier',                              # 65
        'Soldier',                              # 66
        'Soldier',                              # 67
        'Soldier',                              # 68
        'Soldier',                              # 69
        'Soldier',                              # 70
        'Soldier',                              # 71
        'Soldier',                              # 72
        'Soldier',                              # 73
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
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH01650 ._CH',             # 01
        'ED6_DT07/CH01310 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00150 ._CH',             # 05
        'ED6_DT07/CH00160 ._CH',             # 06
        'ED6_DT06/CH20043 ._CH',             # 07
        'ED6_DT07/CH01640 ._CH',             # 08
        'ED6_DT07/CH00321 ._CH',             # 09
        'ED6_DT09/CH10060 ._CH',             # 0A
        'ED6_DT09/CH10061 ._CH',             # 0B
        'ED6_DT09/CH11010 ._CH',             # 0C
        'ED6_DT09/CH11011 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH01650P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00150P._CP',             # 05
        'ED6_DT07/CH00160P._CP',             # 06
        'ED6_DT06/CH20043P._CP',             # 07
        'ED6_DT07/CH01640P._CP',             # 08
        'ED6_DT07/CH00321P._CP',             # 09
        'ED6_DT09/CH10060P._CP',             # 0A
        'ED6_DT09/CH10061P._CP',             # 0B
        'ED6_DT09/CH11010P._CP',             # 0C
        'ED6_DT09/CH11011P._CP',             # 0D
    )

    DeclNpc(
        X                   = 18530,
        Z                   = 0,
        Y                   = 20700,
        Direction           = 270,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 90,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 90,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 90,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 90,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 90,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 18500,
        Direction           = 90,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 17000,
        Direction           = 90,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 15500,
        Direction           = 90,
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
        X                   = 14500,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 90,
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
        X                   = 14500,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 90,
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
        X                   = 14500,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 90,
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
        X                   = 14500,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 90,
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
        X                   = 14500,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 90,
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
        X                   = 14500,
        Z                   = 0,
        Y                   = 18500,
        Direction           = 90,
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
        X                   = 14500,
        Z                   = 0,
        Y                   = 17000,
        Direction           = 90,
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
        X                   = 14500,
        Z                   = 0,
        Y                   = 15500,
        Direction           = 90,
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
        X                   = 13000,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 90,
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
        X                   = 13000,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 90,
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
        X                   = 13000,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 90,
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
        X                   = 13000,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 90,
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
        X                   = 13000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 90,
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
        X                   = 13000,
        Z                   = 0,
        Y                   = 18500,
        Direction           = 90,
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
        X                   = 13000,
        Z                   = 0,
        Y                   = 17000,
        Direction           = 90,
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
        X                   = 13000,
        Z                   = 0,
        Y                   = 15500,
        Direction           = 90,
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
        X                   = 11500,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 90,
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
        X                   = 11500,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 90,
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
        X                   = 11500,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 90,
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
        X                   = 11500,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 90,
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
        X                   = 11500,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 90,
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
        X                   = 11500,
        Z                   = 0,
        Y                   = 18500,
        Direction           = 90,
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
        X                   = 11500,
        Z                   = 0,
        Y                   = 17000,
        Direction           = 90,
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
        X                   = 11500,
        Z                   = 0,
        Y                   = 15500,
        Direction           = 90,
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
        X                   = 10000,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 90,
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
        X                   = 10000,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 90,
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
        X                   = 10000,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 90,
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
        X                   = 10000,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 90,
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
        X                   = 10000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 90,
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
        X                   = 10000,
        Z                   = 0,
        Y                   = 18500,
        Direction           = 90,
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
        X                   = 10000,
        Z                   = 0,
        Y                   = 17000,
        Direction           = 90,
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
        X                   = 10000,
        Z                   = 0,
        Y                   = 15500,
        Direction           = 90,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 90,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 90,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 90,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 90,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 90,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 18500,
        Direction           = 90,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 17000,
        Direction           = 90,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 15500,
        Direction           = 90,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 90,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 90,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 90,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 90,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 90,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = 18500,
        Direction           = 90,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = 17000,
        Direction           = 90,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = 15500,
        Direction           = 90,
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
        X                   = 5500,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 90,
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
        X                   = 5500,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 90,
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
        X                   = 5500,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 90,
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
        X                   = 5500,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 90,
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
        X                   = 5500,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 90,
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
        X                   = 5500,
        Z                   = 0,
        Y                   = 18500,
        Direction           = 90,
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
        X                   = 5500,
        Z                   = 0,
        Y                   = 17000,
        Direction           = 90,
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
        X                   = 5500,
        Z                   = 0,
        Y                   = 15500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -44530,
        Z                   = 0,
        Y                   = 58590,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x245,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16570,
        Z                   = 0,
        Y                   = 59280,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x246,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14450,
        Z                   = 0,
        Y                   = 31660,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x247,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15470,
        Z                   = 0,
        Y                   = 29810,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x245,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18860,
        Z                   = 0,
        Y                   = 12280,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x246,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5110,
        Z                   = 0,
        Y                   = 17530,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x247,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17400,
        Z                   = 0,
        Y                   = 12730,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x245,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42340,
        Z                   = 0,
        Y                   = 9500,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x246,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41490,
        Z                   = 0,
        Y                   = 41570,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x247,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19000,
        Z                   = 0,
        Y                   = 44460,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x245,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -37970,
        Z                   = 0,
        Y                   = 29960,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x246,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 2410,
        TriggerRange        = 1500,
        ActorX              = 0,
        ActorZ              = 1500,
        ActorY              = 2410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1000,
        TriggerZ            = 500,
        TriggerY            = 36080,
        TriggerRange        = 800,
        ActorX              = -1000,
        ActorZ              = 1500,
        ActorY              = 36080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -52400,
        TriggerZ            = 500,
        TriggerY            = 17020,
        TriggerRange        = 800,
        ActorX              = -52400,
        ActorZ              = 1500,
        ActorY              = 17020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_ADA",          # 00, 0
        "Function_1_D1C",          # 01, 1
        "Function_2_D56",          # 02, 2
        "Function_3_D7A",          # 03, 3
        "Function_4_D9E",          # 04, 4
        "Function_5_DC2",          # 05, 5
        "Function_6_DE6",          # 06, 6
        "Function_7_1FEB",         # 07, 7
        "Function_8_2041",         # 08, 8
        "Function_9_2097",         # 09, 9
        "Function_10_20D9",        # 0A, 10
        "Function_11_211B",        # 0B, 11
        "Function_12_2150",        # 0C, 12
        "Function_13_2199",        # 0D, 13
        "Function_14_21E2",        # 0E, 14
        "Function_15_224C",        # 0F, 15
        "Function_16_27CF",        # 10, 16
        "Function_17_2BBD",        # 11, 17
        "Function_18_2C5D",        # 12, 18
        "Function_19_2D0C",        # 13, 19
        "Function_20_2DC0",        # 14, 20
    )


    def Function_0_ADA(): pass

    label("Function_0_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_AE8")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_AF9")
    Jump("loc_AF9")

    label("loc_AF9")

    SetChrPos(0x13, 22160, 0, 11940, 180)
    SetChrPos(0x14, 7890, 0, 11990, 180)
    SetChrPos(0x15, -8220, 0, 11930, 270)
    SetChrPos(0x16, -25800, 0, 11830, 100)
    SetChrPos(0x17, -37890, 0, 11800, 272)
    SetChrPos(0x18, -38090, 0, 29890, 13)
    SetChrPos(0x19, -25930, 0, 29970, 69)
    SetChrPos(0x1A, -8039, 0, 29860, 90)
    SetChrPos(0x1B, 7940, 0, 29730, 71)
    SetChrPos(0x1C, 21810, 0, 29930, 68)
    SetChrPos(0x1D, -37900, 0, 45970, 195)
    SetChrPos(0x1E, -26080, 0, 45970, 87)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    OP_43(0x1D, 0x0, 0x0, 0x2)
    OP_43(0x1E, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x3)
    OP_43(0x17, 0x0, 0x0, 0x3)
    OP_43(0x18, 0x0, 0x0, 0x3)
    OP_43(0x19, 0x0, 0x0, 0x3)
    OP_43(0x14, 0x0, 0x0, 0x4)
    OP_43(0x15, 0x0, 0x0, 0x4)
    OP_43(0x1A, 0x0, 0x0, 0x4)
    OP_43(0x1B, 0x0, 0x0, 0x4)
    OP_43(0x1C, 0x0, 0x0, 0x5)
    OP_43(0x13, 0x0, 0x0, 0x5)
    OP_43(0x13, 0x1, 0x0, 0xF)
    OP_43(0x14, 0x1, 0x0, 0xF)
    OP_43(0x15, 0x1, 0x0, 0xF)
    OP_43(0x16, 0x1, 0x0, 0xF)
    OP_43(0x17, 0x1, 0x0, 0xF)
    OP_43(0x18, 0x1, 0x0, 0xF)
    OP_43(0x19, 0x1, 0x0, 0xF)
    OP_43(0x1A, 0x1, 0x0, 0xF)
    OP_43(0x1B, 0x1, 0x0, 0xF)
    OP_43(0x1C, 0x1, 0x0, 0xF)
    OP_43(0x1D, 0x1, 0x0, 0xF)
    OP_43(0x1E, 0x1, 0x0, 0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_CCF")
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x17, 0x80)
    OP_44(0x15, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x17, 0xFF)

    label("loc_CCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_CF5")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_44(0x13, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1B, 0xFF)

    label("loc_CF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_D1B")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_44(0x1A, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x14, 0xFF)

    label("loc_D1B")

    Return()

    # Function_0_ADA end

    def Function_1_D1C(): pass

    label("Function_1_D1C")

    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_END)), "loc_D36")
    OP_71(0x1, 0x10)
    OP_64(0x1, 0x1)

    label("loc_D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D47")
    OP_1B(0x1, 0x0, 0x14)

    label("loc_D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_D55")
    OP_22(0xAC, 0x1, 0x64)
    OP_B6(0x0)

    label("loc_D55")

    Return()

    # Function_1_D1C end

    def Function_2_D56(): pass

    label("Function_2_D56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D79")
    OP_8D(0xFE, -50290, 47710, -13220, 34370, 2200)
    Jump("Function_2_D56")

    label("loc_D79")

    Return()

    # Function_2_D56 end

    def Function_3_D7A(): pass

    label("Function_3_D7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D9D")
    OP_8D(0xFE, -48590, 32880, -16920, 5190, 2200)
    Jump("Function_3_D7A")

    label("loc_D9D")

    Return()

    # Function_3_D7A end

    def Function_4_D9E(): pass

    label("Function_4_D9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DC1")
    OP_8D(0xFE, -14620, 32800, 13430, 4930, 2200)
    Jump("Function_4_D9E")

    label("loc_DC1")

    Return()

    # Function_4_D9E end

    def Function_5_DC2(): pass

    label("Function_5_DC2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE5")
    OP_8D(0xFE, 10630, 32450, 23760, 5080, 2200)
    Jump("Function_5_DC2")

    label("loc_DE5")

    Return()

    # Function_5_DC2 end

    def Function_6_DE6(): pass

    label("Function_6_DE6")

    EventBegin(0x0)
    OP_22(0xAC, 0x1, 0x64)
    OP_B6(0x0)
    OP_6D(-32990, 0, 64260, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -32119, 0, 62630, 135)
    SetChrPos(0x102, -33540, 0, 62350, 180)
    SetChrPos(0x106, -32290, 0, 63720, 135)
    SetChrPos(0x10B, -33230, 0, 63910, 225)
    SetChrPos(0x107, -34440, 0, 63230, 270)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x107,
        "#065FWh-What's that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10B,
        "#102F#6PGuess the jig is up!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x30, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x31, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x32, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x33, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x34, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x35, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x36, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x37, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x38, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x39, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x40, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x41, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x42, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x43, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x44, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x45, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x47, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x48, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
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
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    SetChrChipByIndex(0x11, 8)
    SetChrChipByIndex(0x12, 8)
    SetChrChipByIndex(0x13, 8)
    SetChrChipByIndex(0x14, 8)
    SetChrChipByIndex(0x15, 8)
    SetChrChipByIndex(0x16, 8)
    SetChrChipByIndex(0x17, 8)
    SetChrChipByIndex(0x18, 8)
    SetChrChipByIndex(0x19, 8)
    SetChrChipByIndex(0x1A, 8)
    SetChrChipByIndex(0x1B, 8)
    SetChrChipByIndex(0x1C, 8)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 8)
    SetChrChipByIndex(0x1F, 8)
    SetChrChipByIndex(0x20, 8)
    SetChrChipByIndex(0x21, 8)
    SetChrChipByIndex(0x22, 8)
    SetChrChipByIndex(0x23, 8)
    SetChrChipByIndex(0x24, 8)
    SetChrChipByIndex(0x25, 8)
    SetChrChipByIndex(0x26, 8)
    SetChrChipByIndex(0x27, 8)
    SetChrChipByIndex(0x28, 8)
    SetChrChipByIndex(0x29, 8)
    SetChrChipByIndex(0x2A, 8)
    SetChrChipByIndex(0x2B, 8)
    SetChrChipByIndex(0x2C, 8)
    SetChrChipByIndex(0x2D, 8)
    SetChrChipByIndex(0x2E, 8)
    SetChrChipByIndex(0x2F, 8)
    SetChrChipByIndex(0x30, 8)
    SetChrChipByIndex(0x31, 8)
    SetChrChipByIndex(0x32, 8)
    SetChrChipByIndex(0x33, 8)
    SetChrChipByIndex(0x34, 8)
    SetChrChipByIndex(0x35, 8)
    SetChrChipByIndex(0x36, 8)
    SetChrChipByIndex(0x37, 8)
    SetChrChipByIndex(0x38, 8)
    SetChrChipByIndex(0x39, 8)
    SetChrChipByIndex(0x3A, 8)
    SetChrChipByIndex(0x3B, 8)
    SetChrChipByIndex(0x3C, 8)
    SetChrChipByIndex(0x3D, 8)
    SetChrChipByIndex(0x3E, 8)
    SetChrChipByIndex(0x3F, 8)
    SetChrChipByIndex(0x40, 8)
    SetChrChipByIndex(0x41, 8)
    SetChrChipByIndex(0x42, 8)
    SetChrChipByIndex(0x43, 8)
    SetChrChipByIndex(0x44, 8)
    SetChrChipByIndex(0x45, 8)
    SetChrChipByIndex(0x46, 8)
    SetChrChipByIndex(0x47, 8)
    SetChrChipByIndex(0x48, 8)
    Fade(1000)
    OP_6D(-11480, 0, 27470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_14AA():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14AA)

    def lambda_14BA():
        OP_6D(14990, 0, 20730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14BA)

    def lambda_14D2():
        OP_67(0, 8220, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14D2)

    def lambda_14EA():
        OP_6B(2300, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14EA)

    def lambda_14FA():
        OP_6E(405, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_14FA)
    Sleep(5000)

    ChrTalk(    #2
        0x8,
        (
            "#700FIt appears we have an intruder!\x02\x03",

            "Get out there and start\x01",
            "searching, men!\x02\x03",

            "#703FPlatoons one through four will\x01",
            "go to the airship port and the\x01",
            "docks and establish a blockade!\x02\x03",

            "Five, six and seven will search \x01",
            "the barracks, watchtower and\x01",
            "research facilities, respectively!\x02\x03",

            "Platoon eight will accompany\x01",
            "me to headquarters!\x02\x03",

            "#704F#3SThat is all. Move out!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 60, -1, -1)
    SetChrName("Soldiers")

    AnonymousTalk(    #3
        "\x07\x00#5SYes, sir!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)

    def lambda_16B2():
        OP_6D(14990, 0, 20730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16B2)

    def lambda_16CA():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16CA)

    def lambda_16E2():
        OP_6B(3890, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16E2)

    def lambda_16F2():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16F2)

    def lambda_1702():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1702)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x30, 0x40)
    SetChrFlags(0x38, 0x40)
    SetChrFlags(0x40, 0x40)
    SetChrFlags(0x48, 0x40)
    OP_43(0x10, 0x1, 0x0, 0xE)
    OP_43(0x18, 0x1, 0x0, 0xE)
    OP_43(0x20, 0x1, 0x0, 0xE)
    OP_43(0x28, 0x1, 0x0, 0xE)
    OP_43(0x30, 0x1, 0x0, 0xE)
    OP_43(0x38, 0x1, 0x0, 0xE)
    OP_43(0x40, 0x1, 0x0, 0xE)
    OP_43(0x48, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0xF, 0x1, 0x0, 0xD)
    OP_43(0x17, 0x1, 0x0, 0xD)
    OP_43(0x1F, 0x1, 0x0, 0xD)
    OP_43(0x27, 0x1, 0x0, 0xD)
    OP_43(0x2F, 0x1, 0x0, 0xD)
    OP_43(0x37, 0x1, 0x0, 0xD)
    OP_43(0x3F, 0x1, 0x0, 0xD)
    OP_43(0x47, 0x1, 0x0, 0xD)
    Sleep(100)

    def lambda_17B9():
        OP_8E(0xFE, 0x4736, 0x0, 0x6B1C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17B9)
    Sleep(700)
    OP_43(0xE, 0x1, 0x0, 0xC)
    OP_43(0x16, 0x1, 0x0, 0xC)
    OP_43(0x1E, 0x1, 0x0, 0xC)
    OP_43(0x26, 0x1, 0x0, 0xC)
    OP_43(0x2E, 0x1, 0x0, 0xC)
    OP_43(0x36, 0x1, 0x0, 0xC)
    OP_43(0x3E, 0x1, 0x0, 0xC)
    OP_43(0x46, 0x1, 0x0, 0xC)
    WaitChrThread(0x8, 0x1)

    def lambda_1816():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x7EC2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1816)
    OP_43(0xD, 0x1, 0x0, 0xB)
    OP_43(0x15, 0x1, 0x0, 0xB)
    OP_43(0x1D, 0x1, 0x0, 0xB)
    OP_43(0x25, 0x1, 0x0, 0xB)
    OP_43(0x2D, 0x1, 0x0, 0xB)
    OP_43(0x35, 0x1, 0x0, 0xB)
    OP_43(0x3D, 0x1, 0x0, 0xB)
    OP_43(0x45, 0x1, 0x0, 0xB)
    Sleep(1000)
    OP_43(0xC, 0x1, 0x0, 0xA)
    OP_43(0x14, 0x1, 0x0, 0xA)
    OP_43(0x1C, 0x1, 0x0, 0xA)
    OP_43(0x24, 0x1, 0x0, 0xA)
    OP_43(0x2C, 0x1, 0x0, 0xA)
    OP_43(0x34, 0x1, 0x0, 0xA)
    OP_43(0x3C, 0x1, 0x0, 0xA)
    OP_43(0x44, 0x1, 0x0, 0xA)
    OP_43(0xB, 0x1, 0x0, 0x9)
    OP_43(0x13, 0x1, 0x0, 0x9)
    OP_43(0x1B, 0x1, 0x0, 0x9)
    OP_43(0x23, 0x1, 0x0, 0x9)
    OP_43(0x2B, 0x1, 0x0, 0x9)
    OP_43(0x33, 0x1, 0x0, 0x9)
    OP_43(0x3B, 0x1, 0x0, 0x9)
    OP_43(0x43, 0x1, 0x0, 0x9)
    OP_43(0x42, 0x1, 0x0, 0x8)
    OP_43(0x41, 0x1, 0x0, 0x7)
    Sleep(530)
    OP_43(0x39, 0x1, 0x0, 0x7)
    OP_43(0x3A, 0x1, 0x0, 0x8)
    Sleep(530)
    OP_43(0x32, 0x1, 0x0, 0x8)
    OP_43(0x31, 0x1, 0x0, 0x7)
    Sleep(530)
    OP_43(0x2A, 0x1, 0x0, 0x8)
    OP_43(0x29, 0x1, 0x0, 0x7)
    Sleep(530)
    OP_43(0x22, 0x1, 0x0, 0x8)
    OP_43(0x21, 0x1, 0x0, 0x7)
    Sleep(530)
    OP_43(0x1A, 0x1, 0x0, 0x8)
    OP_43(0x19, 0x1, 0x0, 0x7)
    Sleep(530)
    OP_43(0x12, 0x1, 0x0, 0x8)
    OP_43(0x11, 0x1, 0x0, 0x7)
    Sleep(530)
    OP_43(0xA, 0x1, 0x0, 0x8)
    OP_43(0x9, 0x1, 0x0, 0x7)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x106, 0x8, 0)
    TurnDirection(0x107, 0x8, 0)
    TurnDirection(0x10B, 0x8, 0)
    Sleep(4000)
    Fade(1000)
    OP_6D(-33270, 0, 63630, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x40, 0x80)
    SetChrFlags(0x48, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x41, 0x80)
    SetChrFlags(0x42, 0x80)
    SetChrFlags(0x43, 0x80)
    SetChrFlags(0x44, 0x80)
    SetChrFlags(0x45, 0x80)
    SetChrFlags(0x46, 0x80)
    SetChrFlags(0x47, 0x80)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    SetChrPos(0x13, 22160, 0, 11940, 180)
    SetChrPos(0x14, 7890, 0, 11990, 180)
    SetChrPos(0x15, -8220, 0, 11930, 270)
    SetChrPos(0x16, -25800, 0, 11830, 100)
    SetChrPos(0x17, -37890, 0, 11800, 272)
    SetChrPos(0x18, -38090, 0, 29890, 13)
    SetChrPos(0x19, -25930, 0, 29970, 69)
    SetChrPos(0x1A, -8039, 0, 29860, 90)
    SetChrPos(0x1B, 7940, 0, 29730, 71)
    SetChrPos(0x1C, 21810, 0, 29930, 68)
    SetChrPos(0x1D, -37900, 0, 45970, 195)
    SetChrPos(0x1E, -26080, 0, 45970, 87)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    OP_43(0x1D, 0x0, 0x0, 0x2)
    OP_43(0x1E, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x3)
    OP_43(0x17, 0x0, 0x0, 0x3)
    OP_43(0x18, 0x0, 0x0, 0x3)
    OP_43(0x19, 0x0, 0x0, 0x3)
    OP_43(0x14, 0x0, 0x0, 0x4)
    OP_43(0x15, 0x0, 0x0, 0x4)
    OP_43(0x1A, 0x0, 0x0, 0x4)
    OP_43(0x1B, 0x0, 0x0, 0x4)
    OP_43(0x1C, 0x0, 0x0, 0x5)
    OP_43(0x13, 0x0, 0x0, 0x5)
    OP_43(0x13, 0x1, 0x0, 0xF)
    OP_43(0x14, 0x1, 0x0, 0xF)
    OP_43(0x15, 0x1, 0x0, 0xF)
    OP_43(0x16, 0x1, 0x0, 0xF)
    OP_43(0x17, 0x1, 0x0, 0xF)
    OP_43(0x18, 0x1, 0x0, 0xF)
    OP_43(0x19, 0x1, 0x0, 0xF)
    OP_43(0x1A, 0x1, 0x0, 0xF)
    OP_43(0x1B, 0x1, 0x0, 0xF)
    OP_43(0x1C, 0x1, 0x0, 0xF)
    OP_43(0x1D, 0x1, 0x0, 0xF)
    OP_43(0x1E, 0x1, 0x0, 0xF)
    SetChrChipByIndex(0x11, 1)
    SetChrChipByIndex(0x12, 1)
    SetChrChipByIndex(0x13, 1)
    SetChrChipByIndex(0x14, 1)
    SetChrChipByIndex(0x15, 1)
    SetChrChipByIndex(0x16, 1)
    SetChrChipByIndex(0x17, 1)
    SetChrChipByIndex(0x18, 1)
    SetChrChipByIndex(0x19, 1)
    SetChrChipByIndex(0x1A, 1)
    SetChrChipByIndex(0x1B, 1)
    SetChrChipByIndex(0x1C, 1)
    SetChrChipByIndex(0x1D, 1)
    SetChrChipByIndex(0x1E, 1)
    SetChrChipByIndex(0x1F, 1)
    SetChrChipByIndex(0x20, 1)
    SetChrChipByIndex(0x21, 1)
    SetChrChipByIndex(0x22, 1)
    SetChrChipByIndex(0x23, 1)
    SetChrChipByIndex(0x24, 1)
    SetChrChipByIndex(0x25, 1)
    SetChrChipByIndex(0x26, 1)
    SetChrChipByIndex(0x27, 1)
    SetChrChipByIndex(0x28, 1)
    SetChrChipByIndex(0x29, 1)
    SetChrChipByIndex(0x2A, 1)
    SetChrChipByIndex(0x2B, 1)
    SetChrChipByIndex(0x2C, 1)
    SetChrChipByIndex(0x2D, 1)
    SetChrChipByIndex(0x2E, 1)
    SetChrChipByIndex(0x2F, 1)
    SetChrChipByIndex(0x30, 1)
    SetChrChipByIndex(0x31, 1)
    SetChrChipByIndex(0x32, 1)
    SetChrChipByIndex(0x33, 1)
    SetChrChipByIndex(0x34, 1)
    SetChrChipByIndex(0x35, 1)
    SetChrChipByIndex(0x36, 1)
    SetChrChipByIndex(0x37, 1)
    SetChrChipByIndex(0x38, 1)
    SetChrChipByIndex(0x39, 1)
    SetChrChipByIndex(0x3A, 1)
    SetChrChipByIndex(0x3B, 1)
    SetChrChipByIndex(0x3C, 1)
    SetChrChipByIndex(0x3D, 1)
    SetChrChipByIndex(0x3E, 1)
    SetChrChipByIndex(0x3F, 1)
    SetChrChipByIndex(0x40, 1)
    SetChrChipByIndex(0x41, 1)
    SetChrChipByIndex(0x42, 1)
    SetChrChipByIndex(0x43, 1)
    SetChrChipByIndex(0x44, 1)
    SetChrChipByIndex(0x45, 1)
    SetChrChipByIndex(0x46, 1)
    SetChrChipByIndex(0x47, 1)
    SetChrChipByIndex(0x48, 1)
    OP_0D()
    Sleep(300)

    ChrTalk(    #4
        0x101,
        (
            "#005FCrap...\x01",
            "Here come the soldiers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#012FLooks like they're putting\x01",
            "the squeeze on the airship\x01",
            "port and the docks...\x02\x03",

            "The major knows what he's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10B,
        (
            "#104FHeh... What else would you\x01",
            "expect from the C.O. of a\x01",
            "fort defense regiment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x107,
        (
            "#065FWh-What should we do...?\x01",
            "Where do we go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        (
            "#057FWell, leaving by the docks\x01",
            "is going to be tricky...\x02\x03",

            "#054FWe need to avoid the guards\x01",
            "and find another way out!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 26890, 0, 25790, 270)
    SetChrPos(0xA, 26950, 0, 19870, 270)
    OP_A2(0x56B)
    OP_28(0x44, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_6_DE6 end

    def Function_7_1FEB(): pass

    label("Function_7_1FEB")

    OP_90(0xFE, 0x5DC, 0x0, 0xFFFFF448, 0x1770, 0x0)
    OP_8E(0xFE, 0x45F6, 0x0, 0x59EC, 0x1770, 0x0)
    OP_8E(0xFE, 0x6914, 0x0, 0x5672, 0x1770, 0x0)
    OP_8E(0xFE, 0x9024, 0x0, 0x5672, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_1FEB end

    def Function_8_2041(): pass

    label("Function_8_2041")

    OP_90(0xFE, 0x5DC, 0x0, 0xFFFFF448, 0x1770, 0x0)
    OP_8E(0xFE, 0x45F6, 0x0, 0x542E, 0x1770, 0x0)
    OP_8E(0xFE, 0x6914, 0x0, 0x514A, 0x1770, 0x0)
    OP_8E(0xFE, 0x9024, 0x0, 0x514A, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_2041 end

    def Function_9_2097(): pass

    label("Function_9_2097")

    OP_8E(0xFE, 0x45F6, 0x0, 0x59EC, 0x1770, 0x0)
    OP_8E(0xFE, 0x6914, 0x0, 0x5672, 0x1770, 0x0)
    OP_8E(0xFE, 0x9024, 0x0, 0x5672, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_2097 end

    def Function_10_20D9(): pass

    label("Function_10_20D9")

    OP_8E(0xFE, 0x45F6, 0x0, 0x542E, 0x1770, 0x0)
    OP_8E(0xFE, 0x6914, 0x0, 0x514A, 0x1770, 0x0)
    OP_8E(0xFE, 0x9024, 0x0, 0x514A, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_20D9 end

    def Function_11_211B(): pass

    label("Function_11_211B")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xE92, 0x0, 0x4DD0, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF3724, 0x1F4, 0x4222, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_211B end

    def Function_12_2150(): pass

    label("Function_12_2150")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xDE8, 0x0, 0x483A, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFC82E, 0x0, 0x6004, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF7FF4, 0x0, 0xFECE, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_2150 end

    def Function_13_2199(): pass

    label("Function_13_2199")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xECE, 0x0, 0x4286, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFC82E, 0x0, 0x6004, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF7FF4, 0x0, 0xFECE, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_2199 end

    def Function_14_21E2(): pass

    label("Function_14_21E2")

    OP_8E(0xFE, 0x45D8, 0x0, 0x3D04, 0x1770, 0x0)
    OP_8E(0xFE, 0x4862, 0x0, 0x50DC, 0x1770, 0x0)
    OP_8E(0xFE, 0x4736, 0x0, 0x6B1C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x7EC2, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFFC36, 0x1F4, 0x8DEA, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_21E2 end

    def Function_15_224C(): pass

    label("Function_15_224C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27CE")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_227F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_227F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22A5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_22A5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22CB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_22CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22F2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_22F2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2318")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_2318")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_233E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_233E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2363")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_2363")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2388")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_2388")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_239C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27CB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x2, 0xFE, 0)
    TurnDirection(0x3, 0xFE, 0)
    TurnDirection(0x4, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    OP_69(0xFE, 0x3E8)
    OP_23(0xAC)
    Battle(0x24F, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_24BD"),
        (SWITCH_DEFAULT, "loc_24C0"),
    )


    label("loc_24BD")

    OP_B4(0x0)
    Return()

    label("loc_24C0")

    EventBegin(0x0)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x106, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x106, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x107, 6)
    OP_6D(-26010, 0, 31860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -26500, 0, 33350, 183)
    SetChrPos(0x106, -27660, 0, 32600, 140)
    SetChrPos(0x102, -25580, 0, 33330, 188)
    SetChrPos(0x107, -27660, 0, 33860, 155)
    SetChrPos(0x10B, -26280, 0, 34780, 168)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 7)
    SetChrChipByIndex(0xA, 7)
    SetChrChipByIndex(0xB, 7)
    SetChrChipByIndex(0xC, 7)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, -27380, 0, 30460, 198)
    SetChrPos(0xA, -25280, 0, 31010, 89)
    SetChrPos(0xB, -26360, 0, 28750, 278)
    SetChrPos(0xC, -25160, 0, 29280, 2)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272B")

    ChrTalk(    #9
        0x101,
        (
            "#004FDamn it...\x01",
            "We're in trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#012FThat last one seems to have\x01",
            "alerted the other soldiers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x106,
        (
            "#054FLet's withdraw to the research\x01",
            "area for now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B1")

    label("loc_272B")


    ChrTalk(    #12
        0x101,
        "#007FOops... Not again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x106,
        (
            "#057FThe rest of the drones have joined\x01",
            "the party... Let's get back to the\x01",
            "research area for now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B1")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C3107   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_27CB")

    Jump("Function_15_224C")

    label("loc_27CE")

    Return()

    # Function_15_224C end

    def Function_16_27CF(): pass

    label("Function_16_27CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27DC")
    Return()

    label("loc_27DC")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2858():
        TurnDirection(0xFE, 0x0, 800)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2858)

    def lambda_2866():
        TurnDirection(0xFE, 0x0, 800)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2866)
    OP_6D(24450, 0, 23030, 1000)

    ChrTalk(    #14
        0x11,
        "You!\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_28A6():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_28A6)

    def lambda_28B4():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_28B4)

    def lambda_28C2():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_28C2)

    def lambda_28D0():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_28D0)

    def lambda_28DE():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_28DE)

    ChrTalk(    #15
        0x12,
        "Intruders spotted!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2920")

    ChrTalk(    #16
        0x101,
        "#005FCrap...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2981")

    label("loc_2920")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2942")

    ChrTalk(    #17
        0x102,
        "#012FDamn it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2981")

    label("loc_2942")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2963")

    ChrTalk(    #18
        0x107,
        "#065FEep...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2981")

    label("loc_2963")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2981")

    ChrTalk(    #19
        0x106,
        "#057FBah...!\x02",
    )

    CloseMessageWindow()

    label("loc_2981")

    OP_23(0xAC)
    Battle(0x24E, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_299D"),
        (SWITCH_DEFAULT, "loc_29A0"),
    )


    label("loc_299D")

    OP_B4(0x0)
    Return()

    label("loc_29A0")

    EventBegin(0x0)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x106, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x106, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x107, 6)
    OP_6D(27210, 0, 23250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(66000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 24110, 0, 23210, 88)
    SetChrPos(0x106, 23600, 0, 24470, 127)
    SetChrPos(0x102, 23740, 0, 21940, 72)
    SetChrPos(0x107, 22580, 0, 23620, 91)
    SetChrPos(0x10B, 22110, 0, 22320, 94)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 7)
    SetChrChipByIndex(0xA, 7)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0x9, 26660, 0, 24400, 270)
    SetChrPos(0xA, 26530, 0, 22820, 225)
    SetChrPos(0xC, 36620, 400, 22980, 45)
    SetChrPos(0xB, 36620, 400, 22980, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #20
        0xC,
        "What was that noise?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xB,
        "Intruders?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#580FMore incoming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x106,
        "#054FBack to the research area!\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C3107   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_27CF end

    def Function_17_2BBD(): pass

    label("Function_17_2BBD")

    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #24
        "\x07\x05The door is firmly shut.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    Return()

    # Function_17_2BBD end

    def Function_18_2C5D(): pass

    label("Function_18_2C5D")

    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #25
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    Return()

    # Function_18_2C5D end

    def Function_19_2D0C(): pass

    label("Function_19_2D0C")

    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #26
        "\x07\x05The door is firmly shut.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    Return()

    # Function_19_2D0C end

    def Function_20_2DC0(): pass

    label("Function_20_2DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3223")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 38740, 400, 22480, 270)
    SetChrPos(0x12, 38480, 400, 23440, 270)

    ChrTalk(    #27
        0x11,
        "You!\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2E27():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2E27)

    def lambda_2E35():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2E35)

    def lambda_2E43():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2E43)

    def lambda_2E51():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2E51)

    def lambda_2E5F():
        TurnDirection(0xFE, 0x11, 800)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_2E5F)
    Sleep(500)
    Fade(2000)

    def lambda_2E77():
        OP_6D(36080, 400, 23100, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2E77)

    def lambda_2E8F():
        OP_6C(80000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E8F)
    WaitChrThread(0x12, 0x1)
    OP_0D()

    ChrTalk(    #28
        0x12,
        "#6PIntruders spotted!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EDC")

    ChrTalk(    #29
        0x101,
        "#005FCrap...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F3D")

    label("loc_2EDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EFE")

    ChrTalk(    #30
        0x102,
        "#016FDamn it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F3D")

    label("loc_2EFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F1F")

    ChrTalk(    #31
        0x107,
        "#065FEep...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F3D")

    label("loc_2F1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3D")

    ChrTalk(    #32
        0x106,
        "#057FBah...!\x02",
    )

    CloseMessageWindow()

    label("loc_2F3D")

    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x106, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x106, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x107, 6)

    def lambda_2F83():
        OP_6D(29430, 0, 23120, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F83)
    SetChrChipByIndex(0x11, 9)

    def lambda_2FA0():
        OP_8E(0xFE, 0x7120, 0x190, 0x57C6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2FA0)
    Sleep(200)
    SetChrChipByIndex(0x12, 9)

    def lambda_2FC5():
        OP_8E(0xFE, 0x7166, 0x190, 0x5BF4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2FC5)
    Sleep(1000)
    OP_23(0xAC)
    Battle(0x24E, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2FFB"),
        (SWITCH_DEFAULT, "loc_2FFE"),
    )


    label("loc_2FFB")

    OP_B4(0x0)
    Return()

    label("loc_2FFE")

    EventBegin(0x0)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x106, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x106, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x107, 6)
    OP_6D(26830, 0, 24070, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(66000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 24110, 0, 23210, 88)
    SetChrPos(0x106, 23600, 0, 24470, 127)
    SetChrPos(0x102, 23740, 0, 21940, 72)
    SetChrPos(0x107, 22580, 0, 23620, 91)
    SetChrPos(0x10B, 22110, 0, 22320, 94)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 7)
    SetChrChipByIndex(0xA, 7)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0x9, 26660, 0, 24400, 270)
    SetChrPos(0xA, 26530, 0, 22820, 225)
    SetChrPos(0xC, 36620, 400, 22980, 45)
    SetChrPos(0xB, 36620, 400, 22980, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #33
        0xC,
        "#3PWhat was that noise?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        "#3PIntruders?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#580FMore incoming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x106,
        "#054FBack to the research area!\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C3107   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3387")

    label("loc_3223")

    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C7")

    ChrTalk(    #37
        0x106,
        (
            "#057FThe port is no good...\x01",
            "It's already been secured.\x02\x03",

            "We have to find another escape route.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333C")

    label("loc_32C7")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #38
        0x106,
        (
            "#057FHey, the port's a no-go. The\x01",
            "soldiers have it locked down.\x02\x03",

            "We've got to find another\x01",
            "escape route.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333C")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)

    label("loc_3387")

    Return()

    # Function_20_2DC0 end

    SaveToFile()

Try(main)
