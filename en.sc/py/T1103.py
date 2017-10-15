from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1103   ._SN',
        MapName             = 'Bose',
        Location            = 'T1103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1103_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Loewe',                                # 9
        'Lugran',                               # 10
        'Paul',                                 # 11
        'Citizen',                              # 12
        'Citizen',                              # 13
        'Citizen',                              # 14
        'Citizen',                              # 15
        'Citizen',                              # 16
        'Citizen',                              # 17
        'Citizen',                              # 18
        'Citizen',                              # 19
        'Citizen',                              # 20
        'Citizen',                              # 21
        'Citizen',                              # 22
        'Citizen',                              # 23
        'Citizen',                              # 24
        'Citizen',                              # 25
        'Citizen',                              # 26
        'Citizen',                              # 27
        'Mayor Maybelle',                       # 28
        'Soldier',                              # 29
        'Soldier',                              # 30
        'Soldier',                              # 31
        'Soldier',                              # 32
        'Ancient Dragon',                       # 33
        'Dragon',                               # 34
        'Carol',                                # 35
        'Gantz',                                # 36
        'Lyndon',                               # 37
        'Aldan',                                # 38
        'Borden',                               # 39
        'Trino',                                # 40
        'Buck',                                 # 41
        'Lyril',                                # 42
        'Claire',                               # 43
        'Corna',                                # 44
        'Jacob',                                # 45
        'Letta',                                # 46
        'Fannie',                               # 47
        'Royal Army Officer',                   # 48
        'Soldier',                              # 49
        'Soldier',                              # 50
        'Soldier',                              # 51
        'Harry',                                # 52
        'Mina',                                 # 53
        'Orvid',                                # 54
        'Carpenter',                            # 55
        'Carpenter',                            # 56
        'Carpenter',                            # 57
        'Carpenter',                            # 58
        'Carpenter',                            # 59
        'Young Butler',                         # 60
        'Meissen',                              # 61
        'West Bose Highway',                    # 62
        'East Bose Highway',                    # 63
        'Bose - South Block',                   # 64
        'Bose International Port',              # 65
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
        'ED6_DT07/CH02040 ._CH',             # 00
        'ED6_DT07/CH02380 ._CH',             # 01
        'ED6_DT07/CH01220 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01570 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01690 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01150 ._CH',             # 0A
        'ED6_DT07/CH02360 ._CH',             # 0B
        'ED6_DT07/CH01300 ._CH',             # 0C
        'ED6_DT26/CH20363 ._CH',             # 0D
        'ED6_DT07/CH01030 ._CH',             # 0E
        'ED6_DT07/CH01270 ._CH',             # 0F
        'ED6_DT07/CH01660 ._CH',             # 10
        'ED6_DT07/CH01040 ._CH',             # 11
        'ED6_DT07/CH01680 ._CH',             # 12
        'ED6_DT07/CH01200 ._CH',             # 13
        'ED6_DT07/CH01140 ._CH',             # 14
        'ED6_DT07/CH01070 ._CH',             # 15
        'ED6_DT07/CH01150 ._CH',             # 16
        'ED6_DT07/CH01180 ._CH',             # 17
        'ED6_DT07/CH01000 ._CH',             # 18
        'ED6_DT07/CH01040 ._CH',             # 19
        'ED6_DT07/CH01050 ._CH',             # 1A
        'ED6_DT07/CH01600 ._CH',             # 1B
        'ED6_DT07/CH01640 ._CH',             # 1C
        'ED6_DT07/CH01160 ._CH',             # 1D
        'ED6_DT07/CH01170 ._CH',             # 1E
        'ED6_DT07/CH01120 ._CH',             # 1F
        'ED6_DT07/CH01500 ._CH',             # 20
        'ED6_DT26/CH20243 ._CH',             # 21
        'ED6_DT27/CH04540 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
        'ED6_DT07/CH02380P._CP',             # 01
        'ED6_DT07/CH01220P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01570P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01690P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01150P._CP',             # 0A
        'ED6_DT07/CH02360P._CP',             # 0B
        'ED6_DT07/CH01300P._CP',             # 0C
        'ED6_DT26/CH20363P._CP',             # 0D
        'ED6_DT07/CH01030P._CP',             # 0E
        'ED6_DT07/CH01270P._CP',             # 0F
        'ED6_DT07/CH01660P._CP',             # 10
        'ED6_DT07/CH01040P._CP',             # 11
        'ED6_DT07/CH01680P._CP',             # 12
        'ED6_DT07/CH01200P._CP',             # 13
        'ED6_DT07/CH01140P._CP',             # 14
        'ED6_DT07/CH01070P._CP',             # 15
        'ED6_DT07/CH01150P._CP',             # 16
        'ED6_DT07/CH01180P._CP',             # 17
        'ED6_DT07/CH01000P._CP',             # 18
        'ED6_DT07/CH01040P._CP',             # 19
        'ED6_DT07/CH01050P._CP',             # 1A
        'ED6_DT07/CH01600P._CP',             # 1B
        'ED6_DT07/CH01640P._CP',             # 1C
        'ED6_DT07/CH01160P._CP',             # 1D
        'ED6_DT07/CH01170P._CP',             # 1E
        'ED6_DT07/CH01120P._CP',             # 1F
        'ED6_DT07/CH01500P._CP',             # 20
        'ED6_DT26/CH20243P._CP',             # 21
        'ED6_DT27/CH04540P._CP',             # 22
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63800,
        Z                   = 0,
        Y                   = 43560,
        Direction           = 321,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49430,
        Z                   = 0,
        Y                   = 47820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29530,
        Z                   = 0,
        Y                   = 76910,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 37770,
        Z                   = 0,
        Y                   = 73470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 44080,
        Z                   = 0,
        Y                   = 76420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48620,
        Z                   = 0,
        Y                   = 81230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 42290,
        Z                   = 0,
        Y                   = 44430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 44100,
        Z                   = 0,
        Y                   = 42920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 61700,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 66890,
        Z                   = 0,
        Y                   = 49260,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 46080,
        Z                   = 0,
        Y                   = 42060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 68260,
        Z                   = 0,
        Y                   = 52310,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 63060,
        Z                   = 0,
        Y                   = 49000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 41990,
        Z                   = 0,
        Y                   = 46350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 37580,
        Z                   = 0,
        Y                   = 47610,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 46060,
        Z                   = 0,
        Y                   = 77320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 72340,
        Z                   = 0,
        Y                   = 63740,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 22580,
        Z                   = 0,
        Y                   = 48730,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 45370,
        Z                   = 0,
        Y                   = 78340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 30140,
        Z                   = 0,
        Y                   = 73750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 30140,
        Z                   = 0,
        Y                   = 72630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 49430,
        Z                   = 0,
        Y                   = 47820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 44780,
        Z                   = 4600,
        Y                   = 51050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53490,
        Z                   = 6420,
        Y                   = 59900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56870,
        Z                   = 4600,
        Y                   = 53430,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 41670,
        Z                   = 4600,
        Y                   = 68230,
        Direction           = 314,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55760,
        Z                   = 4600,
        Y                   = 62760,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 66030,
        Z                   = 0,
        Y                   = 70470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 29410,
        Z                   = 0,
        Y                   = 56670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 45190,
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

    DeclNpc(
        X                   = 87650,
        Z                   = 0,
        Y                   = 60410,
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

    DeclNpc(
        X                   = 47990,
        Z                   = -3000,
        Y                   = 29310,
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

    DeclNpc(
        X                   = 47940,
        Z                   = 0,
        Y                   = 93220,
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


    DeclEvent(
        X                   = 75900,
        Y                   = -1000,
        Z                   = 53900,
        Range               = 76600,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x10554,
        Unknown_18          = 0x0,
        Unknown_1C          = 51,
    )

    DeclEvent(
        X                   = 17000,
        Y                   = -1000,
        Z                   = 50100,
        Range               = 18000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9D6C,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = 25200,
        Y                   = 0,
        Z                   = 57940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 67,
    )

    DeclEvent(
        X                   = 18880,
        Y                   = 0,
        Z                   = 76030,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 68,
    )

    DeclEvent(
        X                   = 36200,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 70,
    )

    DeclEvent(
        X                   = 38540,
        Y                   = 0,
        Z                   = 59990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 48040,
        Y                   = 100,
        Z                   = 69500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 57480,
        Y                   = 0,
        Z                   = 60010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 48010,
        Y                   = 0,
        Z                   = 50550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 67340,
        Y                   = -500,
        Z                   = 73070,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 72,
    )

    DeclEvent(
        X                   = 72240,
        Y                   = 0,
        Z                   = 44910,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 73,
    )

    DeclEvent(
        X                   = 47960,
        Y                   = 0,
        Z                   = 85570,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 74,
    )


    ScpFunction(
        "Function_0_A82",          # 00, 0
        "Function_1_CEF",          # 01, 1
        "Function_2_DDB",          # 02, 2
        "Function_3_EF8",          # 03, 3
        "Function_4_F45",          # 04, 4
        "Function_5_F97",          # 05, 5
        "Function_6_1024",         # 06, 6
        "Function_7_10DB",         # 07, 7
        "Function_8_159D",         # 08, 8
        "Function_9_1AE7",         # 09, 9
        "Function_10_1F59",        # 0A, 10
        "Function_11_2209",        # 0B, 11
        "Function_12_22D4",        # 0C, 12
        "Function_13_238A",        # 0D, 13
        "Function_14_2651",        # 0E, 14
        "Function_15_27E7",        # 0F, 15
        "Function_16_2A66",        # 10, 16
        "Function_17_2B5C",        # 11, 17
        "Function_18_2DA9",        # 12, 18
        "Function_19_3152",        # 13, 19
        "Function_20_33B6",        # 14, 20
        "Function_21_36A2",        # 15, 21
        "Function_22_38E4",        # 16, 22
        "Function_23_3BD7",        # 17, 23
        "Function_24_406B",        # 18, 24
        "Function_25_4496",        # 19, 25
        "Function_26_4538",        # 1A, 26
        "Function_27_4676",        # 1B, 27
        "Function_28_49C7",        # 1C, 28
        "Function_29_4BA8",        # 1D, 29
        "Function_30_5067",        # 1E, 30
        "Function_31_5124",        # 1F, 31
        "Function_32_6428",        # 20, 32
        "Function_33_643F",        # 21, 33
        "Function_34_6486",        # 22, 34
        "Function_35_6610",        # 23, 35
        "Function_36_6C21",        # 24, 36
        "Function_37_6CDD",        # 25, 37
        "Function_38_6D39",        # 26, 38
        "Function_39_6D7F",        # 27, 39
        "Function_40_6DC5",        # 28, 40
        "Function_41_6E0B",        # 29, 41
        "Function_42_6E51",        # 2A, 42
        "Function_43_6E97",        # 2B, 43
        "Function_44_6EDD",        # 2C, 44
        "Function_45_6F23",        # 2D, 45
        "Function_46_6F55",        # 2E, 46
        "Function_47_6F85",        # 2F, 47
        "Function_48_6FDD",        # 30, 48
        "Function_49_700D",        # 31, 49
        "Function_50_703D",        # 32, 50
        "Function_51_71AB",        # 33, 51
        "Function_52_7850",        # 34, 52
        "Function_53_79AA",        # 35, 53
        "Function_54_7A1E",        # 36, 54
        "Function_55_7A92",        # 37, 55
        "Function_56_7B06",        # 38, 56
        "Function_57_7B7A",        # 39, 57
        "Function_58_7DED",        # 3A, 58
        "Function_59_7E6D",        # 3B, 59
        "Function_60_7EAA",        # 3C, 60
        "Function_61_7EE9",        # 3D, 61
        "Function_62_7F28",        # 3E, 62
        "Function_63_8952",        # 3F, 63
        "Function_64_89DB",        # 40, 64
        "Function_65_8A36",        # 41, 65
        "Function_66_8A93",        # 42, 66
        "Function_67_8AEC",        # 43, 67
        "Function_68_8AF0",        # 44, 68
        "Function_69_8AF4",        # 45, 69
        "Function_70_8AF8",        # 46, 70
        "Function_71_8AFC",        # 47, 71
        "Function_72_8B00",        # 48, 72
        "Function_73_8B04",        # 49, 73
        "Function_74_8B08",        # 4A, 74
    )


    def Function_0_A82(): pass

    label("Function_0_A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_AD4")
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x23, 40190, 0, 71770, 270)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3C, 0x80)
    Jump("loc_C75")

    label("loc_AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_B84")
    SetChrPos(0x1B, 47960, 0, 76090, 180)
    SetChrPos(0x25, 65480, 0, 69210, 225)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x22, 29530, 0, 76910, 270)
    SetChrPos(0x33, 30140, 0, 73750, 135)
    SetChrPos(0x34, 30140, 0, 72630, 135)
    SetChrPos(0x24, 30060, 0, 66160, 90)
    SetChrPos(0x2C, 65269, 0, 59980, 275)
    OP_43(0x2C, 0x0, 0x6, 0x2)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    Jump("loc_C75")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_END)), "loc_BFA")
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x22, 29530, 0, 76910, 270)
    SetChrPos(0x33, 30140, 0, 73750, 135)
    SetChrPos(0x34, 30140, 0, 72630, 135)
    SetChrPos(0x24, 30060, 0, 66160, 90)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    Jump("loc_C75")

    label("loc_BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_C75")
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrPos(0x2D, 66520, 0, 53320, 283)
    OP_43(0x2D, 0x0, 0x6, 0x2)
    SetChrPos(0x2E, 67200, 0, 51980, 270)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x23, 0x80)
    ClearChrFlags(0x3B, 0x80)
    OP_4A(0x36, 255)
    OP_4A(0x37, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    OP_4A(0x3A, 255)

    label("loc_C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_C85")
    SetChrFlags(0x35, 0x80)

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_C9B")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 57)
    Jump("loc_CEE")

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_CBA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 62)
    Jump("loc_CEE")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_CD9")
    OP_A3(0x10F4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 35)
    Jump("loc_CEE")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 31)

    label("loc_CEE")

    Return()

    # Function_0_A82 end

    def Function_1_CEF(): pass

    label("Function_1_CEF")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEF660, 0x230041)
    OP_72(0x13, 0x20)
    OP_72(0x13, 0x8)
    OP_71(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_END)), "loc_D1F")
    OP_71(0x1F, 0x4)
    Jump("loc_D68")

    label("loc_D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68")
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x20, 0x4)

    label("loc_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D83")
    OP_72(0x21, 0x4)
    OP_72(0x22, 0x4)
    OP_72(0x23, 0x4)

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_END)), "loc_D8D")
    Jump("loc_D9E")

    label("loc_D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D9E")
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)

    label("loc_D9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDA")
    OP_72(0xA, 0x10)
    OP_72(0xB, 0x10)
    OP_72(0xC, 0x10)
    OP_72(0xD, 0x10)
    OP_6F(0xA, 59)
    OP_6F(0xB, 59)
    OP_6F(0xC, 59)
    OP_6F(0xD, 59)

    label("loc_DDA")

    Return()

    # Function_1_CEF end

    def Function_2_DDB(): pass

    label("Function_2_DDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EF7")
    OP_8E(0xFE, 0xF654, 0x0, 0x119F4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF2A8, 0x0, 0x12214, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEF74, 0x0, 0x12426, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8A16, 0x0, 0x12426, 0x7D0, 0x0)
    OP_8E(0xFE, 0x839A, 0x0, 0x120A2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0x11E36, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0xEA7E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x8048, 0x0, 0xBC66, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8264, 0x0, 0xB414, 0x7D0, 0x0)
    OP_8E(0xFE, 0x85E8, 0x0, 0xAFE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEB96, 0x0, 0xAFE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF122, 0x0, 0xB1C6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF654, 0x0, 0xB874, 0x7D0, 0x0)
    Jump("Function_2_DDB")

    label("loc_EF7")

    Return()

    # Function_2_DDB end

    def Function_3_EF8(): pass

    label("Function_3_EF8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F44")
    OP_8E(0xFE, 0xF0BE, 0x0, 0xCC1A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xF104, 0x0, 0xD7E6, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(3000)
    Jump("Function_3_EF8")

    label("loc_F44")

    Return()

    # Function_3_EF8 end

    def Function_4_F45(): pass

    label("Function_4_F45")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F96")
    Sleep(1500)
    OP_8E(0xFE, 0xA6AE, 0x0, 0xB50E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xA1A4, 0x0, 0xB50E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_4_F45")

    label("loc_F96")

    Return()

    # Function_4_F45 end

    def Function_5_F97(): pass

    label("Function_5_F97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1023")
    OP_8E(0xFE, 0x99DE, 0x11F8, 0xDEBC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x9AD8, 0x11F8, 0xC7B0, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xAF32, 0x11F8, 0xC7B0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x9AD8, 0x11F8, 0xC7B0, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(3000)
    Jump("Function_5_F97")

    label("loc_1023")

    Return()

    # Function_5_F97 end

    def Function_6_1024(): pass

    label("Function_6_1024")

    TalkBegin(0x3C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_10D7")

    ChrTalk(    #0
        0xFE,
        "Oho ho ho!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "The construction's come quite a ways\x01",
            "in a short time, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Mmmmm! I can't wait to once again stroll\x01",
            "the market, browsing the antiques...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D7")

    TalkEnd(0x3C)
    Return()

    # Function_6_1024 end

    def Function_7_10DB(): pass

    label("Function_7_10DB")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_12AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11A0")

    ChrTalk(    #3
        0xFE,
        (
            "The army is really busy with their dragon\x01",
            "hunt, and everyone in town is busy with\x01",
            "the repairs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "And here I am, trying to figure out\x01",
            "what to serve for dinner tonight!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A9")

    label("loc_11A0")


    ChrTalk(    #5
        0xFE,
        (
            "The army is really busy with their dragon\x01",
            "hunt, and everyone in town is busy with\x01",
            "the repairs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "And here I am, trying to figure out\x01",
            "what to serve for dinner tonight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "It feels petty in comparison, but even\x01",
            "small things like this can be hard work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_12A9")

    Jump("loc_1599")

    label("loc_12AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_13D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1322")

    ChrTalk(    #8
        0xFE,
        (
            "The market merchants are working\x01",
            "out of the hotel for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "I'm amazed at their dedication!\x02",
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_1322")


    ChrTalk(    #10
        0xFE,
        (
            "The market merchants are working\x01",
            "out of the hotel for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Their dedication really is amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "It does mean I've lost my excuse to\x01",
            "be lazy about dinner, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_13D5")

    Jump("loc_1599")

    label("loc_13D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_148C")

    ChrTalk(    #13
        0xFE,
        (
            "I never imagined something like that\x01",
            "could happen to the market! Or the city!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "My dinner thoughts seem trivial in\x01",
            "comparison. I can't even concentrate...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_148C")


    ChrTalk(    #15
        0xFE,
        (
            "I never imagined something like that\x01",
            "could happen to the market! Or the city!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "My dinner thoughts seem trivial in\x01",
            "comparison. I can't even concentrate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "You know what, today will be bread\x01",
            "and soup. If they don't like it, well,\x01",
            "they don't have to eat!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1599")

    TalkEnd(0x22)
    Return()

    # Function_7_10DB end

    def Function_8_159D(): pass

    label("Function_8_159D")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_174A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1633")

    ChrTalk(    #18
        0xFE,
        "I decided to help out with the repairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I want the lady who runs the castella shop\x01",
            "to get back where she was, and soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_1633")


    ChrTalk(    #20
        0xFE,
        "I decided to help out with the repairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I want the lady who runs the castella shop\x01",
            "to get back where she was, and soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Once the market reopens, her fiance\x01",
            "will probably go back to his ice cream\x01",
            "stand, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "Not that it bothers me! No. Nope. No siree.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1747")

    Jump("loc_1AE3")

    label("loc_174A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_194A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_181C")

    ChrTalk(    #24
        0xFE,
        (
            "The lady running the castella shop is in\x01",
            "the same space as her fiance right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I think they'll go back to separate stands\x01",
            "once the market reopens...but, then\x01",
            "again, they might not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1947")

    label("loc_181C")


    ChrTalk(    #26
        0xFE,
        (
            "*sigh* I'd really like to get to know\x01",
            "the lady who runs the castella shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Right now she's running her shop with\x01",
            "her fiance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I think they'll go back to separate stands\x01",
            "once the market reopens...but, then\x01",
            "again, they might not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Maybe I should help out with the\x01",
            "reconstruction.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1947")

    Jump("loc_1AE3")

    label("loc_194A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19FF")

    ChrTalk(    #30
        0xFE,
        (
            "The lady running the castella shop is in\x01",
            "the same space as her fiance right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I knew it would happen at some point,\x01",
            "but it was still a bit of a shock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE3")

    label("loc_19FF")


    ChrTalk(    #32
        0xFE,
        (
            "I'd heard the castella shop lady\x01",
            "had evacuated to the bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "But when I checked inside, she was\x01",
            "running her business with her fiance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I knew they'd start working together at\x01",
            "some point, but it was still a shock.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1AE3")

    TalkEnd(0x23)
    Return()

    # Function_8_159D end

    def Function_9_1AE7(): pass

    label("Function_9_1AE7")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B97")

    ChrTalk(    #35
        0xFE,
        (
            "According to all the ancient legends,\x01",
            "dragons are supposed to be gentle\x01",
            "and intelligent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Why would one wreck a marketplace and\x01",
            "torch orchards...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D6C")

    label("loc_1B97")


    ChrTalk(    #37
        0xFE,
        (
            "From all appearances, that was indeed\x01",
            "a dragon of old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "Something still feels wrong, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "According to all the ancient legends,\x01",
            "dragons are supposed to be gentle\x01",
            "and intelligent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "But the dragon we've seen brazenly\x01",
            "attacked a city and put orchards to the\x01",
            "flame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Legends are never one hundred percent\x01",
            "reality, but there's usually at least a kernel\x01",
            "of truth to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Why would our dragon be so different\x01",
            "from the ones in the legends...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1D6C")

    Jump("loc_1F55")

    label("loc_1D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E13")

    ChrTalk(    #43
        0xFE,
        (
            "That was absolutely an ancient dragon.\x01",
            "No question at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "All right, Lyndon, calm down.\x01",
            "I need to collect testimony from the witnesses!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F55")

    label("loc_1E13")


    ChrTalk(    #45
        0xFE,
        (
            "D-D-Did you see that just now?!\x01",
            "That was an ancient dragon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "A DRAGON! One of the legendary creatures\x01",
            "said to have lived since before the\x01",
            "Great Collapse over a millennium ago!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I knew I was right when I theorized they\x01",
            "still lived!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I-I need to get testimony from the\x01",
            "witnesses and draw a sketch and...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1F55")

    TalkEnd(0x24)
    Return()

    # Function_9_1AE7 end

    def Function_10_1F59(): pass

    label("Function_10_1F59")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_20C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1FE4")

    ChrTalk(    #49
        0xFE,
        (
            "The Liberl News bought that photo\x01",
            "I took of the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Hehehe! I can't wait for the next issue\x01",
            "to come out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C5")

    label("loc_1FE4")


    ChrTalk(    #51
        0xFE,
        "That monster was apparently an ancient dragon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "No one's seen one in, like, a billion years,\x01",
            "apparently, so the Liberl News bought the\x01",
            "photo I took of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Hehehe! I can't wait for the next issue\x01",
            "to come out!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_20C5")

    Jump("loc_2205")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_212A")

    ChrTalk(    #54
        0xFE,
        "I-I got a photo of that monster...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Do you think this could be a scoop?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2205")

    label("loc_212A")


    ChrTalk(    #56
        0xFE,
        (
            "I-I saw that monster fly overhead on\x01",
            "my way in from the landing port!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "I took a photo without even thinking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Do you think this could be a scoop?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Maybe I can sell this to a magazine or something!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2205")

    TalkEnd(0x25)
    Return()

    # Function_10_1F59 end

    def Function_11_2209(): pass

    label("Function_11_2209")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_22D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_226A")

    ChrTalk(    #60
        0xFE,
        (
            "The market is the heart of Bose.\x01",
            "We need to deal with this immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D0")

    label("loc_226A")


    ChrTalk(    #61
        0xFE,
        (
            "What a disaster.\x01",
            "The market, brazenly attacked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "We need to deal with this immediately.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_22D0")

    TalkEnd(0x26)
    Return()

    # Function_11_2209 end

    def Function_12_22D4(): pass

    label("Function_12_22D4")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2386")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2345")

    ChrTalk(    #63
        0xFE,
        (
            "With the market a ruin, Bose's economic\x01",
            "future is dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "We've got to do something!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2386")

    label("loc_2345")


    ChrTalk(    #65
        0xFE,
        "What lunacy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "It's practically like a war's started!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2386")

    TalkEnd(0x27)
    Return()

    # Function_12_22D4 end

    def Function_13_238A(): pass

    label("Function_13_238A")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_250E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2435")

    ChrTalk(    #67
        0xFE,
        "Construction work's goin' pretty smoothly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "We should have everything open again\x01",
            "ahead of schedule. The power of people\x01",
            "comin' together, man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250B")

    label("loc_2435")


    ChrTalk(    #69
        0xFE,
        "Construction work's goin' pretty smoothly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "The opinion going around is that we'll\x01",
            "be done sooner than expected at the\x01",
            "rate we're going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Got the strength of the merchants of\x01",
            "Bose on display, here!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_250B")

    Jump("loc_264D")

    label("loc_250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_264D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2589")

    ChrTalk(    #72
        0xFE,
        "We've already started repairing the market.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Nobody asked, but I figured I should\x01",
            "volunteer too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264D")

    label("loc_2589")


    ChrTalk(    #74
        0xFE,
        "We're already started repairing the market.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "We can't just hang out and bother the\x01",
            "folks in the hotel forever, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I left the store to Trayton and came\x01",
            "out to lend a hand.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_264D")

    TalkEnd(0x28)
    Return()

    # Function_13_238A end

    def Function_14_2651(): pass

    label("Function_14_2651")

    TalkBegin(0x29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_26DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_268B")

    ChrTalk(    #77
        0xFE,
        "I hope they fix the market soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26D7")

    label("loc_268B")


    ChrTalk(    #78
        0xFE,
        "I can shop all by myself now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "I hope they fix the market soon.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_26D7")

    Jump("loc_27E3")

    label("loc_26DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_27E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2742")

    ChrTalk(    #80
        0xFE,
        "The father at the church said, um.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "He said that dragons are really peaceful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E3")

    label("loc_2742")


    ChrTalk(    #82
        0xFE,
        "The father at the church said, um.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "He said that dragons are really peaceful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "But why are they so scary, then?\x01",
            "Why did this one do a bad thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_27E3")

    TalkEnd(0x29)
    Return()

    # Function_14_2651 end

    def Function_15_27E7(): pass

    label("Function_15_27E7")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_292E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2889")

    ChrTalk(    #85
        0xFE,
        (
            "So many townspeople are helping with\x01",
            "the reconstruction!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Things are going so well, it seems like\x01",
            "they'll be done ahead of schedule!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_292B")

    label("loc_2889")


    ChrTalk(    #87
        0xFE,
        (
            "So many townspeople are helping with\x01",
            "the reconstruction!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "I'd like to help, too, if I could.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I feel like I'd just be getting in the\x01",
            "way, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_292B")

    Jump("loc_2A62")

    label("loc_292E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_29A6")

    ChrTalk(    #90
        0xFE,
        (
            "What a surprise!\x01",
            "They've already started work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "When did they get everything ready,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A62")

    label("loc_29A6")


    ChrTalk(    #92
        0xFE,
        (
            "It was really loud this morning,\x01",
            "so I came out to have a look,\x01",
            "and saw this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "What a surprise!\x01",
            "They've already started work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "When did they get everything ready,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2A62")

    TalkEnd(0x2A)
    Return()

    # Function_15_27E7 end

    def Function_16_2A66(): pass

    label("Function_16_2A66")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2AE3")

    ChrTalk(    #95
        0xFE,
        "I've looked so hard and still can't find her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "I wonder if she'd even still be here,\x01",
            "if she's alive...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B58")

    label("loc_2AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2B58")

    ChrTalk(    #97
        0xFE,
        (
            "I still need to search around here\x01",
            "before I go to the southern block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "Oh, dumpling...where are you?\x02",
    )

    CloseMessageWindow()

    label("loc_2B58")

    TalkEnd(0x2B)
    Return()

    # Function_16_2A66 end

    def Function_17_2B5C(): pass

    label("Function_17_2B5C")

    TalkBegin(0x2C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2CA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2BC6")

    ChrTalk(    #99
        0xFE,
        (
            "The town right now reminds me of how it\x01",
            "was after the war with the Empire ended.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C9F")

    label("loc_2BC6")


    ChrTalk(    #100
        0xFE,
        (
            "Hmm. The way the town is now...\x01",
            "It reminds me of how it all was just after\x01",
            "we kicked the Erebonians out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Back then, too, the town was in such\x01",
            "a state that everyone chipped in to\x01",
            "put it all back together.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2C9F")

    Jump("loc_2DA5")

    label("loc_2CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2DA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2D0D")

    ChrTalk(    #102
        0xFE,
        "They've already started work, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Maybelle's doing a right excellent job of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA5")

    label("loc_2D0D")


    ChrTalk(    #104
        0xFE,
        (
            "Already started work, have they?\x01",
            "Maybelle must be working as hard as anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "The way she's handling all this...\x01",
            "Her father would be proud.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2DA5")

    TalkEnd(0x2C)
    Return()

    # Function_17_2B5C end

    def Function_18_2DA9(): pass

    label("Function_18_2DA9")

    TalkBegin(0x2D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2E4C")

    ChrTalk(    #106
        0xFE,
        "Mayor Maybelle came to oversee things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "She's gotta be super-busy already, but she\x01",
            "took the time to encourage each of us,\x01",
            "one by one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1B")

    label("loc_2E4C")


    ChrTalk(    #108
        0xFE,
        "Mayor Maybelle came to oversee things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "She's gotta be super-busy already, but she\x01",
            "took the time to encourage each of us,\x01",
            "one by one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Seeing her like that makes me want\x01",
            "to work even harder!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_2F1B")

    Jump("loc_314E")

    label("loc_2F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_30CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2FE4")

    ChrTalk(    #111
        0xFE,
        (
            "Fannie and I came to help with the\x01",
            "construction work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "I dunno if we'll be super-helpful or anything,\x01",
            "but I can't just sit to the side like a 'good\x01",
            "little girl' and watch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C7")

    label("loc_2FE4")


    ChrTalk(    #113
        0xFE,
        (
            "Fannie and I came to help with the\x01",
            "construction work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "I dunno if we'll be super-helpful or anything,\x01",
            "but I can't just sit to the side like a 'good\x01",
            "little girl' and watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "Anyway, we'll work as hard as we can!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_30C7")

    Jump("loc_314E")

    label("loc_30CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_314E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_30FF")

    ChrTalk(    #116
        0xFE,
        "Wh-Wh-What was that just now?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_314E")

    label("loc_30FF")


    ChrTalk(    #117
        0xFE,
        "Wh-Wh-What was that just now?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "I've never seen a monster so huge!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_314E")

    TalkEnd(0x2D)
    Return()

    # Function_18_2DA9 end

    def Function_19_3152(): pass

    label("Function_19_3152")

    TalkBegin(0x2E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_31FC")

    ChrTalk(    #119
        0xFE,
        (
            "Heehee! Mayor Maybelle said something\x01",
            "to me personally. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I'm not doing this because I want to\x01",
            "be praised or anything, but it does\x01",
            "make me happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B2")

    label("loc_31FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_327D")

    ChrTalk(    #121
        0xFE,
        "We decided to come help, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "After all, I don't have much of a part-time\x01",
            "job if the market's closed!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3351")

    label("loc_327D")


    ChrTalk(    #123
        0xFE,
        (
            "We decided to come help with the\x01",
            "construction, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "After all, I don't have much of a part-time\x01",
            "job if the market's closed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Besides, you gotta help each other\x01",
            "out when you're in trouble, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3351")

    Jump("loc_33B2")

    label("loc_3354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_33B2")

    ChrTalk(    #126
        0xFE,
        "Th-The ceiling of the market's a total wreeeck!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "How many people are inside?!\x02",
    )

    CloseMessageWindow()

    label("loc_33B2")

    TalkEnd(0x2E)
    Return()

    # Function_19_3152 end

    def Function_20_33B6(): pass

    label("Function_20_33B6")

    TalkBegin(0x2F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_344E")

    ChrTalk(    #128
        0xFE,
        (
            "Unfortunately, our capture operation fell\x01",
            "apart dramatically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I still can't believe that thing's flight\x01",
            "capacity, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3544")

    label("loc_344E")


    ChrTalk(    #130
        0xFE,
        (
            "Unfortunately, our capture operation fell\x01",
            "completely on its as--ahem! Posterior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I still can't believe how that dragon out-\x01",
            "maneuvered and outran our ships, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "That thing really does possess power\x01",
            "beyond our understanding.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3544")

    Jump("loc_369E")

    label("loc_3547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_369E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_35E7")

    ChrTalk(    #133
        0xFE,
        (
            "Until we succeed in capturing the dragon,\x01",
            "we're in charge of security in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "If you run into any problems,\x01",
            "contact us immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_369E")

    label("loc_35E7")


    ChrTalk(    #135
        0xFE,
        "We'll send some guards at once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Until we succeed in capturing the dragon,\x01",
            "we're in charge of security in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "If you run into any problems,\x01",
            "contact us immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_369E")

    TalkEnd(0x2F)
    Return()

    # Function_20_33B6 end

    def Function_21_36A2(): pass

    label("Function_21_36A2")

    TalkBegin(0x30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3748")

    ChrTalk(    #138
        0xFE,
        (
            "It seems like a lot of the average\x01",
            "citizens are chipping in to help with\x01",
            "the reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "At this rate, the market should reopen\x01",
            "very soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E0")

    label("loc_3748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_38E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_37F5")

    ChrTalk(    #140
        0xFE,
        (
            "Gotta be honest, there's NO WAY we're a\x01",
            "match for that ancient dragon in a straight\x01",
            "fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Right now we just have to pray our\x01",
            "capture plan works.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E0")

    label("loc_37F5")


    ChrTalk(    #142
        0xFE,
        "Our role's to relieve the citizens.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "We may look like we're on guard, but\x01",
            "we'd be up against an ancient dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "If it attacked again, I gotta be honest,\x01",
            "there's NO WAY we're a match for that\x01",
            "thing in a straight fight.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_38E0")

    TalkEnd(0x30)
    Return()

    # Function_21_36A2 end

    def Function_22_38E4(): pass

    label("Function_22_38E4")

    TalkBegin(0x31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3965")

    ChrTalk(    #145
        0xFE,
        "The dragon has flown towards Nebel Valley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "I wonder what General Morgan has planned\x01",
            "at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3F")

    label("loc_3965")


    ChrTalk(    #147
        0xFE,
        "The dragon has flown towards Nebel Valley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Flying in a mountainous region like that\x01",
            "is dangerous enough, but the fog there\x01",
            "never lifts, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I wonder what General Morgan has planned\x01",
            "at this point.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_3A3F")

    Jump("loc_3BD3")

    label("loc_3A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3AEC")

    ChrTalk(    #150
        0xFE,
        (
            "The orchards over in Ravennue were\x01",
            "torched as well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "Why even bother attacking the\x01",
            "orchards? What was that\x01",
            "damn lizard trying to accomplish...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD3")

    label("loc_3AEC")


    ChrTalk(    #152
        0xFE,
        (
            "The orchards over in Ravennue were\x01",
            "torched as well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "The men dispatched over there said\x01",
            "it looked pretty bad for the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Why even bother attacking the\x01",
            "orchards? What was that\x01",
            "damn lizard trying to accomplish...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_3BD3")

    TalkEnd(0x31)
    Return()

    # Function_22_38E4 end

    def Function_23_3BD7(): pass

    label("Function_23_3BD7")

    TalkBegin(0x32)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_3C86")

    ChrTalk(    #155
        0xFE,
        (
            "The Erebonians didn't really react to our\x01",
            "mobilizing the Air Force for the plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "Maybe they really ARE going to respect\x01",
            "the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E12")

    label("loc_3C86")


    ChrTalk(    #157
        0xFE,
        (
            "We were worried the Erebonians might\x01",
            "react badly to the capture attempt and\x01",
            "all those airships being mobilized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "We haven't heard a peep from\x01",
            "them, either way, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Honestly, that's making a few of us\x01",
            "even MORE worried. Bose sits right on\x01",
            "the Empire's 'southern march.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "It's not like the Blood and Iron Chancellor\x01",
            "guy to stay quiet when something this\x01",
            "big is going on...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_3E12")

    Jump("loc_4067")

    label("loc_3E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_4067")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_3F04")

    ChrTalk(    #161
        0xFE,
        (
            "Capturing the dragon is going to be a massive\x01",
            "operation involving the majority of the Air\x01",
            "Force, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "It's going to take us near the border, so\x01",
            "we'll have to be careful not to violate\x01",
            "Erebonian territory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4067")

    label("loc_3F04")


    ChrTalk(    #163
        0xFE,
        (
            "Capturing the dragon is going to be a massive\x01",
            "operation involving the majority of the Air\x01",
            "Force, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "It's going to take us near the border, so\x01",
            "we'll have to be careful not to violate\x01",
            "Erebonian territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Even with the non-aggression pact in place,\x01",
            "I can't help but think the Erebonians\x01",
            "would be furious if we crossed the border.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_4067")

    TalkEnd(0x32)
    Return()

    # Function_23_3BD7 end

    def Function_24_406B(): pass

    label("Function_24_406B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_416A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared 'Come, Ingredient Hunters' in ch. 1 of SC\x01",      # 0
            "Cleared 'Mushroom Hunting,' 'Escort Job' in FC\x01",         # 1
            "Did not clear\x01",                                          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4134"),
        (1, "loc_4146"),
        (2, "loc_4158"),
        (SWITCH_DEFAULT, "loc_416A"),
    )


    label("loc_4134")

    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_416A")

    label("loc_4146")

    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x10)
    Jump("loc_416A")

    label("loc_4158")

    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_416A")

    label("loc_416A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4187")
    Call(1, 1)
    Return()

    label("loc_4187")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4250")

    ChrTalk(    #166
        0x35,
        (
            "It seems like it will still be a little\x01",
            "while before the market reopens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x35,
        "Mmmmmmrrrr, how frustrating.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x35,
        (
            "With the flights stopped, this is my\x01",
            "chance to get my stock sold, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4492")

    label("loc_4250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_4337")

    ChrTalk(    #169
        0x35,
        (
            "So the market's closed for the\x01",
            "foreseeable future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x35,
        (
            "I WAS going to get close to the local\x01",
            "merchants, and bring a deal to the Anterose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x35,
        (
            "But now my great plans are being washed\x01",
            "away like bubbles on a river.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4492")

    label("loc_4337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_43CE")

    ChrTalk(    #172
        0x35,
        (
            "I was... I was just about to go off to\x01",
            "the market for business, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x35,
        (
            "To have it be attacked by a monster NOW,\x01",
            "of all times!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4492")

    label("loc_43CE")


    ChrTalk(    #174
        0x35,
        (
            "I was... I was just about to go off to\x01",
            "the market for business, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x35,
        (
            "To have it be attacked by a monster NOW,\x01",
            "of all times!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x35,
        (
            "Oh, Aidios, who art in heaven!\x01",
            "Why am I punished so?!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_4492")

    TalkEnd(0x35)
    Return()

    # Function_24_406B end

    def Function_25_4496(): pass

    label("Function_25_4496")

    TalkBegin(0x33)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_44BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_44B3")

    ChrTalk(    #177
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B7")

    label("loc_44B3")

    Call(0, 27)

    label("loc_44B7")

    Jump("loc_452F")

    label("loc_44BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_44E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_44DA")

    ChrTalk(    #178
        0xFE,
        "Maaaan...\x02",
    )

    CloseMessageWindow()
    Jump("loc_44DE")

    label("loc_44DA")

    Call(0, 27)

    label("loc_44DE")

    Jump("loc_452F")

    label("loc_44E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_452F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_452B")

    ChrTalk(    #179
        0xFE,
        "It's safest to evacuate, yeah, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "Darn it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_452F")

    label("loc_452B")

    Call(0, 27)

    label("loc_452F")

    TalkEnd(0x33)
    ClearChrFlags(0x34, 0x10)
    Return()

    # Function_25_4496 end

    def Function_26_4538(): pass

    label("Function_26_4538")

    TalkBegin(0x34)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_45CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_45C7")

    ChrTalk(    #181
        0xFE,
        (
            "It's a good thing to have a goal, but\x01",
            "Harry doesn't have anything specific.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "And that's just a dream, not a goal!\x02",
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_45C7")

    Call(0, 27)

    label("loc_45CB")

    Jump("loc_466D")

    label("loc_45CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_4624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_461D")

    ChrTalk(    #183
        0xFE,
        (
            "Oh, Harry, good intent doesn't always\x01",
            "mean good results.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4621")

    label("loc_461D")

    Call(0, 27)

    label("loc_4621")

    Jump("loc_466D")

    label("loc_4624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_466D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_4669")

    ChrTalk(    #184
        0xFE,
        "I mean, I, um...appreciate the thought, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_466D")

    label("loc_4669")

    Call(0, 27)

    label("loc_466D")

    TalkEnd(0x34)
    ClearChrFlags(0x34, 0x10)
    Return()

    # Function_26_4538 end

    def Function_27_4676(): pass

    label("Function_27_4676")

    OP_4A(0x33, 255)
    OP_4A(0x34, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4798")

    ChrTalk(    #185
        0x33,
        "The mayor's so amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x33,
        (
            "Not only is she awesome at guiding the\x01",
            "city, she's the best merchant in town, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x33,
        "I wish I could be that incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x34,
        "Then try working at it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x34,
        (
            "You can start by getting a full score\x01",
            "on a test at school, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x33,
        "Aww...\x02",
    )

    CloseMessageWindow()
    Jump("loc_49B8")

    label("loc_4798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_488F")
    ClearChrFlags(0x33, 0x10)
    ClearChrFlags(0x34, 0x10)

    ChrTalk(    #191
        0x33,
        "Wowzers! They're already starting work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x33,
        "Maybe I should go help, too.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x34, 0x33, 400)

    ChrTalk(    #193
        0x34,
        "Hmm... If you want to help...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x34,
        "Why not just stay here?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x33, 0x34, 400)

    ChrTalk(    #195
        0x33,
        "Huh? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x34,
        "So you don't get in their way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x33,
        "...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x33, 0x10)
    SetChrFlags(0x34, 0x10)
    Jump("loc_49B8")

    label("loc_488F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_49B8")

    ChrTalk(    #198
        0x33,
        (
            "Mina, are you okay?!\x01",
            "Are you hurt anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x34,
        "N-No, I'm fine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x33,
        (
            "W-Well, don't worry!\x01",
            "I'll protect the town!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x34,
        "Umm, that's a neat idea, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x34,
        (
            "We should worry about protecting\x01",
            "ourselves first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x34,
        (
            "Harry, please, let's just go to\x01",
            "the evacuation site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x33,
        "Well, okay...\x02",
    )

    CloseMessageWindow()

    label("loc_49B8")

    OP_4B(0x33, 255)
    OP_4B(0x34, 255)
    OP_A2(0x10)
    OP_A2(0x11)
    Return()

    # Function_27_4676 end

    def Function_28_49C7(): pass

    label("Function_28_49C7")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_4A54")

    ChrTalk(    #205
        0xFE,
        (
            "The repairs to the market are going\x01",
            "very smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "Meaning the only real problem left is that\x01",
            "damned dragon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA4")

    label("loc_4A54")


    ChrTalk(    #207
        0xFE,
        (
            "Seems like all the work is going faster\x01",
            "than planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "The only problem left is the existence\x01",
            "of that damned dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Even if we fix the market up better than\x01",
            "new, that thing can just swoop down and\x01",
            "ruin it all again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "I hope that plan the army's cooked up\x01",
            "goes as well as what we're doing here,\x01",
            "is what I'm saying.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_4BA4")

    TalkEnd(0xA)
    Return()

    # Function_28_49C7 end

    def Function_29_4BA8(): pass

    label("Function_29_4BA8")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 5)), scpexpr(EXPR_END)), "loc_4C7B")

    ChrTalk(    #211
        0x1B,
        (
            "#610FLooks like we've survived the worst of it, then.\x02\x03",

            "What needs to happen next is the restoration of\x01",
            "the market to operability and getting the\x01",
            "city back to some semblance of normalcy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5063")

    label("loc_4C7B")


    ChrTalk(    #212
        0x1B,
        "#610FHello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#1011FHi, Mayor Maybelle.\x02\x03",

            "#1001FWow. Looks like they've already\x01",
            "started work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #214
        0x1B,
        (
            "#611FYes, thanks to the aid of the citizenry,\x01",
            "we've been able to start construction a\x01",
            "lot sooner than I expected.\x02\x03",

            "I've also sent all the aid I can muster\x01",
            "to Ravennue.\x02\x03",

            "It seems we've finally gotten past the\x01",
            "worst of it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#1015FIt's good that things are settling down,\x01",
            "at least.\x02\x03",

            "#1000FSo, ummm...how's, um, Lila?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x1B,
        (
            "#618FLila's...\x01",
            "Lila hasn't changed since yesterday.\x02\x03",

            "The only thing we can do is wait for the\x01",
            "medicine to take effect and...pray, really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        "#1007FOh... Er, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x1B,
        (
            "#615FNot at all. Simply fretting by her bedside\x01",
            "won't fix anything.\x02\x03",

            "For the moment, I'm of the opinion that\x01",
            "the best thing I can do is fulfill my duty\x01",
            "as mayor.\x02\x03",

            "#610FAfter all, Lila would be quite put out with\x01",
            "me if she knew I was wasting time\x01",
            "worrying about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        (
            "#1006FYeah, she definitely would.\x02\x03",

            "We'll do what we can, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x1B,
        (
            "#611FIt's all in your hands.\x01",
            "Good luck!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A45)

    label("loc_5063")

    TalkEnd(0x1B)
    Return()

    # Function_29_4BA8 end

    def Function_30_5067(): pass

    label("Function_30_5067")

    TalkBegin(0x3B)

    ChrTalk(    #221
        0xFE,
        "Hmm, something most curious has happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "From the appearance of things, however,\x01",
            "the danger has long since passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "It would seem there is no urgent need\x01",
            "to evacuate.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x3B)
    Return()

    # Function_30_5067 end

    def Function_31_5124(): pass

    label("Function_31_5124")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_513B")
    Call(0, 63)
    Call(0, 64)

    label("loc_513B")

    Call(0, 50)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_4A(0x36, 255)
    OP_4A(0x37, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    OP_4A(0x3A, 255)
    OP_71(0x21, 0x4)
    OP_71(0x22, 0x4)
    OP_71(0x23, 0x4)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0xFA, 0x80)
    SetChrFlags(0xFB, 0x80)
    SetChrFlags(0xFC, 0x80)
    OP_6D(59000, 0, 77330, 0)
    OP_67(0, 8620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(344000, 0)
    OP_6E(262, 0)
    OP_72(0x12, 0x4)
    OP_A1(0x20, 0x12)
    SetChrPos(0x20, 48600, 7100, 60940, 45)
    SetChrPos(0x21, 0, 0, 0, 45)
    OP_CF(0x21, 0x12, "Frame127_FireEmitter")
    LoadEffect(0x1, "monster\\ms30703.eff")
    LoadEffect(0x2, "monster\\ms30704.eff")
    ClearMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x106, 0x0, 0x0, 0x25)
    Sleep(2000)

    ChrTalk(    #224
        0x101,
        "#1020F#6PWHOA!\x02",
    )

    WaitChrThread(0x106, 0x0)
    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x2E)
    Sleep(300)

    def lambda_52F2():
        OP_6C(200000, 7000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_52F2)

    def lambda_5302():
        OP_6E(490, 7000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_5302)

    def lambda_5312():
        OP_6D(45280, 500, 51530, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5312)

    def lambda_532A():
        OP_67(0, 7000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_532A)

    def lambda_5342():
        OP_6B(5150, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5342)
    Sleep(5500)
    OP_72(0x12, 0x20)
    OP_73(0x12)
    OP_6F(0x12, 55)
    OP_70(0x12, 0x78)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(41420, 3160, 60230, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(3770, 0)
    OP_6C(223000, 0)
    OP_6E(490, 0)
    Sleep(500)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x258, 0x258, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x12)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x12, 0x20)
    OP_6F(0x12, 5)
    OP_70(0x12, 0x37)

    def lambda_540D():
        OP_6D(49070, 4400, 60770, 3500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_540D)

    def lambda_5425():
        OP_67(0, 8760, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5425)

    def lambda_543D():
        OP_6B(3870, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_543D)

    def lambda_544D():
        OP_6C(210000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_544D)
    OP_72(0xA, 0x800)
    OP_72(0xB, 0x800)
    OP_72(0xC, 0x800)
    OP_72(0xD, 0x800)
    OP_72(0xA, 0x10)
    OP_72(0xB, 0x10)
    OP_72(0xC, 0x10)
    OP_72(0xD, 0x10)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3B)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x3B)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3B)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x3B)
    OP_73(0xD)
    Sleep(500)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xB, 0x1, 0x0, 0x2E)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xC, 0x1, 0x0, 0x2F)
    Sleep(50)
    OP_43(0xD, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xE, 0x1, 0x0, 0x31)
    Sleep(400)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xF, 0x1, 0x0, 0x2E)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x10, 0x1, 0x0, 0x2F)
    Sleep(50)
    OP_43(0x11, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x12, 0x1, 0x0, 0x31)
    Sleep(400)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x13, 0x1, 0x0, 0x2E)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x14, 0x1, 0x0, 0x2F)
    Sleep(50)
    OP_43(0x15, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x16, 0x1, 0x0, 0x31)
    Sleep(400)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x17, 0x1, 0x0, 0x2E)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x18, 0x1, 0x0, 0x2F)
    Sleep(50)
    OP_43(0x19, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x1A, 0x1, 0x0, 0x31)
    Sleep(3500)
    OP_63(0xB)
    OP_63(0xC)
    OP_63(0xD)
    OP_63(0xE)
    OP_63(0xF)
    OP_63(0x10)
    OP_63(0x11)
    OP_63(0x12)
    OP_63(0x13)
    OP_63(0x14)
    OP_63(0x15)
    OP_63(0x16)
    OP_63(0x17)
    OP_63(0x18)
    OP_63(0x19)
    OP_63(0x1A)
    Fade(500)
    OP_6D(58270, 0, 78850, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(344000, 0)
    OP_6E(283, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #225
        0x101,
        "#1020F#5PWhat...in the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x107,
        "#065F#6PWaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x103,
        "#023F#6PIt's gigantic!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x108,
        "#077F#4PThat's a DRAGON!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x105,
        (
            "#043F#2PThat's the ancient dragon!\x02\x03",

            "The one which legends say has\x01",
            "dwelt in Liberl since antiquity...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x104,
        "#032F#6PWell, this is quite the turn of events!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x106,
        "#057F#5PThis is the society's doing, isn't it?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 54630, 4600, 69030, 45)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #232
        0x8,
        "Man's Voice",
        "#2PNo denying it at this point.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(20)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(40)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(20)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5965():
        OP_6D(53140, 0, 73070, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5965)

    def lambda_597D():
        OP_67(0, 6620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_597D)

    def lambda_5995():
        OP_6B(2150, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5995)

    def lambda_59A5():
        OP_6C(264000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_59A5)

    def lambda_59B5():
        OP_6E(588, 4000)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_59B5)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #233
        0x101,
        "#1020F#2PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x106,
        "#052F#2PYou're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x103,
        "#024F#2PAren't you 2nd Lieutenant Lorence Belgar?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #236
        0x8,
        "Silver-Haired Youth",
        "#121FHa, 'Lorence Belgar' was simply an alias.\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS191._CH")
    OP_C6(0x0, 0x0, 125000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Silver-Haired Youth")

    AnonymousTalk(    #237
        (
            "#124FEnforcer No. II, Leonhardt the Bladelord.\x02\x03",

            "You may address me as such from now on.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    Sleep(500)
    OP_C6(0x0, 0x6, 0, 0, 0)

    ChrTalk(    #238
        0x101,
        "#1020F#2PLeonhardt the Bladelord...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x104,
        (
            "#035F#2PAhhhh, now I understand. Leonhardt\x01",
            "the 'lion-hearted,' hmm?\x02\x03",

            "#030FIs that why so many call you 'Loewe,'\x01",
            "or 'lion'?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #240
        0x101,
        "#1005F#2PSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x105,
        "#043F#2PSo you're Loewe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x8,
        (
            "#124FI never chose that name for myself,\x01",
            "but many of my comrades do call me\x01",
            "that.\x02\x03",

            "#123FCall me whatever you like. It doesn't\x01",
            "matter in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x106,
        "#057F#2PThink you're so much better...\x02",
    )

    CloseMessageWindow()
    OP_22(0x11F, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5D4C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D4C)

    def lambda_5D5A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_5D5A)

    def lambda_5D68():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_5D68)
    Sleep(100)

    def lambda_5D7B():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5D7B)

    def lambda_5D89():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D89)
    Sleep(100)

    def lambda_5D9C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5D9C)

    def lambda_5DAA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5DAA)
    Sleep(100)

    def lambda_5DBD():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_5DBD)

    def lambda_5DCB():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DCB)
    Sleep(100)
    Fade(500)
    SetChrPos(0x20, 48600, 7100, 60940, 0)
    OP_6D(31950, 0, 69570, 0)
    OP_67(0, 6310, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(251000, 0)
    OP_6E(490, 0)
    OP_72(0x12, 0x20)
    OP_6F(0x12, 55)
    OP_70(0x12, 0x73)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    PlayEffect(0x1, 0x0, 0x21, 0, 0, 0, 0, -45, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)
    OP_73(0x12)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x12, 0x20)
    OP_6F(0x12, 5)
    OP_70(0x12, 0x37)
    Sleep(1500)
    Fade(500)
    OP_71(0x12, 0x4)
    SetChrPos(0x20, 48600, 7100, 60940, 45)
    OP_6D(57430, 0, 76950, 0)
    OP_67(0, 8390, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(11000, 0)
    OP_6E(291, 0)
    OP_8C(0x8, 225, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #244
        0x101,
        "#1020F#4PAAAAH!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x103,
        "#523F#6PDo you intend to burn the whole city?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x8,
        "#124F#5PWhat a headache.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x8, 33)
    SetChrSubChip(0x8, 1)
    OP_0D()
    Sleep(200)
    ClearChrFlags(0x8, 0x1)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrSubChip(0x8, 2)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0x8, 270, 0)

    def lambda_5FB9():
        OP_96(0xFE, 0xBD2E, 0x3AFC, 0x10054, 0x2AF8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5FB9)
    Sleep(200)
    Fade(100)
    OP_72(0x12, 0x4)
    OP_6D(56240, 18870, 65550, 0)
    OP_67(0, 8780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(312, 0)
    WaitChrThread(0x8, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x8, 1)
    ClearChrFlags(0x8, 0x4)
    OP_CF(0x8, 0x12, "Frame141_back_Null1")
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_8C(0x8, 90, 0)
    Sleep(500)
    SetChrChipByIndex(0x8, 34)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 180, 400)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6082():
        OP_67(0, 8740, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_6082)

    def lambda_609A():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_609A)

    def lambda_60AA():
        OP_6E(442, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_60AA)

    def lambda_60BA():
        OP_6D(52240, 18870, 65550, 2000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_60BA)

    def lambda_60D2():
        OP_8C(0xFE, 315, 80)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_60D2)
    OP_72(0x12, 0x20)
    OP_6F(0x12, 116)
    OP_70(0x12, 0x91)
    OP_73(0x12)
    OP_B0(0x12, 0x5)
    OP_71(0x12, 0x20)
    OP_6F(0x12, 145)
    OP_70(0x12, 0x9E)
    Sleep(200)
    OP_43(0x20, 0x3, 0x0, 0x20)
    Sleep(500)
    OP_43(0x20, 0x1, 0x0, 0x21)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #247
        0x106,
        "#055F#5PWait a minute, you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x8,
        (
            "#122F#6POur experiment this time is somewhat\x01",
            "irregular.\x02\x03",

            "I'll be frank: You could never hope to\x01",
            "handle this.\x02\x03",

            "#125FLeave it to the Royal Army. Back down\x01",
            "for your own sakes.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_620B():
        OP_6D(48240, 18870, 69550, 4000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_620B)

    def lambda_6223():
        OP_67(0, 10000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6223)

    def lambda_623B():
        OP_6B(4010, 4000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_623B)

    def lambda_624B():
        OP_6C(270000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_624B)

    def lambda_625B():
        OP_6E(395, 4000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_625B)

    def lambda_626B():

        label("loc_626B")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_626B")

    QueueWorkItem2(0x101, 1, lambda_626B)

    def lambda_627C():

        label("loc_627C")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_627C")

    QueueWorkItem2(0x106, 1, lambda_627C)

    def lambda_628D():

        label("loc_628D")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_628D")

    QueueWorkItem2(0xF8, 1, lambda_628D)

    def lambda_629E():

        label("loc_629E")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_629E")

    QueueWorkItem2(0xF9, 1, lambda_629E)

    def lambda_62AF():

        label("loc_62AF")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_62AF")

    QueueWorkItem2(0xFA, 1, lambda_62AF)

    def lambda_62C0():

        label("loc_62C0")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_62C0")

    QueueWorkItem2(0xFB, 1, lambda_62C0)

    def lambda_62D1():

        label("loc_62D1")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_62D1")

    QueueWorkItem2(0xFC, 1, lambda_62D1)

    def lambda_62E2():

        label("loc_62E2")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_62E2")

    QueueWorkItem2(0x9, 1, lambda_62E2)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    OP_72(0x12, 0x20)
    OP_73(0x12)
    OP_B0(0x12, 0x14)
    OP_6F(0x12, 145)
    OP_70(0x12, 0xAA)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    PlayEffect(0x2, 0x0, 0x20, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x1, 0x20, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x12, 0x20)
    OP_B0(0x12, 0x19)
    OP_6F(0x12, 170)
    OP_70(0x12, 0xBE)
    PlayEffect(0x2, 0x2, 0x20, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x20, 0x1)
    OP_43(0x20, 0x0, 0x0, 0x22)
    WaitChrThread(0x101, 0x0)
    Sleep(2500)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    OP_A2(0x10FE)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5124 end

    def Function_32_6428(): pass

    label("Function_32_6428")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_643E")
    OP_22(0x120, 0x0, 0x64)
    Sleep(2700)
    Jump("Function_32_6428")

    label("loc_643E")

    Return()

    # Function_32_6428 end

    def Function_33_643F(): pass

    label("Function_33_643F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6485")
    PlayEffect(0x2, 0xFF, 0x20, 0, -6000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(2700)
    Jump("Function_33_643F")

    label("loc_6485")

    Return()

    # Function_33_643F end

    def Function_34_6486(): pass

    label("Function_34_6486")

    OP_22(0x120, 0x0, 0x64)

    def lambda_6491():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6491)
    Sleep(200)
    PlayEffect(0x2, 0x0, 0x20, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_64E6():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_64E6)
    Sleep(200)
    PlayEffect(0x2, 0x1, 0x20, 0, -2000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x120, 0x0, 0x64)

    def lambda_6540():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6540)
    Sleep(200)
    PlayEffect(0x2, 0x1, 0x20, 0, -4000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_6595():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6595)
    Sleep(200)

    def lambda_65B5():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_65B5)
    Sleep(200)
    OP_22(0x120, 0x0, 0x64)

    def lambda_65DA():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_65DA)
    Sleep(300)

    def lambda_65FA():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0xFA00, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_65FA)
    Return()

    # Function_34_6486 end

    def Function_35_6610(): pass

    label("Function_35_6610")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(58650, 0, 78150, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(344000, 0)
    OP_6E(283, 0)
    OP_71(0x21, 0x4)
    OP_71(0x22, 0x4)
    OP_71(0x23, 0x4)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0xFA, 0x1)
    OP_44(0xFB, 0x1)
    OP_44(0xFC, 0x1)
    OP_44(0x9, 0x1)
    SetChrPos(0x101, 59570, 0, 76570, 315)
    SetChrPos(0x106, 58320, 0, 76730, 315)
    SetChrPos(0x107, 57360, 0, 77470, 315)
    SetChrPos(0x103, 58660, 0, 77700, 315)
    SetChrPos(0x104, 58080, 0, 78840, 315)
    SetChrPos(0x105, 60210, 0, 77350, 315)
    SetChrPos(0x108, 59500, 0, 78870, 315)
    SetChrPos(0x9, 59050, 500, 79890, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_4A(0x36, 255)
    OP_4A(0x37, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    OP_4A(0x3A, 255)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 59)
    OP_72(0xC, 0x10)
    OP_6F(0xC, 59)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #249
        0x101,
        (
            "#1005F#2PWhat should we do?! He'll get away\x01",
            "at this rate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x106,
        (
            "#053F#6PI'm going after the lizard.\x02\x03",

            "#057FYou guys check on the damage while\x01",
            "you wait for the army to get here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_686E():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_686E)
    Sleep(10)

    def lambda_6881():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_6881)
    Sleep(20)

    def lambda_6894():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6894)
    Sleep(10)

    def lambda_68A7():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_68A7)
    Sleep(30)

    def lambda_68BA():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_68BA)
    Sleep(10)

    def lambda_68CD():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_68CD)
    Sleep(20)

    def lambda_68E0():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_68E0)
    Sleep(400)

    def lambda_68F3():

        label("loc_68F3")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_68F3")

    QueueWorkItem2(0x101, 1, lambda_68F3)

    def lambda_6904():

        label("loc_6904")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_6904")

    QueueWorkItem2(0xF8, 1, lambda_6904)

    def lambda_6915():

        label("loc_6915")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_6915")

    QueueWorkItem2(0xF9, 1, lambda_6915)

    def lambda_6926():

        label("loc_6926")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_6926")

    QueueWorkItem2(0xFA, 1, lambda_6926)

    def lambda_6937():

        label("loc_6937")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_6937")

    QueueWorkItem2(0xFB, 1, lambda_6937)

    def lambda_6948():

        label("loc_6948")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_6948")

    QueueWorkItem2(0xFC, 1, lambda_6948)

    def lambda_6959():

        label("loc_6959")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_6959")

    QueueWorkItem2(0x9, 1, lambda_6959)

    ChrTalk(    #251
        0x101,
        "#1020F#2PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x103,
        "#023F#4PAgate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x106,
        "#054F#6PI'll be in touch!\x02",
    )

    CloseMessageWindow()

    def lambda_69B1():
        OP_6C(302000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_69B1)

    def lambda_69C1():
        OP_6D(55320, 0, 76560, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_69C1)

    def lambda_69D9():
        OP_8E(0xFE, 0x94E8, 0x0, 0x12066, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_69D9)
    Sleep(2000)
    OP_44(0x101, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0xFA, 0x1)
    OP_44(0xFB, 0x1)
    OP_44(0xFC, 0x1)
    OP_44(0x9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #254
        0x107,
        "#065F#5PAgate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        "#1020F#5PW-Wait!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 49540, 0, 70870, 0)
    ClearChrFlags(0xA, 0x80)

    ChrTalk(    #256
        0xA,
        "#4PThank Aidios, you're here!\x02",
    )

    CloseMessageWindow()

    def lambda_6A82():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A82)

    def lambda_6A90():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_6A90)

    def lambda_6A9E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6A9E)

    def lambda_6AAC():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_6AAC)

    def lambda_6ABA():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_6ABA)

    def lambda_6AC8():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_6AC8)

    def lambda_6AD6():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6AD6)

    def lambda_6AE4():
        OP_6C(270000, 1800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AE4)

    def lambda_6AF4():
        OP_6D(54350, 0, 74950, 1800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6AF4)

    def lambda_6B0C():
        OP_8E(0xFE, 0xD232, 0x0, 0x121E2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6B0C)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0xA, 0x1)
    OP_4A(0xA, 255)

    def lambda_6B42():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6B42)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #257
        0xA,
        "#6PPlease, help us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xA,
        (
            "#6PThere are people who couldn't get out\x01",
            "in time! They're trapped under the rubble!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #259
        0x108,
        "#072F#2PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        "#1005F#2PLet's go help!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1123   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_35_6610 end

    def Function_36_6C21(): pass

    label("Function_36_6C21")


    def lambda_6C27():
        OP_8F(0xFE, 0xC666, 0x0, 0x1249E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C27)
    Sleep(300)

    def lambda_6C47():
        OP_8F(0xFE, 0xC6CA, 0x0, 0x12886, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6C47)
    Sleep(100)

    def lambda_6C67():
        OP_8F(0xFE, 0xCB84, 0x0, 0x1255C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C67)
    Sleep(100)

    def lambda_6C87():
        OP_8F(0xFE, 0xCA08, 0x0, 0x1200C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C87)
    Sleep(100)

    def lambda_6CA7():
        OP_8F(0xFE, 0xCF26, 0x0, 0x11DB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6CA7)
    Sleep(100)

    def lambda_6CC7():
        OP_8F(0xFE, 0xE8F8, 0x0, 0x13182, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_6CC7)
    Return()

    # Function_36_6C21 end

    def Function_37_6CDD(): pass

    label("Function_37_6CDD")

    OP_43(0x106, 0x1, 0x0, 0x27)
    Sleep(400)
    OP_43(0x101, 0x1, 0x0, 0x26)
    Sleep(400)
    OP_43(0x107, 0x1, 0x0, 0x28)
    Sleep(400)
    OP_43(0x103, 0x1, 0x0, 0x29)
    Sleep(400)
    OP_43(0x105, 0x1, 0x0, 0x2B)
    Sleep(400)
    OP_43(0x104, 0x1, 0x0, 0x2A)
    Sleep(400)
    OP_43(0x108, 0x1, 0x0, 0x2C)
    Sleep(400)
    OP_43(0x9, 0x1, 0x0, 0x2D)
    Return()

    # Function_37_6CDD end

    def Function_38_6D39(): pass

    label("Function_38_6D39")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE8B2, 0x0, 0x12B1A, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_38_6D39 end

    def Function_39_6D7F(): pass

    label("Function_39_6D7F")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE3D0, 0x0, 0x12BBA, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_39_6D7F end

    def Function_40_6DC5(): pass

    label("Function_40_6DC5")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE010, 0x0, 0x12E9E, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_40_6DC5 end

    def Function_41_6E0B(): pass

    label("Function_41_6E0B")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE524, 0x0, 0x12F84, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_41_6E0B end

    def Function_42_6E51(): pass

    label("Function_42_6E51")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE2E0, 0x0, 0x133F8, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_42_6E51 end

    def Function_43_6E97(): pass

    label("Function_43_6E97")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xEB32, 0x0, 0x12E26, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_43_6E97 end

    def Function_44_6EDD(): pass

    label("Function_44_6EDD")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE86C, 0x0, 0x13416, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_44_6EDD end

    def Function_45_6F23(): pass

    label("Function_45_6F23")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6AA, 0x1F4, 0x13812, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_45_6F23 end

    def Function_46_6F55(): pass

    label("Function_46_6F55")

    SetChrPos(0xFE, 54510, 0, 60010, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11B8E, 0x0, 0xEA6A, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_46_6F55 end

    def Function_47_6F85(): pass

    label("Function_47_6F85")

    SetChrPos(0xFE, 41460, 0, 59990, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x7F44, 0x0, 0xEA56, 0x1388, 0x0)
    OP_8E(0xFE, 0x7FC6, 0x0, 0xAAF0, 0x1388, 0x0)
    OP_8E(0xFE, 0x42F4, 0x0, 0xA776, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_47_6F85 end

    def Function_48_6FDD(): pass

    label("Function_48_6FDD")

    SetChrPos(0xFE, 48010, 0, 53480, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xBDBA, 0xFFFFF448, 0x4402, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_48_6FDD end

    def Function_49_700D(): pass

    label("Function_49_700D")

    SetChrPos(0xFE, 48040, 0, 66510, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xBB76, 0xBB8, 0x163C8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_49_700D end

    def Function_50_703D(): pass

    label("Function_50_703D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7076")
    AddParty(0x2, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_7076")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70C3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70AB")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_70C3")

    label("loc_70AB")

    AddParty(0x6, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_70C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7138")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70F8")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7138")

    label("loc_70F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7120")
    AddParty(0x3, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7138")

    label("loc_7120")

    AddParty(0x3, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_7138")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7185")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716D")
    AddParty(0x4, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7185")

    label("loc_716D")

    AddParty(0x4, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_7185")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71AA")
    AddParty(0x7, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_71AA")

    Return()

    # Function_50_703D end

    def Function_51_71AB(): pass

    label("Function_51_71AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_730C")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7246")

    ChrTalk(    #261
        0x108,
        (
            "#074FI'm not sure we have a lot of time to\x01",
            "wander about.\x02\x03",

            "#070FWe should get what we need and head\x01",
            "for the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72EE")

    label("loc_7246")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_725C")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_7263")

    label("loc_725C")

    TurnDirection(0x103, 0x0, 400)

    label("loc_7263")


    ChrTalk(    #262
        0x103,
        (
            "#020FWe are rather on the clock this time,\x01",
            "Estelle.\x02\x03",

            "Once we've picked up anything we need,\x01",
            "we really should get to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72EE")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_784F")

    label("loc_730C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75AC")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_733A"),
        (2, "loc_7393"),
        (4, "loc_7405"),
        (3, "loc_7463"),
        (6, "loc_74E9"),
        (7, "loc_7544"),
        (SWITCH_DEFAULT, "loc_758E"),
    )


    label("loc_733A")


    ChrTalk(    #263
        0x101,
        (
            "#1002FOh, man, we don't have time to waste!\x02\x03",

            "We need to get to Ravennue, pronto!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_758E")

    label("loc_7393")


    ChrTalk(    #264
        0x103,
        (
            "#022FThis is not the time to be wandering around.\x02\x03",

            "We need to get to Ravennue as\x01",
            "soon as we possibly can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_758E")

    label("loc_7405")


    ChrTalk(    #265
        0x105,
        (
            "#042FThis is no time for detours.\x02\x03",

            "We must go to Ravennue as soon\x01",
            "as we are prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_758E")

    label("loc_7463")


    ChrTalk(    #266
        0x104,
        (
            "#032FThe stage is aflame, and we must not dally.\x02\x03",

            "We must proceed with haste to Ravennue,\x01",
            "for the next scene awaits us there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_758E")

    label("loc_74E9")


    ChrTalk(    #267
        0x107,
        (
            "#062FWe can't waste time here!\x01",
            "At all!\x02\x03",

            "We need to follow Agate as soon as we can!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_758E")

    label("loc_7544")


    ChrTalk(    #268
        0x108,
        (
            "#072FThis is no time to wander.\x02\x03",

            "We must get to Ravennue quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_758E")

    label("loc_758E")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_784F")

    label("loc_75AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_784F")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_75DA"),
        (2, "loc_762F"),
        (4, "loc_7687"),
        (3, "loc_76D5"),
        (6, "loc_7749"),
        (7, "loc_77D7"),
        (SWITCH_DEFAULT, "loc_7834"),
    )


    label("loc_75DA")


    ChrTalk(    #269
        0x101,
        (
            "#1002FWe need to get to Ravennue, pronto...\x02\x03",

            "Let's go through the west gate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7834")

    label("loc_762F")


    ChrTalk(    #270
        0x103,
        (
            "#022FThe fastest way to Ravennue will be\x01",
            "through the west gate.\x02\x03",

            "We must hurry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7834")

    label("loc_7687")


    ChrTalk(    #271
        0x105,
        (
            "#042FRavennue is to the west of Bose.\x02\x03",

            "Let us leave by the west gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7834")

    label("loc_76D5")


    ChrTalk(    #272
        0x104,
        (
            "#032FRavennue lies to the west of this fair city.\x02\x03",

            "The fastest way there would be through\x01",
            "the western gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7834")

    label("loc_7749")


    ChrTalk(    #273
        0x107,
        (
            "#065FUm, um, um, if we're going to Ravennue\x01",
            "the west gate would be fastest!\x02\x03",

            "#062FCome on, let's go! We need to catch\x01",
            "up to Agate...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7834")

    label("loc_77D7")


    ChrTalk(    #274
        0x108,
        (
            "#072FThe shortest path to Ravennue lies out\x01",
            "of the western gate.\x02\x03",

            "Let us make haste!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7834")

    label("loc_7834")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_784F")

    Return()

    # Function_51_71AB end

    def Function_52_7850(): pass

    label("Function_52_7850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79A9")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78E6")

    ChrTalk(    #275
        0x108,
        (
            "#074FI'm not sure we have a lot of time to\x01",
            "wander about.\x02\x03",

            "#070FWe should get what we need and head\x01",
            "for the landing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_798E")

    label("loc_78E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78FC")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_7903")

    label("loc_78FC")

    TurnDirection(0x103, 0x0, 400)

    label("loc_7903")


    ChrTalk(    #276
        0x103,
        (
            "#020FWe are rather on the clock this time,\x01",
            "Estelle.\x02\x03",

            "Once we've picked up anything we need,\x01",
            "we really should get to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_798E")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_79A9")

    Return()

    # Function_52_7850 end

    def Function_53_79AA(): pass

    label("Function_53_79AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_79B2")
    Return()

    label("loc_79B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_7A02")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #277
        "\x07\x05◆立入禁止用の障壁の代用\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_7A02")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_53_79AA end

    def Function_54_7A1E(): pass

    label("Function_54_7A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_7A26")
    Return()

    label("loc_7A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_7A76")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #278
        "\x07\x05◆立入禁止用の障壁の代用\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_7A76")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_54_7A1E end

    def Function_55_7A92(): pass

    label("Function_55_7A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_7A9A")
    Return()

    label("loc_7A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_7AEA")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #279
        "\x07\x05◆立入禁止用の障壁の代用\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_7AEA")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_55_7A92 end

    def Function_56_7B06(): pass

    label("Function_56_7B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_7B0E")
    Return()

    label("loc_7B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_7B5E")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #280
        "\x07\x05◆立入禁止用の障壁の代用\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_7B5E")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_7B06 end

    def Function_57_7B7A(): pass

    label("Function_57_7B7A")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_E5(0x2A, 0x0, 0x0)
    OP_6D(47330, 400, 59690, 0)
    OP_67(0, 14540, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(314000, 0)
    OP_6E(556, 0)
    OP_71(0xC, 0x4)
    OP_71(0x23, 0x4)
    SetChrPos(0x1B, 45230, 0, 74390, 90)
    SetChrPos(0xB, 47000, 0, 73840, 270)
    SetChrPos(0xC, 46950, 0, 74750, 270)
    SetChrPos(0xD, 46540, 0, 72950, 315)
    SetChrPos(0x1D, 46630, 0, 75700, 225)
    SetChrPos(0x1C, 48040, 0, 71510, 90)
    SetChrPos(0xF, 49220, 0, 71700, 90)
    SetChrPos(0x11, 49940, 0, 72980, 135)
    SetChrPos(0x1E, 51670, 0, 72890, 90)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    OP_E5(0x1B, 0x0, 0x0)
    OP_E5(0xB, 0x0, 0x0)
    OP_E5(0xC, 0x0, 0x0)
    OP_E5(0xD, 0x0, 0x0)
    OP_E5(0xF, 0x0, 0x0)
    OP_E5(0x11, 0x0, 0x0)
    OP_E5(0x1C, 0x0, 0x0)
    OP_E5(0x1D, 0x0, 0x0)
    OP_E5(0x1E, 0x0, 0x0)
    OP_22(0x1C2, 0x0, 0x64)
    OP_43(0x1B, 0x1, 0x0, 0x3A)
    OP_43(0x1E, 0x1, 0x0, 0x3B)

    def lambda_7CDA():
        OP_6C(213000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7CDA)
    FadeToBright(2000, 0)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)

    def lambda_7D02():
        OP_6D(46830, 400, 72760, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7D02)

    def lambda_7D1A():
        OP_67(0, 9760, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D1A)

    def lambda_7D32():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D32)

    def lambda_7D42():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7D42)
    OP_8E(0x1C, 0xBBA8, 0x12C, 0x10F7C, 0x7D0, 0x0)
    OP_72(0xC, 0x10)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3B)
    OP_73(0xC)
    TurnDirection(0x1C, 0xF, 400)
    Sleep(1000)
    OP_43(0xF, 0x1, 0x0, 0x3C)
    Sleep(800)
    OP_43(0x11, 0x1, 0x0, 0x3D)
    Sleep(2000)
    OP_8C(0x1C, 180, 400)

    def lambda_7DA7():
        OP_8E(0xFE, 0xBBA8, 0x1F4, 0x103CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7DA7)
    WaitChrThread(0x1C, 0x1)
    SetChrFlags(0x1C, 0x80)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_E5(0x2A, 0x0, 0x1)
    OP_DC()
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_57_7B7A end

    def Function_58_7DED(): pass

    label("Function_58_7DED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E6C")
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    Jump("Function_58_7DED")

    label("loc_7E6C")

    Return()

    # Function_58_7DED end

    def Function_59_7E6D(): pass

    label("Function_59_7E6D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EA9")
    OP_8C(0xFE, 0, 300)
    Sleep(1000)
    OP_8C(0xFE, 270, 300)
    Sleep(1000)
    OP_8C(0xFE, 0, 300)
    Sleep(1000)
    OP_8C(0xFE, 90, 300)
    Sleep(1000)
    Jump("Function_59_7E6D")

    label("loc_7EA9")

    Return()

    # Function_59_7E6D end

    def Function_60_7EAA(): pass

    label("Function_60_7EAA")

    Sleep(500)
    TurnDirection(0xFE, 0x1C, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xBBA8, 0x12C, 0x10F7C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBBA8, 0x1F4, 0x103CE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_60_7EAA end

    def Function_61_7EE9(): pass

    label("Function_61_7EE9")

    Sleep(500)
    TurnDirection(0xFE, 0x1C, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xBE00, 0x0, 0x11A44, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBBA8, 0x1F4, 0x103CE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_61_7EE9 end

    def Function_62_7F28(): pass

    label("Function_62_7F28")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F3F")
    Call(0, 63)
    Call(0, 66)

    label("loc_7F3F")

    OP_31(0xFF, 0xFE, 0x0)
    OP_6D(48700, 0, 83750, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(30000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 47650, 1500, 87720, 180)
    SetChrPos(0x106, 49120, 1500, 87720, 180)
    SetChrPos(0x107, 49200, 2500, 89250, 180)
    SetChrPos(0xF9, 47650, 2500, 89250, 180)
    FadeToBright(1000, 0)

    def lambda_7FD4():
        OP_8E(0xFE, 0xBA22, 0x0, 0x14320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7FD4)
    Sleep(70)

    def lambda_7FF4():
        OP_8E(0xFE, 0xBFE0, 0x0, 0x14320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7FF4)
    Sleep(80)

    def lambda_8014():
        OP_8E(0xFE, 0xBA22, 0x0, 0x1491A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8014)
    Sleep(70)

    def lambda_8034():
        OP_8E(0xFE, 0xC030, 0x0, 0x1491A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8034)
    WaitChrThread(0x101, 0x1)

    def lambda_8054():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8054)
    WaitChrThread(0x106, 0x1)

    def lambda_8067():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_8067)
    WaitChrThread(0xF9, 0x1)

    def lambda_807A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_807A)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 225, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8149")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Whemler in previous game\x01",               # 0
            "Set as did not meet Whemler in previous game\x01",      # 1
            "No change\x01",                                         # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_813D"),
        (1, "loc_8143"),
        (SWITCH_DEFAULT, "loc_8149"),
    )


    label("loc_813D")

    OP_A2(0x1A80)
    Jump("loc_8149")

    label("loc_8143")

    OP_A3(0x1A80)
    Jump("loc_8149")

    label("loc_8149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 0)), scpexpr(EXPR_END)), "loc_81E1")

    ChrTalk(    #281
        0x101,
        (
            "#1006F#5POkay, so we're going to go see Whemler\x01",
            "in Nebel Valley, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x106,
        (
            "#053F#4PYeah.\x02\x03",

            "#552FMore importantly, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x96, 0x1, 0x4)
    OP_28(0x96, 0x1, 0x8)
    Jump("loc_82BB")

    label("loc_81E1")


    ChrTalk(    #283
        0x101,
        (
            "#1006F#5POkay, so we're going to go see Whemler\x01",
            "in Nebel Valley, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x106,
        (
            "#053F#4PYeah. He should be in this little mountain\x01",
            "hut on the eastern side of the valley.\x02\x03",

            "#552FMore importantly, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x96, 0x1, 0x10)
    OP_28(0x96, 0x1, 0x20)

    label("loc_82BB")

    TurnDirection(0x106, 0x107, 400)
    Sleep(500)

    ChrTalk(    #285
        0x106,
        "#555FAre you really tagging along, Tita?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)
    Sleep(500)

    ChrTalk(    #286
        0x107,
        (
            "#061FHeehee, of course!\x02\x03",

            "#560FIf the vibration unit breaks, I can fix\x01",
            "it right then and there!\x02\x03",

            "I think my cannon can lend a hand\x01",
            "against any flying monsters, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x106,
        (
            "#053FTch... Fine, whatever.\x02\x03",

            "#051FJust don't slow us down, shortstuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x107,
        "#067FNo problem!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8445")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_8479")

    label("loc_8445")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8467")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_8479")

    label("loc_8467")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_8479")

    Sleep(1500)
    OP_8C(0x106, 270, 400)
    Sleep(100)
    TurnDirection(0x107, 0x101, 400)
    Sleep(300)
    OP_62(0x106, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #289
        0x107,
        "#560F#6PEstelle? What is it?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_63(0xF9)

    ChrTalk(    #290
        0x106,
        "#555F#4PWhat's with the look?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1028F#5POh, nothiiiing. Much. How do I put it...?\x02\x03",

            "I was just thinking that you two seem\x01",
            "a lot closer now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85E9")

    ChrTalk(    #292
        0x103,
        (
            "#027F#3PI think someone finally burrowed all the\x01",
            "way into Agate's heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86EE")

    label("loc_85E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_862F")

    ChrTalk(    #293
        0x105,
        "#048F#3PHe's been so sweet to you lately, Tita.\x02",
    )

    CloseMessageWindow()
    Jump("loc_86EE")

    label("loc_862F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86A3")

    ChrTalk(    #294
        0x104,
        (
            "#037F#3PAh, the proud Raven wears his white\x01",
            "armor openly at last! It moves a man to\x01",
            "tears! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86EE")

    label("loc_86A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86EE")

    ChrTalk(    #295
        0x108,
        (
            "#071F#3PHaha, I'm guessing Tita finally won\x01",
            "Agate over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86EE")


    ChrTalk(    #296
        0x107,
        "#065F#6PWha...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #297
        0x106,
        "#055F#4PThe hell are you going on about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x101,
        (
            "#1001F#5PAhaha! Look at that blush!\x02\x03",

            "#1006FBut seriously, it looks like you've\x01",
            "got your feelings all sorted out, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x106,
        (
            "#051F#4PYeah... Yeah, I do.\x02\x03",

            "I ain't gonna run off alone and get\x01",
            "wrecked like a chump anymore.\x02\x03",

            "If I do, I'm gonna have a certain little\x01",
            "someone guilt-tripping me with her\x01",
            "pouty face again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x107,
        "#562FAwww, Agate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1012F#5PAhaha, I see, I see.\x02\x03",

            "#1018FOkay, then! Let's hurry to Nebel Valley!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x107,
        "#061FYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x106,
        "#051F#4PLet's move out!\x02",
    )

    CloseMessageWindow()
    OP_28(0x95, 0x1, 0x40)
    OP_28(0x95, 0x1, 0x80)
    OP_28(0x95, 0x1, 0x100)
    OP_28(0x96, 0x4, 0x2)
    OP_28(0x96, 0x4, 0x8)
    OP_28(0x96, 0x1, 0x1)
    OP_28(0x96, 0x1, 0x2)
    OP_20(0x3E8)
    OP_21()
    EventEnd(0x0)
    OP_1D(0xB)
    Return()

    # Function_62_7F28 end

    def Function_63_8952(): pass

    label("Function_63_8952")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_89CE"),
        (1, "loc_89D4"),
        (SWITCH_DEFAULT, "loc_89DA"),
    )


    label("loc_89CE")

    OP_A2(0x1200)
    Jump("loc_89DA")

    label("loc_89D4")

    OP_A2(0x1201)
    Jump("loc_89DA")

    label("loc_89DA")

    Return()

    # Function_63_8952 end

    def Function_64_89DB(): pass

    label("Function_64_89DB")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_64_89DB end

    def Function_65_8A36(): pass

    label("Function_65_8A36")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_65_8A36 end

    def Function_66_8A93(): pass

    label("Function_66_8A93")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_66_8A93 end

    def Function_67_8AEC(): pass

    label("Function_67_8AEC")

    SetPlaceName(0x2A)
    Return()

    # Function_67_8AEC end

    def Function_68_8AF0(): pass

    label("Function_68_8AF0")

    SetPlaceName(0x26)
    Return()

    # Function_68_8AF0 end

    def Function_69_8AF4(): pass

    label("Function_69_8AF4")

    SetPlaceName(0x25)
    Return()

    # Function_69_8AF4 end

    def Function_70_8AF8(): pass

    label("Function_70_8AF8")

    SetPlaceName(0x20)
    Return()

    # Function_70_8AF8 end

    def Function_71_8AFC(): pass

    label("Function_71_8AFC")

    SetPlaceName(0x28)
    Return()

    # Function_71_8AFC end

    def Function_72_8B00(): pass

    label("Function_72_8B00")

    SetPlaceName(0x2B)
    Return()

    # Function_72_8B00 end

    def Function_73_8B04(): pass

    label("Function_73_8B04")

    SetPlaceName(0x21)
    Return()

    # Function_73_8B04 end

    def Function_74_8B08(): pass

    label("Function_74_8B08")

    SetPlaceName(0x27)
    Return()

    # Function_74_8B08 end

    SaveToFile()

Try(main)
