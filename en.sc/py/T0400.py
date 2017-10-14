from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0400   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0400.x',
        MapIndex            = 13,
        MapDefaultBGM       = "ed60015",
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
        'Alraune',                              # 9
        'Alraune',                              # 10
        'Alraune',                              # 11
        'Tio',                                  # 12
        'Will',                                 # 13
        'Chere',                                # 14
        'Franz',                                # 15
        'ウシ',                                 # 16
        'ウシ',                                 # 17
        'ニワトリ',                             # 18
        'ニワトリ',                             # 19
        'ニワトリ',                             # 20
        'ニワトリ',                             # 21
        'Royal Guardsman',                      # 22
        'Royal Guardsman',                      # 23
        'Milch Main Road',                      # 24
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
        'ED6_DT29/CH12890 ._CH',             # 00
        'ED6_DT27/CH04000 ._CH',             # 01
        'ED6_DT27/CH04001 ._CH',             # 02
        'ED6_DT07/CH00160 ._CH',             # 03
        'ED6_DT07/CH00161 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT07/CH00121 ._CH',             # 06
        'ED6_DT07/CH00140 ._CH',             # 07
        'ED6_DT07/CH00141 ._CH',             # 08
        'ED6_DT29/CH12891 ._CH',             # 09
        'ED6_DT07/CH02480 ._CH',             # 0A
        'ED6_DT07/CH01060 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT07/CH01020 ._CH',             # 0D
        'ED6_DT07/CH01710 ._CH',             # 0E
        'ED6_DT07/CH01720 ._CH',             # 0F
        'ED6_DT07/CH01640 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT29/CH12890P._CP',             # 00
        'ED6_DT27/CH04000P._CP',             # 01
        'ED6_DT27/CH04001P._CP',             # 02
        'ED6_DT07/CH00160P._CP',             # 03
        'ED6_DT07/CH00161P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT07/CH00121P._CP',             # 06
        'ED6_DT07/CH00140P._CP',             # 07
        'ED6_DT07/CH00141P._CP',             # 08
        'ED6_DT29/CH12891P._CP',             # 09
        'ED6_DT07/CH02480P._CP',             # 0A
        'ED6_DT07/CH01060P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT07/CH01020P._CP',             # 0D
        'ED6_DT07/CH01710P._CP',             # 0E
        'ED6_DT07/CH01720P._CP',             # 0F
        'ED6_DT07/CH01640P._CP',             # 10
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40470,
        Z                   = 0,
        Y                   = 16320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 25300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 25100,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 27590,
        Z                   = -60,
        Y                   = 34960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 39010,
        Z                   = 600,
        Y                   = 22850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 48160,
        Z                   = 460,
        Y                   = 18800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 38780,
        Z                   = 0,
        Y                   = 19310,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 25880,
        Z                   = 390,
        Y                   = 53570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 23960,
        Z                   = 140,
        Y                   = 43890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 23910,
        Z                   = 30,
        Y                   = 66820,
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
        X                   = 28330,
        Y                   = -1000,
        Z                   = 47700,
        Range               = 30790,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xDF66,
        Unknown_18          = 0x0,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 20560,
        Y                   = -1000,
        Z                   = 57690,
        Range               = 26700,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xD8CC,
        Unknown_18          = 0x0,
        Unknown_1C          = 35,
    )


    DeclActor(
        TriggerX            = 16370,
        TriggerZ            = 570,
        TriggerY            = 23100,
        TriggerRange        = 800,
        ActorX              = 16370,
        ActorZ              = 1570,
        ActorY              = 23100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_396",          # 00, 0
        "Function_1_446",          # 01, 1
        "Function_2_4E3",          # 02, 2
        "Function_3_660",          # 03, 3
        "Function_4_684",          # 04, 4
        "Function_5_6A8",          # 05, 5
        "Function_6_7F5",          # 06, 6
        "Function_7_90C",          # 07, 7
        "Function_8_1AB6",         # 08, 8
        "Function_9_1D5D",         # 09, 9
        "Function_10_1F4E",        # 0A, 10
        "Function_11_21E4",        # 0B, 11
        "Function_12_226A",        # 0C, 12
        "Function_13_2290",        # 0D, 13
        "Function_14_2296",        # 0E, 14
        "Function_15_24DC",        # 0F, 15
        "Function_16_26B1",        # 10, 16
        "Function_17_303F",        # 11, 17
        "Function_18_3084",        # 12, 18
        "Function_19_30C9",        # 13, 19
        "Function_20_3102",        # 14, 20
        "Function_21_313B",        # 15, 21
        "Function_22_317F",        # 16, 22
        "Function_23_31C3",        # 17, 23
        "Function_24_3207",        # 18, 24
        "Function_25_324B",        # 19, 25
        "Function_26_342D",        # 1A, 26
        "Function_27_3449",        # 1B, 27
        "Function_28_3465",        # 1C, 28
        "Function_29_3481",        # 1D, 29
        "Function_30_349D",        # 1E, 30
        "Function_31_34CE",        # 1F, 31
        "Function_32_34F3",        # 20, 32
        "Function_33_3518",        # 21, 33
        "Function_34_353D",        # 22, 34
        "Function_35_36B2",        # 23, 35
        "Function_36_382E",        # 24, 36
    )


    def Function_0_396(): pass

    label("Function_0_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3C5")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0xB, 29090, 0, 13250, 180)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_430")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3E5")
    SetChrPos(0xB, 28990, 0, 13230, 180)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_430")

    label("loc_3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_41C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_430")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_430")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_430")
    SetChrFlags(0xB, 0x10)

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_445")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_445")

    Return()

    # Function_0_396 end

    def Function_1_446(): pass

    label("Function_1_446")

    OP_16(0x2, 0xFA0, 0xFFFE8900, 0xFFFE8900, 0x230004)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_47F")
    OP_10(0x4, 0x0)
    OP_10(0x5, 0x1)

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    OP_72(0x0, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_49B")

    label("loc_497")

    OP_64(0x0, 0x1)

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_4A5")
    Jump("loc_4C1")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4C1")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D0")
    OP_A2(0x1888)

    label("loc_4D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2")
    OP_C4(0x0, 0x4)

    label("loc_4E2")

    Return()

    # Function_1_446 end

    def Function_2_4E3(): pass

    label("Function_2_4E3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_508")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_64A")

    label("loc_508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_64A")

    label("loc_521")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_64A")

    label("loc_53A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_64A")

    label("loc_553")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_64A")

    label("loc_56C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_64A")

    label("loc_585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_64A")

    label("loc_59E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_64A")

    label("loc_5B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_64A")

    label("loc_5D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_64A")

    label("loc_5E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_602")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_64A")

    label("loc_602")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_64A")

    label("loc_61B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_634")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_64A")

    label("loc_634")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_64A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_64A")

    label("loc_65F")

    Return()

    # Function_2_4E3 end

    def Function_3_660(): pass

    label("Function_3_660")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_683")
    OP_8D(0xFE, 19800, 21600, 24000, 30300, 3000)
    Jump("Function_3_660")

    label("loc_683")

    Return()

    # Function_3_660 end

    def Function_4_684(): pass

    label("Function_4_684")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A7")
    OP_8D(0xFE, 19800, 21600, 28200, 24800, 3000)
    Jump("Function_4_684")

    label("loc_6A7")

    Return()

    # Function_4_684 end

    def Function_5_6A8(): pass

    label("Function_5_6A8")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 28710, 33610, 41830, 44000, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F4")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B9")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7026), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x834A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xA366), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xABE0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78E")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_77B():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77B)
    Jump("loc_7B1")

    label("loc_78E")


    def lambda_794():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_794)
    Sleep(200)

    label("loc_7B1")

    Sleep(30)
    Jump("loc_7F1")

    label("loc_7B9")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    OP_44(0xFE, 0x2)

    def lambda_7D9():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D9)

    label("loc_7F1")

    Jump("loc_6D1")

    label("loc_7F4")

    Return()

    # Function_5_6A8 end

    def Function_6_7F5(): pass

    label("Function_6_7F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90B")
    OP_8E(0xFE, 0x5DE8, 0x0, 0x9B78, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4CA4, 0x0, 0x9AE2, 0x7D0, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0x5DE8, 0x0, 0x9B78, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5FAA, 0x0, 0x77CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x858E, 0xBE, 0x79CC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x8516, 0x0, 0x489E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x7210, 0x0, 0x484E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x7166, 0x12C, 0x56AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D8E, 0x0, 0x5AF0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D0C, 0x3C, 0xD32C, 0x7D0, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0x5D98, 0x8C, 0xAB72, 0x7D0, 0x0)
    Jump("Function_6_7F5")

    label("loc_90B")

    Return()

    # Function_6_7F5 end

    def Function_7_90C(): pass

    label("Function_7_90C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1194")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAA")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0x101,
        "#1001FHey, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1040FHey, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Estelle? And Joshua?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1000FAhaha, sorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        "#1040FWere you...worried, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "No, it's okay. I heard all about\x01",
            "what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Besides, I'm pretty sure Estelle was\x01",
            "more worried than anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Apparently she cried quite a lot, and\x01",
            "a maiden's tears carry a high price,\x01",
            "you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1008FH-Hey, whoa, Tio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1054FHaha... Don't worry, I'm ready to\x01",
            "accept the punishment for my crimes.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #10
        0xFE,
        (
            "And you will. It's going to take a lot\x01",
            "to make it up to her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDB")

    ChrTalk(    #11
        0xFE,
        "...Incidentally, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Since Schera's with you, I assume you're\x01",
            "doing guild work again today, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_BDB")


    ChrTalk(    #13
        0xFE,
        (
            "...Incidentally, you two, are you doing\x01",
            "guild work again today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(    #14
        0x101,
        (
            "#1006FYeah, we're patrolling the outskirts of Rolent,\x01",
            "mostly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC0")

    ChrTalk(    #15
        0x103,
        (
            "#020FIt's to help us get a handle on the situation\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D03")

    label("loc_CC0")


    ChrTalk(    #16
        0x102,
        (
            "#1040FIt'll help us get a grasp of the situation\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D03")

    Jump("loc_DA2")

    label("loc_D06")


    ChrTalk(    #17
        0x101,
        "#1006FYeah, we're about to head to Rolent.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D75")

    ChrTalk(    #18
        0x103,
        "#020FWe've got a delivery for the guild.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DA2")

    label("loc_D75")


    ChrTalk(    #19
        0x102,
        "#1040FWe have a delivery for the guild.\x02",
    )

    CloseMessageWindow()

    label("loc_DA2")


    ChrTalk(    #20
        0xFE,
        "I see... Being a bracer sounds rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "But, you did come all the way back home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "You guys should come see me again\x01",
            "once your work's all done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        "#1040FWe will. You have my word.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1006FI'm sure it's hard right now,\x01",
            "but hang in there, Tio.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20A9)
    Jump("loc_1191")

    label("loc_EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_FAD")

    ChrTalk(    #25
        0xFE,
        "All the orbments in Rolent have stopped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "And it's causing lots of problems, since\x01",
            "we can't use our pump or our greenhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Phew! Carrying buckets is a pain when\x01",
            "you haven't done it in a while. And I haven't\x01",
            "done it in a loooong time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1191")

    label("loc_FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D8")

    ChrTalk(    #28
        0xFE,
        (
            "Still, though, that patrol ship's emergency\x01",
            "landing sure was a surprise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "The soldiers said they already requested\x01",
            "a rescue, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "...well, does their rescue squad even\x01",
            "have any way of getting to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Hmm, seems like it'll be a while\x01",
            "before they're able to leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1191")

    label("loc_10D8")


    ChrTalk(    #32
        0xFE,
        (
            "Boy, was I ever surprised when that\x01",
            "patrol ship made an emergency landing\x01",
            "on the highway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Really, the world's full of things you'd\x01",
            "never expect to happen. Life is a surprise!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1191")

    Jump("loc_1AB2")

    label("loc_1194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_15A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 5)), scpexpr(EXPR_END)), "loc_1221")

    ChrTalk(    #34
        0xFE,
        "I'm really thankful to Kevin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "On top of protecting us, he also looked\x01",
            "after the kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "We really owe him big.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15A2")

    label("loc_1221")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #37
        0xFE,
        "Ah, Estelle and Schera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1001FHeya, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x103,
        "#020FHow are you feeling?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #40
        0xFE,
        "Fine, totally fine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Kevin told us all the details.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #42
        0xFE,
        (
            "I just can't help but cause you worry, huh,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "But you don't need to worry anymore.\x01",
            "Everyone's just fine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1025FYeah, I'm glad... I really am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "I was a bit surprised when I woke up, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "That guy, Kevin, was right in front of me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1016FAhaha...\x02\x03",

            "Yeah, I can see how that might be a little\x01",
            "surprising. Or...freaky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#021FIt's not as if he has what\x01",
            "you'd call a 'common' look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Yeah, I didn't believe he was a priest at first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "But he really looked after us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "We didn't really get a chance to show it,\x01",
            "but we're very, very thankful to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "He even played with the kids\x01",
            "before he left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "He really looked after us right\x01",
            "up until the last minute.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A65)

    label("loc_15A2")

    Jump("loc_1AB2")

    label("loc_15A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 4)), scpexpr(EXPR_END)), "loc_1628")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #54
        0xFE,
        "Chere and Will both want to see Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "When you get some time off work,\x01",
            "you two should come by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB2")

    label("loc_1628")


    ChrTalk(    #56
        0x101,
        "#1018FHeya, Tio!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #57
        0xFE,
        "Ah, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Since Schera's with you, I assume\x01",
            "that means you're on the job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1015FA bit, yeah. We're doing an investigation.\x02\x03",

            "#1006FBut it's not a big case or anything,\x01",
            "so there's no need to worry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #60
        0xFE,
        "Oh, that's good to hear, but...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #61
        0xFE,
        "...Hey, Estelle. What's with those clothes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1016FHaha... You noticed, huh?\x02\x03",

            "Schera got them for me as a present\x01",
            "to celebrate me becoming a full-on bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "So Schera picked them out for you, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "No wonder they're so stylish.\x01",
            "They look great on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Hmm... I might have to look into getting a skirt\x01",
            "like that myself. It's functional AND super-cute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1008FAhaha... Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "I heard about Joshua, too. From Elissa.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I'm sure it's hard on you, Estelle, so if\x01",
            "you ever need an ear, mine is at your disposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Talking about this kind of stuff makes\x01",
            "it a little lighter, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1025FYeah...\x02\x03",

            "Thanks. I might just take you up on that.\x02\x03",

            "#1006FWell then, Tio, hopefully we'll catch you\x01",
            "later. It was fun talking. It's been a while! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "Yeah, it has been.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Talk to you later, Estelle!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_A2(0x189C)

    label("loc_1AB2")

    TalkEnd(0xB)
    Return()

    # Function_7_90C end

    def Function_8_1AB6(): pass

    label("Function_8_1AB6")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 6)), scpexpr(EXPR_END)), "loc_1B6A")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #73
        0xFE,
        (
            "We're in your care again, and not long\x01",
            "after that monster hunt from before, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Having bracers like you around really\x01",
            "is a huge help, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D59")

    label("loc_1B6A")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #75
        0xFE,
        "Ohh, Estelle and Scherazard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Seems we're in your care again,\x01",
            "and not long after that monster hunt\x01",
            "from before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I heard from Father Kevin that apparently\x01",
            "this is all thanks to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1007FNo, no... I've still got a lot to work on.\x02\x03",

            "This case made that pretty clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Haha. That's enough humility from you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "It's the unique privilege of the young to be\x01",
            "able to reflect honestly on their mistakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Be sure you treasure that feeling.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A66)

    label("loc_1D59")

    TalkEnd(0xE)
    Return()

    # Function_8_1AB6 end

    def Function_9_1D5D(): pass

    label("Function_9_1D5D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1DE5")

    ChrTalk(    #82
        0xFE,
        "Father Kevin sure is nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "It was fun talking to him,\x01",
            "and he played with me, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "He's kinda like Joshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F4A")

    label("loc_1DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1F4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 5)), scpexpr(EXPR_END)), "loc_1E49")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #85
        0xFE,
        "Come back again with Joshua sometime, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "I wanna see him, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F4A")

    label("loc_1E49")

    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #87
        0xFE,
        "Oh! Hi, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1000FHello, Chere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "Umm... Where's Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1015FO-Oh... We're, uh, working separately\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Umm... Come by together sometime,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "I wanna see him again, too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x189D)

    label("loc_1F4A")

    TalkEnd(0xD)
    Return()

    # Function_9_1D5D end

    def Function_10_1F4E(): pass

    label("Function_10_1F4E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_20AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FA8")

    ChrTalk(    #94
        0xFE,
        "That priest sure was funny.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "Haha. I hope he comes by again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20A9")

    label("loc_1FA8")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #96
        0xFE,
        "Hi, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "When I woke up, there was this\x01",
            "really weird priest guy,\x01",
            "and I was kinda scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "But, he was actually kinda fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "And he had a reeeally cool weapon, too.\x01",
            "'Specially for a priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "Haha. I hope he comes by again.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_20A9")

    Jump("loc_21E0")

    label("loc_20AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_21E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2133")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #101
        0xFE,
        (
            "You haven't been by in a looong time, either,\x01",
            "AND you've got a job. What's that about?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "Booooriiing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_21E0")

    label("loc_2133")

    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #103
        0xFE,
        "Hiya, Estelle! Did you come to play?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1007FSorry, Will. I can't. I've got work to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "Awww, maaaaaan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "Booooriiing!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_21E0")

    TalkEnd(0xC)
    Return()

    # Function_10_1F4E end

    def Function_11_21E4(): pass

    label("Function_11_21E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2269")
    OP_43(0xFE, 0x2, 0x0, 0xC)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2269")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_2269")
    TalkBegin(0xFE)
    OP_A2(0x5)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #107
        "\x07\x00Received #907i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_2269")

    Return()

    # Function_11_21E4 end

    def Function_12_226A(): pass

    label("Function_12_226A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2285")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_12_226A")

    label("loc_2285")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_226A end

    def Function_13_2290(): pass

    label("Function_13_2290")

    OP_22(0x190, 0x0, 0x64)
    Return()

    # Function_13_2290 end

    def Function_14_2296(): pass

    label("Function_14_2296")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_232D")

    ChrTalk(    #108
        0xFE,
        "*sigh* Isn't that rescue squad here yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "This farm's nice and peaceful, but I'm\x01",
            "worried about the other regions in the\x01",
            "kingdom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D8")

    label("loc_232D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_24D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2428")

    ChrTalk(    #110
        0xFE,
        (
            "I'm a crewmember from the airship that\x01",
            "was stopped on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "We're patrolling around here as our\x01",
            "way of saying thanks to the farm for\x01",
            "taking care of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "This is about all we can do\x01",
            "TO show our thanks, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_24D8")

    label("loc_2428")


    ChrTalk(    #113
        0xFE,
        (
            "We're patrolling around here as our\x01",
            "way of saying thanks to the farm for\x01",
            "taking care of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "The highway lights are off, after all,\x01",
            "so the roads are pretty dangerous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D8")

    TalkEnd(0x15)
    Return()

    # Function_14_2296 end

    def Function_15_24DC(): pass

    label("Function_15_24DC")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_25A3")

    ChrTalk(    #115
        0xFE,
        (
            "It's been a while since I had a chance to just\x01",
            "spend the whole day someplace green like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "It's so peaceful here, I'm halfway forgetting\x01",
            "that we're in a state of emergency.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AD")

    label("loc_25A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_26AD")

    ChrTalk(    #117
        0xFE,
        (
            "The greenhouse and the pump here\x01",
            "have stopped working, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "All the tools and such that make use of\x01",
            "orbal energy have stopped working, from\x01",
            "the looks of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I guess it's thanks to that same phenomenon\x01",
            "that our airship dropped out of the sky...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AD")

    TalkEnd(0x16)
    Return()

    # Function_15_24DC end

    def Function_16_26B1(): pass

    label("Function_16_26B1")

    EventBegin(0x0)
    OP_DB()
    SetChrPos(0x101, 23540, 0, 59780, 180)
    SetChrPos(0x103, 24540, 80, 59780, 180)
    SetChrPos(0x107, 23540, 0, 60780, 180)
    SetChrPos(0x105, 24540, 0, 60780, 180)
    OP_6D(44190, 0, 16580, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3830, 0)
    OP_6C(269000, 0)
    OP_6E(261, 0)
    OP_C8(0x200, 0x46, "C_PLAC14._CH", 0x0, 0x7D0)
    OP_DE("Perzel Farm")
    FadeToBright(2000, 0)

    def lambda_2766():
        OP_6C(0, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2766)
    OP_6D(22290, 0, 23280, 6000)

    def lambda_2787():
        OP_6D(24020, 0, 51850, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2787)
    Sleep(4000)
    OP_43(0x101, 0x1, 0x0, 0x11)
    Sleep(200)
    OP_43(0x103, 0x1, 0x0, 0x12)
    Sleep(200)
    OP_43(0x107, 0x1, 0x0, 0x13)
    Sleep(200)
    OP_43(0x105, 0x1, 0x0, 0x14)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    Fade(1000)
    OP_6D(23830, 50, 51930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_DC()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B3")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as visited yesterday\x01",           # 0
            "Set as didn't visit yesterday\x01",      # 1
            "No change\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_28A7"),
        (1, "loc_28AD"),
        (SWITCH_DEFAULT, "loc_28B3"),
    )


    label("loc_28A7")

    OP_A2(0x1888)
    Jump("loc_28B3")

    label("loc_28AD")

    OP_A3(0x1888)
    Jump("loc_28B3")

    label("loc_28B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 0)), scpexpr(EXPR_END)), "loc_28FE")

    ChrTalk(    #120
        0x101,
        (
            "#1026F#6POh, man, there wasn't even any\x01",
            "fog here yesterday!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2975")

    label("loc_28FE")


    ChrTalk(    #121
        0x101,
        (
            "#1025F#6PTio's house... Ah, here comes another\x01",
            "nostalgia rush.\x02\x03",

            "#1007FBut oh, man, the fog's like soup here,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2975")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #122
        0x103,
        (
            "#020F#4PYes, let's go explain the situation to\x01",
            "Mr. Perzel.\x02\x03",

            "I doubt even Franz would try to go and\x01",
            "make a delivery out in this mess...\x01",
            "I hope, anyway.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #123
        0x101,
        "#1015F#6PWelllll...knowing Mr. Perzel, I dunno.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(200)
    OP_22(0x118, 0x0, 0x4B)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2AD4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2AD4)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #124
        0x107,
        "#065FThat was...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        "#042F#4PNo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1005F#6PSCHERA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x103,
        "#024F#4PCome on!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x56)
    Sleep(300)

    def lambda_2B44():
        OP_6D(23310, 0, 25480, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B44)

    def lambda_2B5C():
        OP_67(0, 5180, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B5C)

    def lambda_2B74():
        OP_6E(290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B74)

    def lambda_2B84():
        OP_6B(3190, 4000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2B84)

    def lambda_2B94():
        OP_6C(180000, 4000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_2B94)
    OP_43(0x101, 0x1, 0x0, 0x15)
    Sleep(300)
    OP_43(0x103, 0x1, 0x0, 0x16)
    Sleep(200)
    OP_43(0x107, 0x1, 0x0, 0x17)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x18)
    OP_A2(0x1820)
    OP_28(0x91, 0x1, 0x4)
    LoadEffect(0x0, "map\\\\mp107_00.eff")
    Sleep(2800)
    SetChrPos(0x8, 21820, 1200, 25100, 45)
    SetChrPos(0x9, 20580, 1300, 25650, 45)
    SetChrPos(0xA, 22800, 1300, 23640, 45)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x8, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)

    def lambda_2CA2():
        OP_8F(0xFE, 0x553C, 0x2BC, 0x620C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2CA2)

    def lambda_2CBD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2CBD)
    Sleep(300)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x9, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)

    def lambda_2D13():
        OP_8F(0xFE, 0x5064, 0x320, 0x6432, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2D13)

    def lambda_2D2E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D2E)
    Sleep(300)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xA, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)

    def lambda_2D84():
        OP_8F(0xFE, 0x5910, 0x320, 0x5C58, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2D84)

    def lambda_2D9F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2D9F)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #128
        0x101,
        "#1020F#1PWhat th-!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    ChrTalk(    #129
        0x101,
        "#1005F#1PThe heck are THESE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x105,
        "#043F#1PMonsters made of...fog?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x107,
        "#065F#1PWhaaa?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x103,
        (
            "#024F#1PWe've no time for debate!\x01",
            "Take them down!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 5)
    SetChrSubChip(0x103, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 7)
    SetChrSubChip(0x105, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 3)
    SetChrSubChip(0x107, 0)
    OP_0D()
    Sleep(500)

    def lambda_2ED6():
        OP_6D(22500, 0, 26430, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ED6)

    def lambda_2EEE():
        OP_6B(2400, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EEE)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 2)

    def lambda_2F08():
        OP_8E(0xFE, 0x5758, 0x0, 0x6BBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F08)
    SetChrChipByIndex(0x8, 9)

    def lambda_2F28():
        OP_8E(0xFE, 0x5712, 0x1F4, 0x6626, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2F28)
    Sleep(50)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 6)

    def lambda_2F52():
        OP_8E(0xFE, 0x5B0E, 0x0, 0x69B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2F52)
    SetChrChipByIndex(0x9, 9)

    def lambda_2F72():
        OP_8E(0xFE, 0x52F8, 0x258, 0x66B2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2F72)
    Sleep(50)
    SetChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x107, 4)

    def lambda_2F9C():
        OP_8E(0xFE, 0x573A, 0x0, 0x6FC2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2F9C)
    SetChrChipByIndex(0xA, 9)

    def lambda_2FBC():
        OP_8E(0xFE, 0x59F6, 0x2BC, 0x62D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2FBC)
    Sleep(50)
    SetChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x105, 8)

    def lambda_2FE6():
        OP_8E(0xFE, 0x5B0E, 0x5A, 0x69B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2FE6)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x799, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3035"),
        (SWITCH_DEFAULT, "loc_303A"),
    )


    label("loc_3035")

    OP_B4(0x0)
    Jump("loc_303A")

    label("loc_303A")

    Call(0, 25)
    Return()

    # Function_16_26B1 end

    def Function_17_303F(): pass

    label("Function_17_303F")

    OP_8E(0xFE, 0x5BF4, 0x46, 0xC738, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(100)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_17_303F end

    def Function_18_3084(): pass

    label("Function_18_3084")

    OP_8E(0xFE, 0x5FDC, 0x64, 0xC738, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    OP_8C(0xFE, 180, 400)
    Sleep(100)
    OP_8C(0xFE, 225, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_18_3084 end

    def Function_19_30C9(): pass

    label("Function_19_30C9")

    OP_8E(0xFE, 0x5BF4, 0xDC, 0xCB20, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Sleep(100)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_19_30C9 end

    def Function_20_3102(): pass

    label("Function_20_3102")

    OP_8E(0xFE, 0x5FDC, 0xC8, 0xCB20, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Sleep(100)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_20_3102 end

    def Function_21_313B(): pass

    label("Function_21_313B")

    OP_8E(0xFE, 0x5E56, 0x0, 0xBC8E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5E24, 0x0, 0x8CA0, 0x1388, 0x0)
    OP_8E(0xFE, 0x5CF8, 0x50, 0x74A4, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_21_313B end

    def Function_22_317F(): pass

    label("Function_22_317F")

    OP_8E(0xFE, 0x5E56, 0x0, 0xBC8E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5E24, 0x0, 0x9088, 0x1388, 0x0)
    OP_8E(0xFE, 0x6158, 0x3C, 0x7260, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_22_317F end

    def Function_23_31C3(): pass

    label("Function_23_31C3")

    OP_8E(0xFE, 0x5E56, 0x0, 0xBC8E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5E24, 0x0, 0x9470, 0x1388, 0x0)
    OP_8E(0xFE, 0x5DCA, 0x14, 0x7AB2, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_23_31C3 end

    def Function_24_3207(): pass

    label("Function_24_3207")

    OP_8E(0xFE, 0x5E56, 0x0, 0xBC8E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5E24, 0x0, 0x9858, 0x1388, 0x0)
    OP_8E(0xFE, 0x61E4, 0x0, 0x77F6, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_24_3207 end

    def Function_25_324B(): pass

    label("Function_25_324B")

    EventBegin(0x0)
    OP_1D(0x51)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_44(0x101, 0x0)
    OP_44(0x103, 0x0)
    OP_44(0x107, 0x0)
    OP_44(0x105, 0x0)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x107, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x101, 21610, 0, 25150, 225)
    SetChrPos(0x103, 22820, 0, 25050, 135)
    SetChrPos(0x107, 22880, 0, 26430, 90)
    SetChrPos(0x105, 21580, 0, 26380, 315)
    OP_6D(21690, 0, 25340, 0)
    OP_67(0, 8180, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x1, 0x0, 0x1E)
    OP_43(0x103, 0x1, 0x0, 0x1F)
    OP_43(0x107, 0x1, 0x0, 0x20)
    OP_43(0x105, 0x1, 0x0, 0x21)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #133
        0x101,
        "#1026FDid we beat them?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 270, 400)

    ChrTalk(    #134
        0x103,
        (
            "#022FYes, but...they were simply a\x01",
            "roadblock.\x02\x03",

            "We need to find the Perzels. Now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33E6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33E6)
    Sleep(100)

    def lambda_33F9():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_33F9)
    Sleep(100)
    OP_8C(0x105, 160, 400)

    ChrTalk(    #135
        0x101,
        "#1005F#4PRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1821)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_25_324B end

    def Function_26_342D(): pass

    label("Function_26_342D")

    OP_8E(0xFE, 0x5B4A, 0x1E, 0x744A, 0x1388, 0x0)
    OP_8C(0xFE, 203, 400)
    Return()

    # Function_26_342D end

    def Function_27_3449(): pass

    label("Function_27_3449")

    OP_8E(0xFE, 0x5F96, 0x1E, 0x7288, 0x1388, 0x0)
    OP_8C(0xFE, 203, 400)
    Return()

    # Function_27_3449 end

    def Function_28_3465(): pass

    label("Function_28_3465")

    OP_8E(0xFE, 0x5C44, 0xA0, 0x79CC, 0x1388, 0x0)
    OP_8C(0xFE, 203, 400)
    Return()

    # Function_28_3465 end

    def Function_29_3481(): pass

    label("Function_29_3481")

    OP_8E(0xFE, 0x6266, 0x0, 0x76FC, 0x1388, 0x0)
    OP_8C(0xFE, 203, 400)
    Return()

    # Function_29_3481 end

    def Function_30_349D(): pass

    label("Function_30_349D")

    Sleep(400)
    OP_8C(0xFE, 340, 400)
    Sleep(500)
    OP_8C(0xFE, 250, 400)
    Sleep(100)
    OP_8C(0xFE, 161, 400)
    Sleep(500)
    OP_8C(0xFE, 206, 400)
    Return()

    # Function_30_349D end

    def Function_31_34CE(): pass

    label("Function_31_34CE")

    Sleep(550)
    OP_8C(0xFE, 250, 400)
    Sleep(200)
    OP_8C(0xFE, 120, 400)
    Sleep(500)
    OP_8C(0xFE, 70, 400)
    Return()

    # Function_31_34CE end

    def Function_32_34F3(): pass

    label("Function_32_34F3")

    Sleep(450)
    OP_8C(0xFE, 70, 400)
    Sleep(600)
    OP_8C(0xFE, 300, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_32_34F3 end

    def Function_33_3518(): pass

    label("Function_33_3518")

    Sleep(500)
    OP_8C(0xFE, 340, 400)
    Sleep(200)
    OP_8C(0xFE, 116, 400)
    Sleep(400)
    OP_8C(0xFE, 250, 400)
    Return()

    # Function_33_3518 end

    def Function_34_353D(): pass

    label("Function_34_353D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36B1")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3596")

    ChrTalk(    #136
        0x101,
        "#1000F(What am I doing?! This is the long way around!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3691")

    label("loc_3596")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F2")

    ChrTalk(    #137
        0x101,
        "#1000FHey, Schera, that's the long way around!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        "#020FOops! Got'cha.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3691")

    label("loc_35F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3648")

    ChrTalk(    #139
        0x101,
        "#1000FHey, Kloe, that's the long way around!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x105,
        "#040FOh, sorry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3691")

    label("loc_3648")


    ChrTalk(    #141
        0x101,
        "#1000FHey, Tita, that's the long way around!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x107,
        "#060FOh! R-Right!\x02",
    )

    CloseMessageWindow()

    label("loc_3691")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_36B1")

    Return()

    # Function_34_353D end

    def Function_35_36B2(): pass

    label("Function_35_36B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_382D")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3709")

    ChrTalk(    #143
        0x101,
        "#1002F(What am I even doing?! I've got to find Tio!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_380D")

    label("loc_3709")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3762")

    ChrTalk(    #144
        0x103,
        (
            "#022F(We can't be wasting time right now.\x01",
            "We've got people to find!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_380D")

    label("loc_3762")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D0")

    ChrTalk(    #145
        0x105,
        (
            "#042F(...This is the exit. We're not ready\x01",
            "to leave yet. There are still people\x01",
            "to find!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_380D")

    label("loc_37D0")


    ChrTalk(    #146
        0x101,
        "#1002FIsn't that the exit, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x107,
        "#062FOh! R-Right!\x02",
    )

    CloseMessageWindow()

    label("loc_380D")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_382D")

    Return()

    # Function_35_36B2 end

    def Function_36_382E(): pass

    label("Function_36_382E")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #148
        "\x07\x05The door is locked.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D2")

    ChrTalk(    #149
        0x101,
        "#1004FHuh? Why's it locked?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x103,
        "#022FLet's look for another way in.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_38D2")

    TalkEnd(0xFF)
    Return()

    # Function_36_382E end

    SaveToFile()

Try(main)
