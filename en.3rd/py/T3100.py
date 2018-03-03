from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Escalator Thread',                     # 9
        'Dan',                                  # 10
        'Tita',                                 # 11
        'Erika',                                # 12
        'Elise',                                # 13
        'Vince',                                # 14
        'Knowles',                              # 15
        'Monika',                               # 16
        'Cosimo',                               # 17
        'Bruno',                                # 18
        'Target Camera',                        # 19
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
        'ED6_DT27/CH03980 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH01470 ._CH',             # 03
        'ED6_DT07/CH01060 ._CH',             # 04
        'ED6_DT07/CH02490 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
        'ED6_DT07/CH01530 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03980P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH01470P._CP',             # 03
        'ED6_DT07/CH01060P._CP',             # 04
        'ED6_DT07/CH02490P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
        'ED6_DT07/CH01530P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C0,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14850,
        Z                   = 3500,
        Y                   = 72210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 16520,
        Z                   = 3500,
        Y                   = 73590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 47550,
        Z                   = 0,
        Y                   = 64810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 47500,
        Z                   = 0,
        Y                   = 65880,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 37980,
        Z                   = 0,
        Y                   = 77980,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 36810,
        Z                   = 0,
        Y                   = 45690,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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


    DeclEvent(
        X                   = 39780,
        Y                   = 0,
        Z                   = 90710,
        Range               = 46240,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x16544,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = 69760,
        Y                   = 0,
        Z                   = 48040,
        Range               = 70360,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xE20E,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = 33000,
        TriggerZ            = 500,
        TriggerY            = 85510,
        TriggerRange        = 800,
        ActorX              = 33000,
        ActorZ              = 1500,
        ActorY              = 85510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_363",          # 01, 1
        "Function_2_3C7",          # 02, 2
        "Function_3_544",          # 03, 3
        "Function_4_754",          # 04, 4
        "Function_5_9A0",          # 05, 5
        "Function_6_BAE",          # 06, 6
        "Function_7_CEE",          # 07, 7
        "Function_8_E4D",          # 08, 8
        "Function_9_1088",         # 09, 9
        "Function_10_1243",        # 0A, 10
        "Function_11_16A2",        # 0B, 11
        "Function_12_1948",        # 0C, 12
        "Function_13_1A10",        # 0D, 13
        "Function_14_1CB6",        # 0E, 14
        "Function_15_1DBB",        # 0F, 15
        "Function_16_1DF3",        # 10, 16
        "Function_17_1F17",        # 11, 17
        "Function_18_204A",        # 12, 18
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E2")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)

    label("loc_2E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_317")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_304")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_317")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_317")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_317")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_339")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_362")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_34F")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_362")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_362")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_362")

    Return()

    # Function_0_2AE end

    def Function_1_363(): pass

    label("Function_1_363")

    OP_16(0x2, 0xFA0, 0xFFFE94B8, 0xFFFEF278, 0x230051)
    OP_43(0x10, 0x0, 0x0, 0xF)
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    SoundDistance(0xA0, 0x1CC, 0xADC, 0xE63C, 0x2710, 0x7530, 0x64, 0x0)
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C6")
    OP_B2(0x1, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)

    label("loc_3C6")

    Return()

    # Function_1_363 end

    def Function_2_3C7(): pass

    label("Function_2_3C7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_52E")

    label("loc_3EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_405")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_52E")

    label("loc_405")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_52E")

    label("loc_41E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_52E")

    label("loc_437")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_450")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_52E")

    label("loc_450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_469")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_52E")

    label("loc_469")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_52E")

    label("loc_482")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_52E")

    label("loc_49B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_52E")

    label("loc_4B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_52E")

    label("loc_4CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_52E")

    label("loc_4E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_52E")

    label("loc_4FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_518")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_52E")

    label("loc_518")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_52E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_543")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_52E")

    label("loc_543")

    Return()

    # Function_2_3C7 end

    def Function_3_544(): pass

    label("Function_3_544")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_565"),
        (1, "loc_583"),
        (2, "loc_5A1"),
        (SWITCH_DEFAULT, "loc_5FB"),
    )


    label("loc_565")

    SetChrPos(0x18, 34000, 0, 71810, 90)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FB")

    label("loc_583")

    SetChrPos(0x18, 10000, 0, 71120, 90)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FB")

    label("loc_5A1")

    SetChrPos(0x18, 21000, 0, 69900, 357)
    OP_8E(0xFE, 0x5208, 0x0, 0x12322, 0x7D0, 0x0)
    OP_8E(0xFE, 0x506E, 0x0, 0x1262E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4DD0, 0x0, 0x128E0, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FB")

    label("loc_5FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_753")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_657")
    OP_8E(0xFE, 0x84D0, 0x0, 0x12124, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8070, 0x0, 0x1264C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7CBA, 0x0, 0x128E0, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_657")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AA")
    OP_8E(0xFE, 0x2D82, 0x0, 0x128E0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2940, 0x0, 0x1266A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2710, 0x0, 0x12214, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD")
    OP_8E(0xFE, 0x2710, 0x0, 0xF352, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2AA8, 0x0, 0xF064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2F62, 0x0, 0xEC54, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_750")
    OP_8E(0xFE, 0x803E, 0x0, 0xEC54, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8444, 0x0, 0xEFF6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0x0, 0xF488, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_750")

    Jump("loc_5FB")

    label("loc_753")

    Return()

    # Function_3_544 end

    def Function_4_754(): pass

    label("Function_4_754")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_99C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_847")

    ChrTalk(    #0
        0xFE,
        "Heehee. Manoria Village really was a lovely place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "They're apparently going to be holding a bazaar\x01",
            "there at some point in the future, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Maybe I should use that as an excuse to head\x01",
            "back for another visit!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99C")

    label("loc_847")


    ChrTalk(    #3
        0xFE,
        (
            "I paid a visit to Manoria Village over near Ruan\x01",
            "a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "It was quite easy to see why Irene\x01",
            "recommended it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Oh! Irene sells flowers, by the way. And there\x01",
            "were beautiful flowers everywhere there! Now\x01",
            "I know why it's famous for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Much as I like living here, I'd love to live\x01",
            "in a place like that if I could. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_99C")

    TalkEnd(0xFE)
    Return()

    # Function_4_754 end

    def Function_5_9A0(): pass

    label("Function_5_9A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A58")

    ChrTalk(    #7
        0xFE,
        (
            "I'll never be able to forget the sight of that \x01",
            "flying structure collapsing before my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I think I'll still be able to recall it even on my\x01",
            "death bed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAA")

    label("loc_A58")


    ChrTalk(    #9
        0xFE,
        (
            "I'm glad the domestic situation's finally calmed\x01",
            "down now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "My mother seems to have put all that happened\x01",
            "out of her mind and forgotten about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "...but not me. I'll never be able to forget the sight\x01",
            "of that flying structure collapsing before my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I think I'll still be able to recall it even on my\x01",
            "death bed.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_BAA")

    TalkEnd(0xFE)
    Return()

    # Function_5_9A0 end

    def Function_6_BAE(): pass

    label("Function_6_BAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_BEF")

    ChrTalk(    #13
        0xFE,
        "Okay! Here goes, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "One, two...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEA")

    label("loc_BEF")

    OP_4A(0x17, 255)

    ChrTalk(    #15
        0x16,
        "Just take a quick look and then go with your gut.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x16,
        (
            "Choose the apple out of the basket that grabs\x01",
            "your attention most, and you can't go wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x16,
        "These things are all about instinct!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x17,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x17,
        "All right. I'll go with that.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    OP_A2(0x4)

    label("loc_CEA")

    TalkEnd(0xFE)
    Return()

    # Function_6_BAE end

    def Function_7_CEE(): pass

    label("Function_7_CEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D4B")

    ChrTalk(    #20
        0xFE,
        "Actually, WAIT!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I don't think I'm mentally ready for this yet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E49")

    label("loc_D4B")

    OP_4A(0x16, 255)

    ChrTalk(    #22
        0x16,
        "Just take a quick look and then go with your gut.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x16,
        (
            "Choose the apple out of the basket that grabs your\x01",
            "attention the most and you can't go wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x16,
        "These things are all about instinct!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x17,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x17,
        "All right. I'll go with that.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x16, 255)
    OP_A2(0x4)

    label("loc_E49")

    TalkEnd(0xFE)
    Return()

    # Function_7_CEE end

    def Function_8_E4D(): pass

    label("Function_8_E4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_1084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_EFA")

    ChrTalk(    #27
        0xFE,
        "I'll remember that day as long as I live.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "She came right to me after it happened, crying\x01",
            "her eyes out...and then launched a flying kick at\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1084")

    label("loc_EFA")


    ChrTalk(    #29
        0xFE,
        (
            "So that troublemaker Erika is finally back in town,\x01",
            "is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "It baffles me how that woman turned out.\x01",
            "She used to be such a pretty little thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "When she was younger, she always used to go\x01",
            "on about how she wanted to be a sister of the\x01",
            "church when she grew up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Her personality was the same as it is now,\x01",
            "though. Father Vixen told her flat out, 'Not\x01",
            "with YOUR personality.'\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1084")

    TalkEnd(0xFE)
    Return()

    # Function_8_E4D end

    def Function_9_1088(): pass

    label("Function_9_1088")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_123F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_117A")

    ChrTalk(    #33
        0xFE,
        (
            "If you live in Zeiss for long enough, you kind of\x01",
            "naturally learn how to do these kinds of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "It's a useful skill if you ever try to go anywhere\x01",
            "else, actually. These skills aren't half as common\x01",
            "elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123F")

    label("loc_117A")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #35
        0xFE,
        (
            "Oops... Looks like the orbal engine's not\x01",
            "in very good shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "No surprise with how hard I've been working\x01",
            "this baby lately, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Let's get the hood off and take a look.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_123F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1088 end

    def Function_10_1243(): pass

    label("Function_10_1243")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(30600, 0, 60800, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(432, 0)
    OP_4A(0x18, 255)
    SetChrPos(0x18, 34580, 0, 60020, 270)

    def lambda_12A7():
        OP_8F(0xFE, 0x2328, 0x0, 0xEA74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_12A7)
    SetChrPos(0x106, 7260, 60, 61360, 90)
    SetChrFlags(0x106, 0x8)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 12000, 0, 75840, 90)

    def lambda_12EE():
        OP_6D(26680, 0, 75360, 10000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_12EE)

    def lambda_1306():
        OP_6C(120000, 10000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1306)
    FadeToBright(2000, 0)

    def lambda_131F():
        OP_8E(0xFE, 0x6590, 0x0, 0x12840, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_131F)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    OP_8C(0x12, 135, 500)
    Sleep(800)
    OP_8C(0x12, 45, 500)
    Sleep(800)
    OP_8C(0x12, 90, 500)
    WaitChrThread(0x1A, 0x0)
    Fade(1000)
    OP_6D(26420, 0, 75500, 0)
    OP_67(0, 8039, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(120000, 0)
    OP_6E(260, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x12, 135, 500)
    Sleep(800)
    OP_8C(0x12, 45, 500)
    Sleep(800)
    OP_8C(0x12, 90, 500)
    Sleep(500)

    ChrTalk(    #38
        0x12,
        (
            "#063FWhere is she?\x02\x03",

            "I could've sworn I saw her running this way...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #39
        0x12,
        "#561FWhere could she have gone?\x02",
    )

    CloseMessageWindow()

    def lambda_1460():
        OP_8E(0xFE, 0x8E94, 0x0, 0x12840, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1460)
    Sleep(2000)
    ClearChrFlags(0x106, 0x8)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x19, 25780, 0, 57700, 270)

    def lambda_149B():
        OP_8F(0xFE, 0x22C4, 0x0, 0xE164, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_149B)

    def lambda_14B6():
        OP_6D(12960, 0, 61690, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_14B6)

    def lambda_14CE():
        OP_6C(666000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_14CE)

    def lambda_14DE():
        OP_67(0, 8560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_14DE)

    def lambda_14F6():
        OP_6E(282, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_14F6)
    Sleep(3000)

    def lambda_150B():
        OP_8E(0xFE, 0x6978, 0x0, 0xEBF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_150B)
    Sleep(2000)

    def lambda_152B():
        OP_6D(25300, 0, 61320, 8000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_152B)
    Sleep(2000)

    ChrTalk(    #40 op#A op#5
        0x106,
        (
            "#053F#5P#30AProbably shouldn't have arrived so early...\x02\x03",

            "#053F#5P#45AMight as well drop by the guild and see if\x01",
            "there's any work to do until evening.\x05\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x106, 0x1)
    OP_59()
    Sleep(300)

    def lambda_15EF():
        OP_6D(25040, 0, 65400, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_15EF)

    def lambda_1607():
        OP_6C(320000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1607)

    def lambda_1617():
        OP_67(0, 6860, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1617)
    OP_8C(0x106, 0, 400)

    def lambda_1636():
        OP_8E(0xFE, 0x6978, 0x0, 0xF80C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1636)
    WaitChrThread(0x106, 0x1)
    OP_70(0xC, 0x1E)
    OP_73(0xC)

    def lambda_1660():
        OP_8E(0xFE, 0x6978, 0x1F4, 0xFFDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1660)
    Sleep(500)

    def lambda_1680():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1680)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1243 end

    def Function_11_16A2(): pass

    label("Function_11_16A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(29020, 0, 61520, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 35180, 0, 60000, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 28260, 0, 68000, 0)

    def lambda_1722():
        OP_6B(2700, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1722)
    FadeToBright(2000, 0)

    def lambda_173B():
        OP_8E(0xFE, 0x6B6C, 0x0, 0xEA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_173B)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #41
        0x12,
        (
            "#561FI can't find her anywhere in town at all...\x01",
            "and she hasn't gone home...\x02\x03",

            "Just where could Mom have run off to?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(600)

    NpcTalk(    #42
        0x13,
        "Female Voice",
        "#4P...It's not my fault you're not listening to me.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #43
        0x13,
        "Female Voice",
        (
            "#4PAs I said, if you help with these tests, I might \x01",
            "even be gracious enough to consider reducing\x01",
            "your punishment. A little.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x12, 0, 400)
    Sleep(300)

    ChrTalk(    #44
        0x12,
        (
            "#064FThat sounded like Mom.\x02\x03",

            "Could she be in the guild...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_191B():
        OP_8E(0xFE, 0x6B6C, 0x0, 0xF870, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_191B)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_16A2 end

    def Function_12_1948(): pass

    label("Function_12_1948")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(54480, 0, 66180, 0)
    OP_67(0, 8340, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(320000, 0)
    OP_6E(520, 0)
    SetChrPos(0x107, 48000, 0, 17800, 0)
    OP_22(0x1C2, 0x0, 0x64)

    def lambda_19AD():
        OP_6D(53400, 0, 22600, 13000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_19AD)

    def lambda_19C5():
        OP_6C(230000, 13000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_19C5)

    def lambda_19D5():
        OP_67(0, 6850, -10000, 13000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_19D5)
    FadeToBright(4000, 0)
    WaitChrThread(0x1A, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_23(0x1C2)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1948 end

    def Function_13_1A10(): pass

    label("Function_13_1A10")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(59400, 500, 23660, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(216000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x107, 0x40)
    SetChrFlags(0x107, 0x4)
    SetChrPos(0x107, 59900, 500, 24160, 0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x11, 59800, 500, 23160, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #45
        0x107,
        "#4PAll right! I'm off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        (
            "#5PTake care. Don't go trying to run over to\x01",
            "ZCF so fast you trip or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        "#4PI-I won't!\x02",
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x107, 0x40)
    ClearChrFlags(0x107, 0x4)
    SetChrPos(0x107, 59800, 500, 23160, 0)
    Sleep(500)

    def lambda_1B4F():
        OP_67(0, 6800, -10000, 2200)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1B4F)
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_70(0xA, 0x1D)
    OP_73(0xA)

    def lambda_1B77():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1B77)

    def lambda_1B89():
        OP_8E(0xFE, 0xE998, 0x0, 0x6400, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1B89)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_8C(0x107, 180, 500)
    Sleep(300)
    OP_72(0x200A, 0x0)
    ExitThread()
    OP_72(0xA, 0x8)
    ExitThread()
    OP_6F(0xA, 29)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0xA, 0x0)
    OP_73(0xA)
    Sleep(500)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #48
        0x107,
        (
            "#066F#12P(Heehee...)\x02\x03",

            "#067F(It's so great to have them back home.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 600)
    Sleep(500)

    ChrTalk(    #49
        0x107,
        "#560F#5P(And now it's off to the factory!)\x02",
    )

    CloseMessageWindow()

    def lambda_1C84():
        OP_8E(0xFE, 0xE998, 0x0, 0xB220, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C84)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1A10 end

    def Function_14_1CB6(): pass

    label("Function_14_1CB6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(6980, 0, 64160, 0)
    OP_67(0, 9020, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(302, 0)
    SetChrPos(0x107, 1860, 2250, 61700, 90)

    def lambda_1D16():
        OP_67(0, 7020, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1D16)

    def lambda_1D2E():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1D2E)
    FadeToBright(2000, 0)
    Sleep(6000)

    def lambda_1D4C():
        OP_8E(0xFE, 0x24E0, 0x0, 0xF104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1D4C)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_8C(0x107, 135, 500)
    Sleep(600)
    OP_8C(0x107, 0, 500)
    Sleep(300)

    def lambda_1D89():
        OP_8E(0xFE, 0x24E0, 0x0, 0x1287C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1D89)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1CB6 end

    def Function_15_1DBB(): pass

    label("Function_15_1DBB")

    OP_72(0x2010, 0x0)
    ExitThread()
    OP_72(0x200E, 0x0)
    ExitThread()

    label("loc_1DC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF2")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_1DC7")

    label("loc_1DF2")

    Return()

    # Function_15_1DBB end

    def Function_16_1DF3(): pass

    label("Function_16_1DF3")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E7F")

    ChrTalk(    #50
        0x106,
        (
            "#053FThat new weapon's supposedly being developed\x01",
            "over in Zeiss Central Factory.\x02\x03",

            "#057FI'd better hurry over there... Ugh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F00")

    label("loc_1E7F")


    ChrTalk(    #51
        0x106,
        (
            "#052FWait. This way leads outta town, doesn't it?\x02\x03",

            "#057FCan't make my exit when I've gotta hurry to\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1F00")

    OP_90(0x106, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_16_1DF3 end

    def Function_17_1F17(): pass

    label("Function_17_1F17")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1FB2")

    ChrTalk(    #52
        0x106,
        (
            "#053FKilika said that weapon's being developed over\x01",
            "at the central factory.\x02\x03",

            "#057FI ain't happy about this, but I've gotta get a\x01",
            "move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2033")

    label("loc_1FB2")


    ChrTalk(    #53
        0x106,
        (
            "#052FWait. This way leads outta town, doesn't it?\x02\x03",

            "#057FCan't make my exit when I've gotta hurry to\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2033")

    OP_90(0x106, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_17_1F17 end

    def Function_18_204A(): pass

    label("Function_18_204A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #54
        (
            "\x07\x05'First Orbally-Powered Clock'\x01",
            "Made in year 1162 of the Septian Calendar\x01",
            "by Zeissian manufacturers.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_18_204A end

    SaveToFile()

Try(main)
