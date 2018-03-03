from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7002   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7002.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            'ED6_DT21/U7002_6 ._SN',
            'ED6_DT21/U7002_4 ._SN',
            'ED6_DT21/U7002_5 ._SN',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Kevin',                                # 9
        'Ries',                                 # 10
        'Tita',                                 # 11
        'Julia',                                # 12
        'Mueller',                              # 13
        'Josette',                              # 14
        'Joshua',                               # 15
        'Kloe',                                 # 16
        'Sieg',                                 # 17
        'Olivier',                              # 18
        'Zin',                                  # 19
        'Anelace',                              # 20
        'Scherazard',                           # 21
        'Agate',                                # 22
        'Estelle',                              # 23
        'Richard',                              # 24
        'Renne',                                # 25
        ' ',                                    # 26
        ' ',                                    # 27
        ' ',                                    # 28
        ' ',                                    # 29
        ' ',                                    # 30
        ' ',                                    # 31
        ' ',                                    # 32
        ' ',                                    # 33
        ' ',                                    # 34
        ' ',                                    # 35
        ' ',                                    # 36
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
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT27/CH03150 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT27/CH03580 ._CH',             # 03
        'ED6_DT27/CH03570 ._CH',             # 04
        'ED6_DT27/CH03100 ._CH',             # 05
        'ED6_DT27/CH03250 ._CH',             # 06
        'ED6_DT27/CH03210 ._CH',             # 07
        'ED6_DT07/CH02323 ._CH',             # 08
        'ED6_DT27/CH03260 ._CH',             # 09
        'ED6_DT07/CH00070 ._CH',             # 0A
        'ED6_DT07/CH01630 ._CH',             # 0B
        'ED6_DT27/CH03240 ._CH',             # 0C
        'ED6_DT06/CH20053 ._CH',             # 0D
        'ED6_DT27/CH03000 ._CH',             # 0E
        'ED6_DT07/CH02030 ._CH',             # 0F
        'ED6_DT27/CH03510 ._CH',             # 10
        'ED6_DT07/CH00063 ._CH',             # 11
        'ED6_DT27/CH03253 ._CH',             # 12
        'ED6_DT27/CH03213 ._CH',             # 13
        'ED6_DT27/CH03103 ._CH',             # 14
        'ED6_DT07/CH02093 ._CH',             # 15
        'ED6_DT27/CH03573 ._CH',             # 16
        'ED6_DT07/CH00073 ._CH',             # 17
        'ED6_DT27/CH03263 ._CH',             # 18
        'ED6_DT27/CH03093 ._CH',             # 19
        'ED6_DT27/CH03243 ._CH',             # 1A
        'ED6_DT27/CH03003 ._CH',             # 1B
        'ED6_DT07/CH00053 ._CH',             # 1C
        'ED6_DT27/CH03253 ._CH',             # 1D
        'ED6_DT06/CH20020 ._CH',             # 1E
        'ED6_DT06/CH20021 ._CH',             # 1F
        'ED6_DT26/CH20278 ._CH',             # 20
        'ED6_DT06/CH20050 ._CH',             # 21
        'ED6_DT07/CH00152 ._CH',             # 22
        'ED6_DT07/CH00170 ._CH',             # 23
        'ED6_DT07/CH00272 ._CH',             # 24
        'ED6_DT26/CH20241 ._CH',             # 25
        'ED6_DT07/CH00426 ._CH',             # 26
        'ED6_DT26/CH20821 ._CH',             # 27
        'ED6_DT07/CH00270 ._CH',             # 28
        'ED6_DT27/CH03085 ._CH',             # 29
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT27/CH03150P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT27/CH03580P._CP',             # 03
        'ED6_DT27/CH03570P._CP',             # 04
        'ED6_DT27/CH03100P._CP',             # 05
        'ED6_DT27/CH03250P._CP',             # 06
        'ED6_DT27/CH03210P._CP',             # 07
        'ED6_DT07/CH02323P._CP',             # 08
        'ED6_DT27/CH03260P._CP',             # 09
        'ED6_DT07/CH00070P._CP',             # 0A
        'ED6_DT07/CH01630P._CP',             # 0B
        'ED6_DT27/CH03240P._CP',             # 0C
        'ED6_DT06/CH20053P._CP',             # 0D
        'ED6_DT27/CH03000P._CP',             # 0E
        'ED6_DT07/CH02030P._CP',             # 0F
        'ED6_DT27/CH03510P._CP',             # 10
        'ED6_DT07/CH00063P._CP',             # 11
        'ED6_DT27/CH03253P._CP',             # 12
        'ED6_DT27/CH03213P._CP',             # 13
        'ED6_DT27/CH03103P._CP',             # 14
        'ED6_DT07/CH02093P._CP',             # 15
        'ED6_DT27/CH03573P._CP',             # 16
        'ED6_DT07/CH00073P._CP',             # 17
        'ED6_DT27/CH03263P._CP',             # 18
        'ED6_DT27/CH03093P._CP',             # 19
        'ED6_DT27/CH03243P._CP',             # 1A
        'ED6_DT27/CH03003P._CP',             # 1B
        'ED6_DT07/CH00053P._CP',             # 1C
        'ED6_DT27/CH03253P._CP',             # 1D
        'ED6_DT06/CH20020P._CP',             # 1E
        'ED6_DT06/CH20021P._CP',             # 1F
        'ED6_DT26/CH20278P._CP',             # 20
        'ED6_DT06/CH20050P._CP',             # 21
        'ED6_DT07/CH00152P._CP',             # 22
        'ED6_DT07/CH00170P._CP',             # 23
        'ED6_DT07/CH00272P._CP',             # 24
        'ED6_DT26/CH20241P._CP',             # 25
        'ED6_DT07/CH00426P._CP',             # 26
        'ED6_DT26/CH20821P._CP',             # 27
        'ED6_DT07/CH00270P._CP',             # 28
        'ED6_DT27/CH03085P._CP',             # 29
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 3,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 22,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 20,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 21,
        TalkFunctionIndex   = 3,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 19,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 983072,
        ChipIndex           = 0x20,
        NpcIndex            = 0x96,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262175,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327711,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262175,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327711,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966110,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835038,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900574,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966110,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966110,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x148,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3990,
        Y                   = 0,
        Z                   = -4130,
        Range               = 4000,
        Unknown_10          = 0x4074,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = -66590,
        Y                   = 3000,
        Z                   = -65000,
        Range               = 4000,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x2,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -58570,
        Y                   = 0,
        Z                   = -26170,
        Range               = 4000,
        Unknown_10          = 0x2EE0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = -42900,
        Y                   = 0,
        Z                   = -40840,
        Range               = 4000,
        Unknown_10          = 0x2134,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 27,
    )


    DeclActor(
        TriggerX            = -68460,
        TriggerZ            = 4320,
        TriggerY            = -72970,
        TriggerRange        = 2500,
        ActorX              = -67900,
        ActorZ              = 3000,
        ActorY              = -75170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -66240,
        TriggerZ            = 4120,
        TriggerY            = -17400,
        TriggerRange        = 2500,
        ActorX              = -66240,
        ActorZ              = 4120,
        ActorY              = -17400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74280,
        TriggerZ            = 4320,
        TriggerY            = -70820,
        TriggerRange        = 2500,
        ActorX              = -74280,
        ActorZ              = 4820,
        ActorY              = -70820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_686",          # 00, 0
        "Function_1_713",          # 01, 1
        "Function_2_913",          # 02, 2
        "Function_3_1042",         # 03, 3
        "Function_4_1068",         # 04, 4
        "Function_5_108E",         # 05, 5
        "Function_6_10D9",         # 06, 6
        "Function_7_1124",         # 07, 7
        "Function_8_1475",         # 08, 8
        "Function_9_1C15",         # 09, 9
        "Function_10_1F5C",        # 0A, 10
        "Function_11_25E3",        # 0B, 11
        "Function_12_29A6",        # 0C, 12
        "Function_13_2B09",        # 0D, 13
        "Function_14_2B9C",        # 0E, 14
        "Function_15_2C5B",        # 0F, 15
        "Function_16_3B18",        # 10, 16
        "Function_17_402C",        # 11, 17
        "Function_18_405D",        # 12, 18
        "Function_19_4081",        # 13, 19
        "Function_20_40DA",        # 14, 20
        "Function_21_4116",        # 15, 21
        "Function_22_4211",        # 16, 22
        "Function_23_4216",        # 17, 23
        "Function_24_4237",        # 18, 24
        "Function_25_4277",        # 19, 25
        "Function_26_42F9",        # 1A, 26
        "Function_27_4312",        # 1B, 27
    )


    def Function_0_686(): pass

    label("Function_0_686")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EE")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_69E"),
        (SWITCH_DEFAULT, "loc_6EE"),
    )


    label("loc_69E")

    SetChrPos(0x0, -17040, 1000, -15330, 225)
    SetChrPos(0x1, -17040, 1000, -15330, 225)
    SetChrPos(0x2, -17040, 1000, -15330, 225)
    SetChrPos(0x3, -17040, 1000, -15330, 225)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_6EE")

    label("loc_6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_70A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_70A")

    Call(0, 16)
    Call(0, 15)
    Return()

    # Function_0_686 end

    def Function_1_713(): pass

    label("Function_1_713")

    OP_16(0x2, 0xFA0, 0xFFFE2082, 0xFFFD8D0C, 0x23007B)
    SoundDistance(0x1CA, 0xFFFEE044, 0x10E0, 0xFFFEE5A8, 0x1F40, 0x11170, 0x64, 0x0)
    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_759")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77D")
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A1")
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CA")
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_824")
    LoadEffect(0x2, "map\\mp257_00.eff")
    PlayEffect(0x2, 0x5, 0xFF, -74280, 4320, -70820, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Jump("loc_828")

    label("loc_824")

    OP_64(0x2, 0x1)

    label("loc_828")

    Jump("loc_82F")

    label("loc_82B")

    OP_64(0x2, 0x1)

    label("loc_82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83E")
    OP_64(0x0, 0x1)
    Jump("loc_862")

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849")
    Jump("loc_862")

    label("loc_849")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_23, 0x6), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_85B")
    Jump("loc_862")

    label("loc_85B")

    OP_82(0x89, 0x0)
    OP_64(0x0, 0x1)

    label("loc_862")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x46), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_880")
    OP_64(0x1, 0x1)
    Jump("loc_8C8")

    label("loc_880")

    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x4, 0xFF, -66240, 4120, -17400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_8C8")

    Jump("loc_8CF")

    label("loc_8CB")

    OP_64(0x1, 0x1)

    label("loc_8CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_905")
    OP_E5(0x1, 0xFF, 0x15, 262144)
    OP_E5(0x1, 0xFF, 0x1A, 262144)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    OP_82(0x8C, 0x0)
    OP_82(0x8D, 0x0)
    OP_82(0x93, 0x0)
    OP_82(0x94, 0x0)
    OP_82(0x95, 0x0)
    OP_82(0x96, 0x0)

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_912")
    OP_C4(0x0, 0x200)

    label("loc_912")

    Return()

    # Function_1_713 end

    def Function_2_913(): pass

    label("Function_2_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 3)), scpexpr(EXPR_END)), "loc_91B")
    Return()

    label("loc_91B")

    EventBegin(0x0)
    OP_8C(0x0, 225, 400)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-81420, 5520, -75270, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(270000, 0)
    OP_6E(646, 0)

    def lambda_99C():
        OP_6B(2390, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_99C)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    def lambda_9B7():
        OP_6D(-68350, 4320, -67440, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9B7)

    def lambda_9CF():
        OP_67(0, 5420, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9CF)

    def lambda_9E7():
        OP_6B(2390, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9E7)

    def lambda_9F7():
        OP_6C(257000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_9F7)

    def lambda_A07():
        OP_6E(540, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_A07)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(200)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #0
        0x109,
        "#1079F#6PWell, this is nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1444F...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0x5)
    Sleep(300)
    OP_43(0x10F, 0x0, 0x0, 0x6)
    Sleep(500)

    def lambda_A8C():
        OP_6D(-73320, 4320, -70260, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A8C)

    def lambda_AA4():
        OP_67(0, 5290, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AA4)

    def lambda_ABC():
        OP_6B(1800, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_ABC)

    def lambda_ACC():
        OP_6C(257000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_ACC)

    def lambda_ADC():
        OP_6E(530, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_ADC)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #2
        0x109,
        (
            "#1067FLooks like some kind of rest\x01",
            "area or something.\x02\x03",

            "But...why? What's it doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        (
            "#1447FWell, resting is important.\x02\x03",

            "#1442FI'd love to sit and enjoy a relaxing lunch here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1060FWell, I'll give you that it might be kind of nice.\x02\x03",

            "Although personally, my first thought was that\x01",
            "I'd love to sit and fish here...if there were any\x01",
            "fish to BE fished.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_C8B():
        OP_6D(-72290, 4320, -69500, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C8B)

    def lambda_CA3():
        OP_67(0, 5790, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CA3)

    def lambda_CBB():
        OP_6B(1630, 1000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_CBB)
    OP_8C(0x10F, 315, 400)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #5
        0x10F,
        (
            "#1444F#6PReally?\x02\x03",

            "I didn't know you still liked fishing.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 135, 400)
    Sleep(300)

    ChrTalk(    #6
        0x109,
        (
            "#1062F#2PSure. Can't say I've gotten any better at it,\x01",
            "but a hobby's a hobby.\x02\x03",

            "#1061FI was surprised at how many fishing fanatics\x01",
            "there are over in Liberl.\x02\x03",

            "#1066FThere's a guild in Grancel that's REALLY\x01",
            "hardcore into it, and one girl I ran into\x01",
            "would give most pros a run for their money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10F,
        (
            "#1448F#6POh...\x02\x03",

            "#1447F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1079F#2P...?\x02\x03",

            "Something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        (
            "#1446F#6P...It's nothing.\x02\x03",

            "#1448FRegardless, it's a shame there are no fish\x01",
            "in it. The water here is exceptionally clear.\x02\x03",

            "I think this should suffice as a water source\x01",
            "for us, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1075F#2PYeah.\x02\x03",

            "#1060F#2PAll right. Let's go check somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2603)
    Sleep(300)
    OP_30(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBF")

    def lambda_FAA():
        OP_6D(-71410, 4320, -69080, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_FAA)
    Jump("loc_FE3")

    label("loc_FBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE3")

    def lambda_FD1():
        OP_6D(-70220, 4320, -69850, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_FD1)

    label("loc_FE3")


    def lambda_FE9():
        OP_67(0, 7900, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FE9)

    def lambda_1001():
        OP_6B(2530, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1001)

    def lambda_1011():
        OP_6C(270000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1011)

    def lambda_1021():
        OP_6E(450, 1000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1021)
    Sleep(1000)
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_913 end

    def Function_3_1042(): pass

    label("Function_3_1042")

    SetChrPos(0xFE, -59470, 4100, -58910, 225)
    OP_8E(0xFE, 0xFFFF09A2, 0x10E0, 0xFFFF0B1E, 0x7D0, 0x0)
    Return()

    # Function_3_1042 end

    def Function_4_1068(): pass

    label("Function_4_1068")

    SetChrPos(0xFE, -60190, 4100, -57370, 225)
    OP_8E(0xFE, 0xFFFF063C, 0x10E0, 0xFFFF103C, 0x7D0, 0x0)
    Return()

    # Function_4_1068 end

    def Function_5_108E(): pass

    label("Function_5_108E")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFF0BD2, 0x10E0, 0xFFFEFB38, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF0197, 0x10E0, 0xFFFEF340, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFEE90E, 0x10E0, 0xFFFEF228, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_5_108E end

    def Function_6_10D9(): pass

    label("Function_6_10D9")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFF0CA4, 0x10E0, 0xFFFEFF0C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFEFE26, 0x10E0, 0xFFFEF174, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFEEDB4, 0x10E0, 0xFFFEEF26, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_6_10D9 end

    def Function_7_1124(): pass

    label("Function_7_1124")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    OP_6D(-72140, 9370, -76160, 0)
    OP_67(0, 11120, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(310000, 0)
    OP_6E(625, 0)
    OP_E5(0x1, 0xFF, 0x15, 262144)
    OP_E5(0x1, 0xFF, 0x1A, 262144)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    OP_82(0x8C, 0x0)
    OP_82(0x8D, 0x0)
    OP_82(0x93, 0x0)
    OP_82(0x94, 0x0)
    OP_82(0x95, 0x0)
    OP_82(0x96, 0x0)

    def lambda_11AB():
        OP_6D(-69840, 9370, -72110, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11AB)

    def lambda_11C3():
        OP_67(0, 7370, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11C3)

    def lambda_11DB():
        OP_6B(2700, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11DB)

    def lambda_11EB():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_11EB)

    def lambda_11FB():
        OP_6E(625, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_11FB)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    OP_22(0x15F, 0x0, 0x64)
    Fade(1000)
    OP_E5(0x0, 0xFF, 0x15, 262144)
    OP_E5(0x0, 0xFF, 0x1A, 262144)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x93, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x95, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x96, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1446():
        OP_6B(2200, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1446)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_7_1124 end

    def Function_8_1475(): pass

    label("Function_8_1475")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, -69220, 4320, -70540, 180)
    SetChrPos(0x10F, -67840, 4320, -70850, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-69180, 4320, -72230, 0)
    OP_67(0, 6590, -10000, 0)
    OP_6B(1680, 0)
    OP_6C(228000, 0)
    OP_6E(429, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1633")
    Sleep(300)

    ChrTalk(    #11
        0x109,
        "#1079FThe bottom of the water's...glowing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        "#1442FIt's beautiful...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05#2S#40WWelcome...visitors from afar...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x109,
        "#1063F...Again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        "#1444FThat sounded like it came from the spring...\x02",
    )

    CloseMessageWindow()

    label("loc_1633")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x05#2S#40WVisitors from afar, quench your thirst.\x01",
            "#800W \x01",
            "#40WIn accordance with my master's wishes,\x01",
            "I shall grant you vitality...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_CE(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1715")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C12")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Drink\x01",        # 0
            "Refrain\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_175F"),
        (SWITCH_DEFAULT, "loc_1BFF"),
    )


    label("loc_175F")

    Sleep(300)
    LoadEffect(0x0, "map\\mp074_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xB, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F9")
    OP_31(0x8, 0xFB, 0x0)

    label("loc_17F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_180C")
    OP_31(0xE, 0xFB, 0x0)

    label("loc_180C")

    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05CP was restored to maximum.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_A2(0x261E)
    OP_CE(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_82(0x89, 0x0)
    OP_0D()
    Sleep(1500)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x05#2S#40WWhen my radiance is restored, I shall grant\x01",
            "you vitality once more...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #19
        (
            "\x07\x05#2S#40WWhen you have fought several battles,\x01",
            "return to me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(300)
    Fade(500)
    OP_6D(-68990, 4320, -70330, 0)
    OP_67(0, 8450, -10000, 0)
    OP_6B(1930, 0)
    OP_6C(333000, 0)
    OP_6E(417, 0)
    SetChrPos(0x109, -69040, 4320, -70620, 180)
    SetChrPos(0x10F, -67650, 4320, -70940, 180)
    OP_0D()
    Sleep(500)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #20
        0x109,
        (
            "#1068F#5P...I've never had water that actually\x01",
            "energized me like that before.\x02\x03",

            "#1063FHow's this even possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        (
            "#1447F#6PI don't know, but I feel full of life as well.\x02\x03",

            "#1448FIt looks like the water here only has that\x01",
            "effect when it's shining, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        "#1065F#5PYeah.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #23
        0x109,
        (
            "#1840F#5PWell, with all the energy we've got now, I don't think\x01",
            "there's much more we can get from here. We should\x01",
            "check back later if we're ever feelin' tired.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #24
        0x10F,
        "#1448F#6PRight.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x2607)
    OP_A2(0x2608)
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C0F")

    label("loc_1BFF")

    OP_A2(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C0F")

    label("loc_1C0F")

    Jump("loc_1715")

    label("loc_1C12")

    EventEnd(0x0)
    Return()

    # Function_8_1475 end

    def Function_9_1C15(): pass

    label("Function_9_1C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C26")
    Call(0, 8)
    Return()

    label("loc_1C26")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F4F")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Drink\x01",        # 0
            "Refrain\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C90"),
        (SWITCH_DEFAULT, "loc_1F3F"),
    )


    label("loc_1C90")

    Sleep(300)
    LoadEffect(0x0, "map\\mp074_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x3, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xB, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D94")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_1D94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA7")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_1DA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBA")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_1DBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DCD")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_1DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE0")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_1DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF3")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_1DF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E06")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_1E06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E19")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_1E19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E2C")
    OP_31(0x8, 0xFB, 0x0)

    label("loc_1E2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E3F")
    OP_31(0xE, 0xFB, 0x0)

    label("loc_1E3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E52")
    OP_31(0xA, 0xFB, 0x0)

    label("loc_1E52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E65")
    OP_31(0x9, 0xFB, 0x0)

    label("loc_1E65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E78")
    OP_31(0xB, 0xFB, 0x0)

    label("loc_1E78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E8B")
    OP_31(0xC, 0xFB, 0x0)

    label("loc_1E8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E9E")
    OP_31(0xD, 0xFB, 0x0)

    label("loc_1E9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB1")
    OP_31(0xF, 0xFB, 0x0)

    label("loc_1EB1")

    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05CP was restored to maximum.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F18")
    OP_A2(0x261E)

    label("loc_1F18")

    OP_CE(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xD7, 0x0, 0x64)
    OP_82(0x89, 0x2)
    Sleep(500)
    OP_A2(0x2608)
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F4C")

    label("loc_1F3F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F4C")

    label("loc_1F4C")

    Jump("loc_1C46")

    label("loc_1F4F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_9_1C15 end

    def Function_10_1F5C(): pass

    label("Function_10_1F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1FB8")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05There's something shining in the water.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    label("loc_1FB8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05There's something shining in the water.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_6D(-73380, 4320, -70290, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(1920, 0)
    OP_6C(270000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, -72010, 4320, -69840, 211)
    SetChrPos(0x1, -72250, 4320, -68560, 218)
    SetChrPos(0x2, -70340, 4320, -69330, 225)
    SetChrPos(0x3, -70470, 4320, -67980, 224)
    OP_4A(0x1C, 0)
    OP_63(0x1C)
    OP_4A(0x1B, 0)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    OP_22(0x222, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 30, -1, -1)
    Sleep(1500)

    AnonymousTalk(    #28
        (
            "\x07\x05#40WYou who fight with deep resolve...\x01",
            "#500W \x01",
            "#40WReturn when you have chosen your\x01",
            "path through three hundred battles.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #29
        (
            "\x07\x05#40WWhich path you take is yours to decide...\x01",
            "#500W \x01",
            "#40WWhether it is the path of the brave,\x01",
            "or the path of the cowardly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24EF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x16), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E4")
    SetMessageWindowPos(-1, 50, -1, -1)

    AnonymousTalk(    #30
        "\x07\x05#40W...\x07\x00\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 30, -1, -1)

    AnonymousTalk(    #31
        (
            "\x07\x05#40WYou have never turned your back on a fight.\x01",
            "#500W \x01",
            "#40WYou have proven your courage.\x01",
            "I will bestow upon you a blessing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x292, 1)

    AnonymousTalk(    #32
        "\x07\x05Received \x1F\x92\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2679)
    OP_64(0x2, 0x1)
    OP_F7(0x12, 0x0, 0x0)
    OP_82(0x5, 0x2)
    Jump("loc_24EC")

    label("loc_22E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x16), scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23EA")
    SetMessageWindowPos(-1, 50, -1, -1)

    AnonymousTalk(    #33
        "\x07\x05#40W...\x07\x00\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 30, -1, -1)

    AnonymousTalk(    #34
        (
            "\x07\x05#40WYou have run away from many fights.\x01",
            "#500W \x01",
            "#40WYou have proven your cowardice.\x01",
            "I will bestow upon you a blessing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x293, 1)

    AnonymousTalk(    #35
        "\x07\x05Received \x1F\x93\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2679)
    OP_64(0x2, 0x1)
    OP_F7(0x13, 0x0, 0x0)
    OP_82(0x5, 0x2)
    Jump("loc_24EC")

    label("loc_23EA")

    SetMessageWindowPos(-1, 50, -1, -1)

    AnonymousTalk(    #36
        "\x07\x05#40W...\x07\x00\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 40, -1, -1)

    AnonymousTalk(    #37
        (
            "\x07\x05#40WYou are not brave...\x01",
            "#500W \x01",
            "#40WNeither are you cowardly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 30, -1, -1)

    AnonymousTalk(    #38
        (
            "\x07\x05#40WThe path of the brave is closed to you.\x01",
            "#500W \x01",
            "#40WIf you still desire a boon, you must\x01",
            "walk along the path of the cowardly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_24EC")

    Jump("loc_2500")

    label("loc_24EF")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)

    label("loc_2500")

    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x1C, 0)
    OP_4B(0x1B, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253C")
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_253C")

    OP_6D(-72010, 4320, -69840, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(270000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, -72010, 4320, -69840, 211)
    SetChrPos(0x1, -72010, 4320, -69840, 211)
    SetChrPos(0x2, -72010, 4320, -69840, 211)
    SetChrPos(0x3, -72010, 4320, -69840, 211)
    OP_69(0x0, 0x0)
    OP_C4(0x1, 0x800)
    OP_A2(0x11)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_10_1F5C end

    def Function_11_25E3(): pass

    label("Function_11_25E3")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-66200, 4120, -13020, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -64800, 4120, -16200, 225)
    SetChrPos(0x10F, -67600, 4120, -16200, 135)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x10F,
        "#1444F#5PWhat's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x109,
        "#1063F#11PI'm not sure... I'll take a closer look.\x02",
    )

    CloseMessageWindow()
    OP_8F(0x109, 0xFFFEFF5C, 0x1018, 0xFFFFBD34, 0x5DC, 0x0)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x109, 41)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    OP_82(0x4, 0x2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    Call(0, 12)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x109, 0xFFFF0088, 0x1018, 0xFFFFBE60, 0x3E8, 0x0)
    Sleep(300)

    ChrTalk(    #41
        0x109,
        (
            "#1079F#11PHuh? Who dumped all this sepith on\x01",
            "the ground?\x02\x03",

            "#1060FWell, whatever. Don't think anyone'll\x01",
            "complain if we take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10F,
        "#1443F#5P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10F)
    TurnDirection(0x109, 0x10F, 400)
    Sleep(300)

    ChrTalk(    #43
        0x109,
        (
            "#1841F#11P*sigh*\x02\x03",

            "#1840FDon't tell me you're feeling disappointed it\x01",
            "wasn't food.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x10F,
        (
            "#1444F#5P...You're incredible.\x02\x03",

            "#1447FI didn't know you knew how to read people's\x01",
            "minds with your Thaumaturgy. Was that part\x01",
            "of your Dominion training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        "#1068F#11PSure wasn't. All I needed was to know was you...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x2620)
    OP_64(0x1, 0x1)
    Fade(1000)
    OP_6D(-66130, 4120, -17280, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(270000, 0)
    OP_6E(450, 0)
    SetMapFlags(0x1)
    SetChrPos(0x109, -66130, 4120, -17280, 90)
    SetChrPos(0x10F, -66130, 4120, -17280, 90)
    OP_0D()
    EventEnd(0x2)
    Return()

    # Function_11_25E3 end

    def Function_12_29A6(): pass

    label("Function_12_29A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x46), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B5")
    Jump("loc_2B08")

    label("loc_29B5")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x46), scpexpr(EXPR_END)),
        (12, "loc_29D4"),
        (11, "loc_2A13"),
        (10, "loc_2A13"),
        (SWITCH_DEFAULT, "loc_2A34"),
    )


    label("loc_29D4")

    OP_22(0x11, 0x0, 0x64)
    OP_3E(0x15C, 1)

    AnonymousTalk(    #46
        "\x07\x05Found \x1F\x5C\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)
    OP_3E(0x15B, 1)

    AnonymousTalk(    #47
        "\x07\x05Found \x1F\x5B\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_2A34")

    label("loc_2A13")

    OP_22(0x11, 0x0, 0x64)
    OP_3E(0x15B, 1)

    AnonymousTalk(    #48
        "\x07\x05Found \x1F\x5B\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_2A34")

    label("loc_2A34")

    OP_22(0x11, 0x0, 0x64)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #49
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x200\x01",
            "#57IWater Sepith x200\x01",
            "#58IFire Sepith x200\x01",
            "#59IWind Sepith x200\x01",
            "#62ITime Sepith x200\x01",
            "#60ISpace Sepith x200\x01",
            "#61IMirage Sepith x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2B08")

    Return()

    # Function_12_29A6 end

    def Function_13_2B09(): pass

    label("Function_13_2B09")

    OP_D6(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 6)), scpexpr(EXPR_END)), "loc_2B3D")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #50
        "\x07\x05Regained your mira and sepith.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 7)), scpexpr(EXPR_END)), "loc_2B65")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #51
        "\x07\x05Regained your items.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 6)), scpexpr(EXPR_END)), "loc_2B91")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #52
        "\x07\x05Regained your equipment.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2B91")

    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_13_2B09 end

    def Function_14_2B9C(): pass

    label("Function_14_2B9C")

    Call(0, 16)
    Call(0, 15)
    Call(0, 17)
    OP_C0(0x27, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BF7")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_2BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C18")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_2C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C39")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_2C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C5A")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_2C5A")

    Return()

    # Function_14_2B9C end

    def Function_15_2C5B(): pass

    label("Function_15_2C5B")

    OP_63(0x12)
    OP_63(0x19)
    OP_63(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_2D0A")
    SetChrPos(0x1B, -82770, 4100, -62270, 322)
    SetChrPos(0x1C, -70680, 4320, -64690, 219)
    SetChrPos(0x19, -67520, 4120, -15900, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CBE")
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2CBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CDE")
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2CDE")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -68180, 4700, -64720, 0)
    OP_D1(33, 90000, -135000, 0, 0)
    Jump("loc_3B17")

    label("loc_2D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_2E44")
    SetChrChipByIndex(0x16, 29)
    SetChrSubChip(0x16, 0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -82360, 3800, -65120, 125)
    SetChrChipByIndex(0x1E, 27)
    SetChrSubChip(0x1E, 0)
    OP_44(0x1E, 0x0)
    SetChrFlags(0x1E, 0x4)
    SetChrPos(0x1E, -81870, 3800, -64170, 125)
    SetChrChipByIndex(0x1C, 26)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -69220, 4400, -65670, 41)
    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrChipByIndex(0x1D, 28)
    SetChrSubChip(0x1D, 0)
    OP_44(0x1D, 0x0)
    SetChrFlags(0x1D, 0x4)
    SetChrPos(0x1D, -65640, 4400, -64349, 215)
    SetChrPos(0x20, -66180, 4120, -17390, 313)
    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrSubChip(0x23, 1)
    SetChrPos(0x24, -68530, 4700, -65019, 0)
    SetChrPos(0x25, -66510, 4700, -65060, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    SetChrPos(0x29, -68150, 4800, -64500, 0)
    Jump("loc_3B17")

    label("loc_2E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_2FD8")
    SetChrChipByIndex(0x1E, 27)
    SetChrSubChip(0x1E, 0)
    OP_44(0x1E, 0x0)
    SetChrFlags(0x1E, 0x4)
    SetChrPos(0x1E, -54150, 2000, -29940, 135)
    SetChrChipByIndex(0x16, 29)
    SetChrSubChip(0x16, 0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -54720, 2000, -30720, 135)
    SetChrPos(0x20, -28720, 1000, -25080, 282)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EC6")
    SetChrPos(0x12, -74600, 4100, -59540, 185)
    Jump("loc_2ED7")

    label("loc_2EC6")

    SetChrPos(0x12, -72280, 4100, -58240, 177)

    label("loc_2ED7")

    SetChrPos(0x1D, -73290, 4100, -58790, 172)
    SetChrChipByIndex(0x1C, 26)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -69220, 4400, -65670, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F41")
    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    Jump("loc_2F6F")

    label("loc_2F41")

    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrSubChip(0x1C, 0)
    SetChrSubChip(0x19, 1)

    label("loc_2F6F")

    SetChrPos(0x11, -62890, 4100, -78360, 322)
    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrPos(0x24, -68530, 4700, -65019, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    SetChrPos(0x29, -68150, 4800, -64500, 0)
    Jump("loc_3B17")

    label("loc_2FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_30C6")
    SetChrChipByIndex(0x1C, 26)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -69220, 4400, -65670, 41)
    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrPos(0x1F, -69330, 4120, -14250, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3045")
    SetChrChipByIndex(0x1F, 40)

    label("loc_3045")

    SetChrPos(0x1D, -73790, 4320, -66640, 176)
    SetChrPos(0x12, -72540, 4320, -66110, 212)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_END)), "loc_307F")
    SetChrPos(0x11, -62890, 4100, -78360, 322)

    label("loc_307F")

    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrPos(0x25, -68350, 4720, -65030, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    Jump("loc_3B17")

    label("loc_30C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_3170")
    SetChrPos(0x1A, -67650, 4120, -18510, 46)
    SetChrPos(0x1D, -64890, 4120, -15800, 224)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3111")
    SetChrPos(0x1E, -70750, 4320, -70020, 225)
    Jump("loc_3155")

    label("loc_3111")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3133")
    SetChrPos(0x16, -72170, 4320, -68540, 225)
    Jump("loc_3155")

    label("loc_3133")

    SetChrPos(0x16, -72170, 4320, -68540, 139)
    SetChrPos(0x1E, -70750, 4320, -70020, 324)

    label("loc_3155")

    SetChrPos(0x15, -66400, 4320, -69500, 232)
    OP_43(0x15, 0x0, 0x0, 0x12)
    Jump("loc_3B17")

    label("loc_3170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_3352")
    SetChrPos(0x1A, -42280, 1000, -43990, 81)
    SetChrPos(0x1D, -41590, 1000, -42880, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31D1")
    SetChrPos(0x16, -70120, 4320, -68340, 225)
    Jump("loc_334F")

    label("loc_31D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3209")
    SetChrPos(0x11, -70120, 4320, -68340, 35)
    Jump("loc_334F")

    label("loc_3209")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3241")
    SetChrPos(0x1E, -70120, 4320, -68340, 225)
    Jump("loc_334F")

    label("loc_3241")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_328A")
    SetChrPos(0x16, -70070, 4320, -68420, 270)
    SetChrPos(0x11, -71670, 4320, -68850, 67)
    Jump("loc_334F")

    label("loc_328A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D3")
    SetChrPos(0x16, -70100, 4320, -68300, 180)
    SetChrPos(0x1E, -70320, 4320, -70040, 30)
    Jump("loc_334F")

    label("loc_32D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_331C")
    SetChrPos(0x1E, -70320, 4320, -70040, 315)
    SetChrPos(0x11, -71670, 4320, -68850, 135)
    Jump("loc_334F")

    label("loc_331C")

    SetChrPos(0x16, -70120, 4320, -68340, 225)
    SetChrPos(0x1E, -70320, 4320, -70040, 30)
    SetChrPos(0x11, -71670, 4320, -68850, 67)

    label("loc_334F")

    Jump("loc_3B17")

    label("loc_3352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_342C")
    SetChrChipByIndex(0x1C, 26)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -53800, 1750, -50620, 45)
    SetChrPos(0x1B, -52870, 1000, -48760, 316)
    SetChrPos(0x1A, -59860, 4100, -69210, 60)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33C1")
    SetChrPos(0x1D, -60190, 4100, -67190, 92)
    Jump("loc_33D2")

    label("loc_33C1")

    SetChrPos(0x1D, -59670, 4100, -67570, 159)

    label("loc_33D2")

    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    Jump("loc_3B17")

    label("loc_342C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_3548")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3455")
    SetChrPos(0x1B, -70240, 4320, -70210, 255)
    Jump("loc_3499")

    label("loc_3455")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3477")
    SetChrPos(0x1D, -71610, 4320, -68650, 255)
    Jump("loc_3499")

    label("loc_3477")

    SetChrPos(0x1D, -71610, 4320, -68650, 136)
    SetChrPos(0x1B, -70240, 4320, -70210, 318)

    label("loc_3499")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B9")
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_34B9")

    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrChipByIndex(0x12, 39)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -69220, 4400, -65670, 45)
    SetChrPos(0x1A, -59860, 4100, -69210, 30)
    SetChrPos(0x23, -68110, 4720, -65410, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    Jump("loc_3B17")

    label("loc_3548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_366A")
    SetChrPos(0x12, -74940, 4100, -57970, 288)
    SetChrPos(0x1D, -76750, 4100, -57940, 337)
    SetChrChipByIndex(0x1B, 25)
    SetChrSubChip(0x1B, 0)
    OP_44(0x1B, 0x0)
    SetChrFlags(0x1B, 0x4)
    SetChrPos(0x1B, -69000, 4400, -63400, 135)
    SetChrChipByIndex(0x1C, 26)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -69220, 4400, -65670, 45)
    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrChipByIndex(0x1A, 23)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, -65820, 4400, -66630, 315)
    SetChrPos(0x22, -66350, 4720, -65690, 0)
    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrPos(0x26, -68070, 4720, -64019, 0)
    SetChrPos(0x25, -68350, 4720, -65030, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    Jump("loc_3B17")

    label("loc_366A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_36FE")
    SetChrChipByIndex(0x1A, 23)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, -69220, 4400, -65670, 41)
    SetChrPos(0x22, -68530, 4700, -65019, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x1D, -70600, 4320, -68470, 224)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36EA")
    SetChrPos(0x12, -71530, 4320, -69480, 47)
    Jump("loc_36FB")

    label("loc_36EA")

    SetChrPos(0x12, -71530, 4320, -69480, 245)

    label("loc_36FB")

    Jump("loc_3B17")

    label("loc_36FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_37A5")
    SetChrPos(0x1C, -71830, 4320, -69540, 219)
    SetChrPos(0x1B, -71350, 4320, -68160, 209)
    SetChrChipByIndex(0x1A, 23)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, -69220, 4400, -65670, 41)
    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrPos(0x22, -68530, 4700, -65019, 0)
    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    Jump("loc_3B17")

    label("loc_37A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_37AF")
    Jump("loc_3B17")

    label("loc_37AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_37B9")
    Jump("loc_3B17")

    label("loc_37B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_38BE")
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -69000, 4400, -63400, 135)
    SetChrChipByIndex(0x17, 19)
    SetChrSubChip(0x17, 0)
    OP_44(0x17, 0x0)
    SetChrFlags(0x17, 0x4)
    SetChrPos(0x17, -69220, 4400, -65670, 41)
    SetChrChipByIndex(0x15, 20)
    SetChrSubChip(0x15, 0)
    OP_44(0x15, 0x0)
    SetChrFlags(0x15, 0x4)
    SetChrPos(0x15, -65820, 4400, -66630, 315)
    SetChrChipByIndex(0x13, 21)
    SetChrSubChip(0x13, 0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, -66780, 4400, -63250, 215)
    SetChrChipByIndex(0x14, 22)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, -65640, 4400, -64349, 215)
    SetChrChipByIndex(0x16, 29)
    SetChrSubChip(0x16, 0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -68120, 4400, -66900, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38BB")
    SetChrSubChip(0x17, 2)
    SetChrSubChip(0x16, 1)

    label("loc_38BB")

    Jump("loc_3B17")

    label("loc_38BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_3A3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38FD")
    SetChrPos(0x12, -70650, 4320, -69550, 225)
    Jump("loc_3A39")

    label("loc_38FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3935")
    SetChrPos(0x15, -71170, 4320, -67990, 225)
    Jump("loc_3A39")

    label("loc_3935")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_396D")
    SetChrPos(0x16, -72230, 4320, -68570, 225)
    Jump("loc_3A39")

    label("loc_396D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39A0")
    SetChrPos(0x12, -70650, 4320, -69550, 330)
    SetChrPos(0x15, -71170, 4320, -67990, 162)
    Jump("loc_3A39")

    label("loc_39A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39D3")
    SetChrPos(0x16, -72270, 4320, -69010, 45)
    SetChrPos(0x15, -71170, 4320, -67990, 225)
    Jump("loc_3A39")

    label("loc_39D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A06")
    SetChrPos(0x16, -72230, 4320, -68570, 131)
    SetChrPos(0x12, -70650, 4320, -69550, 310)
    Jump("loc_3A39")

    label("loc_3A06")

    SetChrPos(0x16, -72230, 4320, -68570, 131)
    SetChrPos(0x12, -70650, 4320, -69550, 335)
    SetChrPos(0x15, -71170, 4320, -67990, 186)

    label("loc_3A39")

    Jump("loc_3B17")

    label("loc_3A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_3ACA")
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -68120, 4400, -66900, 45)
    SetChrChipByIndex(0x13, 21)
    SetChrSubChip(0x13, 0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, -66780, 4400, -63250, 215)
    SetChrChipByIndex(0x14, 22)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, -65640, 4400, -64349, 215)
    SetChrPos(0x15, -63360, 4320, -64709, 180)
    OP_43(0x15, 0x0, 0x0, 0x12)
    Jump("loc_3B17")

    label("loc_3ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_3B17")
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -69000, 4400, -63400, 135)
    SetChrPos(0x13, -58640, 4100, -72610, 101)
    SetChrPos(0x14, -48020, 1000, -40910, 135)

    label("loc_3B17")

    Return()

    # Function_15_2C5B end

    def Function_16_3B18(): pass

    label("Function_16_3B18")

    OP_C0(0x23, 0x10, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x11, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x12, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x13, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x14, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x15, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x16, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x17, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x18, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x19, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1A, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1B, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1C, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1D, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1E, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1F, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x20, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x10, 9000000, 9000000, 0, 0)
    SetChrPos(0x11, 9000000, 9000000, 0, 0)
    SetChrPos(0x12, 9000000, 9000000, 0, 0)
    SetChrPos(0x13, 9000000, 9000000, 0, 0)
    SetChrPos(0x14, 9000000, 9000000, 0, 0)
    SetChrPos(0x15, 9000000, 9000000, 0, 0)
    SetChrPos(0x16, 9000000, 9000000, 0, 0)
    SetChrPos(0x17, 9000000, 9000000, 0, 0)
    SetChrPos(0x18, 9000000, 9000000, 0, 0)
    SetChrPos(0x19, 9000000, 9000000, 0, 0)
    SetChrPos(0x1A, 9000000, 9000000, 0, 0)
    SetChrPos(0x1B, 9000000, 9000000, 0, 0)
    SetChrPos(0x1C, 9000000, 9000000, 0, 0)
    SetChrPos(0x1D, 9000000, 9000000, 0, 0)
    SetChrPos(0x1E, 9000000, 9000000, 0, 0)
    SetChrPos(0x1F, 9000000, 9000000, 0, 0)
    SetChrPos(0x20, 9000000, 9000000, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E91")
    SetChrFlags(0x12, 0x80)
    Jump("loc_3E96")

    label("loc_3E91")

    ClearChrFlags(0x12, 0x80)

    label("loc_3E96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EAC")
    SetChrFlags(0x13, 0x80)
    Jump("loc_3EB1")

    label("loc_3EAC")

    ClearChrFlags(0x13, 0x80)

    label("loc_3EB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EC7")
    SetChrFlags(0x14, 0x80)
    Jump("loc_3ECC")

    label("loc_3EC7")

    ClearChrFlags(0x14, 0x80)

    label("loc_3ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EE2")
    SetChrFlags(0x15, 0x80)
    Jump("loc_3EE7")

    label("loc_3EE2")

    ClearChrFlags(0x15, 0x80)

    label("loc_3EE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EFD")
    SetChrFlags(0x16, 0x80)
    Jump("loc_3F02")

    label("loc_3EFD")

    ClearChrFlags(0x16, 0x80)

    label("loc_3F02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F18")
    SetChrFlags(0x17, 0x80)
    Jump("loc_3F1D")

    label("loc_3F18")

    ClearChrFlags(0x17, 0x80)

    label("loc_3F1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F33")
    SetChrFlags(0x19, 0x80)
    Jump("loc_3F38")

    label("loc_3F33")

    ClearChrFlags(0x19, 0x80)

    label("loc_3F38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F4E")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_3F53")

    label("loc_3F4E")

    ClearChrFlags(0x1A, 0x80)

    label("loc_3F53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F69")
    SetChrFlags(0x1B, 0x80)
    Jump("loc_3F6E")

    label("loc_3F69")

    ClearChrFlags(0x1B, 0x80)

    label("loc_3F6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F84")
    SetChrFlags(0x1C, 0x80)
    Jump("loc_3F89")

    label("loc_3F84")

    ClearChrFlags(0x1C, 0x80)

    label("loc_3F89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F9F")
    SetChrFlags(0x1D, 0x80)
    Jump("loc_3FA4")

    label("loc_3F9F")

    ClearChrFlags(0x1D, 0x80)

    label("loc_3FA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FBA")
    SetChrFlags(0x1E, 0x80)
    Jump("loc_3FBF")

    label("loc_3FBA")

    ClearChrFlags(0x1E, 0x80)

    label("loc_3FBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FD5")
    SetChrFlags(0x1F, 0x80)
    Jump("loc_3FDA")

    label("loc_3FD5")

    ClearChrFlags(0x1F, 0x80)

    label("loc_3FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FF0")
    SetChrFlags(0x20, 0x80)
    Jump("loc_3FF5")

    label("loc_3FF0")

    ClearChrFlags(0x20, 0x80)

    label("loc_3FF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_400B")
    SetChrFlags(0x11, 0x80)
    Jump("loc_4010")

    label("loc_400B")

    ClearChrFlags(0x11, 0x80)

    label("loc_4010")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4026")
    SetChrFlags(0x10, 0x80)
    Jump("loc_402B")

    label("loc_4026")

    ClearChrFlags(0x10, 0x80)

    label("loc_402B")

    Return()

    # Function_16_3B18 end

    def Function_17_402C(): pass

    label("Function_17_402C")

    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_A3(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    OP_A3(0x9)
    OP_A3(0xA)
    OP_A3(0xB)
    OP_A3(0xC)
    OP_A3(0xD)
    OP_A3(0xE)
    OP_A3(0xF)
    OP_A3(0x11)
    Return()

    # Function_17_402C end

    def Function_18_405D(): pass

    label("Function_18_405D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4080")
    OP_8D(0xFE, -62720, -67560, -62720, -62300, 2000)
    Jump("Function_18_405D")

    label("loc_4080")

    Return()

    # Function_18_405D end

    def Function_19_4081(): pass

    label("Function_19_4081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_408F")
    Call(6, 2)
    Jump("loc_40D9")

    label("loc_408F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_40D5")

    label("loc_4096")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40D2")
    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    Sleep(2000)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(3000)
    Jump("loc_4096")

    label("loc_40D2")

    Jump("loc_40D9")

    label("loc_40D5")

    Call(6, 2)

    label("loc_40D9")

    Return()

    # Function_19_4081 end

    def Function_20_40DA(): pass

    label("Function_20_40DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_40E8")
    Call(6, 2)
    Jump("loc_4115")

    label("loc_40E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_4111")

    label("loc_40EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_410E")
    SetChrChipByIndex(0xFE, 35)
    SetChrSubChip(0xFE, 0)
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Jump("loc_40EF")

    label("loc_410E")

    Jump("loc_4115")

    label("loc_4111")

    Call(6, 2)

    label("loc_4115")

    Return()

    # Function_20_40DA end

    def Function_21_4116(): pass

    label("Function_21_4116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_4158")

    label("loc_411D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4155")
    SetChrChipByIndex(0xFE, 38)
    SetChrSubChip(0xFE, 0)
    Sleep(1000)
    SetChrSubChip(0xFE, 1)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(2000)
    Jump("loc_411D")

    label("loc_4155")

    Jump("loc_4210")

    label("loc_4158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_4166")
    Call(6, 2)
    Jump("loc_4210")

    label("loc_4166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_420C")

    label("loc_416D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4209")
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    Sleep(500)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(700)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    OP_9E(0xFE, 0x14, 0x0, 0x320, 0xBB8)
    Sleep(700)
    Jump("loc_416D")

    label("loc_4209")

    Jump("loc_4210")

    label("loc_420C")

    Call(6, 2)

    label("loc_4210")

    Return()

    # Function_21_4116 end

    def Function_22_4211(): pass

    label("Function_22_4211")

    Call(6, 2)
    Return()

    # Function_22_4211 end

    def Function_23_4216(): pass

    label("Function_23_4216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_4224")
    Call(6, 2)
    Jump("loc_4236")

    label("loc_4224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_4232")
    Call(6, 2)
    Jump("loc_4236")

    label("loc_4232")

    Call(6, 2)

    label("loc_4236")

    Return()

    # Function_23_4216 end

    def Function_24_4237(): pass

    label("Function_24_4237")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_4255():
        OP_90(0x0, 0x3E8, 0x0, 0x3E8, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4255)
    OP_0D()
    NewScene("ED6_DT21/U7000   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_24_4237 end

    def Function_25_4277(): pass

    label("Function_25_4277")

    SetMapFlags(0x80)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -17040, 1000, -15330, 225)
    SetChrPos(0x1, -17040, 1000, -15330, 225)
    SetChrPos(0x2, -17040, 1000, -15330, 225)
    SetChrPos(0x3, -17040, 1000, -15330, 225)
    OP_69(0x0, 0x0)
    Sleep(1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    Return()

    # Function_25_4277 end

    def Function_26_42F9(): pass

    label("Function_26_42F9")


    def lambda_42FF():
        OP_67(0, 3620, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_42FF)
    Return()

    # Function_26_42F9 end

    def Function_27_4312(): pass

    label("Function_27_4312")


    def lambda_4318():
        OP_67(0, 7900, -10000, 700)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_4318)
    Return()

    # Function_27_4312 end

    SaveToFile()

Try(main)
