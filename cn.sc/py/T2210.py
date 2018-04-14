from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2210   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '弗洛拉',                               # 9
        '多米尼克',                             # 10
        '比古',                                 # 11
        '王国军宪兵',                           # 12
        '达里奥',                               # 13
        '索雷诺',                               # 14
        '诺曼市长',                             # 15
        '秘书德尔斯',                           # 16
        '贝尔夫',                               # 17
        '杯子',                                 # 18
        '杯子',                                 # 19
        '水壶',                                 # 20
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
        'ED6_DT06/CH20020 ._CH',             # 00
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH01280 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH01560 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT07/CH01140 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT06/CH20020P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH01280P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH01560P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT07/CH01140P._CP',             # 08
    )

    DeclNpc(
        X                   = 34540,
        Z                   = 0,
        Y                   = 27220,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -63810,
        Z                   = 0,
        Y                   = 34870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 33500,
        Z                   = 0,
        Y                   = 24400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2620,
        Z                   = 0,
        Y                   = 3200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 67820,
        Z                   = -30,
        Y                   = -5200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 0,
        Y                   = 2100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -64500,
        Z                   = 0,
        Y                   = 33170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -7500,
        Z                   = 0,
        Y                   = 33230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 36150,
        Z                   = 0,
        Y                   = 34260,
        Direction           = 193,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 35510,
        Z                   = 750,
        Y                   = 27280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638400,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35450,
        Z                   = 750,
        Y                   = 26890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638400,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35490,
        Z                   = 750,
        Y                   = 26520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703936,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -475,
        TriggerZ            = 0,
        TriggerY            = 3173,
        TriggerRange        = 800,
        ActorX              = -475,
        ActorZ              = 800,
        ActorY              = 3173,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -63800,
        TriggerZ            = 0,
        TriggerY            = 50790,
        TriggerRange        = 900,
        ActorX              = -63800,
        ActorZ              = -300,
        ActorY              = 50790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -62370,
        TriggerZ            = 0,
        TriggerY            = -43110,
        TriggerRange        = 500,
        ActorX              = -62370,
        ActorZ              = 2000,
        ActorY              = -43110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59500,
        TriggerZ            = 250,
        TriggerY            = -36760,
        TriggerRange        = 800,
        ActorX              = -59500,
        ActorZ              = 1250,
        ActorY              = -36760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_302",          # 00, 0
        "Function_1_402",          # 01, 1
        "Function_2_43E",          # 02, 2
        "Function_3_5BB",          # 03, 3
        "Function_4_698",          # 04, 4
        "Function_5_99B",          # 05, 5
        "Function_6_DEA",          # 06, 6
        "Function_7_11E1",         # 07, 7
        "Function_8_163D",         # 08, 8
        "Function_9_185C",         # 09, 9
        "Function_10_1A4A",        # 0A, 10
        "Function_11_20D0",        # 0B, 11
        "Function_12_24EC",        # 0C, 12
        "Function_13_296F",        # 0D, 13
        "Function_14_2FC0",        # 0E, 14
        "Function_15_306D",        # 0F, 15
        "Function_16_3077",        # 10, 16
        "Function_17_3081",        # 11, 17
    )


    def Function_0_302(): pass

    label("Function_0_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B8")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 33760, 0, 25890, 270)
    SetChrPos(0x8, -4550, 0, -4059, 95)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 67400, 0, 32619, 270)
    Jump("loc_3B5")

    label("loc_365")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4070, 0, 35300, 270)
    SetChrPos(0x9, -1900, 0, 4450, 90)
    SetChrPos(0xF, -61820, 0, 30050, 355)
    SetChrPos(0x8, -2750, 0, 42770, 342)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_3B5")

    Jump("loc_401")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrPos(0x8, 35530, 0, 34250, 180)
    Jump("loc_401")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_401")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FA")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_401")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_401")

    label("loc_401")

    Return()

    # Function_0_302 end

    def Function_1_402(): pass

    label("Function_1_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_42C")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)

    label("loc_42C")

    OP_72(0x10, 0x10)
    OP_72(0x10, 0x8)
    OP_6F(0x10, 360)
    Return()

    # Function_1_402 end

    def Function_2_43E(): pass

    label("Function_2_43E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5A5")

    label("loc_463")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5A5")

    label("loc_47C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5A5")

    label("loc_495")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5A5")

    label("loc_4AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5A5")

    label("loc_4C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5A5")

    label("loc_4E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F9")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5A5")

    label("loc_4F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_512")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5A5")

    label("loc_512")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5A5")

    label("loc_52B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5A5")

    label("loc_544")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5A5")

    label("loc_55D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_576")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5A5")

    label("loc_576")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5A5")

    label("loc_58F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A5")

    label("loc_5BA")

    Return()

    # Function_2_43E end

    def Function_3_5BB(): pass

    label("Function_3_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_635")

    label("loc_5C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_632")
    OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xFFFFEAA2, 0x3E8, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_8C(0xFE, 90, 400)
    Sleep(3500)
    OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xFFFFF204, 0x3E8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(4500)
    Jump("loc_5C2")

    label("loc_632")

    Jump("loc_697")

    label("loc_635")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A")
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)

    label("loc_68A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_694")

    Jump("loc_63F")

    label("loc_697")

    Return()

    # Function_3_5BB end

    def Function_4_698(): pass

    label("Function_4_698")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6F6")

    ChrTalk(    #0
        0xFE,
        (
            "伙食非常美味，\x01",
            "不知不觉吃太多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "这样工作下去\x01",
            "会不断长胖的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_760")

    label("loc_6F6")

    OP_A2(0x3)

    ChrTalk(    #2
        0xFE,
        (
            "嗯～厨房\x01",
            "飘来好香的味道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "这里的厨师做的饭菜\x01",
            "非常非常好吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "因此我的皮带\x01",
            "都紧起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_760")

    Jump("loc_997")

    label("loc_763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_81C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7B8")

    ChrTalk(    #5
        0xFE,
        (
            "竟然在自己家里\x01",
            "养魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "居然还有人\x01",
            "会去想这么可怕的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_819")

    label("loc_7B8")

    OP_A2(0x3)

    ChrTalk(    #7
        0xFE,
        (
            "房间二楼的\x01",
            "秘密魔兽饲养房间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "……看过了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "居然还有人\x01",
            "会去想这么可怕的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_819")

    Jump("loc_997")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_902")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_88B")

    ChrTalk(    #10
        0xFE,
        (
            "对这等美术品出手的\x01",
            "只可能是绝顶的笨蛋或者天才了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "普通的盗贼\x01",
            "还是有自知之明的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FF")

    label("loc_88B")

    OP_A2(0x3)

    ChrTalk(    #12
        0xFE,
        (
            "从这里的女佣\x01",
            "那里听说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "前不久这个烛台\x01",
            "被偷走过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "好厉害的家伙……不、不，\x01",
            "竟然有这么坏的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FF")

    Jump("loc_997")

    label("loc_902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_948")

    ChrTalk(    #15
        0xFE,
        (
            "所、所以不要\x01",
            "在这附近转悠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "我也很紧张呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_997")

    label("loc_948")

    OP_A2(0x3)

    ChrTalk(    #17
        0xFE,
        (
            "这个烛台现在\x01",
            "由王国军代为保管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "别太靠近。\x01",
            "这可是相当贵重的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_997")

    TalkEnd(0xFE)
    Return()

    # Function_4_698 end

    def Function_5_99B(): pass

    label("Function_5_99B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A13")

    ChrTalk(    #19
        0xFE,
        (
            "这是使用柴火的暖炉。\x01",
            "最近的炊事都靠这个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "本来是想要用火才做的，\x01",
            "没想到会这么有用。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_A71")

    label("loc_A13")


    ChrTalk(    #21
        0xFE,
        (
            "这是使用柴火的暖炉。\x01",
            "最近的炊事都靠这个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "不过，适用范围\x01",
            "稍微窄了点，也没办法了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A71")

    Jump("loc_DE6")

    label("loc_A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B02")

    ChrTalk(    #23
        0xFE,
        (
            "管家达里奥\x01",
            "回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "多年服侍戴尔蒙家\x01",
            "的同伴都在一起就心安多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "这么快就欠了雇佣我们的\x01",
            "新市长的人情了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_B52")

    label("loc_B02")


    ChrTalk(    #26
        0xFE,
        (
            "达里奥那家伙\x01",
            "回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "作为服侍戴尔蒙家的同伴，\x01",
            "他回来可让人心安多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B52")

    Jump("loc_DE6")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_BAC")

    ChrTalk(    #28
        0xFE,
        (
            "好，差不多\x01",
            "该准备午饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "我为了士兵们\x01",
            "加倍卖力的自信作品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0A")

    label("loc_BAC")

    OP_A2(0x2)

    ChrTalk(    #30
        0xFE,
        (
            "今天的伙食\x01",
            "是加了橘子调味汁\x01",
            "的照烧仔鸡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "是我将东方的烹调法\x01",
            "加以调整的自信作品。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0A")

    Jump("loc_DE6")

    label("loc_C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_C6B")

    ChrTalk(    #32
        0xFE,
        (
            "我也一直在担心\x01",
            "达里奥那家伙的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "市长被逮捕之后\x01",
            "他的情况确实很奇怪……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CBD")

    ChrTalk(    #34
        0xFE,
        (
            "士兵们也不挑食，\x01",
            "吃得都很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "嗯，也算做得值得了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D16")

    label("loc_CBD")

    OP_A2(0x2)

    ChrTalk(    #36
        0xFE,
        (
            "我现在负责佣人和士兵们\x01",
            "的伙食。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "在这房子也待了很久了。\x01",
            "就让我效劳到最后吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D16")

    Jump("loc_DE6")

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D74")

    ChrTalk(    #38
        0xFE,
        (
            "不管怎么说，\x01",
            "我一直在服侍戴尔蒙家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "家道没落了，\x01",
            "还真是可惜啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_D74")

    OP_A2(0x2)

    ChrTalk(    #40
        0xFE,
        (
            "戴尔蒙市长确实\x01",
            "做了坏事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "但我和管家达里奥\x01",
            "都服侍戴尔蒙家多年了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "家道没落了，\x01",
            "实在是难过啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE6")

    TalkEnd(0xFE)
    Return()

    # Function_5_99B end

    def Function_6_DEA(): pass

    label("Function_6_DEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_E4B")

    ChrTalk(    #43
        0xFE,
        (
            "没有了导力器的光，\x01",
            "这个烛台也真可怜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "就跟被导力文明所装点的\x01",
            "我们一样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DD")

    label("loc_E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDD")

    ChrTalk(    #45
        0xFE,
        (
            "达里奥也完全\x01",
            "恢复状态了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "有段时间还形迹可疑，\x01",
            "让人感觉诡异呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "无论如何，有个熟悉这里\x01",
            "的人在真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_F29")

    label("loc_EDD")


    ChrTalk(    #48
        0xFE,
        (
            "达里奥也完全\x01",
            "恢复状态了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "有段时间还形迹可疑，\x01",
            "让人感觉诡异呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F29")

    Jump("loc_11DD")

    label("loc_F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_FC6")

    ChrTalk(    #50
        0xFE,
        (
            "根据市长选举的结果\x01",
            "找工作的方针也要发生变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "如果诺曼获胜就找旅游相关职业，\x01",
            "要是波尔多斯就去港口酒馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "哼哼，完美的再就业计划。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11DD")

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_FF7")

    ChrTalk(    #53
        0xFE,
        (
            "外面好像\x01",
            "很吵闹……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "怎么啦？\x02",
    )

    CloseMessageWindow()
    Jump("loc_11DD")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1062")

    ChrTalk(    #55
        0xFE,
        (
            "事件之后，管家达里奥\x01",
            "好像变得很奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "戴尔蒙市长被逮捕\x01",
            "似乎让他相当震惊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112E")

    label("loc_1062")

    OP_A2(0x1)

    ChrTalk(    #57
        0xFE,
        (
            "最近，这里的旧管家\x01",
            "达里奥好像都不见人影呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "说到底，那个人\x01",
            "在市长被逮捕以后\x01",
            "就变得有点奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "『还有一个我！』什么的\x01",
            "都说出来了，真是不太妙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "戴尔蒙市长被逮捕\x01",
            "看来让他相当震惊吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112E")

    Jump("loc_11DD")

    label("loc_1131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_11DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1194")

    ChrTalk(    #61
        0xFE,
        (
            "军队管理期间还好，\x01",
            "此后会变成怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "趁现在找到下一份工作\x01",
            "会比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DD")

    label("loc_1194")

    OP_A2(0x1)

    ChrTalk(    #63
        0xFE,
        (
            "军队管理期间还好，\x01",
            "此后会变成怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "佣人还是\x01",
            "会被解雇吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DD")

    TalkEnd(0xFE)
    Return()

    # Function_6_DEA end

    def Function_7_11E1(): pass

    label("Function_7_11E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1236")

    ChrTalk(    #65
        0xFE,
        (
            "除尘器也不能使用\x01",
            "扫除可辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "呼，这栋房子\x01",
            "竟然这么宽广啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1639")

    label("loc_1236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E5")

    ChrTalk(    #67
        0xFE,
        (
            "啊，欢迎～\x01",
            "欢迎光临市长官邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "我们大家全部\x01",
            "都被新市长雇佣了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "导力器不能使用，\x01",
            "做家务虽然辛苦点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "但大家一起努力\x01",
            "一定能渡过难关的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_133D")

    label("loc_12E5")


    ChrTalk(    #71
        0xFE,
        (
            "我们大家全部\x01",
            "都被新市长雇佣了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "达里奥先生也回来了，\x01",
            "这下一切都恢复原样了吧⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133D")

    Jump("loc_1639")

    label("loc_1340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_13D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1386")

    ChrTalk(    #73
        0xFE,
        (
            "我虽然想在这房子里\x01",
            "工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "但还是很难吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13CD")

    label("loc_1386")

    OP_A2(0x0)

    ChrTalk(    #75
        0xFE,
        (
            "多米尼克已经\x01",
            "在找下一份工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "这样一来\x01",
            "我也着急起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CD")

    Jump("loc_1639")

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_14AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_141A")

    ChrTalk(    #77
        0xFE,
        (
            "最近一直没见着\x01",
            "管家达里奥的身影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "怎么回事呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14A7")

    label("loc_141A")

    OP_A2(0x0)

    ChrTalk(    #79
        0xFE,
        (
            "扫除的时候和多米尼克\x01",
            "聊天来着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "最近一直没见着\x01",
            "管家达里奥的身影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "事件之后\x01",
            "情况就很奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "达里奥到底\x01",
            "怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A7")

    Jump("loc_1639")

    label("loc_14AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_153D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14F9")

    ChrTalk(    #83
        0xFE,
        (
            "啦啦～啦⊙\x01",
            "噜噜噜噜～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "士兵先生们\x01",
            "人都很好呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153A")

    label("loc_14F9")

    OP_A2(0x0)

    ChrTalk(    #85
        0xFE,
        (
            "啦啦～啦⊙\x01",
            "噜噜噜噜～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "我正在准备\x01",
            "给士兵们的茶呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153A")

    Jump("loc_1639")

    label("loc_153D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15A6")

    ChrTalk(    #87
        0xFE,
        (
            "老爷被逮捕的时候\x01",
            "还在想会变成怎样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "看来暂时还能和以前一样\x01",
            "在这里生活下去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1639")

    label("loc_15A6")

    OP_A2(0x0)

    ChrTalk(    #89
        0xFE,
        (
            "现在，这栋房子\x01",
            "由王国军管理哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "为了维持宅邸的管理。\x01",
            "我们佣人们\x01",
            "也维持原样被雇佣了下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "嘿嘿，幸好军队的士兵们\x01",
            "都是和善的好人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1639")

    TalkEnd(0xFE)
    Return()

    # Function_7_11E1 end

    def Function_8_163D(): pass

    label("Function_8_163D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_174C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1705")

    ChrTalk(    #92
        0xFE,
        (
            "如此非常时期\x01",
            "竟然又发生事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "最近这世道\x01",
            "是怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "想来前市长的事件\x01",
            "也是难以理解……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "……不，没什么好说的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "前市长的过失是事实。\x01",
            "有罪就要认罪。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1749")

    label("loc_1705")


    ChrTalk(    #97
        0xFE,
        (
            "如此非常时期\x01",
            "竟然又发生事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "到底这世道\x01",
            "是怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1749")

    Jump("loc_1858")

    label("loc_174C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1858")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1804")

    ChrTalk(    #99
        0xFE,
        (
            "我是在戴尔蒙家\x01",
            "服侍多年的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "受新市长的委托，\x01",
            "我作为这个市长官邸的管家\x01",
            "重新回到这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "我当作重获新生\x01",
            "诚心诚意来服侍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "任何事都\x01",
            "敬请吩咐。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1858")

    label("loc_1804")


    ChrTalk(    #103
        0xFE,
        (
            "作为市长官邸的管家\x01",
            "又回到宅邸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "能和同伴们一起工作的幸福\x01",
            "我要牢牢抓住。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1858")

    TalkEnd(0xFE)
    Return()

    # Function_8_163D end

    def Function_9_185C(): pass

    label("Function_9_185C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_194A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F3")

    ChrTalk(    #105
        0xFE,
        (
            "我面见了市长，\x01",
            "请求对玛诺利亚紧急支持……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "但是卢安市\x01",
            "好像情况也相当严峻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "诺曼市长的严肃表情\x01",
            "完全说明了这一点。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1947")

    label("loc_18F3")


    ChrTalk(    #108
        0xFE,
        (
            "已经请求支持村子，\x01",
            "但是卢安的状况也很严峻啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "诺曼市长\x01",
            "看起来也相当疲劳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1947")

    Jump("loc_1A46")

    label("loc_194A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E6")

    ChrTalk(    #110
        0xFE,
        (
            "作为玛诺利亚村的村长代理，\x01",
            "我是来向卢安市长请愿的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "需要尽早请求食品和燃料\x01",
            "的支援啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "好了，立刻去跟新市长\x01",
            "打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1A46")

    label("loc_19E6")


    ChrTalk(    #113
        0xFE,
        (
            "作为玛诺利亚村的村长代理，\x01",
            "我是来向卢安市长请愿的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "需要尽早请求食品和燃料\x01",
            "的支援啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A46")

    TalkEnd(0xFE)
    Return()

    # Function_9_185C end

    def Function_10_1A4A(): pass

    label("Function_10_1A4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1AB7")
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #115
        0xFE,
        "哦哦，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "刚刚收到学院事件\x01",
            "的报告呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1AB7")


    ChrTalk(    #117
        0xFE,
        (
            "哦哦……\x01",
            "你们就是那些游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "正好收到学院事件\x01",
            "的报告呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFD")


    ChrTalk(    #119
        0x101,
        "#1011F哦～消息真灵通啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        (
            "#1040F是嘉恩先生\x01",
            "告知的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "啊啊，从协会\x01",
            "来了使者……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "哦，这么说来\x01",
            "还没打招呼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C03")

    ChrTalk(    #123
        0xFE,
        (
            "和以前见面时相比\x01",
            "我的立场也发生了变化呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#1000F啊，是哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "我是这次就任新市长\x01",
            "的诺曼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "今后请多关照。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C3A")

    label("loc_1C03")


    ChrTalk(    #127
        0xFE,
        (
            "我是这次就任新市长\x01",
            "的诺曼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "以后请多关照了。\x02",
    )

    CloseMessageWindow()

    label("loc_1C3A")


    ChrTalk(    #129
        0x101,
        "#1000F哪里哪里，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x102,
        "#1040F恭喜您当选市长。\x02",
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_1DBF")

    label("loc_1C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1CBF")

    ChrTalk(    #131
        0xFE,
        (
            "我们也\x01",
            "下定了决心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "希望能尽快\x01",
            "解决这个情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBF")

    label("loc_1CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(    #133
        0xFE,
        (
            "关于学院的事件\x01",
            "刚刚才收到报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "勤务员实在可怜，\x01",
            "不过据说平安解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "代表市民，也让我\x01",
            "重新表示感谢吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1DBF")

    label("loc_1D44")


    ChrTalk(    #136
        0xFE,
        (
            "关于学院的事件\x01",
            "刚刚收到报告呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "这种非常时期的占据事件\x01",
            "实在是令人难以置信的暴行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "犯人们应该\x01",
            "受到严惩才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBF")

    Jump("loc_20CC")

    label("loc_1DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2030")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F72")
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #139
        0xFE,
        "哦哦，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "选举中的酒店事件时\x01",
            "承蒙关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1016F啊～那个事件啊。\x02\x03",

            "嗯，记得很～清楚哦。\x01",
            "你的头还撞在门上。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #142
        0x102,
        "#1048F什么？那个事件……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #143
        0xFE,
        "哎呀，真是丢脸……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "不管怎样，趁此机会\x01",
            "请让我重新自我介绍一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "和以前见面时相比\x01",
            "我的立场也发生了变化呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1011F啊，是哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "我是就任新市长的诺曼。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "今后请多关照。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FED")

    label("loc_1F72")


    ChrTalk(    #149
        0xFE,
        (
            "唔……\x01",
            "你们是游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "虽然不是初次见面，\x01",
            "请让我重新自我介绍一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "我是就任新市长的诺曼。\x01",
            "以后也请多关照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FED")


    ChrTalk(    #152
        0x101,
        "#1000F哪里哪里，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        "#1040F恭喜您当选市长。\x02",
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_20CC")

    label("loc_2030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_207E")

    ChrTalk(    #154
        0xFE,
        (
            "我们也\x01",
            "下定了决心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "祈祷事件能尽快解决，\x01",
            "期待诸位的表现。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CC")

    label("loc_207E")


    ChrTalk(    #156
        0xFE,
        (
            "总之市民生活的稳定\x01",
            "可以说是当前的课题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "为此现在正在\x01",
            "寻求各方援助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CC")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A4A end

    def Function_11_20D0(): pass

    label("Function_11_20D0")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #158
        0xFE,
        "唔，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "不过，遗憾的是还不到\x01",
            "沉浸在胜利中的时候……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_215E")

    ChrTalk(    #160
        0x106,
        (
            "#552F啊啊，正是。\x02\x03",

            "您刚刚就任，也真是多灾多难。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F0")

    label("loc_215E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21A4")

    ChrTalk(    #161
        0x103,
        (
            "#025F嗯嗯，我们明白。\x02\x03",

            "您刚刚就任就碰到这些事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F0")

    label("loc_21A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21F0")

    ChrTalk(    #162
        0x108,
        (
            "#074F唔，实在让您伤脑筋了啊。\x02\x03",

            "刚刚就任\x01",
            "就碰到这些难题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F0")


    ChrTalk(    #163
        0xFE,
        (
            "说实话，\x01",
            "真是无从下手啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "当初的混乱虽然收拾了，\x01",
            "但是导力器还是没恢复原状。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "这种时候只能努力\x01",
            "支援市民的生活了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x102,
        (
            "#1043F但是，就现在而言\x01",
            "这是最好的对策。\x02\x03",

            "遗憾的是事态的解决\x01",
            "可能还要花费一些时间。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2334")

    ChrTalk(    #167
        0x108,
        (
            "#072F确实不是一朝一夕\x01",
            "就能解决的事件啊。\x02\x03",

            "为了防止长期延续\x01",
            "需要更有效的对策。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x108, 400)
    Jump("loc_2407")

    label("loc_2334")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A1")

    ChrTalk(    #168
        0x103,
        (
            "#022F是啊，这不是一朝一夕\x01",
            "就能解决的事件。\x02\x03",

            "为了防止长期延续\x01",
            "需要更有效的对策。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_2407")

    label("loc_23A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2407")

    ChrTalk(    #169
        0x106,
        (
            "#050F确实不是一天两天\x01",
            "就能解决的事件。\x02\x03",

            "考虑到事态的延续\x01",
            "需要更有效的对策。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    label("loc_2407")


    ChrTalk(    #170
        0xFE,
        "唔，果然是这样吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "作为新市长的首次工作来说\x01",
            "略感负担沉重……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "为了不负女神的期待，\x01",
            "只有想办法努力克服了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "祈祷事件能尽快解决，\x01",
            "期待诸位的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1006F嗯……\x01",
            "市长也要加油。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x102,
        "#1040F我们会尽力的！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_A2(0x20BC)
    Return()

    # Function_11_20D0 end

    def Function_12_24EC(): pass

    label("Function_12_24EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_296B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26EB")

    ChrTalk(    #176
        0xFE,
        "啊，游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "那、那个……\x01",
            "前几天承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1000F啊～还以为是谁呢，\x01",
            "是宾馆事件的受害者吧。\x02\x03",

            "……撞到的头已经不要紧了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "托你的福已经完全好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "那，今天\x01",
            "来市长官邸有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1000F嗯，其实也没什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#1040F请不用在意。\x01",
            "只是来看看情况的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "算是所谓的市内巡查吧？\x01",
            "一直执行任务真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "那么，有什么事的话\x01",
            "请尽管开口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "我至少也算是\x01",
            "市长秘书嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1000F哦～这样啊。\x02\x03",

            "那么，到时候就请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "啊啊，请不必客气。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x20BD)
    Jump("loc_296B")

    label("loc_26EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2739")

    ChrTalk(    #188
        0xFE,
        (
            "别看我这样，\x01",
            "至少也是市长秘书呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "有什么事情\x01",
            "请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_296B")

    label("loc_2739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_284B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F4")

    ChrTalk(    #190
        0xFE,
        (
            "关于学院的事件\x01",
            "刚刚收到了报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "听说平安解决了，\x01",
            "我和市长总算都放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "现在正忙着做\x01",
            "发放宣传的准备呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "不管怎样得发出消息\x01",
            "让大家感到安心才行呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2848")

    label("loc_27F4")


    ChrTalk(    #194
        0xFE,
        (
            "关于学院的事件\x01",
            "刚刚收到了报告呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "听说平安解决了，\x01",
            "我和市长总算都放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2848")

    Jump("loc_296B")

    label("loc_284B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2915")

    ChrTalk(    #196
        0xFE,
        (
            "呼，应付市民的意见\x01",
            "总算告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "众多的市民一时间全涌过来，\x01",
            "那时候这里也够辛苦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "但是，导力器的问题\x01",
            "还没有解决的头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "总之现在光是支持市民生活\x01",
            "就已经竭尽全力了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_296B")

    label("loc_2915")


    ChrTalk(    #200
        0xFE,
        (
            "导力器的问题\x01",
            "还没有解决的头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "总之现在光是支持市民生活\x01",
            "就已经竭尽全力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296B")

    TalkEnd(0xFE)
    Return()

    # Function_12_24EC end

    def Function_13_296F(): pass

    label("Function_13_296F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2FBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D55")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A60")
    TurnDirection(0xFE, 0x106, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #202
        0xFE,
        "咦，阿加特先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        (
            "#051F哦，好久不见了啊。\x02\x03",

            "看来还是\x01",
            "很有精神嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "哈哈，托你的福……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "老爸当了市长，\x01",
            "我就来帮他的忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "这种情况下，\x01",
            "很多事都需要忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B57")

    label("loc_2A60")


    ChrTalk(    #207
        0xFE,
        "咦，你们是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ABC")

    ChrTalk(    #208
        0x101,
        "#1000F啊，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x103,
        "#021F呵呵，很有精神嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AE6")

    label("loc_2ABC")


    ChrTalk(    #210
        0x101,
        (
            "#1000F啊，好久不见。\x02\x03",

            "怎样？还好吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE6")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #211
        0xFE,
        "哈哈，托你的福还算好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "老爸当了市长，\x01",
            "我现在正在帮他的忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "这种情况下，\x01",
            "很多事都需要忙呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B57")


    ChrTalk(    #214
        0x101,
        (
            "#1011F哦～这可是\x01",
            "正经的工作呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #215
        0xFE,
        (
            "嗯，现在就和\x01",
            "打工差不多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "不过着急也不是办法，\x01",
            "我打算脚踏实地地努力看看。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C51")

    ChrTalk(    #217
        0x106,
        (
            "#051F有这觉悟就没问题了。\x02\x03",

            "……好好干哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #218
        0xFE,
        (
            "是，是。\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "阿加特先生也多保重。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D4C")

    label("loc_2C51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CDC")

    ChrTalk(    #220
        0x103,
        (
            "#020F嗯嗯，有这觉悟就\x01",
            "一定没问题了。\x02\x03",

            "那么，好好干哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #221
        0xFE,
        "嗯、嗯，我会努力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "那么，\x01",
            "你们也多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4C")

    label("loc_2CDC")


    ChrTalk(    #223
        0x101,
        (
            "#1006F有这觉悟就\x01",
            "一定没问题了。\x02\x03",

            "那么，加油工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "嗯、嗯，我会努力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "那么，\x01",
            "你们也多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4C")

    OP_A2(0xB)
    OP_A2(0x20BE)
    Jump("loc_2FBC")

    label("loc_2D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2E0A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DC3")

    ChrTalk(    #226
        0xFE,
        (
            "总之我打算\x01",
            "脚踏实地的努力看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "这种非常时期，\x01",
            "阿加特先生你们也要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E07")

    label("loc_2DC3")


    ChrTalk(    #228
        0xFE,
        (
            "总之我打算\x01",
            "脚踏实地的努力看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "那么，\x01",
            "你们也要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E07")

    Jump("loc_2FBC")

    label("loc_2E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9A")

    ChrTalk(    #230
        0xFE,
        (
            "学院的事件……\x01",
            "从准游击士那里听说啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "这种时候还发生人质事件，\x01",
            "真是受不了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "犯人真是的，\x01",
            "到底在想什么呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_2EF6")

    label("loc_2E9A")


    ChrTalk(    #233
        0xFE,
        (
            "这种时候还发生人质事件，\x01",
            "真是受不了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "大家都在齐心协力的时候，\x01",
            "真是不能原谅啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF6")

    Jump("loc_2FBC")

    label("loc_2EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F79")

    ChrTalk(    #235
        0xFE,
        "我老爸也因为各种事忙得不得了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "应付市民的意见、\x01",
            "食品和医药品的确保……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "真是，要做的事\x01",
            "多得堆成山。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_2FBC")

    label("loc_2F79")


    ChrTalk(    #238
        0xFE,
        "我老爸也因为各种事忙得不得了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "为什么这么喜欢\x01",
            "当市长呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FBC")

    TalkEnd(0xFE)
    Return()

    # Function_13_296F end

    def Function_14_2FC0(): pass

    label("Function_14_2FC0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #240
        (
            "\x07\x05『苍耀之灯火』\x01",
            "　被认为是初期导力艺术的\x01",
            "　极致作品。\x01",
            "　导力革命之后\x01",
            "　由卢安市民\x01",
            "　赠送给为城市发展\x01",
            "　作出贡献的戴尔蒙家。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_2FC0 end

    def Function_15_306D(): pass

    label("Function_15_306D")

    NewScene("ED6_DT21/T2210   ._SN", 123, 1, 0)
    IdleLoop()
    Return()

    # Function_15_306D end

    def Function_16_3077(): pass

    label("Function_16_3077")

    NewScene("ED6_DT21/T2210   ._SN", 121, 1, 0)
    IdleLoop()
    Return()

    # Function_16_3077 end

    def Function_17_3081(): pass

    label("Function_17_3081")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #241
        "\x07\x05有吊桥的控制装置。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_3081 end

    SaveToFile()

Try(main)
