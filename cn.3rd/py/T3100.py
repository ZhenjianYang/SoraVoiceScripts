from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '自动扶梯',                             # 9
        '丹',                                   # 10
        '提妲',                                 # 11
        '艾莉卡',                               # 12
        '阿利瑟',                               # 13
        '温丝',                                 # 14
        '库诺',                                 # 15
        '莫妮卡',                               # 16
        '科奇莫爷爷',                           # 17
        '布鲁诺',                               # 18
        '目标用照相机',                         # 19
        '',                                     # 20
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
        "Function_5_8B5",          # 05, 5
        "Function_6_9C2",          # 06, 6
        "Function_7_AD8",          # 07, 7
        "Function_8_C06",          # 08, 8
        "Function_9_D60",          # 09, 9
        "Function_10_E6E",         # 0A, 10
        "Function_11_12AB",        # 0B, 11
        "Function_12_14CC",        # 0C, 12
        "Function_13_1594",        # 0D, 13
        "Function_14_182C",        # 0E, 14
        "Function_15_1931",        # 0F, 15
        "Function_16_1969",        # 10, 16
        "Function_17_1A30",        # 11, 17
        "Function_18_1AF7",        # 12, 18
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_8B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7E9")

    ChrTalk(    #0
        0xFE,
        (
            "呵呵，玛诺利亚村\x01",
            "是个很好的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "……这么说来，\x01",
            "下次村里好像要开义卖会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "到时我一定要\x01",
            "再去一次才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B1")

    label("loc_7E9")


    ChrTalk(    #3
        0xFE,
        (
            "之前我去了\x01",
            "以花闻名的玛诺利亚村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "卖花的爱玲小姐\x01",
            "推荐的果然名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "呵呵，\x01",
            "村里到处都开满了漂亮的花朵哦。\x02",
        )
    )

    Jump("loc_872")

    label("loc_872")

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "虽然不是不喜欢蔡斯，\x01",
            "但我还真想住在那样的村子里呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_8B1")

    TalkEnd(0xFE)
    Return()

    # Function_4_754 end

    def Function_5_8B5(): pass

    label("Function_5_8B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_9BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_921")

    ChrTalk(    #7
        0xFE,
        (
            "那个浮游物体的崩毁\x01",
            "令人无法忘怀啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "……那恐怕一辈子\x01",
            "都会留在我的记忆中。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BE")

    label("loc_921")


    ChrTalk(    #9
        0xFE,
        (
            "那个异常事件\x01",
            "似乎也了结了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "虽然母亲似乎\x01",
            "完全忘记了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "但我可忘不了\x01",
            "那个浮游物体\x01",
            "崩毁的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "……大概会一辈子留在记忆中吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_9BE")

    TalkEnd(0xFE)
    Return()

    # Function_5_8B5 end

    def Function_6_9C2(): pass

    label("Function_6_9C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A00")

    ChrTalk(    #13
        0xFE,
        "那，开始吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "一～二…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD4")

    label("loc_A00")

    OP_4A(0x17, 255)

    ChrTalk(    #15
        0x16,
        (
            "所以说，\x01",
            "靠第一印象就好啦。\x02",
        )
    )

    Jump("loc_A32")

    label("loc_A32")

    CloseMessageWindow()

    ChrTalk(    #16
        0x16,
        (
            "选择筐子里\x01",
            "自己最喜欢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x16,
        (
            "这种啊，\x01",
            "要靠直觉嘛。\x02",
        )
    )

    Jump("loc_A7C")

    label("loc_A7C")

    CloseMessageWindow()

    ChrTalk(    #18
        0x17,
        "嗯嗯……\x02",
    )

    Jump("loc_A98")

    label("loc_A98")

    CloseMessageWindow()

    ChrTalk(    #19
        0x17,
        (
            "一下子冲出去，\x01",
            "挑自己最喜欢的\x01",
            "苹果就行了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    OP_A2(0x4)

    label("loc_AD4")

    TalkEnd(0xFE)
    Return()

    # Function_6_9C2 end

    def Function_7_AD8(): pass

    label("Function_7_AD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_C02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B2E")

    ChrTalk(    #20
        0xFE,
        (
            "啊啊，\x01",
            "稍微等一下！\x02",
        )
    )

    Jump("loc_B0C")

    label("loc_B0C")

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "我还没做好心理准备……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C02")

    label("loc_B2E")

    OP_4A(0x16, 255)

    ChrTalk(    #22
        0x16,
        (
            "所以说，\x01",
            "靠第一印象就好啦。\x02",
        )
    )

    Jump("loc_B60")

    label("loc_B60")

    CloseMessageWindow()

    ChrTalk(    #23
        0x16,
        (
            "选择筐子里\x01",
            "自己最喜欢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x16,
        (
            "这种啊，\x01",
            "要靠直觉嘛。\x02",
        )
    )

    Jump("loc_BAA")

    label("loc_BAA")

    CloseMessageWindow()

    ChrTalk(    #25
        0x17,
        "嗯嗯……\x02",
    )

    Jump("loc_BC6")

    label("loc_BC6")

    CloseMessageWindow()

    ChrTalk(    #26
        0x17,
        (
            "一下子冲出去，\x01",
            "挑自己最喜欢的\x01",
            "苹果就行了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x16, 255)
    OP_A2(0x4)

    label("loc_C02")

    TalkEnd(0xFE)
    Return()

    # Function_7_AD8 end

    def Function_8_C06(): pass

    label("Function_8_C06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_D5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(    #27
        0xFE,
        (
            "………………我也还清楚记得\x01",
            "那天的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "艾莉卡那家伙，\x01",
            "哇哇大哭着就冲我飞踢过来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5C")

    label("loc_C7C")


    ChrTalk(    #29
        0xFE,
        (
            "艾莉卡好像回去了啊。\x01",
            "那个野丫头………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "别看她这样，\x01",
            "小时候也是个相当可爱的女孩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "还把将来要当修女\x01",
            "当成口头禅一样挂在嘴边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "性格却跟现在没什么两样，\x01",
            "教区长也说\x01",
            "『你这性格是不可能的』。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_D5C")

    TalkEnd(0xFE)
    Return()

    # Function_8_C06 end

    def Function_9_D60(): pass

    label("Function_9_D60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_DD5")

    ChrTalk(    #33
        0xFE,
        (
            "既然住在蔡斯，\x01",
            "这点事情\x01",
            "还是办得到的。\x02",
        )
    )

    Jump("loc_DAA")

    label("loc_DAA")

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "要是去别的地方\x01",
            "可能就难说了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6A")

    label("loc_DD5")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #35
        0xFE,
        (
            "哎呀……\x01",
            "导力引擎的情况不妙啊。\x02",
        )
    )

    Jump("loc_E0E")

    label("loc_E0E")

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "最近一直在不停运转，\x01",
            "脾气变坏了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "打开盖子\x01",
            "稍微看看情况吧。\x02",
        )
    )

    Jump("loc_E66")

    label("loc_E66")

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_E6A")

    TalkEnd(0xFE)
    Return()

    # Function_9_D60 end

    def Function_10_E6E(): pass

    label("Function_10_E6E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(30600, 0, 60800, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(432, 0)
    OP_4A(0x18, 255)
    SetChrPos(0x18, 34580, 0, 60020, 270)

    def lambda_ED2():
        OP_8F(0xFE, 0x2328, 0x0, 0xEA74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_ED2)
    SetChrPos(0x106, 7260, 60, 61360, 90)
    SetChrFlags(0x106, 0x8)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 12000, 0, 75840, 90)

    def lambda_F19():
        OP_6D(26680, 0, 75360, 10000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_F19)

    def lambda_F31():
        OP_6C(120000, 10000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_F31)
    FadeToBright(2000, 0)

    def lambda_F4A():
        OP_8E(0xFE, 0x6590, 0x0, 0x12840, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F4A)
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
            "#063F奇、奇怪啊……\x02\x03",

            "确实是往\x01",
            "这个方向跑的……\x02",
        )
    )

    Jump("loc_1046")

    label("loc_1046")

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #39
        0x12,
        (
            "#561F……妈妈……\x01",
            "到底去哪儿了呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_109D():
        OP_8E(0xFE, 0x8E94, 0x0, 0x12840, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_109D)
    Sleep(2000)
    ClearChrFlags(0x106, 0x8)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x19, 25780, 0, 57700, 270)

    def lambda_10D8():
        OP_8F(0xFE, 0x22C4, 0x0, 0xE164, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10D8)

    def lambda_10F3():
        OP_6D(12960, 0, 61690, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_10F3)

    def lambda_110B():
        OP_6C(666000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_110B)

    def lambda_111B():
        OP_67(0, 8560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_111B)

    def lambda_1133():
        OP_6E(282, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1133)
    Sleep(3000)

    def lambda_1148():
        OP_8E(0xFE, 0x6978, 0x0, 0xEBF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1148)
    Sleep(2000)

    def lambda_1168():
        OP_6D(25300, 0, 61320, 8000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1168)
    Sleep(2000)

    ChrTalk(    #40 op#A op#5
        0x106,
        (
            "#053F#5P#30A……来得太早了。\x02\x03",

            "#053F#5P#47A在傍晚之前，\x01",
            "去清理点公告板上的工作吧……\x05\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x106, 0x1)
    OP_59()
    Sleep(300)

    def lambda_11F8():
        OP_6D(25040, 0, 65400, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_11F8)

    def lambda_1210():
        OP_6C(320000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1210)

    def lambda_1220():
        OP_67(0, 6860, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1220)
    OP_8C(0x106, 0, 400)

    def lambda_123F():
        OP_8E(0xFE, 0x6978, 0x0, 0xF80C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_123F)
    WaitChrThread(0x106, 0x1)
    OP_70(0xC, 0x1E)
    OP_73(0xC)

    def lambda_1269():
        OP_8E(0xFE, 0x6978, 0x1F4, 0xFFDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1269)
    Sleep(500)

    def lambda_1289():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1289)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_E6E end

    def Function_11_12AB(): pass

    label("Function_11_12AB")

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

    def lambda_132B():
        OP_6B(2700, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_132B)
    FadeToBright(2000, 0)

    def lambda_1344():
        OP_8E(0xFE, 0x6B6C, 0x0, 0xEA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1344)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #41
        0x12,
        (
            "#561F街上已经找遍了，\x01",
            "而且也不在家里……\x02\x03",

            "……妈妈到底\x01",
            "去哪儿了呢……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(600)

    NpcTalk(    #42
        0x13,
        "女性的声音",
        "#4P……所以不是说过了吗。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #43
        0x13,
        "女性的声音",
        (
            "#4P只要参加这个实验\x01",
            "就可以考虑给你减刑哦！\x02",
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
            "#064F刚才的是妈妈的声音。\x02\x03",

            "难、难道说……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_149F():
        OP_8E(0xFE, 0x6B6C, 0x0, 0xF870, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_149F)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_12AB end

    def Function_12_14CC(): pass

    label("Function_12_14CC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(54480, 0, 66180, 0)
    OP_67(0, 8340, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(320000, 0)
    OP_6E(520, 0)
    SetChrPos(0x107, 48000, 0, 17800, 0)
    OP_22(0x1C2, 0x0, 0x64)

    def lambda_1531():
        OP_6D(53400, 0, 22600, 13000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1531)

    def lambda_1549():
        OP_6C(230000, 13000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1549)

    def lambda_1559():
        OP_67(0, 6850, -10000, 13000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1559)
    FadeToBright(4000, 0)
    WaitChrThread(0x1A, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_23(0x1C2)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_14CC end

    def Function_13_1594(): pass

    label("Function_13_1594")

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
        "#4P那我走了～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        "#5P别慌慌张张的，小心摔倒哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        "#4P才、才不会呢！\x02",
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x107, 0x40)
    ClearChrFlags(0x107, 0x4)
    SetChrPos(0x107, 59800, 500, 23160, 0)
    Sleep(500)

    def lambda_16B3():
        OP_67(0, 6800, -10000, 2200)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_16B3)
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_70(0xA, 0x1D)
    OP_73(0xA)

    def lambda_16DB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_16DB)

    def lambda_16ED():
        OP_8E(0xFE, 0xE998, 0x0, 0x6400, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_16ED)
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
            "#066F#12P（『我走了』吗……）\x02\x03",

            "#067F（嘿嘿，偶尔这样也不错呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 600)
    Sleep(500)

    ChrTalk(    #49
        0x107,
        (
            "#560F#5P（好、好吧！\x01",
            "　赶快去中央工房！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17FA():
        OP_8E(0xFE, 0xE998, 0x0, 0xB220, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_17FA)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1594 end

    def Function_14_182C(): pass

    label("Function_14_182C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(6980, 0, 64160, 0)
    OP_67(0, 9020, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(302, 0)
    SetChrPos(0x107, 1860, 2250, 61700, 90)

    def lambda_188C():
        OP_67(0, 7020, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_188C)

    def lambda_18A4():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_18A4)
    FadeToBright(2000, 0)
    Sleep(6000)

    def lambda_18C2():
        OP_8E(0xFE, 0x24E0, 0x0, 0xF104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_18C2)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_8C(0x107, 135, 500)
    Sleep(600)
    OP_8C(0x107, 0, 500)
    Sleep(300)

    def lambda_18FF():
        OP_8E(0xFE, 0x24E0, 0x0, 0x1287C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_18FF)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_182C end

    def Function_15_1931(): pass

    label("Function_15_1931")

    OP_72(0x2010, 0x0)
    ExitThread()
    OP_72(0x200E, 0x0)
    ExitThread()

    label("loc_193D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1968")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_193D")

    label("loc_1968")

    Return()

    # Function_15_1931 end

    def Function_16_1969(): pass

    label("Function_16_1969")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19CC")

    ChrTalk(    #50
        0x106,
        (
            "#053F兵器的开发\x01",
            "好像正在中央工房进行啊。\x02\x03",

            "#057F啧，得赶快才行了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A19")

    label("loc_19CC")


    ChrTalk(    #51
        0x106,
        (
            "#052F哦，这边是城外吧。\x02\x03",

            "#057F得赶快去中央工房才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1A19")

    OP_90(0x106, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_16_1969 end

    def Function_17_1A30(): pass

    label("Function_17_1A30")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A93")

    ChrTalk(    #52
        0x106,
        (
            "#053F兵器的开发\x01",
            "好像正在中央工房进行啊。\x02\x03",

            "#057F啧，得赶快才行了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE0")

    label("loc_1A93")


    ChrTalk(    #53
        0x106,
        (
            "#052F哦，这边是城外吧。\x02\x03",

            "#057F得赶快去中央工房才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1AE0")

    OP_90(0x106, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_17_1A30 end

    def Function_18_1AF7(): pass

    label("Function_18_1AF7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #54
        (
            "\x07\x05『导力式时钟第１号机』\x01",
            "　七耀日历1162年·蔡斯技术工房制造\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_18_1AF7 end

    SaveToFile()

Try(main)
