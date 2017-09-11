from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1122   ._SN',
        MapName             = 'Bose',
        Location            = 'T1122.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1122   ._SN',
            'ED6_DT01/T1122_1 ._SN',
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
        'Buck',                                 # 9
        'Trayton',                              # 10
        'Felicia',                              # 11
        'Pomme',                                # 12
        'Spence',                               # 13
        'Katrina',                              # 14
        'Paul',                                 # 15
        'Minuet',                               # 16
        'Lyril',                                # 17
        'Carol',                                # 18
        'Libro',                                # 19
        'Gantz',                                # 20
        'Claire',                               # 21
        'Meissen',                              # 22
        'Emmy',                                 # 23
        'Seagaro',                              # 24
        'Edel',                                 # 25
        'Marco',                                # 26
        'Simon',                                # 27
        'Young Woman',                          # 28
        'Mirano',                               # 29
        'Lila',                                 # 30
        'Sarah',                                # 31
        'Dorothy',                              # 32
        'Finel',                                # 33
        'Olivier',                              # 34
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH02490 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH01010 ._CH',             # 07
        'ED6_DT07/CH01070 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
        'ED6_DT07/CH01270 ._CH',             # 0B
        'ED6_DT07/CH01150 ._CH',             # 0C
        'ED6_DT07/CH01200 ._CH',             # 0D
        'ED6_DT07/CH01050 ._CH',             # 0E
        'ED6_DT07/CH01040 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01043 ._CH',             # 11
        'ED6_DT07/CH01100 ._CH',             # 12
        'ED6_DT07/CH02360 ._CH',             # 13
        'ED6_DT07/CH01140 ._CH',             # 14
        'ED6_DT07/CH01230 ._CH',             # 15
        'ED6_DT07/CH01350 ._CH',             # 16
        'ED6_DT06/CH20063 ._CH',             # 17
        'ED6_DT07/CH02370 ._CH',             # 18
        'ED6_DT07/CH01040 ._CH',             # 19
        'ED6_DT06/CH20064 ._CH',             # 1A
        'ED6_DT07/CH00030 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH02490P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH01010P._CP',             # 07
        'ED6_DT07/CH01070P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
        'ED6_DT07/CH01270P._CP',             # 0B
        'ED6_DT07/CH01150P._CP',             # 0C
        'ED6_DT07/CH01200P._CP',             # 0D
        'ED6_DT07/CH01050P._CP',             # 0E
        'ED6_DT07/CH01040P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01043P._CP',             # 11
        'ED6_DT07/CH01100P._CP',             # 12
        'ED6_DT07/CH02360P._CP',             # 13
        'ED6_DT07/CH01140P._CP',             # 14
        'ED6_DT07/CH01230P._CP',             # 15
        'ED6_DT07/CH01350P._CP',             # 16
        'ED6_DT06/CH20063P._CP',             # 17
        'ED6_DT07/CH02370P._CP',             # 18
        'ED6_DT07/CH01040P._CP',             # 19
        'ED6_DT06/CH20064P._CP',             # 1A
        'ED6_DT07/CH00030P._CP',             # 1B
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = -12700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 8500,
        Z                   = 0,
        Y                   = -8300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 4100,
        Z                   = 0,
        Y                   = 13650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 8250,
        Z                   = 0,
        Y                   = 13600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 9300,
        Z                   = 0,
        Y                   = 6900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -13400,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -16700,
        Z                   = 0,
        Y                   = -8600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -13600,
        Z                   = 0,
        Y                   = 10700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -9150,
        Z                   = -1000,
        Y                   = 340,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 0,
        Y                   = -5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -11100,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -18120,
        Z                   = 0,
        Y                   = 5130,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = 12500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = -1000,
        Y                   = 1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -7700,
        Z                   = 0,
        Y                   = 14700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -15200,
        Z                   = 0,
        Y                   = 15700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 6610,
        Z                   = 0,
        Y                   = 2340,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 700,
        Z                   = -1000,
        Y                   = 4900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 350,
        Z                   = -1000,
        Y                   = 480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 6400,
        Z                   = 0,
        Y                   = 7700,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 12300,
        Z                   = 0,
        Y                   = -8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 7180,
        Z                   = 0,
        Y                   = 540,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -1430,
        Z                   = 0,
        Y                   = 9040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = -12050,
        Z                   = 0,
        Y                   = -2230,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )


    DeclActor(
        TriggerX            = 7540,
        TriggerZ            = 0,
        TriggerY            = 6450,
        TriggerRange        = 400,
        ActorX              = 9300,
        ActorZ              = 1500,
        ActorY              = 6900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6830,
        TriggerZ            = 0,
        TriggerY            = -8820,
        TriggerRange        = 400,
        ActorX              = 8360,
        ActorZ              = 1500,
        ActorY              = -8430,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15120,
        TriggerZ            = 0,
        TriggerY            = -8860,
        TriggerRange        = 400,
        ActorX              = -16700,
        ActorZ              = 1500,
        ActorY              = -8600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_536",          # 00, 0
        "Function_1_7D1",          # 01, 1
        "Function_2_7EE",          # 02, 2
        "Function_3_804",          # 03, 3
        "Function_4_851",          # 04, 4
        "Function_5_8FC",          # 05, 5
        "Function_6_920",          # 06, 6
        "Function_7_944",          # 07, 7
        "Function_8_9B4",          # 08, 8
        "Function_9_B19",          # 09, 9
        "Function_10_B3D",         # 0A, 10
        "Function_11_B42",         # 0B, 11
        "Function_12_1667",        # 0C, 12
        "Function_13_166C",        # 0D, 13
        "Function_14_2049",        # 0E, 14
        "Function_15_28D9",        # 0F, 15
        "Function_16_2ECE",        # 10, 16
        "Function_17_2F4E",        # 11, 17
        "Function_18_311E",        # 12, 18
        "Function_19_3B7D",        # 13, 19
        "Function_20_3B82",        # 14, 20
        "Function_21_4888",        # 15, 21
        "Function_22_488D",        # 16, 22
        "Function_23_55FE",        # 17, 23
        "Function_24_6277",        # 18, 24
        "Function_25_68F6",        # 19, 25
        "Function_26_70D9",        # 1A, 26
        "Function_27_77AC",        # 1B, 27
        "Function_28_7DD0",        # 1C, 28
        "Function_29_85A8",        # 1D, 29
        "Function_30_8CAC",        # 1E, 30
        "Function_31_9322",        # 1F, 31
        "Function_32_9659",        # 20, 32
        "Function_33_9C89",        # 21, 33
        "Function_34_A09D",        # 22, 34
        "Function_35_A287",        # 23, 35
        "Function_36_A43A",        # 24, 36
        "Function_37_A56F",        # 25, 37
        "Function_38_A6FB",        # 26, 38
        "Function_39_AA69",        # 27, 39
        "Function_40_AC53",        # 28, 40
        "Function_41_AD69",        # 29, 41
        "Function_42_B869",        # 2A, 42
    )


    def Function_0_536(): pass

    label("Function_0_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_580")
    SetChrPos(0x10, 1100, 0, -7600, 0)
    ClearChrFlags(0x12, 0x10)
    SetChrPos(0x13, -14500, 0, 4500, 90)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_7A2")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5DB")
    SetChrPos(0x10, 1100, 0, -7600, 0)
    ClearChrFlags(0x12, 0x10)
    SetChrPos(0x13, -14500, 0, 4500, 90)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -19400, 0, 3600, 180)
    Jump("loc_7A2")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_64B")
    SetChrPos(0x12, -12200, 0, 14900, 225)
    SetChrPos(0x16, 5000, 0, 4700, 315)
    SetChrPos(0x13, -11680, 0, -2590, 315)
    SetChrPos(0x17, -7400, -1000, -320, 90)
    SetChrPos(0x18, -7400, 0, 900, 90)
    SetChrPos(0x10, 1100, 0, -7600, 0)
    Jump("loc_7A2")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_6CD")
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x10, 1100, 0, -7600, 0)
    SetChrPos(0x16, -11800, 0, 7900, 315)
    SetChrPos(0x12, -12200, 0, 14900, 225)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrPos(0x18, -15400, 0, 8900, 45)
    SetChrPos(0x17, -13100, 0, 5900, 315)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_7A2")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_72F")
    SetChrPos(0x10, 1100, 0, -7600, 0)
    SetChrPos(0x16, 6500, 0, -7100, 90)
    SetChrFlags(0x18, 0x10)
    SetChrPos(0x18, -14500, 0, -6300, 270)
    SetChrPos(0x17, -11700, 0, -7190, 215)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_7A2")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_77D")
    ClearChrFlags(0x12, 0x10)
    SetChrChipByIndex(0x1F, 26)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -11600, 0, -7100, 225)
    SetChrChipByIndex(0x17, 17)
    OP_44(0x17, 0xFF)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x10)
    SetChrPos(0x17, -8600, 0, 8600, 0)
    Jump("loc_7A2")

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7A2")
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)

    label("loc_7A2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_7BA"),
        (101, "loc_7BA"),
        (102, "loc_7BA"),
        (103, "loc_7BA"),
        (SWITCH_DEFAULT, "loc_7D0"),
    )


    label("loc_7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CD")
    OP_A2(0x30B)
    Event(0, 41)

    label("loc_7CD")

    Jump("loc_7D0")

    label("loc_7D0")

    Return()

    # Function_0_536 end

    def Function_1_7D1(): pass

    label("Function_1_7D1")

    SoundDistance(0x1CB, 0xFFFFEF98, 0xFFFFFC18, 0x276, 0x7D0, 0x61A8, 0x64, 0x0)
    Return()

    # Function_1_7D1 end

    def Function_2_7EE(): pass

    label("Function_2_7EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_803")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7EE")

    label("loc_803")

    Return()

    # Function_2_7EE end

    def Function_3_804(): pass

    label("Function_3_804")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_850")
    OP_8E(0xFE, 0x1798, 0x0, 0x3520, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x203A, 0x0, 0x3520, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_3_804")

    label("loc_850")

    Return()

    # Function_3_804 end

    def Function_4_851(): pass

    label("Function_4_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_87E")

    label("loc_858")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87B")
    OP_8D(0xFE, -800, -7100, 4200, -8700, 2000)
    Jump("loc_858")

    label("loc_87B")

    Jump("loc_8FB")

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_8AB")

    label("loc_885")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A8")
    OP_8D(0xFE, -800, -7100, 4200, -8700, 2000)
    Jump("loc_885")

    label("loc_8A8")

    Jump("loc_8FB")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_8D8")

    label("loc_8B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D5")
    OP_8D(0xFE, -800, -7100, 4200, -8700, 2000)
    Jump("loc_8B2")

    label("loc_8D5")

    Jump("loc_8FB")

    label("loc_8D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FB")
    OP_8D(0xFE, -10160, 3020, -8050, -1770, 2000)
    Jump("loc_8D8")

    label("loc_8FB")

    Return()

    # Function_4_851 end

    def Function_5_8FC(): pass

    label("Function_5_8FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91F")
    OP_8D(0xFE, 6800, -2300, 4700, -12100, 2000)
    Jump("Function_5_8FC")

    label("loc_91F")

    Return()

    # Function_5_8FC end

    def Function_6_920(): pass

    label("Function_6_920")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_943")
    OP_8D(0xFE, 200, 14800, -7900, 10300, 2000)
    Jump("Function_6_920")

    label("loc_943")

    Return()

    # Function_6_920 end

    def Function_7_944(): pass

    label("Function_7_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_971")

    label("loc_94B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96E")
    OP_8D(0xFE, 6700, 3600, 4600, -9900, 2000)
    Jump("loc_94B")

    label("loc_96E")

    Jump("loc_9B3")

    label("loc_971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_990")

    label("loc_978")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_978")

    label("loc_98D")

    Jump("loc_9B3")

    label("loc_990")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B3")
    OP_8D(0xFE, 2100, 4700, -900, -5100, 2000)
    Jump("loc_990")

    label("loc_9B3")

    Return()

    # Function_7_944 end

    def Function_8_9B4(): pass

    label("Function_8_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_9D3")

    label("loc_9BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_9BB")

    label("loc_9D0")

    Jump("loc_B18")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_AF5")

    label("loc_9DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF2")
    OP_8E(0xFE, 0xFFFFC75C, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFC7C0, 0x0, 0xFFFFF510, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBD98, 0x0, 0xFFFFF510, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB94C, 0x0, 0xFFFFDF30, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBFF0, 0x0, 0xFFFFD24C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 200)
    Sleep(4000)
    OP_8E(0xFE, 0xFFFFBFF0, 0x0, 0xFFFFCC70, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFD2B0, 0x0, 0xFFFFCEC8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(4000)
    OP_8E(0xFE, 0xFFFFDECC, 0x0, 0xFFFFCEC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDECC, 0x0, 0xFFFFD954, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFCC70, 0x0, 0xFFFFDC74, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC75C, 0x0, 0xFFFFE764, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 200)
    Sleep(5000)
    Jump("loc_9DA")

    label("loc_AF2")

    Jump("loc_B18")

    label("loc_AF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B18")
    OP_8D(0xFE, -12100, 16600, -16600, 14400, 2000)
    Jump("loc_AF5")

    label("loc_B18")

    Return()

    # Function_8_9B4 end

    def Function_9_B19(): pass

    label("Function_9_B19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3C")
    OP_8D(0xFE, -100, 500, 2300, 6000, 2000)
    Jump("Function_9_B19")

    label("loc_B3C")

    Return()

    # Function_9_B19 end

    def Function_10_B3D(): pass

    label("Function_10_B3D")

    Call(0, 11)
    Return()

    # Function_10_B3D end

    def Function_11_B42(): pass

    label("Function_11_B42")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA2")
    OP_0D()
    OP_A9(0x11)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_BA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB3")
    TalkEnd(0x8)
    Return()

    label("loc_BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C29")
    OP_A2(0x0)

    ChrTalk(    #0
        0x8,
        (
            "So I hear the sky bandits were\x01",
            "finally arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "They sure caused us a lot of trouble!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C83")

    label("loc_C29")


    ChrTalk(    #2
        0x8,
        "The sky bandits, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "No matter the circumstances, it's\x01",
            "never okay to steal!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C83")

    Jump("loc_1663")

    label("loc_C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_D75")

    ChrTalk(    #4
        0x8,
        (
            "The barricades on the roads have been\x01",
            "lifted and though it's only the westward\x01",
            "bound airliner, flights have resumed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "Business has started to pick\x01",
            "up here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "All right then, now it's time to get\x01",
            "down to work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4D")
    OP_A2(0x0)

    ChrTalk(    #7
        0x8,
        (
            "The westward bound airliner has\x01",
            "finally resumed flights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Now I'll finally be able to stock up\x01",
            "on vegetables from Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "All right, now it's time to stock up\x01",
            "and sell, sell, sell!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF2")

    label("loc_E4D")


    ChrTalk(    #10
        0x8,
        (
            "I'm confident in my ability to judge\x01",
            "good vegetables from bad ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "Those ones from Perzel Farm are\x01",
            "especially top-quality. Sales here\x01",
            "couldn't be better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    Jump("loc_1663")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_F9A")

    ChrTalk(    #12
        0x8,
        (
            "I get all my fruit from Ravennue\x01",
            "Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "The village used to be a thriving place\x01",
            "from its mining industry, but now it's\x01",
            "known for its orchards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_113C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A2")
    OP_A2(0x0)

    ChrTalk(    #14
        0x8,
        (
            "Bose merchants are said to like\x01",
            "an atmosphere of freedom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "And for that reason alone, there was\x01",
            "a time where each did as they liked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "But the previous mayor, and now\x01",
            "his daughter, have started bringing\x01",
            "all the merchants together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1139")

    label("loc_10A2")


    ChrTalk(    #17
        0x8,
        (
            "It looks like inspections along the\x01",
            "Eisen Road have been terminated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "Now I'll be able to start getting my\x01",
            "selection of goods back to normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1139")

    Jump("loc_1663")

    label("loc_113C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_13FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133D")
    OP_A2(0x0)

    ChrTalk(    #19
        0x8,
        (
            "When you start a business here\x01",
            "you can receive aid from the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#000FWow, Bose is really a city of commerce\x01",
            "just like everyone says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#020FYeah, that's because since Mayor\x01",
            "Maybelle's father's time the city\x01",
            "has supported this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "The reason we've all been able to have\x01",
            "our own stores like this is because of\x01",
            "the late mayor, Maybelle's father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "Yet I regret to say I've caused a bit\x01",
            "of trouble for the mayor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "I've brought disgrace upon the\x01",
            "merchants of Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FA")

    label("loc_133D")


    ChrTalk(    #25
        0x8,
        (
            "When you start a business here\x01",
            "you can receive aid from the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "The reason we've all been able to have\x01",
            "our own stores like this is because of\x01",
            "the late mayor, Maybelle's father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_1663")

    label("loc_13FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BB")
    OP_A2(0x0)

    ChrTalk(    #27
        0x8,
        (
            "Thanks to the restrictions placed\x01",
            "on everything by the army,\x01",
            "nothing has gone right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "When I think about the price of\x01",
            "getting things in stock, I feel like\x01",
            "my business is going to dry up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#002F(Th-This guy's in a rather foul mood.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#012F(No kidding. Airliner flights have been\x01",
            "canceled and the Eisen Road has\x01",
            "been blockaded off...)\x02\x03",

            "(I'm sure it's not doing wonders for\x01",
            "these merchants' businesses either.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_15BB")


    ChrTalk(    #31
        0x8,
        (
            "After all my hard work and just when\x01",
            "sales were starting to take off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "I guess the only thing I can do now\x01",
            "is just raise prices myself if I want\x01",
            "to survive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1663")

    TalkEnd(0x8)
    Return()

    # Function_11_B42 end

    def Function_12_1667(): pass

    label("Function_12_1667")

    Call(0, 13)
    Return()

    # Function_12_1667 end

    def Function_13_166C(): pass

    label("Function_13_166C")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CC")
    OP_0D()
    OP_A9(0x10)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_16CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16DD")
    TalkEnd(0x9)
    Return()

    label("loc_16DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_184F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BC")
    OP_A2(0x1)

    ChrTalk(    #33
        0x9,
        (
            "I'm thinking about stocking fish\x01",
            "from Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "They've always had a reputation for\x01",
            "bringing in the largest catch in the\x01",
            "entire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        (
            "That's what a seaport city will get\x01",
            "you, I suppose...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184C")

    label("loc_17BC")


    ChrTalk(    #36
        0x9,
        (
            "I'm thinking about stocking fish\x01",
            "from Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "They've always had a reputation for \x01",
            "bringing in the largest catch in the\x01",
            "entire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184C")

    Jump("loc_2045")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1926")

    ChrTalk(    #38
        0x9,
        (
            "A missing airliner and now a string of\x01",
            "burglaries...there sure is a lot of\x01",
            "disturbing news these days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "But luckily for us, Mayor Maybelle runs\x01",
            "this city. I'm sure she'll do something\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_1926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_19AF")

    ChrTalk(    #40
        0x9,
        (
            "I hear there were some burglaries\x01",
            "in the south block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "All of the well-established shops\x01",
            "are situated on that street.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0B")
    OP_A2(0x1)

    ChrTalk(    #42
        0x9,
        (
            "The top dogs here in Bose, aside from\x01",
            "the mayor, would have to be Trino and\x01",
            "Borden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "However, recently Trino's daughter has\x01",
            "been extending her sphere of influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "Let's see... If I remember right, her name\x01",
            "is Mirano.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "Anyway, she appears to have a knack\x01",
            "for business and can hold her own\x01",
            "against her father.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1B0B")


    ChrTalk(    #46
        0x9,
        (
            "That's pretty cool to see a sharp pair\x01",
            "of merchants in a family like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "Oh, I almost forgot to mention Mirano\x01",
            "and the mayor are pretty good friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAD")

    Jump("loc_2045")

    label("loc_1BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D52")
    OP_A2(0x1)

    ChrTalk(    #48
        0x9,
        (
            "Buck and I came to Bose to\x01",
            "make it big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "In the future, it's our dream to open\x01",
            "a huge food market together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "It will have the freshest foods at the\x01",
            "lowest prices in town all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "Doesn't that sound like the kind of\x01",
            "food market you'd like to shop at?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "And with the way distribution has changed\x01",
            "thanks to the advent of airliners, I'm sure\x01",
            "we can make our dream a reality.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC7")

    label("loc_1D52")


    ChrTalk(    #53
        0x9,
        (
            "Buck and I came to Bose to\x01",
            "make it big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "In the future, it's our dream to open\x01",
            "a huge food market together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC7")

    Jump("loc_2045")

    label("loc_1DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8E")
    OP_A2(0x1)

    ChrTalk(    #55
        0x9,
        "We had only thought about profit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "Mayor Maybelle was exactly\x01",
            "right about us when she got\x01",
            "angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "We were on the verge of straying\x01",
            "from the path of a merchant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFA")

    label("loc_1E8E")


    ChrTalk(    #58
        0x9,
        "We had only thought about profit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "We were on the verge of straying\x01",
            "from the path of a merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFA")

    Jump("loc_2045")

    label("loc_1EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2045")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC7")
    OP_A2(0x1)

    ChrTalk(    #60
        0x9,
        (
            "My pal Buck has started raising prices\x01",
            "on his goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "But in light of the situation, I guess\x01",
            "I can understand why...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "Although, some of his prices seem\x01",
            "a bit TOO high.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_1FC7")


    ChrTalk(    #63
        0x9,
        (
            "My pal Buck has started raising prices\x01",
            "on his goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "But in light of the situation, I guess\x01",
            "I can understand why...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2045")

    TalkEnd(0x9)
    Return()

    # Function_13_166C end

    def Function_14_2049(): pass

    label("Function_14_2049")

    TalkBegin(0xA)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A9")
    OP_0D()
    OP_A9(0x13)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_20A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20BA")
    TalkEnd(0xA)
    Return()

    label("loc_20BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_220F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219C")
    OP_A2(0x2)

    ChrTalk(    #65
        0xFE,
        "I swear, my husband never changes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "He started this business so that\x01",
            "we could live together in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "If he's got a reason why he backed\x01",
            "out at the last minute, he should\x01",
            "be clear about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_219C")


    ChrTalk(    #68
        0xFE,
        "I swear, my husband never changes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "He started this business so that\x01",
            "we could live together in Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220C")

    Jump("loc_28D5")

    label("loc_220F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_22BD")

    ChrTalk(    #70
        0xFE,
        (
            "It would be nice if he worried about\x01",
            "us for once and showed his mug\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Sometimes he can be a real jerk.\x01",
            "I wonder why I chose him to begin\x01",
            "with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D5")

    label("loc_22BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2402")
    OP_A2(0x2)

    ChrTalk(    #72
        0xFE,
        (
            "My husband was the one who said,\x01",
            "'Let's start this business,'\x01",
            "to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Then right at the last minute,\x01",
            "he shoved everything on me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "...and ran back to the village by himself,\x01",
            "leaving me to shoulder the burden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "What in the world was he thinking\x01",
            "when he cut and ran like that...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2495")

    label("loc_2402")


    ChrTalk(    #76
        0xFE,
        (
            "My husband was the one who said,\x01",
            "'Let's start this business,' to begin\x01",
            "with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "But then he threw it all on me\x01",
            "and ran back to the village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2495")

    Jump("loc_28D5")

    label("loc_2498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_255F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2517")
    OP_A2(0x2)

    ChrTalk(    #78
        0xFE,
        "Whew, I'm ready for a breather.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I wonder how my husband's getting\x01",
            "along back at the village...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255C")

    label("loc_2517")


    ChrTalk(    #80
        0xFE,
        (
            "I wonder how my husband's getting\x01",
            "along back at the village...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255C")

    Jump("loc_28D5")

    label("loc_255F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_262C")

    ChrTalk(    #81
        0xFE,
        (
            "There have been a lot of strange\x01",
            "things to deal with since I\x01",
            "expanded the store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "But my son, Pomme, has been\x01",
            "really helping me out a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "I couldn't have asked for a better kid.\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D5")

    label("loc_262C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_26AC")

    ChrTalk(    #84
        0xFE,
        (
            "All of my products are made with\x01",
            "a woman's touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "And they're just as good as anyone\x01",
            "else's, if not better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D5")

    label("loc_26AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_28D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288A")
    OP_A2(0x2)

    ChrTalk(    #86
        0xFE,
        "#4SGood day and welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "HEY THERE, YOU TWO! HAVE A\x01",
            "LOOK AT MY GOODS! I HAVE\x01",
            "EVERYTHING YOU NEED!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(700)

    ChrTalk(    #88
        0x101,
        (
            "#004FEeeek! What the-?!\x01",
            "S-So loud! My ears...they bleed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#010FWell, this place is alive and bustling\x01",
            "like everyone says. I wonder if it's\x01",
            "like this all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        (
            "#020FIt is.\x02\x03",

            "People from all corners of Liberl gather\x01",
            "here to grow their businesses.\x02\x03",

            "And their eagerness and zeal to\x01",
            "succeed is nothing to be balked at.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D5")

    label("loc_288A")


    ChrTalk(    #91
        0xFE,
        (
            "If you see anything you like, please\x01",
            "feel free to take a closer look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D5")

    TalkEnd(0xA)
    Return()

    # Function_14_2049 end

    def Function_15_28D9(): pass

    label("Function_15_28D9")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2930")

    ChrTalk(    #92
        0xFE,
        (
            "I wonder what my father is doing right\x01",
            "now back in Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_2930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_29E5")

    ChrTalk(    #93
        0xFE,
        (
            "I'm pretty sure my father had his\x01",
            "reasons for returning to the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "The reason being, he was the one\x01",
            "who was looking forward to\x01",
            "opening the shop the most...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_29E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2A63")

    ChrTalk(    #95
        0xFE,
        (
            "I wonder if my mother wants\x01",
            "to see my father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Sometimes, I can see this look\x01",
            "of loneliness in her face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_2A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2B64")

    ChrTalk(    #97
        0xFE,
        (
            "My father's growing fruit back\x01",
            "at the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "The fruit we're selling here may be\x01",
            "some of the fruit that my father grew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Originally, we were supposed to be\x01",
            "running this business together as a\x01",
            "family, but he chose to stay behind...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_2B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5D")
    OP_A2(0x3)

    ChrTalk(    #100
        0xFE,
        (
            "My mother is very rough in the\x01",
            "way she handles dishes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "My heart always skips a beat every\x01",
            "time I see her pick one up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Since these are the goods we're\x01",
            "supposed to be selling she should\x01",
            "be more careful with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CDF")

    label("loc_2C5D")


    ChrTalk(    #103
        0xFE,
        (
            "My mother is very rough in the\x01",
            "way she handles dishes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "My heart always skips a beat every\x01",
            "time I see her pick one up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDF")

    Jump("loc_2ECA")

    label("loc_2CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DEC")
    OP_A2(0x3)

    ChrTalk(    #105
        0xFE,
        (
            "The mayor just stopped by a minute\x01",
            "ago and gave us some advice on\x01",
            "how to run our business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "She was even kind enough to teach\x01",
            "me about setting out goods and how\x01",
            "to address customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "And after that, she bought some\x01",
            "dishes from us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2E")

    label("loc_2DEC")


    ChrTalk(    #108
        0xFE,
        (
            "The mayor sometimes stops by to\x01",
            "see how the market is doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2E")

    Jump("loc_2ECA")

    label("loc_2E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2ECA")

    ChrTalk(    #109
        0xFE,
        (
            "Tentatively speaking, I'm an employee\x01",
            "here at this store. I help out my mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "I'm not playing around, just in case\x01",
            "you are wondering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ECA")

    TalkEnd(0xB)
    Return()

    # Function_15_28D9 end

    def Function_16_2ECE(): pass

    label("Function_16_2ECE")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2E")
    OP_0D()
    TalkBegin(0xC)
    OP_A9(0xC)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_2F2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F3F")
    TalkEnd(0xC)
    Return()

    label("loc_2F3F")

    OP_A2(0x6)
    Call(0, 17)
    OP_8C(0xC, 270, 0)
    Return()

    # Function_16_2ECE end

    def Function_17_2F4E(): pass

    label("Function_17_2F4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2FE3")
    TalkBegin(0xC)

    ChrTalk(    #111
        0xC,
        (
            "I appreciate you all helping me\x01",
            "out like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xC,
        (
            "Now, I'll be able to work on formulating\x01",
            "new medicine without worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE7")

    label("loc_2FE3")

    Call(0, 18)

    label("loc_2FE7")

    Jump("loc_3113")

    label("loc_2FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x1, 0x4000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_303B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_302C")
    Call(1, 2)
    OP_8C(0xC, 270, 0)
    Return()

    label("loc_302C")

    Call(1, 1)
    OP_8C(0xC, 270, 0)
    Return()

    label("loc_303B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3066")
    Call(1, 1)
    OP_8C(0xC, 270, 0)
    Return()

    label("loc_3066")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_3100")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_30F9")
    TalkBegin(0xC)

    ChrTalk(    #113
        0xC,
        (
            "All right, everyone, I'm looking\x01",
            "forward to hearing some good\x01",
            "news from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        "But whatever you do, please be safe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30FD")

    label("loc_30F9")

    Call(0, 18)

    label("loc_30FD")

    Jump("loc_310C")

    label("loc_3100")

    Call(1, 0)
    OP_8C(0xC, 270, 0)
    Return()

    label("loc_310C")

    Jump("loc_3113")

    label("loc_310F")

    Call(0, 18)

    label("loc_3113")

    TalkEnd(0xC)
    OP_8C(0xC, 270, 0)
    Return()

    # Function_17_2F4E end

    def Function_18_311E(): pass

    label("Function_18_311E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E4")
    OP_A2(0x4)

    ChrTalk(    #115
        0xC,
        (
            "It appears that those evil cretins who\x01",
            "were causing a ruckus here in Bose\x01",
            "finally got what's coming to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        (
            "Now I can get back to my business\x01",
            "without any worries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3244")

    label("loc_31E4")


    ChrTalk(    #117
        0xC,
        (
            "With those evil cretins in the slammer,\x01",
            "I can get back to my business without\x01",
            "any worries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3244")

    Jump("loc_3B6F")

    label("loc_3247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_33DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3350")
    OP_A2(0x4)

    ChrTalk(    #118
        0xC,
        (
            "My shop has been gradually getting\x01",
            "busier and busier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xC,
        (
            "I've been thinking about hiring \x01",
            "somebody...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        (
            "But I always enjoy connecting with\x01",
            "customers face-to-face...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "That's kind of what's got me hung\x01",
            "up about hiring anybody else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33DB")

    label("loc_3350")


    ChrTalk(    #122
        0xC,
        (
            "I've been thinking about hiring\x01",
            "somebody...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xC,
        (
            "But I enjoy connecting with customers\x01",
            "face-to-face and that's what's got me\x01",
            "hung up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33DB")

    Jump("loc_3B6F")

    label("loc_33DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_346B")

    ChrTalk(    #124
        0xC,
        (
            "It looks like we've got some members of\x01",
            "the Royal Army here in the market...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xC,
        (
            "I wonder if there was some sort\x01",
            "of trouble?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B6F")

    label("loc_346B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_3606")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3549")
    OP_A2(0x4)

    ChrTalk(    #126
        0xC,
        (
            "Even if the airliners aren't running,\x01",
            "a true Bose merchant won't get\x01",
            "discouraged so easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xC,
        (
            "How should I put it? A real Bose\x01",
            "merchant knows how to innovate\x01",
            "at times like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        "Ho ho ho.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_3549")


    ChrTalk(    #129
        0xC,
        (
            "Even if the airliners aren't running,\x01",
            "a true Bose merchant won't get\x01",
            "discouraged so easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xC,
        (
            "How should I put it? A real Bose\x01",
            "merchant knows how to innovate\x01",
            "at times like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3603")

    Jump("loc_3B6F")

    label("loc_3606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3701")
    OP_A2(0x4)

    ChrTalk(    #131
        0xC,
        (
            "I formulate medicine for each\x01",
            "one of my customers according\x01",
            "to their symptoms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xC,
        (
            "I've even recently started carrying\x01",
            "Eastern medicine, which has\x01",
            "grown in popularity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xC,
        (
            "Innovation is important when it\x01",
            "comes to business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AF")

    label("loc_3701")


    ChrTalk(    #134
        0xC,
        (
            "I formulate medicine for each\x01",
            "one of my customers according\x01",
            "to their symptoms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        (
            "I've even recently started carrying\x01",
            "Eastern medicine, which has\x01",
            "grown in popularity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AF")

    Jump("loc_3B6F")

    label("loc_37B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_39D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3962")
    OP_A2(0x4)

    ChrTalk(    #136
        0xC,
        (
            "Each month one shop in the market\x01",
            "receives an award from the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xC,
        (
            "And last month my shop was chosen\x01",
            "for being the most scrupulous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xC,
        (
            "Now I just feel like working all\x01",
            "the harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#020FInteresting. It looks like the mayor's got\x01",
            "her own ideas about how to make the\x01",
            "economy grow here in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#010FYeah, she may be young, but you\x01",
            "can definitely see that she's\x01",
            "really supporting the market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D6")

    label("loc_3962")


    ChrTalk(    #141
        0xC,
        (
            "Last month my shop was chosen\x01",
            "for being the most scrupulous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xC,
        (
            "Now I just feel like working\x01",
            "all the harder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D6")

    Jump("loc_3B6F")

    label("loc_39D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3B6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1D")
    OP_A2(0x4)

    ChrTalk(    #143
        0xC,
        "Can I help you find something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xC,
        (
            "My medicine can take care of\x01",
            "almost any kind of ailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#004FSo you sell medicine,\x01",
            "huh?\x02\x03",

            "There seems to be almost anything\x01",
            "one could ever want here in the\x01",
            "Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        (
            "#010FThat's for sure... The sheer amount of\x01",
            "stuff for sale is pretty overwhelming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B6F")

    label("loc_3B1D")


    ChrTalk(    #147
        0xC,
        (
            "Can I help you find something?\x01",
            "My medicine can take care of\x01",
            "almost anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B6F")

    OP_A3(0x6)
    TalkEnd(0xC)
    OP_8C(0xC, 270, 0)
    Return()

    # Function_18_311E end

    def Function_19_3B7D(): pass

    label("Function_19_3B7D")

    Call(0, 20)
    Return()

    # Function_19_3B7D end

    def Function_20_3B82(): pass

    label("Function_20_3B82")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE2")
    OP_0D()
    OP_A9(0x12)
    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_3BE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BF3")
    TalkEnd(0xD)
    Return()

    label("loc_3BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D82")
    OP_A2(0x7)

    ChrTalk(    #148
        0xD,
        (
            "My fiance, who was taken hostage\x01",
            "by the sky bandits, has finally\x01",
            "come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        (
            "But now he's decided to set up\x01",
            "a store of his own!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xD,
        (
            "He seems to be a bit frustrated\x01",
            "that this store got off the ground\x01",
            "without him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        (
            "Teehee! He's as stubborn\x01",
            "and competitive as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xD,
        (
            "I guess that means I'm going to be\x01",
            "competing with him from now on,\x01",
            "so I'll have to work harder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E26")

    label("loc_3D82")


    ChrTalk(    #153
        0xD,
        (
            "Teehee! My fiance is as\x01",
            "stubborn and competitive as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xD,
        (
            "I guess that means I'm going to be\x01",
            "competing with him from now on,\x01",
            "so I'll have to work harder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E26")

    Jump("loc_4884")

    label("loc_3E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3F92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EFF")
    OP_A2(0x7)

    ChrTalk(    #155
        0xD,
        (
            "Guess what? Customers have really\x01",
            "started pouring in and business is\x01",
            "picking up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xD,
        (
            "I'm sure my fiance is going to be\x01",
            "happy when he hears about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xD,
        "I hope he'll come back soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8F")

    label("loc_3EFF")


    ChrTalk(    #158
        0xD,
        (
            "I wonder why my fiance hasn't come\x01",
            "back yet even though the army\x01",
            "found the missing airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        (
            "I've got to work hard to make\x01",
            "him proud.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8F")

    Jump("loc_4884")

    label("loc_3F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4036")

    ChrTalk(    #160
        0xD,
        (
            "I've heard rumors that the army\x01",
            "found the missing airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "I wonder what happened to my\x01",
            "fiance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xD,
        "And what about the other passengers...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4884")

    label("loc_4036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_43B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_40CE")

    ChrTalk(    #163
        0xD,
        (
            "Welcome! Can I help you find\x01",
            "anything today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xD,
        (
            "How about a fluffy, eggy sponge cake?\x01",
            "It's a specialty here at the Bose Market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B6")

    label("loc_40CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4341")
    OP_A2(0x8)

    ChrTalk(    #165
        0xD,
        (
            "My fiance was actually the one\x01",
            "who started this store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xD,
        (
            "But he was aboard the airliner that\x01",
            "disappeared that everybody's\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xD,
        (
            "I truly believe in my heart that he'll\x01",
            "come back safely, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xD,
        (
            "And until he returns, I have to\x01",
            "keep this store alive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #170
        0x102,
        "#012FEstelle, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#002FYou know...she's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        "#014FHuh? How so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#003FIt's not only someone from our family\x01",
            "who was aboard that airliner.\x02\x03",

            "#009FWhich means I need to do my\x01",
            "best as well...\x02\x03",

            "As a member of the Bracer Guild and\x01",
            "as dad's only daughter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x102,
        (
            "#010FEstelle...\x02\x03",

            "You're right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B6")

    label("loc_4341")

    OP_A2(0x7)

    ChrTalk(    #175
        0xD,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#501F???\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #177
        0xD,
        (
            "Oh, sorry. My head's not quite\x01",
            "in the game right now. Welcome!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B6")

    Jump("loc_4884")

    label("loc_43B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_449F")

    ChrTalk(    #178
        0xD,
        (
            "Tee hee. At first I was worried about\x01",
            "how I was going to run the store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xD,
        (
            "But things finally started to sell\x01",
            "little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xD,
        (
            "So I guess the best thing I can\x01",
            "do is give my customers service\x01",
            "with a smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4884")

    label("loc_449F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_466C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B7")
    OP_A2(0x7)

    ChrTalk(    #181
        0xD,
        (
            "I recently started helping here\x01",
            "around the store, but I'm still\x01",
            "learning the ropes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xD,
        (
            "I actually still get embarrassed trying\x01",
            "to invite customers to look at our wares.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xD,
        (
            "Umm, I know I'm going to have to\x01",
            "do something to change my\x01",
            "attitude, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4669")

    label("loc_45B7")


    ChrTalk(    #184
        0xD,
        (
            "I recently started helping here\x01",
            "around the store, but I'm still\x01",
            "learning the ropes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xD,
        (
            "I actually still get embarrassed trying\x01",
            "to invite customers to look at our wares.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4669")

    Jump("loc_4884")

    label("loc_466C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4821")
    OP_A2(0x7)

    ChrTalk(    #186
        0xD,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xD,
        (
            "How about a fluffy, eggy sponge cake?\x01",
            "It's a specialty here at the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#001FWow, this looks so good, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x102,
        (
            "#010FYeah, it does have a nice smell\x01",
            "to it, doesn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #190
        0x101,
        (
            "#001FJoshua, after we find Dad, let's\x01",
            "come here and get one of these\x01",
            "to eat together, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x102,
        "#011FThat's not a bad idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#001FReally? You'd better not forget about\x01",
            "this later on, you hear me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4884")

    label("loc_4821")


    ChrTalk(    #193
        0xD,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xD,
        (
            "How about a fluffy, eggy sponge cake?\x01",
            "It's a specialty here at the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4884")

    TalkEnd(0xD)
    Return()

    # Function_20_3B82 end

    def Function_21_4888(): pass

    label("Function_21_4888")

    Call(0, 22)
    Return()

    # Function_21_4888 end

    def Function_22_488D(): pass

    label("Function_22_488D")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48ED")
    OP_0D()
    OP_A9(0x19)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_48ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48FE")
    TalkEnd(0xE)
    Return()

    label("loc_48FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4AF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A2D")
    OP_A2(0x9)

    ChrTalk(    #195
        0xE,
        (
            "With the airliners all stopped up,\x01",
            "it's kind of hard to get any new\x01",
            "clothes in stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xE,
        (
            "But on the flip side, these new original\x01",
            "store brand clothes are selling better\x01",
            "than I expected them to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xE,
        (
            "I've got to succeed with this business\x01",
            "to make a good living for my family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AF5")

    label("loc_4A2D")


    ChrTalk(    #198
        0xE,
        (
            "These new original store brand clothes\x01",
            "I began selling as an experiment are\x01",
            "doing better than I expected them to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xE,
        (
            "I've got to succeed with this business\x01",
            "to make a good living for my family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AF5")

    Jump("loc_55FA")

    label("loc_4AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD8")
    OP_A2(0x9)

    ChrTalk(    #200
        0xE,
        (
            "I wonder if my wife and daughter are\x01",
            "feeling a bit insecure right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xE,
        (
            "*sigh* When I think about them dealing with\x01",
            "another burglary, I start to feel worried\x01",
            "and can't seem to focus on my work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C38")

    label("loc_4BD8")


    ChrTalk(    #202
        0xE,
        "...I've got it! I know what to do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xE,
        (
            "I'll just close up shop for the day\x01",
            "and head home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C38")

    Jump("loc_55FA")

    label("loc_4C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D86")
    OP_A2(0x9)

    ChrTalk(    #204
        0xE,
        (
            "Some burglars broke into my house\x01",
            "last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xE,
        (
            "Unfortunately, at that time only my\x01",
            "wife and daughter were at home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xE,
        (
            "Though no harm came to them,\x01",
            "they were rather shaken up from\x01",
            "the whole ordeal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xE,
        (
            "My wife sent me off with a smile\x01",
            "this morning, but I'm still worried\x01",
            "about them and the house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E24")

    label("loc_4D86")


    ChrTalk(    #208
        0xE,
        (
            "Some burglars broke into my house\x01",
            "last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xE,
        (
            "And though my wife sent me off with\x01",
            "a smile this morning, I'm still\x01",
            "worried about them and the house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E24")

    Jump("loc_55FA")

    label("loc_4E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ECA")
    OP_A2(0x9)

    ChrTalk(    #210
        0xE,
        (
            "The clothes I designed and tailored\x01",
            "myself are selling quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xE,
        (
            "I think I'm going to try and make\x01",
            "more with numerous variations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F78")

    label("loc_4ECA")


    ChrTalk(    #212
        0xE,
        (
            "I get a lot of inquiries from my female\x01",
            "customers regarding original clothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xE,
        (
            "I think I'm going to try and design\x01",
            "some clothes, this time focused\x01",
            "solely on women.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F78")

    Jump("loc_55FA")

    label("loc_4F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_512F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5087")
    OP_A2(0x9)

    ChrTalk(    #214
        0xE,
        (
            "I'm having a hard time getting the new\x01",
            "brands I ordered from the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xE,
        (
            "And on top of that, merchandise\x01",
            "is in short supply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xE,
        (
            "I guess the only thing left to do is try\x01",
            "my hand at making some original\x01",
            "clothing and see how it goes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_512C")

    label("loc_5087")


    ChrTalk(    #217
        0xE,
        (
            "Actually, I had wanted to try selling\x01",
            "some original store brand clothes\x01",
            "from before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xE,
        (
            "I guess this is as good of an opportunity\x01",
            "as ever to give it a whirl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_512C")

    Jump("loc_55FA")

    label("loc_512F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_534E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A4")
    OP_A2(0x9)

    ChrTalk(    #219
        0xE,
        (
            "Originally, I was a commissioned\x01",
            "officer in the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xE,
        (
            "But for some reason I couldn't give\x01",
            "up my dream so I left it all behind\x01",
            "and opened up this shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xE,
        (
            "My wife fought me tooth and nail about\x01",
            "this so I've got to work hard to make\x01",
            "her understand why I chose this path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xE,
        (
            "My daughter, on the other hand, is\x01",
            "happy about my business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_534B")

    label("loc_52A4")


    ChrTalk(    #223
        0xE,
        (
            "Originally, I was a commissioned\x01",
            "officer in the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xE,
        (
            "But for some reason I couldn't give\x01",
            "up my dream so I left it all behind\x01",
            "and opened up this shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_534B")

    Jump("loc_55FA")

    label("loc_534E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_55FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5541")
    OP_A2(0x9)

    ChrTalk(    #225
        0xE,
        (
            "How are you doing today? Is there\x01",
            "anything I can help you find?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xE,
        (
            "I carry brands from the Royal City\x01",
            "here as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xE,
        (
            "If you would like, please have a\x01",
            "look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        "#010FIt looks like they sell clothes here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        (
            "#000FI'm fine, I already like the clothes\x01",
            "I'm wearing now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(    #230
        0xE,
        (
            "I can also do custom designs or\x01",
            "tailor any clothes you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xE,
        (
            "Just keep that in mind if you decide\x01",
            "you want something more fashionable\x01",
            "than your current...uh, unique outfit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55FA")

    label("loc_5541")


    ChrTalk(    #232
        0xE,
        (
            "I can also do custom designs or\x01",
            "tailor any clothes you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xE,
        (
            "Just keep that in mind if you decide\x01",
            "you want something more fashionable\x01",
            "than your current...uh, unique outfit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55FA")

    TalkEnd(0xE)
    Return()

    # Function_22_488D end

    def Function_23_55FE(): pass

    label("Function_23_55FE")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5676")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_END)), "loc_565F")
    OP_A9(0x6E)
    Jump("loc_566D")

    label("loc_565F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_566B")
    OP_A9(0x1B)
    Jump("loc_566D")

    label("loc_566B")

    OP_A9(0x1A)

    label("loc_566D")

    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_5676")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5687")
    TalkEnd(0xF)
    Return()

    label("loc_5687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_571E")

    ChrTalk(    #234
        0xFE,
        (
            "The goods that customers need often\x01",
            "change with the times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "I need to figure out what those needs\x01",
            "are and get those goods in stock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6273")

    label("loc_571E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_580B")
    OP_A2(0xA)

    ChrTalk(    #236
        0xFE,
        (
            "My supply of goods is finally back\x01",
            "to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "So now I'm thinking about using this\x01",
            "opportunity to expand my selection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "I'm not the type to pass on potential\x01",
            "profits when they come knocking on my\x01",
            "door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5862")

    label("loc_580B")


    ChrTalk(    #239
        0xFE,
        (
            "I'm not the type to pass on potential\x01",
            "profits when they come knocking on my\x01",
            "door.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5862")

    Jump("loc_6273")

    label("loc_5865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_593A")

    ChrTalk(    #240
        0xFE,
        (
            "What's that, you say? The city was\x01",
            "hit up by some burglars?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "What a despicable bunch, trying to\x01",
            "make a profit stealing from others!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "I sure hope someone hurries up\x01",
            "and catches those crooks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6273")

    label("loc_593A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_5BAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1C")
    OP_A2(0xA)

    ChrTalk(    #243
        0xFE,
        "Hi there and welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "Stop by and see what we've got\x01",
            "in stock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "Right now, on sale!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        "Believe it or not!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "We've got a luxury carpet from\x01",
            "the Calvard Republic going for\x01",
            "just 500 mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "You heard it right, just 500 mira!\x01",
            "But that's not all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "At regular price this goes for 1500 mira,\x01",
            "but the price has been reduced to an\x01",
            "amazing 500 mira! But that's not all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "If you buy now, I'll even throw in a\x01",
            "tapestry with matching patterns!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BAA")

    label("loc_5B1C")


    ChrTalk(    #251
        0xFE,
        (
            "We've got a luxury carpet from\x01",
            "the Calvard Republic going for\x01",
            "just 500 mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "You heard it right, just 500 mira!\x01",
            "But that's not all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BAA")

    Jump("loc_6273")

    label("loc_5BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_5D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CB4")
    OP_A2(0xA)

    ChrTalk(    #253
        0xFE,
        (
            "Just how long does the army\x01",
            "intend to blockade the border?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "Because of all this, all my merchandise\x01",
            "which should have come from the\x01",
            "empire hasn't arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "Whatever they're doing, it isn't helping\x01",
            "my business, that's for sure...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D58")

    label("loc_5CB4")


    ChrTalk(    #256
        0xFE,
        (
            "Just how long does the army\x01",
            "intend to blockade the border?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "Because of all this, all my merchandise\x01",
            "which should have come from the\x01",
            "empire hasn't arrived.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D58")

    Jump("loc_6273")

    label("loc_5D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_601D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F57")
    OP_A2(0xA)

    ChrTalk(    #258
        0xFE,
        (
            "I've been doing business here since\x01",
            "back in the days when this was an\x01",
            "open-air market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "In other words, I'm the most senior\x01",
            "merchant here in the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#000FSo, I guess you're a real veteran\x01",
            "here then, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "Yeah...we're talking more than 40 years\x01",
            "ago when I started up this business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "And at that time, there wasn't a wonderful\x01",
            "building here like you see now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "Bose may have changed a lot, but\x01",
            "the air of excitement you see here\x01",
            "is the one thing that hasn't.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_601A")

    label("loc_5F57")


    ChrTalk(    #264
        0xFE,
        (
            "I've been doing business here since the\x01",
            "time this place was an open-air market\x01",
            "and well before this building was built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "In other words, I'm the most senior\x01",
            "merchant here in the market.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_601A")

    Jump("loc_6273")

    label("loc_601D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_6273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61FB")
    OP_A2(0xA)

    ChrTalk(    #266
        0xFE,
        "Good day to you and welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "I carry everything from antique books\x01",
            "to textiles and daily necessities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        (
            "#000FMan, would you look at all this\x01",
            "stuff!\x02\x03",

            "Mr. Rinon's general store has lots\x01",
            "of stuff, but this one carries even\x01",
            "more than he does!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x102,
        (
            "#010FYeah, it's pretty easy to see exactly\x01",
            "why this store's here in the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "I stock a lot of imported goods from\x01",
            "the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "So I'm pretty confident about my\x01",
            "selection.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6273")

    label("loc_61FB")


    ChrTalk(    #272
        0xFE,
        (
            "I carry a lot of imported goods from\x01",
            "the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "So I'm pretty confident about my\x01",
            "selection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6273")

    TalkEnd(0xF)
    Return()

    # Function_23_55FE end

    def Function_24_6277(): pass

    label("Function_24_6277")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63AD")
    OP_A2(0xB)

    ChrTalk(    #274
        0xFE,
        (
            "Now, what was I supposed to\x01",
            "buy here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "Umm, there was onions, carrots,\x01",
            "and then...and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "Umm, there was onions, carrots,\x01",
            "and then...and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "Was I was supposed to get some kind\x01",
            "of meat too? Was it a duck...? Am I\x01",
            "supposed to get a duck?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6456")

    label("loc_63AD")


    ChrTalk(    #280
        0xFE,
        "Onions, carrots, and meat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "Maybe I could remember better if I put the\x01",
            "items I was supposed to get into a song.\x01",
            "La la la, lucky, ducky ducks...in my belly...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6456")

    Jump("loc_68F2")

    label("loc_6459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64FC")
    OP_A2(0xB)

    ChrTalk(    #282
        0xFE,
        (
            "Tee hee. I can go shopping\x01",
            "all by myself now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "Aren't you proud of me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "But I still haven't bought anything\x01",
            "besides cabbage yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6526")

    label("loc_64FC")


    ChrTalk(    #285
        0xFE,
        (
            "I've got to be more like a\x01",
            "grown-up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6526")

    Jump("loc_68F2")

    label("loc_6529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_657C")

    ChrTalk(    #286
        0xFE,
        (
            "There were a bunch of scary men\x01",
            "outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_68F2")

    label("loc_657C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_6619")

    ChrTalk(    #288
        0xFE,
        "The sponge cake looked so yummy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "It's probably not okay for me to use\x01",
            "the money I'm supposed to use for\x01",
            "these errands, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68F2")

    label("loc_6619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_67A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6719")
    OP_A2(0xB)

    ChrTalk(    #291
        0xFE,
        (
            "Cabbage, cabbage...that's what my mom\x01",
            "asked me to pick up for her. And a duck.\x01",
            "Delicious, delicious duck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "But I'm too scared to talk to\x01",
            "people I don't know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "That's why I've been pacing in front\x01",
            "of the store like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A1")

    label("loc_6719")


    ChrTalk(    #294
        0xFE,
        "I know! Maybe I should practice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "One head of cabbage, please...\x01",
            "One head of cabbage, please...\x01",
            "One head of cabbage, please...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67A1")

    Jump("loc_68F2")

    label("loc_67A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_6856")

    ChrTalk(    #296
        0xFE,
        (
            "*sniffle* I forgot what I was\x01",
            "supposed to buy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "And this is after my mom let me\x01",
            "come here all by myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "Maybe I should just go home\x01",
            "and ask again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68F2")

    label("loc_6856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_68F2")

    ChrTalk(    #299
        0xFE,
        (
            "Tee hee. This is the first time I've\x01",
            "ever been allowed to go on an\x01",
            "errand all by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "Umm, let's see... Now what was I\x01",
            "supposed to buy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68F2")

    TalkEnd(0x10)
    Return()

    # Function_24_6277 end

    def Function_25_68F6(): pass

    label("Function_25_68F6")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69CD")
    OP_A2(0xC)

    ChrTalk(    #301
        0xFE,
        (
            "I wonder if I should splurge occasionally\x01",
            "and buy something with steak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "If we're going to dine well tonight,\x01",
            "then it will be fun thinking about\x01",
            "what to do for the side dishes, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A3F")

    label("loc_69CD")


    ChrTalk(    #303
        0xFE,
        (
            "If we're going to dine well tonight,\x01",
            "then it will be fun thinking about\x01",
            "what to do for the side dishes, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A3F")

    Jump("loc_70D5")

    label("loc_6A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B2F")
    OP_A2(0xC)

    ChrTalk(    #304
        0xFE,
        (
            "You know, maybe we should take\x01",
            "turns at home thinking about what\x01",
            "to do for the side dishes, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "Or better yet, maybe it would be best\x01",
            "to decide on what to do about side\x01",
            "dishes every other day of the week.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B95")

    label("loc_6B2F")


    ChrTalk(    #306
        0xFE,
        (
            "You know, maybe we should take\x01",
            "turns at home thinking about what\x01",
            "to do for the side dishes, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B95")

    Jump("loc_70D5")

    label("loc_6B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_6D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF5")
    OP_A2(0xC)

    ChrTalk(    #307
        0xFE,
        (
            "Meat, vegetables, fish...\x01",
            "I wonder what I should make\x01",
            "for supper tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "I've got to think about what to do for a\x01",
            "side dish whether we have to deal with\x01",
            "burglars, the Royal Army, or whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "I wonder if the queen would ever entertain\x01",
            "the idea of making a holiday where we\x01",
            "don't have to think about side dishes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D72")

    label("loc_6CF5")


    ChrTalk(    #310
        0xFE,
        (
            "I wonder if the queen would ever entertain\x01",
            "the idea of making a holiday where we\x01",
            "don't have to think about side dishes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D72")

    Jump("loc_70D5")

    label("loc_6D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_6E54")

    ChrTalk(    #311
        0xFE,
        (
            "I wonder what I should do\x01",
            "about a side dish today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "I just can't decide what would sit\x01",
            "well on the table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "I thought I could decide once I got to\x01",
            "the store, but now I'm here and I still\x01",
            "don't know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D5")

    label("loc_6E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_6F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F34")
    OP_A2(0xC)

    ChrTalk(    #314
        0xFE,
        "Today I'll be making a dish with meat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "Should I grill a steak or should\x01",
            "I make some stew?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        "I just can't decide...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "It's not easy trying to think of\x01",
            "what to do about the menu every\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F65")

    label("loc_6F34")


    ChrTalk(    #318
        0xFE,
        (
            "You know, maybe I should just\x01",
            "go with fish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F65")

    Jump("loc_70D5")

    label("loc_6F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_7042")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7005")
    OP_A2(0xC)

    ChrTalk(    #319
        0xFE,
        (
            "All right, I've decided! Today we're\x01",
            "going to have fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        (
            "Now the bigger question is: whether\x01",
            "to grill the fish or to boil it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_703F")

    label("loc_7005")


    ChrTalk(    #321
        0xFE,
        (
            "You know, maybe I should\x01",
            "just stick with meat today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_703F")

    Jump("loc_70D5")

    label("loc_7042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_70D5")

    ChrTalk(    #322
        0xFE,
        (
            "Let's see... Now what to do about\x01",
            "today's side dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "Should I try making something with\x01",
            "meat or should I try something with\x01",
            "fish?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70D5")

    TalkEnd(0x11)
    Return()

    # Function_25_68F6 end

    def Function_26_70D9(): pass

    label("Function_26_70D9")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71AA")
    OP_A2(0xD)

    ChrTalk(    #324
        0xFE,
        (
            "I decided to work a part-time job here\x01",
            "so I could earn money to buy books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "Who would have thought I'd be working\x01",
            "at the same store I've grown so\x01",
            "accustomed to shopping at...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7213")

    label("loc_71AA")


    ChrTalk(    #326
        0xFE,
        (
            "Who would have thought I'd be working\x01",
            "at the same store I've grown so\x01",
            "accustomed to shopping at...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7213")

    Jump("loc_77A8")

    label("loc_7216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_74A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7408")
    OP_A2(0x394)

    ChrTalk(    #327
        0xFE,
        (
            "I came here to buy the next chapter\x01",
            "in the novel series I've been reading,\x01",
            "but it's still not in yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        (
            "Once I've read a book, I almost\x01",
            "never read it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "Anyway, I'm done with this one so\x01",
            "you can have it.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x215, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #330
        "\x07\x00Received \x07\x02Carnelia - Chapter 4\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #331
        0xFE,
        (
            "The lady who owns the shop recruited\x01",
            "me to work here not that long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "I wonder if she hired me because I\x01",
            "was always putting in my thoughts\x01",
            "about her merchandise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74A4")

    label("loc_7408")


    ChrTalk(    #333
        0xFE,
        (
            "The lady who owns the shop recruited\x01",
            "me to work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "I wonder if she hired me because I\x01",
            "was always putting in my thoughts\x01",
            "about her merchandise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74A4")

    Jump("loc_77A8")

    label("loc_74A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_7536")

    ChrTalk(    #335
        0xFE,
        (
            "I sure wish the shop owner\x01",
            "would take better care of the\x01",
            "antique books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        (
            "Maybe I should go put in a word\x01",
            "or two about that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77A8")

    label("loc_7536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_75DD")

    ChrTalk(    #337
        0xFE,
        (
            "All those books in the back\x01",
            "are covered with dust and cobwebs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        (
            "I should probably borrow a feather\x01",
            "duster from the shop owner and\x01",
            "clean them off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77A8")

    label("loc_75DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_767D")

    ChrTalk(    #339
        0xFE,
        (
            "We haven't gotten any foreign\x01",
            "books in recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        (
            "It probably has something to do with\x01",
            "all these restrictions put into effect\x01",
            "by the army.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77A8")

    label("loc_767D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_774B")

    ChrTalk(    #341
        0xFE,
        (
            "Whenever I come by this place I\x01",
            "always find myself stopping in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        (
            "Since I basically come here every day,\x01",
            "I probably know where things are in this\x01",
            "place better than the shop owner herself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77A8")

    label("loc_774B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_77A8")

    ChrTalk(    #343
        0xFE,
        "The book I'm after isn't here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        (
            "Maybe I should try checking at\x01",
            "another shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77A8")

    TalkEnd(0x12)
    Return()

    # Function_26_70D9 end

    def Function_27_77AC(): pass

    label("Function_27_77AC")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_78D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_787D")
    OP_A2(0xE)

    ChrTalk(    #345
        0xFE,
        "Man, what a letdown, I tell you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        (
            "The girl running the confectionery\x01",
            "shop has a fiance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        (
            "I'm disappointed to say the least,\x01",
            "but as her fan I'll still come buy\x01",
            "her stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78D4")

    label("loc_787D")


    ChrTalk(    #348
        0xFE,
        (
            "Man...I just found out that the girl\x01",
            "running the confectionery shop\x01",
            "has a fiance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78D4")

    Jump("loc_7DCC")

    label("loc_78D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_7962")

    ChrTalk(    #349
        0xFE,
        (
            "This shop sure has gotten popular\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "I thought this might happen.\x01",
            "It's because the girl here is\x01",
            "working so hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DCC")

    label("loc_7962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_7A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A07")
    OP_A2(0xE)

    ChrTalk(    #351
        0xFE,
        (
            "The girl working here at the\x01",
            "confectionery shop has been\x01",
            "looking a little blue recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        (
            "I wonder if she's worried about\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A52")

    label("loc_7A07")


    ChrTalk(    #353
        0xFE,
        (
            "There sure have been a lot of disturbing\x01",
            "things happening these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A52")

    Jump("loc_7DCC")

    label("loc_7A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_7BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B3C")
    OP_A2(0xE)

    ChrTalk(    #354
        0xFE,
        "That girl at the confectioner's shop...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        (
            "Her sweets have gotten tons better\x01",
            "since she started making them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        (
            "I should know because I eat them\x01",
            "every day and they just keep\x01",
            "getting better and better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB0")

    label("loc_7B3C")


    ChrTalk(    #357
        0xFE,
        "That girl at the confectioner's shop...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        (
            "Her sweets have gotten tons better\x01",
            "since she started making them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BB0")

    Jump("loc_7DCC")

    label("loc_7BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_7C8D")

    ChrTalk(    #359
        0xFE,
        (
            "Ever since this girl started selling her\x01",
            "sweets, the sales of her sponge\x01",
            "cake have really started taking off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        (
            "And now I've found myself coming\x01",
            "here to shop just so I can get a\x01",
            "glimpse of her smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DCC")

    label("loc_7C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_7D35")

    ChrTalk(    #361
        0xFE,
        (
            "The pure smile of the girl who works\x01",
            "here at this shop is to die for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        (
            "In fact, I come here to buy sweets\x01",
            "several times a day just to see\x01",
            "her smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DCC")

    label("loc_7D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7DCC")

    ChrTalk(    #363
        0xFE,
        (
            "It looks like a girl is running the\x01",
            "confectionery shop now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xFE,
        (
            "Before it was some guy running this place.\x01",
            "I wonder what happened to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DCC")

    TalkEnd(0x13)
    Return()

    # Function_27_77AC end

    def Function_28_7DD0(): pass

    label("Function_28_7DD0")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EAC")
    OP_A2(0xF)

    ChrTalk(    #365
        0xFE,
        (
            "I just love the atmosphere of\x01",
            "this market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        (
            "No matter how mad my parents get,\x01",
            "I just can't stop sneaking off to\x01",
            "come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        (
            "It's not like there's anything to\x01",
            "do at home, after all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F30")

    label("loc_7EAC")


    ChrTalk(    #368
        0xFE,
        (
            "I just love the atmosphere of\x01",
            "this market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        (
            "No matter how mad my parents get,\x01",
            "I just can't stop sneaking off to\x01",
            "come here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F30")

    Jump("loc_85A4")

    label("loc_7F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_80C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8044")
    OP_A2(0xF)

    ChrTalk(    #370
        0xFE,
        (
            "My parents don't like me coming here,\x01",
            "but I just love the atmosphere of this\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "So much so in fact, that I just can't\x01",
            "help sneaking off to come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        (
            "It's just so boring sitting around\x01",
            "the house. I'd rather be at the\x01",
            "market any day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80BD")

    label("loc_8044")


    ChrTalk(    #373
        0xFE,
        (
            "If I come here I can hear, see, and\x01",
            "taste all kinds of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        (
            "And most importantly, I think\x01",
            "it's good for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80BD")

    Jump("loc_85A4")

    label("loc_80C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_811A")

    ChrTalk(    #375
        0xFE,
        (
            "My mom caught me sneaking into\x01",
            "the market and yelled at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        "*sniffle*\x02",
    )

    CloseMessageWindow()
    Jump("loc_85A4")

    label("loc_811A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_82E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_825C")
    OP_A2(0xF)

    ChrTalk(    #377
        0xFE,
        (
            "I just bought something by myself\x01",
            "for the first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "It was some kind of sponge cake\x01",
            "someone was selling near the\x01",
            "fountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        (
            "A bunch of people were eating sweets\x01",
            "over there so I joined in with them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        (
            "I couldn't believe how good they\x01",
            "were. What a great experience\x01",
            "that was for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82E6")

    label("loc_825C")


    ChrTalk(    #381
        0xFE,
        (
            "I thought it was unbecoming to eat\x01",
            "away from the table like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "But there are some tastes you\x01",
            "can only experience this way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82E6")

    Jump("loc_85A4")

    label("loc_82E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_835E")

    ChrTalk(    #383
        0xFE,
        (
            "Instead of just staring at things\x01",
            "all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        (
            "Maybe I should try and buy something\x01",
            "for once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85A4")

    label("loc_835E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_83FF")

    ChrTalk(    #385
        0xFE,
        (
            "I snuck off to come here and look\x01",
            "around. There are so many unusual\x01",
            "things to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xFE,
        (
            "So I guess this is where everybody\x01",
            "comes to shop, huh...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85A4")

    label("loc_83FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_85A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84F6")
    OP_A2(0xF)

    ChrTalk(    #387
        0xFE,
        (
            "I've been living in Bose my whole life,\x01",
            "but this is the first time I've actually\x01",
            "come to the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xFE,
        (
            "Where to start? There are goods\x01",
            "and stores all over the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xFE,
        (
            "And...*cough cough*...there's\x01",
            "dust everywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85A4")

    label("loc_84F6")


    ChrTalk(    #390
        0xFE,
        (
            "I've been living in Bose my whole life,\x01",
            "but this is the first time I've actually\x01",
            "come to the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xFE,
        (
            "Where to start? There are goods\x01",
            "and stores all over the place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85A4")

    TalkEnd(0x14)
    Return()

    # Function_28_7DD0 end

    def Function_29_85A8(): pass

    label("Function_29_85A8")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_867A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_863C")
    OP_A2(0x10)

    ChrTalk(    #392
        0xFE,
        (
            "Ho ho, they've got some new and\x01",
            "interesting wares in today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xFE,
        (
            "I see...so this is what an Eastern\x01",
            "design looks like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8677")

    label("loc_863C")


    ChrTalk(    #394
        0xFE,
        (
            "I see...so this is what an Eastern\x01",
            "design looks like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8677")

    Jump("loc_8CA8")

    label("loc_867A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_8731")

    ChrTalk(    #395
        0xFE,
        (
            "I've heard they make all kinds of\x01",
            "porcelain in countries to the east\x01",
            "of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0xFE,
        (
            "I'd sure like to go on a journey in\x01",
            "search of these porcelain goods\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CA8")

    label("loc_8731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_87D2")

    ChrTalk(    #397
        0xFE,
        (
            "It appears that we've got the army\x01",
            "coming and going here in town now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0xFE,
        (
            "I can't stand that repugnant group\x01",
            "with their pretentious attitudes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CA8")

    label("loc_87D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_89D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8926")
    OP_A2(0x10)

    ChrTalk(    #399
        0xFE,
        (
            "The porcelain made in the Empire has\x01",
            "an artistic quality in the absolutely\x01",
            "gorgeous designs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        (
            "Just the opposite, the porcelain from the Republic\x01",
            "employs simple colors and patterns, but its beauty\x01",
            "comes out the more you use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xFE,
        (
            "The varied and contrasting styles\x01",
            "are why porcelain wares are so\x01",
            "interesting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89D0")

    label("loc_8926")


    ChrTalk(    #402
        0xFE,
        (
            "Liberl's porcelain, on the other hand,\x01",
            "may have a simple shape and design,\x01",
            "but there is an elegance about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0xFE,
        (
            "I guess that's the best way to sum\x01",
            "them all up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89D0")

    Jump("loc_8CA8")

    label("loc_89D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_8C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4C")
    OP_A2(0x10)

    ChrTalk(    #404
        0xFE,
        (
            "I try to find things with hidden value\x01",
            "and get my hands on them for a\x01",
            "reasonable price.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0xFE,
        (
            "The thrill of this is something you\x01",
            "can't experience that easily in\x01",
            "other occupations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0xFE,
        (
            "To be honest though, I am still quite\x01",
            "an amateur at this myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0xFE,
        (
            "No matter how carefully I choose\x01",
            "what I buy, more than half of what\x01",
            "I get turns out to be junk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C05")

    label("loc_8B4C")


    ChrTalk(    #408
        0xFE,
        (
            "I try to find things with hidden value\x01",
            "and get my hands on them for a\x01",
            "reasonable price.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0xFE,
        (
            "The thrill of this is something you\x01",
            "can't experience that easily in\x01",
            "other occupations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C05")

    Jump("loc_8CA8")

    label("loc_8C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_8C7A")

    ChrTalk(    #410
        0xFE,
        "I love looking for bargains.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xFE,
        (
            "Whenever there are antiques to be\x01",
            "found, I just can't ignore it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CA8")

    label("loc_8C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_8CA8")

    ChrTalk(    #412
        0xFE,
        "Hmm...this one's quite a catch...\x02",
    )

    CloseMessageWindow()

    label("loc_8CA8")

    TalkEnd(0x15)
    Return()

    # Function_29_85A8 end

    def Function_30_8CAC(): pass

    label("Function_30_8CAC")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_8DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D77")
    OP_A2(0x11)

    ChrTalk(    #413
        0xFE,
        (
            "It's unfortunate that I can't buy\x01",
            "a lot of perishable goods at the\x01",
            "same time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xFE,
        (
            "If I could buy a lot of them when\x01",
            "they're cheap, it'd certainly help\x01",
            "out my home budget...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DCA")

    label("loc_8D77")


    ChrTalk(    #415
        0xFE,
        (
            "It's unfortunate that I can't buy\x01",
            "a lot of perishable goods at the\x01",
            "same time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DCA")

    Jump("loc_931E")

    label("loc_8DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_8EFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EA5")
    OP_A2(0x11)

    ChrTalk(    #416
        0xFE,
        (
            "Today I came shopping with\x01",
            "a coupon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0xFE,
        (
            "How to buy quality goods for\x01",
            "cheap...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        "That's one of my passions in life.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xFE,
        (
            "All right, now it's time to shop like a\x01",
            "budget-minded housewife!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EF8")

    label("loc_8EA5")


    ChrTalk(    #420
        0xFE,
        (
            "How to buy quality goods for\x01",
            "cheap...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xFE,
        "That's one of my passions in life.\x02",
    )

    CloseMessageWindow()

    label("loc_8EF8")

    Jump("loc_931E")

    label("loc_8EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_8FFE")

    ChrTalk(    #422
        0xFE,
        (
            "It doesn't look like there's anything\x01",
            "in particular on sale at any of these\x01",
            "stores today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        (
            "But this is no time to shirk my\x01",
            "duties. This is for the future\x01",
            "of my home budget!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xFE,
        (
            "And who knows, there may just be\x01",
            "a bargain in here somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_931E")

    label("loc_8FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_9141")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90C9")
    OP_A2(0x11)

    ChrTalk(    #425
        0xFE,
        (
            "This is terrible! How could this\x01",
            "have happened?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0xFE,
        (
            "I've spent all the money I have\x01",
            "for today! Noooooooooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "I can't figure out when they're\x01",
            "going to slash prices here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913E")

    label("loc_90C9")


    ChrTalk(    #428
        0xFE,
        (
            "This is terrible! How could this\x01",
            "have happened?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xFE,
        (
            "I've spent all the money I have\x01",
            "for today! Noooooooooooo!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_913E")

    Jump("loc_931E")

    label("loc_9141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_91DC")

    ChrTalk(    #430
        0xFE,
        (
            "Meat goes on sale for a limited time\x01",
            "after three o'clock this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        (
            "I need to find a place to camp out\x01",
            "near the store until then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_931E")

    label("loc_91DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_92A1")

    ChrTalk(    #432
        0xFE,
        (
            "If you want to get your hands on advertised\x01",
            "items, you'll have to camp out in front of the\x01",
            "market well before it opens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0xFE,
        (
            "That's pretty much the basic of\x01",
            "all basics for shoppers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_931E")

    label("loc_92A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_931E")

    ChrTalk(    #434
        0xFE,
        (
            "Let's see... Now who is having a\x01",
            "sale today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        (
            "Where's my memo...? I know I've got\x01",
            "it written down somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_931E")

    TalkEnd(0x16)
    Return()

    # Function_30_8CAC end

    def Function_31_9322(): pass

    label("Function_31_9322")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_93E5")

    ChrTalk(    #436
        0xFE,
        (
            "Due to airliner flights being canceled,\x01",
            "I've had way more than my fill of\x01",
            "shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        (
            "It looks like my husband's about to\x01",
            "have a heart attack after seeing\x01",
            "how much I bought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9655")

    label("loc_93E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_94C7")

    ChrTalk(    #438
        0xFE,
        "Wow, this is really cheap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0xFE,
        (
            "But if I buy this too, it'll just\x01",
            "add to my already...uh, substantial\x01",
            "amount of luggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0xFE,
        (
            "I wonder if I can get someone to\x01",
            "deliver it directly to my home in\x01",
            "the Royal City...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9655")

    label("loc_94C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_95B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9570")
    OP_A2(0x12)

    ChrTalk(    #441
        0xFE,
        (
            "All right then, it looks like it's\x01",
            "time to hit up the next shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0xFE,
        (
            "All this shopping is why I came along\x01",
            "with my husband on his pilgrimage!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95B6")

    label("loc_9570")


    ChrTalk(    #443
        0xFE,
        (
            "All right then, it looks like it's time\x01",
            "to hit up the next shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95B6")

    Jump("loc_9655")

    label("loc_95B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_9655")

    ChrTalk(    #444
        0xFE,
        (
            "Tee hee. I feel sorry for my husband,\x01",
            "but I feel kind of lucky that our flight\x01",
            "was canceled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0xFE,
        (
            "Now I'll be able to spend more\x01",
            "time shopping!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9655")

    TalkEnd(0x18)
    Return()

    # Function_31_9322 end

    def Function_32_9659(): pass

    label("Function_32_9659")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_9813")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_976F")
    OP_A2(0x13)

    ChrTalk(    #446
        0xFE,
        (
            "It looks like flights have started\x01",
            "back up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0xFE,
        "Now we can finally head to Ruan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xFE,
        (
            "I've really got to start keeping an eye\x01",
            "on my wife's shopping habits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0xFE,
        (
            "Personally, I think people should\x01",
            "live a little more modestly than\x01",
            "my wife does.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9810")

    label("loc_976F")


    ChrTalk(    #450
        0xFE,
        (
            "I've really got to start keeping an eye\x01",
            "on my wife's shopping habits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0xFE,
        (
            "Personally, I think people should\x01",
            "live a little more modestly than\x01",
            "my wife does.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9810")

    Jump("loc_9C85")

    label("loc_9813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_9986")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98FC")
    OP_A2(0x13)

    ChrTalk(    #452
        0xFE,
        (
            "Unbelievable. My wife is set on\x01",
            "buying more stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        (
            "Not to mention she was just barely\x01",
            "shopping here not a few minutes ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0xFE,
        (
            "I hope they can get these flights going\x01",
            "again sooner rather than later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9983")

    label("loc_98FC")


    ChrTalk(    #455
        0xFE,
        (
            "Unbelievable. My wife is set on\x01",
            "buying more stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0xFE,
        (
            "Not to mention she was just barely\x01",
            "shopping here not a few minutes ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9983")

    Jump("loc_9C85")

    label("loc_9986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_9AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A64")
    OP_A2(0x13)

    ChrTalk(    #457
        0xFE,
        (
            "My wife is shopping like a\x01",
            "crazy woman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0xFE,
        (
            "If I don't intervene, she'll never\x01",
            "stop shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xFE,
        (
            "Money is not the issue here, I just wish\x01",
            "my wife would practice a little bit of\x01",
            "self-control.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AF6")

    label("loc_9A64")


    ChrTalk(    #460
        0xFE,
        (
            "My wife is shopping like a\x01",
            "crazy woman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xFE,
        (
            "Money is not the issue here, I just\x01",
            "wish my wife would practice a little\x01",
            "bit of self-control.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AF6")

    Jump("loc_9C85")

    label("loc_9AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_9C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BF1")
    OP_A2(0x13)

    ChrTalk(    #462
        0xFE,
        "Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xFE,
        (
            "I guess if I wanted to walk to\x01",
            "Ruan, I'd have to hike over a\x01",
            "mountain, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        (
            "There's no way I could get my\x01",
            "wife to do that with me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "But at this rate, the cost of lodging\x01",
            "is only going to pile up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C85")

    label("loc_9BF1")


    ChrTalk(    #466
        0xFE,
        (
            "Umm, I don't know if making the trip to\x01",
            "Ruan on foot is really an option.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        (
            "But at this rate, the cost of lodging\x01",
            "is only going to pile up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C85")

    TalkEnd(0x17)
    Return()

    # Function_32_9659 end

    def Function_33_9C89(): pass

    label("Function_33_9C89")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_9F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E31")
    OP_A2(0x14)

    ChrTalk(    #468
        0xFE,
        (
            "I've decided to stay in Bose until I can\x01",
            "start doing business again with the\x01",
            "orbal factory that was burglarized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0xFE,
        (
            "That's because the orbments in\x01",
            "Liberl are really that fascinating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0xFE,
        (
            "Then again, all I've done is wait since\x01",
            "I've arrived here in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xFE,
        (
            "Oh well, patience is a virtue for\x01",
            "merchants in any case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0xFE,
        (
            "I guess I'll just take my sweet time\x01",
            "and wait till things blow over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F13")

    label("loc_9E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC7")
    OP_A2(0x15)

    ChrTalk(    #473
        0xFE,
        (
            "Oh well, patience is a virtue for\x01",
            "merchants in any case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0xFE,
        (
            "I guess I'll just take my sweet time\x01",
            "and wait till things blow over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F13")

    label("loc_9EC7")


    ChrTalk(    #475
        0xFE,
        (
            "That orbal factory owner sure seems\x01",
            "to be in a bit of a tizzy, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F13")

    Jump("loc_A099")

    label("loc_9F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_A099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FEE")
    OP_A2(0x14)

    ChrTalk(    #476
        0xFE,
        (
            "So this is the Bose Market,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0xFE,
        (
            "Pretty lively for a marketplace in a\x01",
            "small country, if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0xFE,
        (
            "Maybe I'll have a look around after\x01",
            "I finish up with my business deals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A099")

    label("loc_9FEE")


    ChrTalk(    #479
        0xFE,
        (
            "This place is pretty lively for a\x01",
            "marketplace in a small country,\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xFE,
        (
            "Maybe I'll have a look around after\x01",
            "I finish up with my business deals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A099")

    TalkEnd(0x19)
    Return()

    # Function_33_9C89 end

    def Function_34_A09D(): pass

    label("Function_34_A09D")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1C5")
    OP_A2(0x16)

    ChrTalk(    #481
        0xFE,
        (
            "Who would have thought that Trino\x01",
            "would be on the airliner that\x01",
            "disappeared...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0xFE,
        (
            "Now Mirano is taking care of all\x01",
            "of her father's business deals in\x01",
            "his stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0xFE,
        (
            "I know I shouldn't have expected anything\x01",
            "less...but I hope she doesn't take on\x01",
            "more than she can handle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A283")

    label("loc_A1C5")


    ChrTalk(    #484
        0xFE,
        (
            "Mirano is taking care of all\x01",
            "of her father's business deals in\x01",
            "his stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0xFE,
        (
            "I know I shouldn't have expected anything\x01",
            "less...but I hope she doesn't take on\x01",
            "more than she can handle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A283")

    TalkEnd(0x1A)
    Return()

    # Function_34_A09D end

    def Function_35_A287(): pass

    label("Function_35_A287")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3B1")
    OP_A2(0x17)

    ChrTalk(    #486
        0xFE,
        (
            "I'd really like to leave my father's business\x01",
            "deals up to Simon, but he still lacks\x01",
            "understanding of the business world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0xFE,
        (
            "And it would be a perfect time\x01",
            "for Borden to take advantage\x01",
            "of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0xFE,
        (
            "But I guess if I get overwhelmed,\x01",
            "I'll get Simon to help me out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A436")

    label("loc_A3B1")


    ChrTalk(    #489
        0xFE,
        "Trust is the first rule of business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xFE,
        (
            "So I've just got to make sure I don't\x01",
            "get wrapped up in the middle of this\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A436")

    TalkEnd(0x1C)
    Return()

    # Function_35_A287 end

    def Function_36_A43A(): pass

    label("Function_36_A43A")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4F4")
    OP_A2(0x18)

    ChrTalk(    #491
        0xFE,
        (
            "#620FMiss Maybelle is the type of person\x01",
            "who thrives the busier she is.\x02\x03",

            "#621FShe's just like her father in\x01",
            "that respect.\x02\x03",

            "#620FBut I'm worried about her health...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A56B")

    label("loc_A4F4")


    ChrTalk(    #492
        0xFE,
        (
            "#620FMiss Maybelle is the type of person\x01",
            "who thrives the busier she is.\x02\x03",

            "#620FBut I'm worried about her health...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A56B")

    TalkEnd(0x1D)
    Return()

    # Function_36_A43A end

    def Function_37_A56F(): pass

    label("Function_37_A56F")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A690")
    OP_A2(0x19)

    ChrTalk(    #493
        0xFE,
        (
            "I may not look like it, but I run the\x01",
            "kitchen at the mayor's residence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0xFE,
        (
            "And though I can't cook anything like\x01",
            "the Anterose, I can still whip up a\x01",
            "decent meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0xFE,
        (
            "The mayor has been so busy recently,\x01",
            "so I need to at least get her to take in\x01",
            "some nourishment...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6F7")

    label("loc_A690")


    ChrTalk(    #496
        0xFE,
        (
            "The mayor has been so busy recently,\x01",
            "so I need to at least get her to take in\x01",
            "some nourishment...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6F7")

    TalkEnd(0x1E)
    Return()

    # Function_37_A56F end

    def Function_38_A6FB(): pass

    label("Function_38_A6FB")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_A87B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A827")
    OP_A2(0x1A)

    ChrTalk(    #497
        0x102,
        (
            "#010FOh hi, Dorothy.\x01",
            "What are you up to?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 270, 100)
    OP_8C(0x1F, 180, 100)
    OP_8C(0x1F, 225, 100)

    ChrTalk(    #498
        0x1F,
        (
            "#151FWell, don't you all have shining\x01",
            "faces today?\x02\x03",

            "Okay, now smile for the camera,\x01",
            "please!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x101,
        "#501FIt looks like she can't hear you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x102,
        (
            "#014FY-Yeah...I guess she's off in her\x01",
            "own little world again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A878")

    label("loc_A827")


    ChrTalk(    #501
        0x1F,
        (
            "#150FLet's see...\x02\x03",

            "I've got to get those photographs\x01",
            "that Nial asked for...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A878")

    Jump("loc_AA65")

    label("loc_A87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_AA65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9D8")
    OP_A2(0x1A)

    ChrTalk(    #502
        0x101,
        "#004FHuh...? Dorothy, is that you?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1F, 90, 100)
    OP_8C(0x1F, 180, 100)
    OP_8C(0x1F, 270, 100)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)

    ChrTalk(    #503
        0x1F,
        (
            "#151FWow, look at all the stuff they're\x01",
            "selling here.\x02\x03",

            "I'm getting a kink in my neck just\x01",
            "turning my head to try and take all\x01",
            "of it in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x102,
        (
            "#014FShe's so into her surroundings,\x01",
            "it looks like she can't even hear\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0x101,
        "#007FAh ha ha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA65")

    label("loc_A9D8")


    ChrTalk(    #506
        0x1F,
        (
            "#151FWow, look at all the stuff they're\x01",
            "selling here.\x02\x03",

            "I'm getting a kink in my neck just\x01",
            "turning my head to try and take all\x01",
            "of it in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA65")

    TalkEnd(0x1F)
    Return()

    # Function_38_A6FB end

    def Function_39_AA69(): pass

    label("Function_39_AA69")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_AC4F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB9B")
    OP_A2(0x1B)

    ChrTalk(    #507
        0xFE,
        (
            "While I was being held hostage by\x01",
            "the sky bandits my fiance, Katrina,\x01",
            "held down the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xFE,
        (
            "But what kind of man would I be if\x01",
            "I took over the store now after\x01",
            "she's made it this successful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xFE,
        (
            "I guess I'm just going to have to\x01",
            "start my own business from the\x01",
            "ground up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC4F")

    label("loc_AB9B")


    ChrTalk(    #510
        0xFE,
        (
            "What kind of man would I be if\x01",
            "I took over the store now after\x01",
            "she's made it this successful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xFE,
        (
            "I guess I'm just going to have to\x01",
            "start my own business from the\x01",
            "ground up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC4F")

    TalkEnd(0x20)
    Return()

    # Function_39_AA69 end

    def Function_40_AC53(): pass

    label("Function_40_AC53")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_ACEE")

    ChrTalk(    #512
        0xFE,
        (
            "#030FMaybe I'll just stroll on\x01",
            "over to the renowned Anterose\x01",
            "restaurant.\x02\x03",

            "#035FI can't wait to taste the quintessence\x01",
            "of Liberl cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD65")

    label("loc_ACEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_AD65")

    ChrTalk(    #513
        0xFE,
        (
            "#030FThis marketplace is much more lively\x01",
            "than I could have ever imagined. It\x01",
            "was definitely worth seeing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD65")

    TalkEnd(0x21)
    Return()

    # Function_40_AC53 end

    def Function_41_AD69(): pass

    label("Function_41_AD69")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_9F(0x101, 0xC8, 0xFF, 0xFF, 0xFF, 0x0)
    OP_67(0, 9500, -10000, 0)
    SetChrPos(0x8, -84, -1000, -4656, 0)
    SetChrPos(0x9, 1100, -1000, -3970, 270)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_8C(0x1B, 135, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x16, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_ADE3"),
        (103, "loc_AE2A"),
        (101, "loc_AE71"),
        (100, "loc_AEC9"),
        (SWITCH_DEFAULT, "loc_AF21"),
    )


    label("loc_ADE3")

    SetChrPos(0x134, -4819, 0, 15920, 180)
    SetChrPos(0x101, -3723, 0, 16050, 180)
    SetChrPos(0x102, -3383, 0, 17070, 180)
    SetChrPos(0x103, -5216, 0, 17120, 180)
    Jump("loc_AF21")

    label("loc_AE2A")

    SetChrPos(0x134, 11560, 0, -630, 270)
    SetChrPos(0x101, 11200, 0, 680, 270)
    SetChrPos(0x102, 11974, 0, 1065, 270)
    SetChrPos(0x103, 12448, 0, 181, 270)
    Jump("loc_AF21")

    label("loc_AE71")

    OP_6D(-17200, 0, 1000, 0)
    SetChrPos(0x134, -19570, 0, 1459, 90)
    SetChrPos(0x101, -19730, 0, 487, 90)
    SetChrPos(0x102, -20300, 0, 1991, 90)
    SetChrPos(0x103, -20600, 0, -237, 90)
    Jump("loc_AF21")

    label("loc_AEC9")

    OP_6D(-3530, 0, -11850, 0)
    SetChrPos(0x134, -2950, 0, -15160, 0)
    SetChrPos(0x101, -4030, 0, -15400, 0)
    SetChrPos(0x102, -4400, 0, -16490, 0)
    SetChrPos(0x103, -3060, 0, -16480, 0)
    Jump("loc_AF21")

    label("loc_AF21")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #514
        0x101,
        (
            "#000FWow...this place is really huge.\x02\x03",

            "I wonder where the mayor is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0x134,
        (
            "#620FWell, she does stand out in a\x01",
            "crowd, so I'm sure you'll find\x01",
            "her right away...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x134, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #516
        0x134,
        "#623FOh, just as I thought...\x02",
    )

    CloseMessageWindow()
    OP_69(0x1B, 0x7D0)

    NpcTalk(    #517
        0x1B,
        "Young Woman",
        (
            "#612FThe two of you should be absolutely\x01",
            "ashamed of yourselves!\x02\x03",

            "Trying to force up the price of food\x01",
            "at a time like this by buying it all\x01",
            "up...\x02\x03",

            "You're not fit to be merchants\x01",
            "in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0x8,
        "B-But, ma'am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x9,
        (
            "We were just thinking about how\x01",
            "to increase sales for the Bose\x01",
            "Market in general...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #520
        0x1B,
        "Young Woman",
        (
            "#614FI don't want to hear anymore\x01",
            "from you!\x02\x03",

            "If it were other products it would be a different\x01",
            "story, but making undue profits on necessities\x01",
            "will lead to negative publicity for the market!\x02\x03",

            "Return these goods to their original\x01",
            "prices at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x8,
        "A-All right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x9,
        "We'll do as you say...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #523
        0x1B,
        "Young Woman",
        (
            "#615FNow I don't doubt your passion\x01",
            "for the Bose Market, but I want\x01",
            "you to understand this.\x02\x03",

            "Commerce, when you get right down to\x01",
            "it, is the established relationship\x01",
            "of trust between people.\x02\x03",

            "#610FAnd believe me, if you do business\x01",
            "with that in mind, you can become\x01",
            "wonderful merchants in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x8,
        "Y-Yes, ma'am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0x9,
        "We'll do our best!\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x2A)
    OP_8C(0x1B, 90, 300)
    Sleep(3000)

    NpcTalk(    #526
        0x1B,
        "Young Woman",
        "#610FWhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x134,
        "#620FMadam...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_B46A"),
        (103, "loc_B46A"),
        (101, "loc_B53E"),
        (100, "loc_B53E"),
        (SWITCH_DEFAULT, "loc_B612"),
    )


    label("loc_B46A")

    SetChrPos(0x134, 4913, -250, 1250, 0)
    SetChrPos(0x101, 4913, -250, 1250, 0)
    SetChrPos(0x102, 4913, -250, 1250, 0)
    SetChrPos(0x103, 4913, -250, 1250, 0)
    OP_8C(0x1B, 45, 400)

    def lambda_B4BB():
        OP_6D(920, -1000, -2130, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B4BB)

    def lambda_B4D3():
        OP_92(0xFE, 0x1B, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x134, 1, lambda_B4D3)
    Sleep(400)

    def lambda_B4ED():
        OP_8E(0xFE, 0x884, 0xFFFFFC18, 0xFFFFF79A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4ED)
    Sleep(400)

    def lambda_B50D():
        OP_8E(0xFE, 0x668, 0xFFFFFC18, 0xFFFFFAD8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B50D)
    Sleep(400)
    OP_8E(0x103, 0xB54, 0xFFFFFC18, 0xFFFFFC18, 0xBB8, 0x0)
    Jump("loc_B612")

    label("loc_B53E")

    SetChrPos(0x134, -6440, 0, -10600, 0)
    SetChrPos(0x101, -6440, 0, -10600, 0)
    SetChrPos(0x102, -6440, 0, -10600, 0)
    SetChrPos(0x103, -6440, 0, -10600, 0)
    OP_8C(0x1B, 225, 400)

    def lambda_B58F():
        OP_6D(-1270, -1000, -4770, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B58F)

    def lambda_B5A7():
        OP_92(0xFE, 0x1B, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x134, 1, lambda_B5A7)
    Sleep(400)

    def lambda_B5C1():
        OP_8E(0xFE, 0xFFFFF43E, 0xFFFFFC18, 0xFFFFEA34, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5C1)
    Sleep(400)

    def lambda_B5E1():
        OP_8E(0xFE, 0xFFFFF740, 0xFFFFFC18, 0xFFFFE732, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5E1)
    Sleep(400)
    OP_8E(0x103, 0xFFFFF3E4, 0xFFFFFC18, 0xFFFFE5DE, 0xBB8, 0x0)
    Jump("loc_B612")

    label("loc_B612")

    WaitChrThread(0x134, 0x1)

    NpcTalk(    #528
        0x1B,
        "Young Woman",
        (
            "#610FLila...so you came, huh?\x02\x03",

            "#617FI'm sorry you had to see that\x01",
            "side of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0x134,
        (
            "#621FActually...you did a wonderful job\x01",
            "as always.\x02\x03",

            "But never mind that, these people\x01",
            "are here to see you.\x02\x03",

            "Please come back home\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #530
        0x1B,
        "Young Woman",
        (
            "#610FOh, that emblem is...\x02\x03",

            "#610FCould you be the bracers\x01",
            "I requested?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0x101,
        "#000FYep. That's us, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0x102,
        "#010FSo does that mean that you're...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #533
        0x1B,
        "Young Woman",
        (
            "#611FHeehee. Forgive me for\x01",
            "not introducing myself.\x02\x03",

            "My name is Maybelle.\x02\x03",

            "I'm the owner of this market and\x01",
            "the mayor of the Bose region.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x20)
    OP_28(0x35, 0x1, 0x40)
    OP_28(0x35, 0x1, 0x80)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1131   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_41_AD69 end

    def Function_42_B869(): pass

    label("Function_42_B869")

    OP_8C(0xFE, 45, 400)
    OP_8E(0xFE, 0x7CB, 0xFFFFFC18, 0xFFFFF844, 0xBB8, 0x0)
    OP_8E(0xFE, 0x13B7, 0x0, 0x8C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x23B2, 0x0, 0xFFFFF31C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_B869 end

    SaveToFile()

Try(main)
