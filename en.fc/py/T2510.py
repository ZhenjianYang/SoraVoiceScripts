from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2510   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2510.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Dean Collins',                         # 9
        'Jill',                                 # 10
        'Hans',                                 # 11
        'Male Student',                         # 12
        'Male Student',                         # 13
        'Male Student',                         # 14
        'Female Student',                       # 15
        'Female Teacher',                       # 16
        'Fauna',                                # 17
        'Mr. Ratio',                            # 18
        'Ms. Wiola',                            # 19
        'Ms. Millia',                           # 20
        'Mr. Effort',                           # 21
        'Rhody',                                # 22
        'Kaden',                                # 23
        'Alice',                                # 24
        'Taylor',                               # 25
        'Purity',                               # 26
        'Logic',                                # 27
        'Roy',                                  # 28
        'Monika',                               # 29
        'Thelma',                               # 30
        'Gerome',                               # 31
        'Nikita',                               # 32
        'Mayor Maybelle',                       # 33
        'Mayor Dalmore',                        # 34
        'CH22000',                              # 35
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
        'ED6_DT07/CH02600 ._CH',             # 00
        'ED6_DT07/CH02393 ._CH',             # 01
        'ED6_DT07/CH02553 ._CH',             # 02
        'ED6_DT07/CH01360 ._CH',             # 03
        'ED6_DT07/CH01370 ._CH',             # 04
        'ED6_DT07/CH01430 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01660 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
        'ED6_DT07/CH01430 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH01360 ._CH',             # 0B
        'ED6_DT07/CH01580 ._CH',             # 0C
        'ED6_DT07/CH01590 ._CH',             # 0D
        'ED6_DT07/CH01370 ._CH',             # 0E
        'ED6_DT07/CH01090 ._CH',             # 0F
        'ED6_DT07/CH01080 ._CH',             # 10
        'ED6_DT07/CH01580 ._CH',             # 11
        'ED6_DT07/CH02360 ._CH',             # 12
        'ED6_DT07/CH00003 ._CH',             # 13
        'ED6_DT07/CH00013 ._CH',             # 14
        'ED6_DT07/CH00043 ._CH',             # 15
        'ED6_DT07/CH01363 ._CH',             # 16
        'ED6_DT07/CH01083 ._CH',             # 17
        'ED6_DT07/CH01583 ._CH',             # 18
        'ED6_DT07/CH01373 ._CH',             # 19
        'ED6_DT07/CH01663 ._CH',             # 1A
        'ED6_DT07/CH01213 ._CH',             # 1B
        'ED6_DT07/CH01433 ._CH',             # 1C
        'ED6_DT07/CH01463 ._CH',             # 1D
        'ED6_DT07/CH01593 ._CH',             # 1E
        'ED6_DT07/CH01093 ._CH',             # 1F
        'ED6_DT07/CH02603 ._CH',             # 20
        'ED6_DT06/CH20021 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH02600P._CP',             # 00
        'ED6_DT07/CH02393P._CP',             # 01
        'ED6_DT07/CH02553P._CP',             # 02
        'ED6_DT07/CH01360P._CP',             # 03
        'ED6_DT07/CH01370P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01660P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
        'ED6_DT07/CH01430P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH01360P._CP',             # 0B
        'ED6_DT07/CH01580P._CP',             # 0C
        'ED6_DT07/CH01590P._CP',             # 0D
        'ED6_DT07/CH01370P._CP',             # 0E
        'ED6_DT07/CH01090P._CP',             # 0F
        'ED6_DT07/CH01080P._CP',             # 10
        'ED6_DT07/CH01580P._CP',             # 11
        'ED6_DT07/CH02360P._CP',             # 12
        'ED6_DT07/CH00003P._CP',             # 13
        'ED6_DT07/CH00013P._CP',             # 14
        'ED6_DT07/CH00043P._CP',             # 15
        'ED6_DT07/CH01363P._CP',             # 16
        'ED6_DT07/CH01083P._CP',             # 17
        'ED6_DT07/CH01583P._CP',             # 18
        'ED6_DT07/CH01373P._CP',             # 19
        'ED6_DT07/CH01663P._CP',             # 1A
        'ED6_DT07/CH01213P._CP',             # 1B
        'ED6_DT07/CH01433P._CP',             # 1C
        'ED6_DT07/CH01463P._CP',             # 1D
        'ED6_DT07/CH01593P._CP',             # 1E
        'ED6_DT07/CH01093P._CP',             # 1F
        'ED6_DT07/CH02603P._CP',             # 20
        'ED6_DT06/CH20021P._CP',             # 21
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 30700,
        Z                   = 0,
        Y                   = 55110,
        Direction           = 270,
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
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
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
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
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
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
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
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
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
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
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
        X                   = 41400,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 84450,
        Z                   = 250,
        Y                   = 1030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 84450,
        Z                   = 250,
        Y                   = 2790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 87540,
        Z                   = 250,
        Y                   = 2770,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -700,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -3100,
        Z                   = 0,
        Y                   = 5400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 4490,
        Z                   = 250,
        Y                   = 34880,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 4790,
        Z                   = 250,
        Y                   = -1130,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 5400,
        Z                   = 300,
        Y                   = 30500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 3040,
        Z                   = 0,
        Y                   = 35050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 85800,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 84080,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3900,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        X                   = 85590,
        Z                   = 700,
        Y                   = 3050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835041,
        ChipIndex           = 0x21,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 51000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )


    DeclActor(
        TriggerX            = 33000,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 33000,
        ActorZ              = 1000,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33000,
        TriggerZ            = 0,
        TriggerY            = 32200,
        TriggerRange        = 800,
        ActorX              = 33000,
        ActorZ              = 1000,
        ActorY              = 32200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59000,
        TriggerZ            = 0,
        TriggerY            = 32000,
        TriggerRange        = 800,
        ActorX              = 59000,
        ActorZ              = 1000,
        ActorY              = 32000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41200,
        TriggerZ            = 0,
        TriggerY            = 5490,
        TriggerRange        = 400,
        ActorX              = 41400,
        ActorZ              = 1500,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85590,
        TriggerZ            = 700,
        TriggerY            = 3400,
        TriggerRange        = 1000,
        ActorX              = 85590,
        ActorZ              = 1000,
        ActorY              = 3050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_692",          # 00, 0
        "Function_1_ADC",          # 01, 1
        "Function_2_B61",          # 02, 2
        "Function_3_CDE",          # 03, 3
        "Function_4_1520",         # 04, 4
        "Function_5_1525",         # 05, 5
        "Function_6_1F7F",         # 06, 6
        "Function_7_233B",         # 07, 7
        "Function_8_26EE",         # 08, 8
        "Function_9_2C9B",         # 09, 9
        "Function_10_3131",        # 0A, 10
        "Function_11_332E",        # 0B, 11
        "Function_12_373E",        # 0C, 12
        "Function_13_39F6",        # 0D, 13
        "Function_14_3BA1",        # 0E, 14
        "Function_15_3C34",        # 0F, 15
        "Function_16_44F5",        # 10, 16
        "Function_17_459C",        # 11, 17
        "Function_18_45E8",        # 12, 18
        "Function_19_4791",        # 13, 19
        "Function_20_48AB",        # 14, 20
        "Function_21_4B0D",        # 15, 21
        "Function_22_4E6C",        # 16, 22
        "Function_23_5668",        # 17, 23
        "Function_24_5A54",        # 18, 24
        "Function_25_5B4A",        # 19, 25
        "Function_26_5BAE",        # 1A, 26
        "Function_27_5C16",        # 1B, 27
        "Function_28_5C1A",        # 1C, 28
        "Function_29_5C1E",        # 1D, 29
        "Function_30_5C22",        # 1E, 30
        "Function_31_5C26",        # 1F, 31
    )


    def Function_0_692(): pass

    label("Function_0_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7A9")
    SetChrPos(0x11, 5320, 250, 2110, 270)
    SetChrPos(0x16, -3060, 0, 3170, 45)
    SetChrPos(0x15, 560, 100, 240, 90)
    SetChrChipByIndex(0x15, 22)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x10)
    OP_44(0x15, 0xFF)
    SetChrPos(0x12, 5300, 250, 32080, 180)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x1B, -1100, 0, 32240, 270)
    SetChrChipByIndex(0x1D, 31)
    SetChrPos(0x1D, -2660, 100, 32180, 90)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x10)
    OP_44(0x1D, 0xFF)
    SetChrChipByIndex(0x1A, 23)
    SetChrPos(0x1A, -5950, 100, 34220, 90)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x10)
    OP_44(0x1A, 0xFF)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 86430, 0, 31990, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 95400, 250, 31050, 90)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x13, 28)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    OP_44(0x13, 0xFF)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x8, 32)
    Jump("loc_A78")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_7F4")
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
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x8, 32)
    Jump("loc_A78")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_886")
    SetChrPos(0x11, 1710, 0, 4970, 180)
    SetChrPos(0x12, -6910, 0, 33220, 90)
    SetChrPos(0x13, 95370, 250, 34220, 225)
    SetChrPos(0x8, 42950, 0, 1120, 270)
    SetChrPos(0x16, -7060, 0, 1680, 90)
    SetChrPos(0x17, 920, 0, -1500, 0)
    SetChrPos(0x18, -1590, 0, 34700, 0)
    SetChrPos(0x1A, 1300, 0, 28510, 90)
    Jump("loc_A78")

    label("loc_886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_91B")
    SetChrPos(0x11, 1710, 0, 4970, 180)
    SetChrPos(0x12, -6910, 0, 33220, 90)
    SetChrPos(0x13, 95370, 250, 34220, 225)
    SetChrPos(0x8, 43470, 0, 5280, 225)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x16, -7060, 0, 1680, 90)
    SetChrPos(0x17, 920, 0, -1500, 0)
    SetChrPos(0x1A, 1300, 0, 28510, 90)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_A78")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_976")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrPos(0x16, -5200, 0, 2050, 0)
    SetChrPos(0x17, 4500, 250, 4019, 270)
    SetChrPos(0x1A, 790, 0, 34680, 0)
    SetChrChipByIndex(0x8, 32)
    Jump("loc_A78")

    label("loc_976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_A27")
    SetChrPos(0x12, 5300, 250, 32080, 90)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x13, 28)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    OP_44(0x13, 0xFF)
    SetChrChipByIndex(0x11, 26)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    OP_44(0x11, 0xFF)
    SetChrChipByIndex(0x16, 24)
    SetChrPos(0x16, -2650, 100, 4200, 90)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x10)
    OP_44(0x16, 0xFF)
    SetChrChipByIndex(0x1F, 30)
    SetChrPos(0x1F, 84120, 100, 30200, 90)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x10)
    OP_44(0x1F, 0xFF)
    SetChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x8, 32)
    Jump("loc_A78")

    label("loc_A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_A78")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 32)

    label("loc_A78")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (114, "loc_A84"),
        (SWITCH_DEFAULT, "loc_AB5"),
    )


    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AB2")
    OP_A2(0x42F)
    OP_71(0x1, 0x10)
    OP_71(0x2, 0x10)
    OP_71(0x3, 0x10)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Event(0, 22)

    label("loc_AB2")

    Jump("loc_AB5")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_ADB")
    OP_A3(0x3FA)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1D, 0x80)
    Event(0, 23)
    OP_B1("t2510_n")

    label("loc_ADB")

    Return()

    # Function_0_692 end

    def Function_1_ADC(): pass

    label("Function_1_ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AFD")
    OP_B1("t2510_y")
    Jump("loc_B06")

    label("loc_AFD")

    OP_B1("t2510_n")

    label("loc_B06")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B39")
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)

    label("loc_B39")

    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_B4C")
    OP_65(0x5, 0x1)

    label("loc_B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_B60")
    OP_64(0x5, 0x1)
    SetChrFlags(0x22, 0x80)

    label("loc_B60")

    Return()

    # Function_1_ADC end

    def Function_2_B61(): pass

    label("Function_2_B61")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B86")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CC8")

    label("loc_B86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9F")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CC8")

    label("loc_B9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB8")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CC8")

    label("loc_BB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD1")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CC8")

    label("loc_BD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEA")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CC8")

    label("loc_BEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C03")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CC8")

    label("loc_C03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CC8")

    label("loc_C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C35")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CC8")

    label("loc_C35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CC8")

    label("loc_C4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CC8")

    label("loc_C67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C80")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CC8")

    label("loc_C80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C99")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CC8")

    label("loc_C99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB2")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CC8")

    label("loc_CB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CC8")

    label("loc_CDD")

    Return()

    # Function_2_B61 end

    def Function_3_CDE(): pass

    label("Function_3_CDE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_EF3")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D0A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_D25")

    label("loc_D0A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D20")
    SetChrSubChip(0xFE, 0)
    Jump("loc_D25")

    label("loc_D20")

    SetChrSubChip(0xFE, 2)

    label("loc_D25")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E52")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "#782FAh, hello there.\x02\x03",

            "I've known Dalmore for so long that\x01",
            "it's difficult to contain my shock at\x01",
            "what he's been doing...\x02\x03",

            "#783FIt's not so much that his crimes\x01",
            "are unforgivable, but I think he\x01",
            "might be, too...\x02\x03",

            "I pray that he will come to regret\x01",
            "straying from the path.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEB")

    label("loc_E52")


    ChrTalk(    #1
        0xFE,
        (
            "#783FIt's not so much that his crimes\x01",
            "are unforgivable, but I think he\x01",
            "might be, too...\x02\x03",

            "I pray that he will come to regret\x01",
            "straying from the path.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEB")

    SetChrSubChip(0xFE, 0)
    Jump("loc_151C")

    label("loc_EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_10FD")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F1C")
    SetChrSubChip(0xFE, 1)
    Jump("loc_F37")

    label("loc_F1C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F32")
    SetChrSubChip(0xFE, 0)
    Jump("loc_F37")

    label("loc_F32")

    SetChrSubChip(0xFE, 2)

    label("loc_F37")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1062")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "#780FEstelle and Joshua...we are\x01",
            "greatly indebted to you for\x01",
            "your help.\x02\x03",

            "I saw the play, and I thought it\x01",
            "was magnificent.\x02\x03",

            "Joshua's portrayal of Princess\x01",
            "Cecilia was particularly\x01",
            "memorable, I thought.\x02\x03",

            "If you have the chance, I hope\x01",
            "you will come back to our school.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F5")

    label("loc_1062")


    ChrTalk(    #3
        0xFE,
        (
            "#780FAt any rate, I'm just glad that\x01",
            "we were able to come to\x01",
            "Matron Theresa's aid.\x02\x03",

            "This whole arson affair has simply\x01",
            "been too much for her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F5")

    SetChrSubChip(0xFE, 0)
    Jump("loc_151C")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AC")
    OP_A2(0x0)

    ChrTalk(    #4
        0xFE,
        (
            "#780FAh, Kloe. Everything's been a great\x01",
            "success, thus far.\x02\x03",

            "I'm looking forward to seeing the\x01",
            "play. I expect it will be a big hit\x01",
            "for the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120E")

    label("loc_11AC")


    ChrTalk(    #5
        0xFE,
        (
            "#780FI'm looking forward to seeing the\x01",
            "play. I expect it will be a big hit\x01",
            "for the festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120E")

    Jump("loc_151C")

    label("loc_1211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_13D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131A")
    OP_A2(0x0)

    ChrTalk(    #6
        0xFE,
        (
            "#780FI've not seen you since last year's\x01",
            "Royal Council, Mayor Dalmore.\x02\x03",

            "Has much changed since then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x21,
        (
            "#660FAs you can see, I'm feeling\x01",
            "quite well. You look to be in\x01",
            "good health, also.\x02\x03",

            "I expect that today will be\x01",
            "quite enjoyable.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    Jump("loc_13D1")

    label("loc_131A")


    ChrTalk(    #8
        0xFE,
        (
            "#780FI'd like to get your input on some\x01",
            "of the school's affairs, if you have\x01",
            "the time.\x02\x03",

            "Though we may be chartered by\x01",
            "the monarchy, it's still important\x01",
            "to hear the local views.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D1")

    Jump("loc_151C")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_151C")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13FD")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1418")

    label("loc_13FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1413")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1418")

    label("loc_1413")

    SetChrSubChip(0xFE, 2)

    label("loc_1418")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #9
        0xFE,
        (
            "#780FDon't worry, I'll make sure you have a place\x01",
            "to stay. And I'm greatly looking forward to\x01",
            "your...erm...'transformation'...\x02\x03",

            "There's also a cafeteria on campus, which\x01",
            "you may use at your leisure. Just relax,\x01",
            "and work hard on the play.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_151C")

    TalkEnd(0x8)
    Return()

    # Function_3_CDE end

    def Function_4_1520(): pass

    label("Function_4_1520")

    Call(0, 5)
    Return()

    # Function_4_1520 end

    def Function_5_1525(): pass

    label("Function_5_1525")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1602")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B2")
    OP_A2(0x1)

    ChrTalk(    #10
        0x10,
        "Oh, did you need me for something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "Classes just ended, so the students\x01",
            "should be milling about any moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FF")

    label("loc_15B2")


    ChrTalk(    #12
        0x10,
        (
            "Classes just ended, so the students\x01",
            "should be milling about any moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FF")

    Jump("loc_1F7B")

    label("loc_1602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1692")

    ChrTalk(    #13
        0x10,
        (
            "Ha ha...the festival was a\x01",
            "huge success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "I always worry that the people\x01",
            "with children will lose track of\x01",
            "them in the crowd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7B")

    label("loc_1692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_17B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175A")
    OP_A2(0x1)

    ChrTalk(    #15
        0x10,
        (
            "Success! This is possibly our\x01",
            "best turnout yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "Though I do always worry that the people\x01",
            "with children will lose track of them in\x01",
            "the crowd. But so far...no fatalities!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B4")

    label("loc_175A")


    ChrTalk(    #17
        0x10,
        "Is someone looking for them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "I can call for them on the campus\x01",
            "P.A. if need be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B4")

    Jump("loc_1F7B")

    label("loc_17B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_192A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C6")
    OP_A2(0x1)

    ChrTalk(    #19
        0x10,
        (
            "The event will be held on the\x01",
            "grounds and in the main building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "There's a play scheduled to be held\x01",
            "in the auditorium, this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "The Student Council has set up the\x01",
            "cafeteria as the rest area, so please,\x01",
            "feel free to relax there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1927")

    label("loc_18C6")


    ChrTalk(    #22
        0x10,
        (
            "In order to help prevent crime,\x01",
            "the dorms are locked down\x01",
            "for the duration of the festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1927")

    Jump("loc_1F7B")

    label("loc_192A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C6")
    OP_A2(0x1)

    ChrTalk(    #23
        0x10,
        (
            "Have you finished getting ready?\x01",
            "Tomorrow isn't far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "It looks like we'll have more\x01",
            "attendees tomorrow than\x01",
            "ever before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A05")

    label("loc_19C6")


    ChrTalk(    #25
        0x10,
        (
            "Have you finished getting ready?\x01",
            "Tomorrow isn't far away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A05")

    Jump("loc_1F7B")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABA")
    OP_A2(0x1)

    ChrTalk(    #26
        0x10,
        (
            "Even with classes done, it's still\x01",
            "extremely busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        "It's almost festival time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "I hope all of the students are\x01",
            "trying their hardest for this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_1ABA")


    ChrTalk(    #29
        0x10,
        "It's almost festival time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "I hope all of the students are\x01",
            "trying their hardest for this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1F")

    Jump("loc_1F7B")

    label("loc_1B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_1CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C37")
    OP_A2(0x1)
    TurnDirection(0x10, 0x105, 0)

    ChrTalk(    #31
        0x10,
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        "#040FPardon me, Fauna...I just got back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "Ha ha, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "If you're looking for the dean,\x01",
            "he just went to his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        "He's been quite worried about you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x105,
        "#040FOh, all right. I'll go and see him now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA7")

    label("loc_1C37")

    TurnDirection(0x10, 0x105, 0)

    ChrTalk(    #37
        0x10,
        (
            "If you're looking for the dean,\x01",
            "he just went to his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "He's been quite worried about you.\x02",
    )

    CloseMessageWindow()

    label("loc_1CA7")

    Jump("loc_1F7B")

    label("loc_1CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1DA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D82")
    OP_A2(0x1)

    ChrTalk(    #39
        0x10,
        (
            "Hello, Kloe. Are you already done\x01",
            "with your off-campus errands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        (
            "#040FOh, not yet...\x02\x03",

            "I'm sorry, but I still have some\x01",
            "errands left to run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "That's fine. Just take care\x01",
            "of yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA4")

    label("loc_1D82")


    ChrTalk(    #42
        0x10,
        "Take care of yourself, Kloe.\x02",
    )

    CloseMessageWindow()

    label("loc_1DA4")

    Jump("loc_1F7B")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_1E26")

    ChrTalk(    #43
        0x10,
        "Oh, did you want a guided tour?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "I'm terribly sorry, but I can't\x01",
            "show you around while class\x01",
            "is in session.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7B")

    label("loc_1E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2A")
    OP_A2(0x1)

    ChrTalk(    #45
        0x10,
        (
            "Oh, hello, Kloe. Are you back\x01",
            "to stay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x105,
        (
            "#040FNo...I'm just showing some folks\x01",
            "around on the way to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "I see...well, since this is your\x01",
            "vacation, make sure you let\x01",
            "your hair down and have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        "#040FI will...thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F7B")

    label("loc_1F2A")


    ChrTalk(    #49
        0x10,
        (
            "Since this is your vacation,\x01",
            "make sure you let your hair\x01",
            "down and have fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7B")

    TalkEnd(0x10)
    Return()

    # Function_5_1525 end

    def Function_6_1F7F(): pass

    label("Function_6_1F7F")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1FD0")

    ChrTalk(    #50
        0xFE,
        (
            "Class may be over, but I still\x01",
            "get questions from my students.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2045")

    ChrTalk(    #51
        0xFE,
        (
            "Hmm...my class has done a\x01",
            "fine job on the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "They really put a lot of work\x01",
            "into this set.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_2045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_20BB")

    ChrTalk(    #53
        0xFE,
        (
            "The lead roles will be played\x01",
            "by students, will they not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Everyone's even more active\x01",
            "than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_20BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2224")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2192")
    OP_A2(0x2)

    ChrTalk(    #55
        0xFE,
        (
            "You kids came from Rolent,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I'm actually from there, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Speaking of which, my parents will\x01",
            "be visiting to attend the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "It's good that they were invited.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2221")

    label("loc_2192")


    ChrTalk(    #59
        0xFE,
        (
            "Ah, yes...I had a chance to watch\x01",
            "the rehearsals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I'm quite looking forward to\x01",
            "the performance. The, uh,\x01",
            "princess is something else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2221")

    Jump("loc_2337")

    label("loc_2224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2337")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_224D")
    SetChrSubChip(0xFE, 1)
    Jump("loc_227E")

    label("loc_224D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2263")
    SetChrSubChip(0xFE, 0)
    Jump("loc_227E")

    label("loc_2263")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2279")
    SetChrSubChip(0xFE, 2)
    Jump("loc_227E")

    label("loc_2279")

    SetChrSubChip(0xFE, 1)

    label("loc_227E")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #61
        0xFE,
        (
            "With the festival coming up, the\x01",
            "kids practically vibrate in their\x01",
            "seats when class is almost out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Ha ha...but I suppose there's\x01",
            "nothing to be done about it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_2337")

    TalkEnd(0x11)
    Return()

    # Function_6_1F7F end

    def Function_7_233B(): pass

    label("Function_7_233B")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_23EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BA")
    OP_A2(0x3)

    ChrTalk(    #63
        0xFE,
        "Let's see...this problem here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0xFE,
        "How do you do it?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    Jump("loc_23EC")

    label("loc_23BA")


    ChrTalk(    #66
        0xFE,
        (
            "Wow, the students here are\x01",
            "really dedicated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23EC")

    Jump("loc_26EA")

    label("loc_23EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_245A")

    ChrTalk(    #67
        0xFE,
        "This afternoon is the big play.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Good thing you two seem like\x01",
            "the really reliable sort.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26EA")

    label("loc_245A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250F")
    OP_A2(0x3)

    ChrTalk(    #69
        0xFE,
        "Hmm...my class is fairly low-key...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "To be honest, I think the research\x01",
            "periodical is pretty plain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "But it's okay. I'm just glad we\x01",
            "have readers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253E")

    label("loc_250F")


    ChrTalk(    #72
        0xFE,
        "I don't want to lose to Millia's class...\x02",
    )

    CloseMessageWindow()

    label("loc_253E")

    Jump("loc_26EA")

    label("loc_2541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_26EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A2")
    OP_A2(0x3)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #73
        0xFE,
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x105,
        (
            "#040FHello, Ms. Wiola.\x02\x03",

            "I'm sorry I missed your class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Ha ha...you don't need to worry\x01",
            "about that, dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "You did have important business\x01",
            "to attend to, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "If you stop by the faculty lounge later,\x01",
            "I can give you a printout of the\x01",
            "work you missed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#040FYes, ma'am. I will.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26EA")

    label("loc_26A2")


    ChrTalk(    #79
        0xFE,
        (
            "Now, then...I suppose I should get\x01",
            "started on grading these tests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EA")

    TalkEnd(0x12)
    Return()

    # Function_7_233B end

    def Function_8_26EE(): pass

    label("Function_8_26EE")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_27E7")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_271A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_274B")

    label("loc_271A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2730")
    SetChrSubChip(0xFE, 0)
    Jump("loc_274B")

    label("loc_2730")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2746")
    SetChrSubChip(0xFE, 2)
    Jump("loc_274B")

    label("loc_2746")

    SetChrSubChip(0xFE, 1)

    label("loc_274B")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #80
        0xFE,
        (
            "I've been put in charge of writing\x01",
            "up the entrance examinations\x01",
            "for this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Ha ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "I look forward to the challenge.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_2C97")

    label("loc_27E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_28D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2876")
    OP_A2(0x4)

    ChrTalk(    #83
        0xFE,
        (
            "Why is my class doing fortune-\x01",
            "telling and games, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Wiola's kids are doing something\x01",
            "far more direct.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D6")

    label("loc_2876")


    ChrTalk(    #85
        0xFE,
        (
            "The students in that class are\x01",
            "impressive...though the same\x01",
            "can't be said for the teacher.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D6")

    Jump("loc_2C97")

    label("loc_28D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_293F")

    ChrTalk(    #86
        0xFE,
        (
            "Anyway, have you seen the size\x01",
            "of the crowd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "I wonder if they're all on vacation.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C97")

    label("loc_293F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F4")
    OP_A2(0x4)

    ChrTalk(    #88
        0xFE,
        (
            "Well, the students will show\x01",
            "everyone the fruits of their\x01",
            "labors tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I'll do my best to keep my criticisms\x01",
            "to myself...as valid as they may be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A44")

    label("loc_29F4")


    ChrTalk(    #90
        0xFE,
        (
            "Well, the students will show\x01",
            "everyone the fruits of their\x01",
            "labors tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A44")

    Jump("loc_2C97")

    label("loc_2A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2C97")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A70")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2AA1")

    label("loc_2A70")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A86")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2AA1")

    label("loc_2A86")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A9C")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2AA1")

    label("loc_2A9C")

    SetChrSubChip(0xFE, 1)

    label("loc_2AA1")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC8")
    OP_A2(0x4)

    ChrTalk(    #91
        0xFE,
        (
            "Everyone tends to slack off in\x01",
            "the lead-up to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "I suppose all the instruction in\x01",
            "the world can't change that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Perhaps tomorrow, I'll give the kids a pop quiz.\x01",
            "And just to show them...it will NOT be multiple\x01",
            "choice! Mwa ha ha ha...ha... Ahem!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C92")

    label("loc_2BC8")


    ChrTalk(    #94
        0xFE,
        (
            "Everyone tends to slack off in the\x01",
            "lead-up to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Perhaps tomorrow, I'll give the kids a pop quiz.\x01",
            "And just to show them...it will NOT be multiple\x01",
            "choice! Mwa ha ha ha...ha... Ahem!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C92")

    SetChrSubChip(0xFE, 0)

    label("loc_2C97")

    TalkEnd(0x13)
    Return()

    # Function_8_26EE end

    def Function_9_2C9B(): pass

    label("Function_9_2C9B")

    TalkBegin(0x14)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CC0")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2CF1")

    label("loc_2CC0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CD6")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2CF1")

    label("loc_2CD6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CEC")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2CF1")

    label("loc_2CEC")

    SetChrSubChip(0xFE, 2)

    label("loc_2CF1")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2D7B")

    ChrTalk(    #96
        0xFE,
        "I should make my rounds, soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "The students are generally\x01",
            "well-behaved enough to not\x01",
            "require me to hover.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3128")

    label("loc_2D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2EE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2E22")

    ChrTalk(    #98
        0xFE,
        (
            "Ah, thanks for everything you\x01",
            "did yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "I don't really have anything\x01",
            "I need to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "I'm just staying here,\x01",
            "in case I'm needed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EE5")

    label("loc_2E22")


    ChrTalk(    #101
        0xFE,
        (
            "I heard some students talking\x01",
            "yesterday about having seen\x01",
            "monsters in the old building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I'll be making sure everything is\x01",
            "locked up tight before my rounds,\x01",
            "just to be on the safe side.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EE5")

    Jump("loc_3128")

    label("loc_2EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_308B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE0")
    OP_A2(0x5)

    ChrTalk(    #103
        0xFE,
        (
            "There are three major courses\x01",
            "offered at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "All of them are important,\x01",
            "but I'm personally in charge\x01",
            "of physical education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "There are no classes at the\x01",
            "moment. Perfect time to get\x01",
            "the papers sorted out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3088")

    label("loc_2FE0")


    ChrTalk(    #106
        0xFE,
        (
            "All of them are important,\x01",
            "but I'm personally in charge\x01",
            "of physical education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "There are no classes at the\x01",
            "moment. Perfect time to get\x01",
            "the papers sorted out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3088")

    Jump("loc_3128")

    label("loc_308B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30FE")
    OP_A2(0x5)

    ChrTalk(    #108
        0xFE,
        "Hey, aren't you students?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Class is in session. You'll need\x01",
            "a pass to go off-campus.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3128")

    label("loc_30FE")


    ChrTalk(    #110
        0xFE,
        "You'll need a pass to go off-campus.\x02",
    )

    CloseMessageWindow()

    label("loc_3128")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x14)
    Return()

    # Function_9_2C9B end

    def Function_10_3131(): pass

    label("Function_10_3131")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_31F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B6")
    OP_A2(0x6)

    ChrTalk(    #111
        0xFE,
        (
            "Ahhh...finally, classes are done\x01",
            "for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Afternoon classes always make\x01",
            "me want to take a nap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F0")

    label("loc_31B6")


    ChrTalk(    #113
        0xFE,
        (
            "Afternoon classes always make\x01",
            "me want to take a nap.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F0")

    Jump("loc_332A")

    label("loc_31F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_332A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A7")
    OP_A2(0x6)

    ChrTalk(    #114
        0xFE,
        (
            "I've been involved in the club's\x01",
            "food stand the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I didn't have a chance to get\x01",
            "involved in the class project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "Yep, I'm feeling good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_332A")

    label("loc_32A7")


    ChrTalk(    #117
        0xFE,
        (
            "I've been involved in the club's\x01",
            "food stand the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "I didn't have a chance to get\x01",
            "involved in the class project.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_332A")

    TalkEnd(0x15)
    Return()

    # Function_10_3131 end

    def Function_11_332E(): pass

    label("Function_11_332E")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3391")

    ChrTalk(    #119
        0xFE,
        "Okay, time for the club activities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "I've GOT to finish this painting today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_373A")

    label("loc_3391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3427")

    ChrTalk(    #121
        0xFE,
        (
            "Since I'm working on the coffee house,\x01",
            "I've got to push myself! And to do that...\x01",
            "I NEED MORE COFFEEEEEE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "This is pretty tough...\x02",
    )

    CloseMessageWindow()
    Jump("loc_373A")

    label("loc_3427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_34E9")

    ChrTalk(    #123
        0xFE,
        (
            "Whew...I'm not sure how, but I\x01",
            "managed to finish up in time.\x01",
            "Musta been the 36 lattes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Pulling an all-nighter sure leaves\x01",
            "me exhausted. Or is that the\x01",
            "caffeine withdrawal?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373A")

    label("loc_34E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_35D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3580")
    OP_A2(0x7)

    ChrTalk(    #125
        0xFE,
        (
            "Whoa! What the hell?!\x01",
            "This is a cappuccino...\x01",
            "I ordered an espresso! Nooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I'll never finish up in time\x01",
            "at this rate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35D6")

    label("loc_3580")


    ChrTalk(    #127
        0xFE,
        "Hmm...maybe if I work all night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Ahhh...that should give me\x01",
            "plenty of time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D6")

    Jump("loc_373A")

    label("loc_35D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_373A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D9")
    OP_A2(0x7)

    ChrTalk(    #129
        0xFE,
        (
            "Hmmhmmhmmmmm... ♪\x01",
            "They've got an awful lot of coffee... ♪\x01",
            "An awful lot of coffee... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I'm making outfits to wear at\x01",
            "the food stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I've got to really throw myself\x01",
            "into this! And to do that...\x01",
            "I NEED MORE COFFEEEEEE!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373A")

    label("loc_36D9")


    ChrTalk(    #132
        0xFE,
        "I love making stuff like this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Oh, right, I've got to make\x01",
            "decorations for the room...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_373A")

    TalkEnd(0x16)
    Return()

    # Function_11_332E end

    def Function_12_373E(): pass

    label("Function_12_373E")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3783")

    ChrTalk(    #134
        0xFE,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I'd be glad to show you to\x01",
            "your seats.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F2")

    label("loc_3783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_37DE")

    ChrTalk(    #136
        0xFE,
        "Hee hee...isn't this a cute outfit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "Kaden's been making a lot of them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39F2")

    label("loc_37DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_38B8")

    ChrTalk(    #138
        0xFE,
        (
            "He thought we had more time than we actually\x01",
            "do. Thankfully, with enough coffee in him, we\x01",
            "can still make the deadline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "So worry not, we'll be ready!\x01",
            "I want this to be the cutest\x01",
            "little place ever!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F2")

    label("loc_38B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_39F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397C")
    OP_A2(0x8)

    ChrTalk(    #140
        0xFE,
        (
            "Kaden's really good with his hands,\x01",
            "and if you give him a little coffee,\x01",
            "then he can do just about anything! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Maybe I can get him to make\x01",
            "some stuffed dolls next...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F2")

    label("loc_397C")


    ChrTalk(    #142
        0xFE,
        (
            "Despite the fact that he's appearing\x01",
            "in the play, he still managed to find\x01",
            "the time to make maid outfits for us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F2")

    TalkEnd(0x17)
    Return()

    # Function_12_373E end

    def Function_13_39F6(): pass

    label("Function_13_39F6")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3A42")

    ChrTalk(    #143
        0xFE,
        (
            "I didn't really understand the\x01",
            "lesson in my last class...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B9D")

    label("loc_3A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B3C")
    OP_A2(0x9)

    ChrTalk(    #144
        0xFE,
        (
            "Everyone in the social studies\x01",
            "class is working on the research\x01",
            "periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "Oh, wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "My class is doing either a tea house or a\x01",
            "haunted house. Not sure which, though,\x01",
            "frankly I think there's cross-over potential.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B9D")

    label("loc_3B3C")


    ChrTalk(    #147
        0xFE,
        (
            "Everyone in the social studies\x01",
            "class is working on the research\x01",
            "periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "Oh, wow...\x02",
    )

    CloseMessageWindow()

    label("loc_3B9D")

    TalkEnd(0x18)
    Return()

    # Function_13_39F6 end

    def Function_14_3BA1(): pass

    label("Function_14_3BA1")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3BD5")

    ChrTalk(    #149
        0xFE,
        "Welcome to the Fontana Tea House.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C30")

    label("loc_3BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3C30")

    ChrTalk(    #150
        0xFE,
        (
            "I'm kind of embarrassed to be\x01",
            "dressed like this, but it is for\x01",
            "the festival...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C30")

    TalkEnd(0x19)
    Return()

    # Function_14_3BA1 end

    def Function_15_3C34(): pass

    label("Function_15_3C34")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3C70")

    ChrTalk(    #151
        0xFE,
        (
            "Hmm...today's lesson was\x01",
            "very worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F1")

    label("loc_3C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3DEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D5D")
    OP_A2(0xB)

    ChrTalk(    #152
        0xFE,
        (
            "I understand the need to enjoy oneself,\x01",
            "but at the end of the day, I still need to\x01",
            "hand in my research results, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "That's especially true when\x01",
            "you're a senior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "Getting good grades is paramount.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DEB")

    label("loc_3D5D")


    ChrTalk(    #155
        0xFE,
        (
            "I understand the need to engage in outside\x01",
            "activities, but at the end of the day, I still\x01",
            "need to hand in my research results, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DEB")

    Jump("loc_44F1")

    label("loc_3DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_421C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_3F89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F55")
    OP_A2(0xB)

    ChrTalk(    #156
        0xFE,
        (
            "My social studies class has been using various\x01",
            "economic indicators to predict future trends\x01",
            "and we'll be displaying the results here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "We also have a collection of materials\x01",
            "summarising the history and development of this\x01",
            "region in a simple, easy to read format.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F86")

    label("loc_3F55")


    ChrTalk(    #159
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F86")

    Jump("loc_4219")

    label("loc_3F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F7")
    OP_A2(0xB)

    ChrTalk(    #160
        0xFE,
        (
            "My social studies class will be\x01",
            "researching various economic\x01",
            "indicators to predict future trends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "Reviewing the history and growth\x01",
            "of Ruan should provide useful\x01",
            "data for this project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "If any details are missing, you just\x01",
            "have to go with what makes the most\x01",
            "sense from the data available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4219")

    label("loc_40F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_41E8")

    ChrTalk(    #164
        0xFE,
        (
            "It may push me past deadline, but I'd\x01",
            "love to get my hands on a copy of 'Ruan\x01",
            "Economics.' Very useful data in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "If you should happen to see any\x01",
            "of the volumes, would you please\x01",
            "return them to the reference room?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4219")

    label("loc_41E8")


    ChrTalk(    #166
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4219")

    Jump("loc_44F1")

    label("loc_421C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42EA")
    OP_A2(0xB)

    ChrTalk(    #167
        0xFE,
        (
            "I need more research materials\x01",
            "to better substantiate my findings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "I don't think there's enough time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "I suppose I'll just have to do the\x01",
            "best I can with what I have.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4334")

    label("loc_42EA")


    ChrTalk(    #170
        0xFE,
        (
            "I need more research materials\x01",
            "to better substantiate my findings...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4334")

    Jump("loc_44F1")

    label("loc_4337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_44F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C8")
    OP_A2(0xB)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #171
        0xFE,
        (
            "Hello, Kloe.\x01",
            "So, you've come back to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "The preparations for the class\x01",
            "program appear to be coming\x01",
            "along well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "How fares the play?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "I'm told the casting has not yet\x01",
            "been finalized, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x105,
        (
            "#040FHa ha. That was done some\x01",
            "time ago, Logic.\x02\x03",

            "It's going to be great.\x01",
            "I hope you'll enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "Ah, yes, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "Then I wish you the best of luck.\x02",
    )

    CloseMessageWindow()
    Jump("loc_44F1")

    label("loc_44C8")

    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #178
        0xFE,
        "I wish you the best of luck.\x02",
    )

    CloseMessageWindow()

    label("loc_44F1")

    TalkEnd(0x1A)
    Return()

    # Function_15_3C34 end

    def Function_16_44F5(): pass

    label("Function_16_44F5")

    TalkBegin(0x1B)

    ChrTalk(    #179
        0xFE,
        (
            "Rumor has it the queen's birthday\x01",
            "celebration is going to feature the\x01",
            "biggest competition yet this year!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "I'd love for my Fencing Club\x01",
            "to participate.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_16_44F5 end

    def Function_17_459C(): pass

    label("Function_17_459C")

    TalkBegin(0x1C)

    ChrTalk(    #181
        0xFE,
        "Here, Ms. Wiola.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "Right here's where I started\x01",
            "to get lost.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1C)
    Return()

    # Function_17_459C end

    def Function_18_45E8(): pass

    label("Function_18_45E8")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4666")

    ChrTalk(    #183
        0xFE,
        "Okay, archery practice today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "It's been a while since I've had a\x01",
            "break from working on the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_478D")

    label("loc_4666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_470F")
    OP_A2(0xE)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #185
        0xFE,
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "We've got to start putting up the\x01",
            "decorations soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "If we can't finish up one task,\x01",
            "we can't move on to the next...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_478D")

    label("loc_470F")


    ChrTalk(    #188
        0xFE,
        (
            "We've got to start putting\x01",
            "up the decorations soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "If we can't finish up one task,\x01",
            "we can't move on to the next...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478D")

    TalkEnd(0x1D)
    Return()

    # Function_18_45E8 end

    def Function_19_4791(): pass

    label("Function_19_4791")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_482E")

    ChrTalk(    #190
        0xFE,
        "All right...done with classes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "Time to go for club activities. And\x01",
            "my club is the 'lounge around at home\x01",
            "club,' so I'm quite excited!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48A7")

    label("loc_482E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_48A7")

    ChrTalk(    #192
        0xFE,
        (
            "*sigh* But I guess I have some\x01",
            "shopping to do first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "I've got to buy some of everything\x01",
            "I can think of.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48A7")

    TalkEnd(0x1E)
    Return()

    # Function_19_4791 end

    def Function_20_48AB(): pass

    label("Function_20_48AB")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_49BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4968")
    OP_A2(0x10)

    ChrTalk(    #194
        0xFE,
        (
            "Aww, man...I wanted to ask Ms. Millia\x01",
            "about the stuff I didn't understand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "...but she always leaves the classroom\x01",
            "in such a hurry, I never get a chance!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BC")

    label("loc_4968")


    ChrTalk(    #196
        0xFE,
        (
            "I promised my sister I'd help out\x01",
            "with her shop, too, so I have to\x01",
            "get back...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49BC")

    Jump("loc_4B09")

    label("loc_49BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_4B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ABA")
    OP_A2(0x10)

    ChrTalk(    #197
        0xFE,
        (
            "I swear...why can't you learn to\x01",
            "have some kind of schedule?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "Everyone else is busy and you\x01",
            "don't have any assistants, so you\x01",
            "need to learn to be efficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Are you planning to make a round\x01",
            "trip to Ruan from campus?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B09")

    label("loc_4ABA")


    ChrTalk(    #200
        0xFE,
        (
            "*sigh* Gerome has absolutely no\x01",
            "idea of how to make good use of\x01",
            "his time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B09")

    TalkEnd(0x1F)
    Return()

    # Function_20_48AB end

    def Function_21_4B0D(): pass

    label("Function_21_4B0D")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4E68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDD")
    OP_A2(0x11)

    ChrTalk(    #201
        0x101,
        "#000FMayor Maybelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "#610FOh! Estelle! And Joshua, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        "#000FWhat are you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "#610FHa ha...to tell you the truth,\x01",
            "I actually graduated from here.\x02\x03",

            "I always make a point of going\x01",
            "to the campus festival each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#000FOh, okay. That's cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "#610FBut enough about me. How\x01",
            "have you two been doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        "#000FHeh heh...well, actually...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #208
        "\x07\x05Estelle told Mayor Maybelle what had been going on.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #209
        0xFE,
        (
            "#610FOh, so you're helping out\x01",
            "with the play?\x02\x03",

            "I've always found them to be\x01",
            "slightly tiresome.\x02\x03",

            "Hah a...but if you're going to be\x01",
            "on stage, I certainly don't want\x01",
            "to miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x102,
        (
            "#010F(Ugh...I'd really rather not have\x01",
            "anyone I KNOW in the audience\x01",
            "for this...)\x02",
        )
    )

    Jump("loc_4E68")

    label("loc_4DDD")


    ChrTalk(    #211
        0xFE,
        (
            "#610FI've always found plays to be\x01",
            "slightly tiresome.\x02\x03",

            "Ha ha...but if you're going to be\x01",
            "on stage, I certainly don't want\x01",
            "to miss it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E68")

    TalkEnd(0x20)
    Return()

    # Function_21_4B0D end

    def Function_22_4E6C(): pass

    label("Function_22_4E6C")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(116280, 0, 2160, 0)
    SetChrPos(0x101, 117450, 0, -1700, 0)
    SetChrPos(0x102, 116510, 0, -1950, 0)
    SetChrPos(0x105, 117000, 0, -1020, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #212
        0x105,
        "#040FI'm back, Dean Collins.\x02",
    )

    CloseMessageWindow()

    def lambda_4EE9():
        OP_6D(117230, 0, 4590, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4EE9)

    def lambda_4F01():
        OP_8E(0xFE, 0x1C890, 0x0, 0x690, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F01)
    Sleep(500)

    def lambda_4F21():
        OP_8E(0xFE, 0x1CB10, 0x0, 0x690, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F21)
    Sleep(300)

    def lambda_4F41():
        OP_8E(0xFE, 0x1C64C, 0x0, 0x5D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F41)
    WaitChrThread(0x105, 0x1)

    def lambda_4F61():
        OP_8E(0xFE, 0x1C58E, 0x0, 0x9F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F61)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x105, 400)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #213
        0x8,
        (
            "#780F#3PAh, hello, Kloe.\x02\x03",

            "And who might you be? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        "#000FIt's nice to meet you, Dean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        "#010FWe're from the Bracer Guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        (
            "#780F#3PBut you're so young.\x01",
            "Very impressive, indeed.\x02\x03",

            "Are you, by any chance, here\x01",
            "because of the fire at the\x01",
            "orphanage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x105,
        "#049F#2PYes, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #218
        "\x07\x05Kloe explained the entire situation surrounding the fire to Dean Collins.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #219
        0x8,
        (
            "#780F#3PI see... That's terrible.\x02\x03",

            "I wish I could do something\x01",
            "to help...\x02\x03",

            "...\x02\x03",

            "Well, first, there's the matter\x01",
            "of cheering up the children.\x02\x03",

            "Perhaps I could start there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x105,
        (
            "#047FYes, sir...\x02\x03",

            "#040FIn that case, I will work on the\x01",
            "play with Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x8,
        (
            "#781F#3PI think that's a good idea.\x02\x03",

            "#780FEstelle and Joshua, I wish you\x01",
            "both the best. Do what you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#006FY-Yes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x102,
        "#010FTo the best of our meager ability.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x8,
        (
            "#780F#3PI'm letting the head of the student\x01",
            "council handle the matter of the\x01",
            "play. Her name is Jill.\x02\x03",

            "She can tell you far more\x01",
            "about it than I ever could.\x02\x03",

            "I'll see about setting up\x01",
            "dorm rooms for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#004F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        "#014FDorms?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x8,
        (
            "#780F#3PWell, the campus festival IS\x01",
            "almost upon us.\x02\x03",

            "I'd imagine that you'll need to\x01",
            "rehearse every day for long\x01",
            "hours.\x02\x03",

            "And if that's the case, you'll need\x01",
            "a place to sleep, will you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        "#501FOh, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x102,
        "#019FThat would be greatly appreciated.\x02",
    )

    CloseMessageWindow()
    OP_22(0x8A, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #230
        0x8,
        (
            "#780F#3PAh, lessons seem to have\x01",
            "concluded for the day.\x02\x03",

            "Why not go and introduce yourselves\x01",
            "to the president, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x105,
        "#041FYes, sir.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    ChrTalk(    #232
        0x105,
        (
            "#040F#1PWe should go to the student\x01",
            "council room next.\x02\x03",

            "It's to the right of the main\x01",
            "building, on the second floor\x01",
            "of the clubhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        "#006FOkay. Let's go.\x02",
    )

    CloseMessageWindow()
    OP_28(0x3D, 0x1, 0x8)
    OP_28(0x3D, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_22_4E6C end

    def Function_23_5668(): pass

    label("Function_23_5668")

    EventBegin(0x0)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_6D(-1190, 0, 33250, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 19)
    SetChrChipByIndex(0x102, 20)
    SetChrChipByIndex(0x105, 21)
    SetChrChipByIndex(0xB, 23)
    SetChrChipByIndex(0xC, 24)
    SetChrChipByIndex(0xD, 22)
    SetChrChipByIndex(0xE, 25)
    SetChrPos(0x101, 500, 200, 32060, 90)
    SetChrPos(0x102, 500, 200, 29980, 90)
    SetChrPos(0x105, 520, 200, 34100, 90)
    SetChrPos(0xA, -2750, 200, 30010, 90)
    SetChrPos(0x9, -2750, 200, 32060, 90)
    SetChrPos(0xC, -2750, 100, 34060, 90)
    SetChrPos(0xB, -5900, 100, 30010, 90)
    SetChrPos(0xD, -5900, 100, 34160, 90)
    SetChrPos(0xE, -5900, 100, 31920, 90)
    SetChrPos(0xF, 5300, 250, 32119, 90)

    def lambda_57A7():
        OP_6D(3580, 0, 33240, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57A7)
    FadeToBright(2000, 0)
    OP_8E(0xF, 0x150E, 0xFA, 0x76FC, 0x3E8, 0x0)
    OP_8C(0xF, 90, 400)
    Sleep(500)
    OP_8E(0xF, 0x14FA, 0xFA, 0x7CD8, 0x3E8, 0x0)
    OP_8C(0xF, 90, 400)
    Sleep(500)
    OP_8E(0xF, 0x150E, 0xFA, 0x76FC, 0x3E8, 0x0)
    OP_8C(0xF, 270, 400)
    Sleep(1000)

    def lambda_5828():
        OP_6D(2000, 0, 33250, 1500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5828)
    OP_8E(0xF, 0xD2A, 0x0, 0x7710, 0x7D0, 0x0)
    OP_8E(0xF, 0xA0A, 0x0, 0x7B70, 0x7D0, 0x0)
    TurnDirection(0xF, 0x101, 400)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x105, 2)
    OP_62(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xF)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1500)
    Sleep(500)
    TurnDirection(0xF, 0x102, 400)
    SetChrSubChip(0x101, 2)
    Sleep(500)
    OP_62(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xF)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)
    Sleep(500)
    OP_62(0xF, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    FadeToDark(1000, 0, -1)

    AnonymousTalk(    #234
        "\x07\x05All throughout the morning, they attended lessons with the other students...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_5668 end

    def Function_24_5A54(): pass

    label("Function_24_5A54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AEC")
    TurnDirection(0x105, 0x1, 400)

    ChrTalk(    #235
        0x105,
        (
            "#040FI'm sorry, but class is\x01",
            "currently in session.\x02\x03",

            "Let's go to the dean's office.\x01",
            "It's on the first floor of this\x01",
            "building.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B46")

    label("loc_5AEC")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #236
        0x102,
        (
            "#010FIt looks like class is in session.\x02\x03",

            "Let's go to the dean's office\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B46")

    TalkEnd(0xFF)
    Return()

    # Function_24_5A54 end

    def Function_25_5B4A(): pass

    label("Function_25_5B4A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #237
        (
            "\x07\x05KEEP OUR HALLWAYS QUIET\x01\x01",
            "       --Student Council\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_5B4A end

    def Function_26_5BAE(): pass

    label("Function_26_5BAE")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x22, 0x80)
    OP_64(0x5, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #238
        "\x07\x00Found \x07\x02Ruan Economics II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33E, 1)
    OP_28(0x27, 0x1, 0x80)
    TalkEnd(0xFF)
    Return()

    # Function_26_5BAE end

    def Function_27_5C16(): pass

    label("Function_27_5C16")

    SetPlaceName(0x6F)
    Return()

    # Function_27_5C16 end

    def Function_28_5C1A(): pass

    label("Function_28_5C1A")

    SetPlaceName(0x5E)
    Return()

    # Function_28_5C1A end

    def Function_29_5C1E(): pass

    label("Function_29_5C1E")

    SetPlaceName(0x6E)
    Return()

    # Function_29_5C1E end

    def Function_30_5C22(): pass

    label("Function_30_5C22")

    SetPlaceName(0x74)
    Return()

    # Function_30_5C22 end

    def Function_31_5C26(): pass

    label("Function_31_5C26")

    SetPlaceName(0x73)
    Return()

    # Function_31_5C26 end

    SaveToFile()

Try(main)
