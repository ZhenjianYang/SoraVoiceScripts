from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
            '',
            'ED6_DT21/U7002_4 ._SN',
            'ED6_DT21/U7002_5 ._SN',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '凯文',                                 # 9
        '莉丝',                                 # 10
        '提妲',                                 # 11
        '尤莉亚\u3000\u3000\u3000\u3000\u3000\u3000\u3000',# 12
        '穆拉',                                 # 13
        '乔丝特',                               # 14
        '约修亚',                               # 15
        '科洛丝',                               # 16
        '基库',                                 # 17
        '奥利维尔',                             # 18
        '金',                                   # 19
        '亚妮拉丝',                             # 20
        '雪拉扎德',                             # 21
        '阿加特',                               # 22
        '艾丝蒂尔',                             # 23
        '理查德',                               # 24
        '玲',                                   # 25
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
        '',                                     # 37
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
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 9,
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
        InitScenaIndex      = 21,
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
        InitScenaIndex      = 19,
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
        InitScenaIndex      = 20,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 10,
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
        InitScenaIndex      = 18,
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
        Unknown_1C          = 23,
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
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -58570,
        Y                   = 0,
        Z                   = -26170,
        Range               = 4000,
        Unknown_10          = 0x2EE0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = -42900,
        Y                   = 0,
        Z                   = -40840,
        Range               = 4000,
        Unknown_10          = 0x2134,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 26,
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
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_662",          # 00, 0
        "Function_1_6EF",          # 01, 1
        "Function_2_893",          # 02, 2
        "Function_3_F24",          # 03, 3
        "Function_4_F4A",          # 04, 4
        "Function_5_F70",          # 05, 5
        "Function_6_FBB",          # 06, 6
        "Function_7_1006",         # 07, 7
        "Function_8_1357",         # 08, 8
        "Function_9_1A08",         # 09, 9
        "Function_10_1D50",        # 0A, 10
        "Function_11_20CC",        # 0B, 11
        "Function_12_2236",        # 0C, 12
        "Function_13_249B",        # 0D, 13
        "Function_14_255A",        # 0E, 14
        "Function_15_3417",        # 0F, 15
        "Function_16_392B",        # 10, 16
        "Function_17_3959",        # 11, 17
        "Function_18_397D",        # 12, 18
        "Function_19_39D6",        # 13, 19
        "Function_20_3A12",        # 14, 20
        "Function_21_3B0D",        # 15, 21
        "Function_22_3B12",        # 16, 22
        "Function_23_3B33",        # 17, 23
        "Function_24_3B73",        # 18, 24
        "Function_25_3BF5",        # 19, 25
        "Function_26_3C0E",        # 1A, 26
    )


    def Function_0_662(): pass

    label("Function_0_662")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CA")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_67A"),
        (SWITCH_DEFAULT, "loc_6CA"),
    )


    label("loc_67A")

    SetChrPos(0x0, -17040, 1000, -15330, 225)
    SetChrPos(0x1, -17040, 1000, -15330, 225)
    SetChrPos(0x2, -17040, 1000, -15330, 225)
    SetChrPos(0x3, -17040, 1000, -15330, 225)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_6CA")

    label("loc_6CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6E6")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_6E6")

    Call(0, 15)
    Call(0, 14)
    Return()

    # Function_0_662 end

    def Function_1_6EF(): pass

    label("Function_1_6EF")

    OP_16(0x2, 0xFA0, 0xFFFE2082, 0xFFFD8D0C, 0x23007B)
    SoundDistance(0x1CA, 0xFFFEE044, 0x10E0, 0xFFFEE5A8, 0x1F40, 0x11170, 0x64, 0x0)
    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_735")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_759")
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77D")
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A6")
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_7A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B5")
    OP_64(0x0, 0x1)
    Jump("loc_7D9")

    label("loc_7B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C0")
    Jump("loc_7D9")

    label("loc_7C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_23, 0x6), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7D2")
    Jump("loc_7D9")

    label("loc_7D2")

    OP_82(0x89, 0x0)
    OP_64(0x0, 0x1)

    label("loc_7D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x46), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x48), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_800")
    OP_64(0x1, 0x1)
    Jump("loc_848")

    label("loc_800")

    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x4, 0xFF, -66240, 4120, -17400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_848")

    Jump("loc_84F")

    label("loc_84B")

    OP_64(0x1, 0x1)

    label("loc_84F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_885")
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

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_892")
    OP_C4(0x0, 0x200)

    label("loc_892")

    Return()

    # Function_1_6EF end

    def Function_2_893(): pass

    label("Function_2_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 3)), scpexpr(EXPR_END)), "loc_89B")
    Return()

    label("loc_89B")

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

    def lambda_91C():
        OP_6B(2390, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_91C)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    def lambda_937():
        OP_6D(-68350, 4320, -67440, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_937)

    def lambda_94F():
        OP_67(0, 5420, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_94F)

    def lambda_967():
        OP_6B(2390, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_967)

    def lambda_977():
        OP_6C(257000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_977)

    def lambda_987():
        OP_6E(540, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_987)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(200)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #0
        0x109,
        "#1079F#6P这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1444F……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0x5)
    Sleep(300)
    OP_43(0x10F, 0x0, 0x0, 0x6)
    Sleep(500)

    def lambda_A24():
        OP_6D(-73320, 4320, -70260, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A24)

    def lambda_A3C():
        OP_67(0, 5290, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A3C)

    def lambda_A54():
        OP_6B(1800, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A54)

    def lambda_A64():
        OP_6C(257000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A64)

    def lambda_A74():
        OP_6E(530, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_A74)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #2
        0x109,
        (
            "#1067F怎么看都感觉\x01",
            "像个休息的地方……\x02\x03",

            "书架也好，石碑也好，\x01",
            "为什么会有这些东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        (
            "#1447F……休息是很重要的。\x02\x03",

            "#1442F在这里吃便当\x01",
            "一定很美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1060F啊～……\x01",
            "的确是不错。\x02\x03",

            "唉，这里要是有鱼的话\x01",
            "就能够垂钓了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_BBD():
        OP_6D(-72290, 4320, -69500, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BBD)

    def lambda_BD5():
        OP_67(0, 5790, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BD5)

    def lambda_BED():
        OP_6B(1630, 1000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BED)
    OP_8C(0x10F, 315, 400)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #5
        0x10F,
        (
            "#1444F#6P凯文……\x02\x03",

            "你现在还钓鱼吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 135, 400)
    Sleep(300)

    ChrTalk(    #6
        0x109,
        (
            "#1062F#2P嗯，这业余爱好我还保留着，\x01",
            "虽然技术很烂就是了。\x02\x03",

            "#1061F说起来，在利贝尔\x01",
            "喜欢钓鱼的人可真多呀。\x02\x03",

            "#1066F不仅成立了超越兴趣程度的团体，\x01",
            "我认识的朋友中也有人\x01",
            "技术能与职业钓手一比高下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10F,
        (
            "#1448F#6P……是吗………\x02\x03",

            "#1447F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1079F#2P……？\x02\x03",

            "哎呀，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        (
            "#1446F#6P……没什么。\x02\x03",

            "#1448F虽然没有鱼很可惜，\x01",
            "不过这水真是非常清澈呢……\x02\x03",

            "总之，\x01",
            "饮用水有了保障。\x02",
        )
    )

    Jump("loc_E22")

    label("loc_E22")

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1075F#2P是啊……\x02\x03",

            "#1060F#2P好，接下来\x01",
            "去其它地方调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2603)
    Sleep(300)
    OP_30(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA1")

    def lambda_E8C():
        OP_6D(-71410, 4320, -69080, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_E8C)
    Jump("loc_EC5")

    label("loc_EA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC5")

    def lambda_EB3():
        OP_6D(-70220, 4320, -69850, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_EB3)

    label("loc_EC5")


    def lambda_ECB():
        OP_67(0, 7900, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_ECB)

    def lambda_EE3():
        OP_6B(2530, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_EE3)

    def lambda_EF3():
        OP_6C(270000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_EF3)

    def lambda_F03():
        OP_6E(450, 1000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F03)
    Sleep(1000)
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_893 end

    def Function_3_F24(): pass

    label("Function_3_F24")

    SetChrPos(0xFE, -59470, 4100, -58910, 225)
    OP_8E(0xFE, 0xFFFF09A2, 0x10E0, 0xFFFF0B1E, 0x7D0, 0x0)
    Return()

    # Function_3_F24 end

    def Function_4_F4A(): pass

    label("Function_4_F4A")

    SetChrPos(0xFE, -60190, 4100, -57370, 225)
    OP_8E(0xFE, 0xFFFF063C, 0x10E0, 0xFFFF103C, 0x7D0, 0x0)
    Return()

    # Function_4_F4A end

    def Function_5_F70(): pass

    label("Function_5_F70")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFF0BD2, 0x10E0, 0xFFFEFB38, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF0197, 0x10E0, 0xFFFEF340, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFEE90E, 0x10E0, 0xFFFEF228, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_5_F70 end

    def Function_6_FBB(): pass

    label("Function_6_FBB")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFF0CA4, 0x10E0, 0xFFFEFF0C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFEFE26, 0x10E0, 0xFFFEF174, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFEEDB4, 0x10E0, 0xFFFEEF26, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_6_FBB end

    def Function_7_1006(): pass

    label("Function_7_1006")

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

    def lambda_108D():
        OP_6D(-69840, 9370, -72110, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_108D)

    def lambda_10A5():
        OP_67(0, 7370, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10A5)

    def lambda_10BD():
        OP_6B(2700, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10BD)

    def lambda_10CD():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_10CD)

    def lambda_10DD():
        OP_6E(625, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_10DD)
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

    def lambda_1328():
        OP_6B(2200, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1328)
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

    # Function_7_1006 end

    def Function_8_1357(): pass

    label("Function_8_1357")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150C")
    Sleep(300)

    ChrTalk(    #11
        0x109,
        (
            "#1079F这是……\x01",
            "水底发光了……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        "#1442F……好漂亮…………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05#2S#40W欢迎……来访者们……\x02",
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
        "#1063F又来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        "#1444F这次……是从泉水里？\x02",
    )

    CloseMessageWindow()

    label("loc_150C")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x05#2S#40W     来访者啊，请滋润喉咙吧。\x01",
            "#800W\x01",
            "#40W     应吾主之愿，赐予汝等活力……\x02",
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

    label("loc_15C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A05")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "喝水\x01",      # 0
            "不喝\x01",      # 1
        )
    )

    Jump("loc_15F3")

    label("loc_15F3")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1619"),
        (SWITCH_DEFAULT, "loc_19F2"),
    )


    label("loc_1619")

    Sleep(300)
    LoadEffect(0x0, "map\\mp074_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xB, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B3")
    OP_31(0x8, 0xFB, 0x0)

    label("loc_16B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C6")
    OP_31(0xE, 0xFB, 0x0)

    label("loc_16C6")

    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05ＣＰ提升至最大值。\x02",
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
        "\x07\x05#2S#40W若光辉未恢复，则无法赐予汝等活力……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05#2S#40W   历经数战后，重返此处即可……\x02",
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
            "#1068F#5P真是被打败了……\x01",
            "没想到还能恢复气力。\x02\x03",

            "#1063F这到底是怎么样的构造呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        (
            "#1447F#6P……的确，\x01",
            "能感到浑身充满了力量。\x02\x03",

            "#1448F不过好像只有在\x01",
            "泉水发光的时候才有效。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        "#1065F#5P似乎是这样。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #23
        0x109,
        (
            "#1840F#5P算了，过一段时间\x01",
            "再来这里吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #24
        0x10F,
        "#1448F#6P嗯。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x2607)
    OP_A2(0x2608)
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A02")

    label("loc_19F2")

    OP_A2(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A02")

    label("loc_1A02")

    Jump("loc_15C7")

    label("loc_1A05")

    EventEnd(0x0)
    Return()

    # Function_8_1357 end

    def Function_9_1A08(): pass

    label("Function_9_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A19")
    Call(0, 8)
    Return()

    label("loc_1A19")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D43")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "喝水\x01",      # 0
            "不喝\x01",      # 1
        )
    )

    Jump("loc_1A65")

    label("loc_1A65")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A8B"),
        (SWITCH_DEFAULT, "loc_1D33"),
    )


    label("loc_1A8B")

    Sleep(300)
    LoadEffect(0x0, "map\\mp074_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x3, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xB, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B8F")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_1B8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA2")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_1BA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB5")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_1BB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC8")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_1BC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BDB")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_1BDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BEE")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_1BEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C01")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_1C01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C14")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_1C14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C27")
    OP_31(0x8, 0xFB, 0x0)

    label("loc_1C27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3A")
    OP_31(0xE, 0xFB, 0x0)

    label("loc_1C3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C4D")
    OP_31(0xA, 0xFB, 0x0)

    label("loc_1C4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C60")
    OP_31(0x9, 0xFB, 0x0)

    label("loc_1C60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C73")
    OP_31(0xB, 0xFB, 0x0)

    label("loc_1C73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C86")
    OP_31(0xC, 0xFB, 0x0)

    label("loc_1C86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C99")
    OP_31(0xD, 0xFB, 0x0)

    label("loc_1C99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAC")
    OP_31(0xF, 0xFB, 0x0)

    label("loc_1CAC")

    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05ＣＰ提升至最大值。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0C")
    OP_A2(0x261E)

    label("loc_1D0C")

    OP_CE(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xD7, 0x0, 0x64)
    OP_82(0x89, 0x2)
    Sleep(500)
    OP_A2(0x2608)
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D40")

    label("loc_1D33")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D40")

    label("loc_1D40")

    Jump("loc_1A39")

    label("loc_1D43")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_9_1A08 end

    def Function_10_1D50(): pass

    label("Function_10_1D50")

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

    ChrTalk(    #26
        0x10F,
        "#1444F#5P凯文，这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1063F#11P啊……\x01",
            "什么东西掉在地上。\x02",
        )
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
    Call(0, 11)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x109, 0xFFFF0088, 0x1018, 0xFFFFBE60, 0x3E8, 0x0)
    Sleep(300)

    ChrTalk(    #28
        0x109,
        (
            "#1079F#11P为什么会有这样的东西……\x02\x03",

            "#1060F……算了。\x01",
            "总之先拿着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10F,
        "#1443F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10F)
    TurnDirection(0x109, 0x10F, 400)
    Sleep(300)

    ChrTalk(    #30
        0x109,
        (
            "#1841F#11P呼……\x02\x03",

            "#1840F反正……\x01",
            "你是在想\x01",
            "『要是吃的就好了』对吧？\x02",
        )
    )

    Jump("loc_1FA6")

    label("loc_1FA6")

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x10F,
        (
            "#1444F#5P……凯文，你好厉害。\x02\x03",

            "#1447F竟然会用读心术，\x01",
            "真不愧是守护骑士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1068F#11P不，\x01",
            "这个根本不需要用读心术的。\x02",
        )
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

    # Function_10_1D50 end

    def Function_11_20CC(): pass

    label("Function_11_20CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x46), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DB")
    Jump("loc_2235")

    label("loc_20DB")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x46), scpexpr(EXPR_END)),
        (12, "loc_20FA"),
        (11, "loc_2121"),
        (10, "loc_2121"),
        (SWITCH_DEFAULT, "loc_2148"),
    )


    label("loc_20FA")

    OP_22(0x11, 0x0, 0x64)
    OP_3E(0x15C, 1)

    AnonymousTalk(    #33
        "\x07\x00得到了\x1F\x5C\x01\x07\x00。\x02",
    )

    Jump("loc_211B")

    label("loc_211B")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_2148")

    label("loc_2121")

    OP_22(0x11, 0x0, 0x64)
    OP_3E(0x15B, 1)

    AnonymousTalk(    #34
        "\x07\x00得到了\x1F\x5B\x01\x07\x00。\x02",
    )

    Jump("loc_2142")

    label("loc_2142")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_2148")

    label("loc_2148")

    OP_22(0x11, 0x0, 0x64)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)

    AnonymousTalk(    #35
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2235")

    Return()

    # Function_11_20CC end

    def Function_12_2236(): pass

    label("Function_12_2236")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x48), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2245")
    Jump("loc_249A")

    label("loc_2245")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x48), scpexpr(EXPR_END)),
        (1, "loc_229D"),
        (2, "loc_22BD"),
        (3, "loc_22DD"),
        (4, "loc_22FD"),
        (5, "loc_231D"),
        (6, "loc_233D"),
        (7, "loc_235B"),
        (8, "loc_2379"),
        (9, "loc_2397"),
        (10, "loc_23B5"),
        (11, "loc_23D4"),
        (12, "loc_23F3"),
        (13, "loc_2412"),
        (14, "loc_2431"),
        (15, "loc_2450"),
        (16, "loc_246F"),
        (SWITCH_DEFAULT, "loc_246F"),
    )


    label("loc_229D")

    OP_3E(0x33B, 1)

    AnonymousTalk(    #36
        "\x07\x00得到1个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_22BA")

    label("loc_22BA")

    Jump("loc_248E")

    label("loc_22BD")

    OP_3E(0x33B, 2)

    AnonymousTalk(    #37
        "\x07\x00得到2个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_22DA")

    label("loc_22DA")

    Jump("loc_248E")

    label("loc_22DD")

    OP_3E(0x33B, 3)

    AnonymousTalk(    #38
        "\x07\x00得到3个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_22FA")

    label("loc_22FA")

    Jump("loc_248E")

    label("loc_22FD")

    OP_3E(0x33B, 4)

    AnonymousTalk(    #39
        "\x07\x00得到4个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_231A")

    label("loc_231A")

    Jump("loc_248E")

    label("loc_231D")

    OP_3E(0x33B, 5)

    AnonymousTalk(    #40
        "\x07\x00得到5个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_233A")

    label("loc_233A")

    Jump("loc_248E")

    label("loc_233D")

    OP_3E(0x33B, 6)

    AnonymousTalk(    #41
        "\x07\x00得到6个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_2358")

    label("loc_2358")

    Jump("loc_248E")

    label("loc_235B")

    OP_3E(0x33B, 7)

    AnonymousTalk(    #42
        "\x07\x00得到7个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_2376")

    label("loc_2376")

    Jump("loc_248E")

    label("loc_2379")

    OP_3E(0x33B, 8)

    AnonymousTalk(    #43
        "\x07\x00得到8个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_2394")

    label("loc_2394")

    Jump("loc_248E")

    label("loc_2397")

    OP_3E(0x33B, 9)

    AnonymousTalk(    #44
        "\x07\x00得到9个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_23B2")

    label("loc_23B2")

    Jump("loc_248E")

    label("loc_23B5")

    OP_3E(0x33B, 10)

    AnonymousTalk(    #45
        "\x07\x00得到10个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_23D1")

    label("loc_23D1")

    Jump("loc_248E")

    label("loc_23D4")

    OP_3E(0x33B, 11)

    AnonymousTalk(    #46
        "\x07\x00得到11个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_23F0")

    label("loc_23F0")

    Jump("loc_248E")

    label("loc_23F3")

    OP_3E(0x33B, 12)

    AnonymousTalk(    #47
        "\x07\x00得到12个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_240F")

    label("loc_240F")

    Jump("loc_248E")

    label("loc_2412")

    OP_3E(0x33B, 13)

    AnonymousTalk(    #48
        "\x07\x00得到13个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_242E")

    label("loc_242E")

    Jump("loc_248E")

    label("loc_2431")

    OP_3E(0x33B, 14)

    AnonymousTalk(    #49
        "\x07\x00得到14个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_244D")

    label("loc_244D")

    Jump("loc_248E")

    label("loc_2450")

    OP_3E(0x33B, 15)

    AnonymousTalk(    #50
        "\x07\x00得到15个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_246C")

    label("loc_246C")

    Jump("loc_248E")

    label("loc_246F")

    OP_3E(0x33B, 16)

    AnonymousTalk(    #51
        "\x07\x00得到16个\x1F\x3B\x03\x07\x00。\x02",
    )

    Jump("loc_248B")

    label("loc_248B")

    Jump("loc_248E")

    label("loc_248E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_249A")

    Return()

    # Function_12_2236 end

    def Function_13_249B(): pass

    label("Function_13_249B")

    Call(0, 15)
    Call(0, 14)
    Call(0, 16)
    OP_C0(0x27, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24F6")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_24F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2517")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_2517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2538")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_2538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2559")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_2559")

    Return()

    # Function_13_249B end

    def Function_14_255A(): pass

    label("Function_14_255A")

    OP_63(0x12)
    OP_63(0x19)
    OP_63(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_2609")
    SetChrPos(0x1B, -82770, 4100, -62270, 322)
    SetChrPos(0x1C, -70680, 4320, -64690, 219)
    SetChrPos(0x19, -67520, 4120, -15900, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25BD")
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_25BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25DD")
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_25DD")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -68180, 4700, -64720, 0)
    OP_D1(33, 90000, -135000, 0, 0)
    Jump("loc_3416")

    label("loc_2609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_2743")
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
    Jump("loc_3416")

    label("loc_2743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_28D7")
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C5")
    SetChrPos(0x12, -74600, 4100, -59540, 185)
    Jump("loc_27D6")

    label("loc_27C5")

    SetChrPos(0x12, -72280, 4100, -58240, 177)

    label("loc_27D6")

    SetChrPos(0x1D, -73290, 4100, -58790, 172)
    SetChrChipByIndex(0x1C, 26)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -69220, 4400, -65670, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2840")
    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    Jump("loc_286E")

    label("loc_2840")

    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrSubChip(0x1C, 0)
    SetChrSubChip(0x19, 1)

    label("loc_286E")

    SetChrPos(0x11, -62890, 4100, -78360, 322)
    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrPos(0x24, -68530, 4700, -65019, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    SetChrPos(0x29, -68150, 4800, -64500, 0)
    Jump("loc_3416")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_29C5")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2944")
    SetChrChipByIndex(0x1F, 40)

    label("loc_2944")

    SetChrPos(0x1D, -73790, 4320, -66640, 176)
    SetChrPos(0x12, -72540, 4320, -66110, 212)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_END)), "loc_297E")
    SetChrPos(0x11, -62890, 4100, -78360, 322)

    label("loc_297E")

    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrPos(0x25, -68350, 4720, -65030, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    Jump("loc_3416")

    label("loc_29C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2A6F")
    SetChrPos(0x1A, -67650, 4120, -18510, 46)
    SetChrPos(0x1D, -64890, 4120, -15800, 224)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A10")
    SetChrPos(0x1E, -70750, 4320, -70020, 225)
    Jump("loc_2A54")

    label("loc_2A10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A32")
    SetChrPos(0x16, -72170, 4320, -68540, 225)
    Jump("loc_2A54")

    label("loc_2A32")

    SetChrPos(0x16, -72170, 4320, -68540, 139)
    SetChrPos(0x1E, -70750, 4320, -70020, 324)

    label("loc_2A54")

    SetChrPos(0x15, -66400, 4320, -69500, 232)
    OP_43(0x15, 0x0, 0x0, 0x11)
    Jump("loc_3416")

    label("loc_2A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_2C51")
    SetChrPos(0x1A, -42280, 1000, -43990, 81)
    SetChrPos(0x1D, -41590, 1000, -42880, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AD0")
    SetChrPos(0x16, -70120, 4320, -68340, 225)
    Jump("loc_2C4E")

    label("loc_2AD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B08")
    SetChrPos(0x11, -70120, 4320, -68340, 35)
    Jump("loc_2C4E")

    label("loc_2B08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B40")
    SetChrPos(0x1E, -70120, 4320, -68340, 225)
    Jump("loc_2C4E")

    label("loc_2B40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B89")
    SetChrPos(0x16, -70070, 4320, -68420, 270)
    SetChrPos(0x11, -71670, 4320, -68850, 67)
    Jump("loc_2C4E")

    label("loc_2B89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BD2")
    SetChrPos(0x16, -70100, 4320, -68300, 180)
    SetChrPos(0x1E, -70320, 4320, -70040, 30)
    Jump("loc_2C4E")

    label("loc_2BD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C1B")
    SetChrPos(0x1E, -70320, 4320, -70040, 315)
    SetChrPos(0x11, -71670, 4320, -68850, 135)
    Jump("loc_2C4E")

    label("loc_2C1B")

    SetChrPos(0x16, -70120, 4320, -68340, 225)
    SetChrPos(0x1E, -70320, 4320, -70040, 30)
    SetChrPos(0x11, -71670, 4320, -68850, 67)

    label("loc_2C4E")

    Jump("loc_3416")

    label("loc_2C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_2D2B")
    SetChrChipByIndex(0x1C, 26)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -53800, 1750, -50620, 45)
    SetChrPos(0x1B, -52870, 1000, -48760, 316)
    SetChrPos(0x1A, -59860, 4100, -69210, 60)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CC0")
    SetChrPos(0x1D, -60190, 4100, -67190, 92)
    Jump("loc_2CD1")

    label("loc_2CC0")

    SetChrPos(0x1D, -59670, 4100, -67570, 159)

    label("loc_2CD1")

    SetChrChipByIndex(0x19, 24)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, -68120, 4400, -66900, 45)
    SetChrPos(0x23, -67270, 4720, -66120, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x28, -67730, 4800, -65379, 0)
    Jump("loc_3416")

    label("loc_2D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_2E47")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D54")
    SetChrPos(0x1B, -70240, 4320, -70210, 255)
    Jump("loc_2D98")

    label("loc_2D54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D76")
    SetChrPos(0x1D, -71610, 4320, -68650, 255)
    Jump("loc_2D98")

    label("loc_2D76")

    SetChrPos(0x1D, -71610, 4320, -68650, 136)
    SetChrPos(0x1B, -70240, 4320, -70210, 318)

    label("loc_2D98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB8")
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2DB8")

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
    Jump("loc_3416")

    label("loc_2E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_2F69")
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
    Jump("loc_3416")

    label("loc_2F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_2FFD")
    SetChrChipByIndex(0x1A, 23)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, -69220, 4400, -65670, 41)
    SetChrPos(0x22, -68530, 4700, -65019, 0)
    SetChrPos(0x27, -67260, 4800, -65600, 0)
    SetChrPos(0x1D, -70600, 4320, -68470, 224)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE9")
    SetChrPos(0x12, -71530, 4320, -69480, 47)
    Jump("loc_2FFA")

    label("loc_2FE9")

    SetChrPos(0x12, -71530, 4320, -69480, 245)

    label("loc_2FFA")

    Jump("loc_3416")

    label("loc_2FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_30A4")
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
    Jump("loc_3416")

    label("loc_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_30AE")
    Jump("loc_3416")

    label("loc_30AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_30B8")
    Jump("loc_3416")

    label("loc_30B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_31BD")
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31BA")
    SetChrSubChip(0x17, 2)
    SetChrSubChip(0x16, 1)

    label("loc_31BA")

    Jump("loc_3416")

    label("loc_31BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_333B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31FC")
    SetChrPos(0x12, -70650, 4320, -69550, 225)
    Jump("loc_3338")

    label("loc_31FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3234")
    SetChrPos(0x15, -71170, 4320, -67990, 225)
    Jump("loc_3338")

    label("loc_3234")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_326C")
    SetChrPos(0x16, -72230, 4320, -68570, 225)
    Jump("loc_3338")

    label("loc_326C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_329F")
    SetChrPos(0x12, -70650, 4320, -69550, 330)
    SetChrPos(0x15, -71170, 4320, -67990, 162)
    Jump("loc_3338")

    label("loc_329F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D2")
    SetChrPos(0x16, -72270, 4320, -69010, 45)
    SetChrPos(0x15, -71170, 4320, -67990, 225)
    Jump("loc_3338")

    label("loc_32D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3305")
    SetChrPos(0x16, -72230, 4320, -68570, 131)
    SetChrPos(0x12, -70650, 4320, -69550, 310)
    Jump("loc_3338")

    label("loc_3305")

    SetChrPos(0x16, -72230, 4320, -68570, 131)
    SetChrPos(0x12, -70650, 4320, -69550, 335)
    SetChrPos(0x15, -71170, 4320, -67990, 186)

    label("loc_3338")

    Jump("loc_3416")

    label("loc_333B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_33C9")
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
    OP_43(0x15, 0x0, 0x0, 0x11)
    Jump("loc_3416")

    label("loc_33C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_3416")
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -69000, 4400, -63400, 135)
    SetChrPos(0x13, -58640, 4100, -72610, 101)
    SetChrPos(0x14, -48020, 1000, -40910, 135)

    label("loc_3416")

    Return()

    # Function_14_255A end

    def Function_15_3417(): pass

    label("Function_15_3417")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3790")
    SetChrFlags(0x12, 0x80)
    Jump("loc_3795")

    label("loc_3790")

    ClearChrFlags(0x12, 0x80)

    label("loc_3795")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37AB")
    SetChrFlags(0x13, 0x80)
    Jump("loc_37B0")

    label("loc_37AB")

    ClearChrFlags(0x13, 0x80)

    label("loc_37B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C6")
    SetChrFlags(0x14, 0x80)
    Jump("loc_37CB")

    label("loc_37C6")

    ClearChrFlags(0x14, 0x80)

    label("loc_37CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37E1")
    SetChrFlags(0x15, 0x80)
    Jump("loc_37E6")

    label("loc_37E1")

    ClearChrFlags(0x15, 0x80)

    label("loc_37E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37FC")
    SetChrFlags(0x16, 0x80)
    Jump("loc_3801")

    label("loc_37FC")

    ClearChrFlags(0x16, 0x80)

    label("loc_3801")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3817")
    SetChrFlags(0x17, 0x80)
    Jump("loc_381C")

    label("loc_3817")

    ClearChrFlags(0x17, 0x80)

    label("loc_381C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3832")
    SetChrFlags(0x19, 0x80)
    Jump("loc_3837")

    label("loc_3832")

    ClearChrFlags(0x19, 0x80)

    label("loc_3837")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_384D")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_3852")

    label("loc_384D")

    ClearChrFlags(0x1A, 0x80)

    label("loc_3852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3868")
    SetChrFlags(0x1B, 0x80)
    Jump("loc_386D")

    label("loc_3868")

    ClearChrFlags(0x1B, 0x80)

    label("loc_386D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3883")
    SetChrFlags(0x1C, 0x80)
    Jump("loc_3888")

    label("loc_3883")

    ClearChrFlags(0x1C, 0x80)

    label("loc_3888")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_389E")
    SetChrFlags(0x1D, 0x80)
    Jump("loc_38A3")

    label("loc_389E")

    ClearChrFlags(0x1D, 0x80)

    label("loc_38A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B9")
    SetChrFlags(0x1E, 0x80)
    Jump("loc_38BE")

    label("loc_38B9")

    ClearChrFlags(0x1E, 0x80)

    label("loc_38BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38D4")
    SetChrFlags(0x1F, 0x80)
    Jump("loc_38D9")

    label("loc_38D4")

    ClearChrFlags(0x1F, 0x80)

    label("loc_38D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38EF")
    SetChrFlags(0x20, 0x80)
    Jump("loc_38F4")

    label("loc_38EF")

    ClearChrFlags(0x20, 0x80)

    label("loc_38F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_390A")
    SetChrFlags(0x11, 0x80)
    Jump("loc_390F")

    label("loc_390A")

    ClearChrFlags(0x11, 0x80)

    label("loc_390F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3925")
    SetChrFlags(0x10, 0x80)
    Jump("loc_392A")

    label("loc_3925")

    ClearChrFlags(0x10, 0x80)

    label("loc_392A")

    Return()

    # Function_15_3417 end

    def Function_16_392B(): pass

    label("Function_16_392B")

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
    Return()

    # Function_16_392B end

    def Function_17_3959(): pass

    label("Function_17_3959")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_397C")
    OP_8D(0xFE, -62720, -67560, -62720, -62300, 2000)
    Jump("Function_17_3959")

    label("loc_397C")

    Return()

    # Function_17_3959 end

    def Function_18_397D(): pass

    label("Function_18_397D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_398B")
    Call(6, 2)
    Jump("loc_39D5")

    label("loc_398B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_39D1")

    label("loc_3992")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39CE")
    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    Sleep(2000)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(3000)
    Jump("loc_3992")

    label("loc_39CE")

    Jump("loc_39D5")

    label("loc_39D1")

    Call(6, 2)

    label("loc_39D5")

    Return()

    # Function_18_397D end

    def Function_19_39D6(): pass

    label("Function_19_39D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_39E4")
    Call(6, 2)
    Jump("loc_3A11")

    label("loc_39E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_3A0D")

    label("loc_39EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A0A")
    SetChrChipByIndex(0xFE, 35)
    SetChrSubChip(0xFE, 0)
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Jump("loc_39EB")

    label("loc_3A0A")

    Jump("loc_3A11")

    label("loc_3A0D")

    Call(6, 2)

    label("loc_3A11")

    Return()

    # Function_19_39D6 end

    def Function_20_3A12(): pass

    label("Function_20_3A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_3A54")

    label("loc_3A19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A51")
    SetChrChipByIndex(0xFE, 38)
    SetChrSubChip(0xFE, 0)
    Sleep(1000)
    SetChrSubChip(0xFE, 1)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(2000)
    Jump("loc_3A19")

    label("loc_3A51")

    Jump("loc_3B0C")

    label("loc_3A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_3A62")
    Call(6, 2)
    Jump("loc_3B0C")

    label("loc_3A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_3B08")

    label("loc_3A69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B05")
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
    Jump("loc_3A69")

    label("loc_3B05")

    Jump("loc_3B0C")

    label("loc_3B08")

    Call(6, 2)

    label("loc_3B0C")

    Return()

    # Function_20_3A12 end

    def Function_21_3B0D(): pass

    label("Function_21_3B0D")

    Call(6, 2)
    Return()

    # Function_21_3B0D end

    def Function_22_3B12(): pass

    label("Function_22_3B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_3B20")
    Call(6, 2)
    Jump("loc_3B32")

    label("loc_3B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_3B2E")
    Call(6, 2)
    Jump("loc_3B32")

    label("loc_3B2E")

    Call(6, 2)

    label("loc_3B32")

    Return()

    # Function_22_3B12 end

    def Function_23_3B33(): pass

    label("Function_23_3B33")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_3B51():
        OP_90(0x0, 0x3E8, 0x0, 0x3E8, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3B51)
    OP_0D()
    NewScene("ED6_DT21/U7000   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_23_3B33 end

    def Function_24_3B73(): pass

    label("Function_24_3B73")

    SetMapFlags(0x80)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_24_3B73 end

    def Function_25_3BF5(): pass

    label("Function_25_3BF5")


    def lambda_3BFB():
        OP_67(0, 3620, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_3BFB)
    Return()

    # Function_25_3BF5 end

    def Function_26_3C0E(): pass

    label("Function_26_3C0E")


    def lambda_3C14():
        OP_67(0, 7900, -10000, 700)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_3C14)
    Return()

    # Function_26_3C0E end

    SaveToFile()

Try(main)
