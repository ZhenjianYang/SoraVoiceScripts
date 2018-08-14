from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5400   ._SN',
        MapName             = 'Other',
        Location            = 'C5400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '歼灭天使玲',                           # 9
        '瘦狼瓦鲁特',                           # 10
        '幻惑之铃露茜奥拉',                     # 11
        '怪盗布卢布兰',                         # 12
        '基尔巴特',                             # 13
        '小丑肯帕雷拉',                         # 14
        '强化猎兵',                             # 15
        '强化猎兵',                             # 16
        '强化猎兵',                             # 17
        '目标用照相机',                         # 18
        '',                                     # 19
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
        'ED6_DT27/CH03540 ._CH',             # 00
        'ED6_DT27/CH03510 ._CH',             # 01
        'ED6_DT27/CH03500 ._CH',             # 02
        'ED6_DT27/CH03523 ._CH',             # 03
        'ED6_DT27/CH03530 ._CH',             # 04
        'ED6_DT27/CH03750 ._CH',             # 05
        'ED6_DT26/CH20475 ._CH',             # 06
        'ED6_DT26/CH20412 ._CH',             # 07
        'ED6_DT26/CH20208 ._CH',             # 08
        'ED6_DT27/CH03600 ._CH',             # 09
        'ED6_DT26/CH20764 ._CH',             # 0A
        'ED6_DT26/CH20763 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT27/CH03540P._CP',             # 00
        'ED6_DT27/CH03510P._CP',             # 01
        'ED6_DT27/CH03500P._CP',             # 02
        'ED6_DT27/CH03523P._CP',             # 03
        'ED6_DT27/CH03530P._CP',             # 04
        'ED6_DT27/CH03750P._CP',             # 05
        'ED6_DT26/CH20475P._CP',             # 06
        'ED6_DT26/CH20412P._CP',             # 07
        'ED6_DT26/CH20208P._CP',             # 08
        'ED6_DT27/CH03600P._CP',             # 09
        'ED6_DT26/CH20764P._CP',             # 0A
        'ED6_DT26/CH20763P._CP',             # 0B
    )

    DeclNpc(
        X                   = 61490,
        Z                   = 0,
        Y                   = -22730,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -134180,
        Z                   = 0,
        Y                   = -28920,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x183,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -130090,
        Z                   = 0,
        Y                   = 9850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -133800,
        Z                   = 0,
        Y                   = 48910,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2740,
        Z                   = 0,
        Y                   = -24540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -38630,
        Z                   = 0,
        Y                   = -68760,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -87010,
        Z                   = 0,
        Y                   = -24670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -37010,
        Z                   = 0,
        Y                   = 66950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        X                   = -42980,
        Y                   = -1000,
        Z                   = 75190,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -36920,
        Y                   = -1000,
        Z                   = -67150,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 70070,
        Y                   = -1000,
        Z                   = -234030,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 21,
    )


    DeclActor(
        TriggerX            = 61080,
        TriggerZ            = 0,
        TriggerY            = -184550,
        TriggerRange        = 1000,
        ActorX              = 61080,
        ActorZ              = 1000,
        ActorY              = -184550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2CE",          # 00, 0
        "Function_1_361",          # 01, 1
        "Function_2_392",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_421",          # 04, 4
        "Function_5_49A",          # 05, 5
        "Function_6_517",          # 06, 6
        "Function_7_65D",          # 07, 7
        "Function_8_913",          # 08, 8
        "Function_9_B7B",          # 09, 9
        "Function_10_F20",         # 0A, 10
        "Function_11_1269",        # 0B, 11
        "Function_12_157A",        # 0C, 12
        "Function_13_15A5",        # 0D, 13
        "Function_14_15D0",        # 0E, 14
        "Function_15_15FB",        # 0F, 15
        "Function_16_250A",        # 10, 16
        "Function_17_253F",        # 11, 17
        "Function_18_2597",        # 12, 18
        "Function_19_26AD",        # 13, 19
        "Function_20_2723",        # 14, 20
        "Function_21_2724",        # 15, 21
        "Function_22_2725",        # 16, 22
        "Function_23_2CB1",        # 17, 23
        "Function_24_3776",        # 18, 24
    )


    def Function_0_2CE(): pass

    label("Function_0_2CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_302")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_32D")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 23)
    Jump("loc_349")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_349")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 22)

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_360")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_360")

    Return()

    # Function_0_2CE end

    def Function_1_361(): pass

    label("Function_1_361")

    OP_72(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x42B, 0x0)
    ExitThread()
    OP_71(0x42C, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()
    OP_71(0x426, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    Return()

    # Function_1_361 end

    def Function_2_392(): pass

    label("Function_2_392")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_392")

    label("loc_3A7")

    Return()

    # Function_2_392 end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_420")
    OP_8E(0xFE, 0xAD2, 0x0, 0x55E6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x131A, 0x0, 0x5582, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x13F6, 0x0, 0xFFFF9F34, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xAB4, 0x0, 0xFFFFA024, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Jump("Function_3_3A8")

    label("loc_420")

    Return()

    # Function_3_3A8 end

    def Function_4_421(): pass

    label("Function_4_421")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_499")
    OP_8E(0xFE, 0xFFFEAC64, 0x0, 0x5726, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFEA340, 0x0, 0x562C, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFEA2B4, 0x0, 0xFFFF9FB6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xFFFEAC1E, 0x0, 0xFFFF9FA2, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Jump("Function_4_421")

    label("loc_499")

    Return()

    # Function_4_421 end

    def Function_5_49A(): pass

    label("Function_5_49A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_516")
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFF4782, 0x0, 0x10842, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xFFFF6F6E, 0x0, 0x10586, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Jump("Function_5_49A")

    label("loc_516")

    Return()

    # Function_5_49A end

    def Function_6_517(): pass

    label("Function_6_517")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_523")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65C")
    OP_99(0xFE, 0x0, 0x2, 0x3E8)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")
    Sleep(1000)
    Jump("loc_5AF")

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56B")
    Sleep(1500)
    Jump("loc_5AF")

    label("loc_56B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_580")
    Sleep(2000)
    Jump("loc_5AF")

    label("loc_580")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_595")
    Sleep(2500)
    Jump("loc_5AF")

    label("loc_595")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA")
    Sleep(3000)
    Jump("loc_5AF")

    label("loc_5AA")

    Sleep(1800)

    label("loc_5AF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_600")
    Sleep(1000)
    Jump("loc_659")

    label("loc_600")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_615")
    Sleep(1500)
    Jump("loc_659")

    label("loc_615")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62A")
    Sleep(2000)
    Jump("loc_659")

    label("loc_62A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63F")
    Sleep(2500)
    Jump("loc_659")

    label("loc_63F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_654")
    Sleep(3000)
    Jump("loc_659")

    label("loc_654")

    Sleep(1800)

    label("loc_659")

    Jump("loc_523")

    label("loc_65C")

    Return()

    # Function_6_517 end

    def Function_7_65D(): pass

    label("Function_7_65D")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC")
    OP_A2(0x0)

    ChrTalk(    #0
        0x10,
        (
            "#260F啊，莱维。\x02\x03",

            "不会是\x01",
            "教授叫你了吧？\x02",
        )
    )

    Jump("loc_6A3")

    label("loc_6A3")

    CloseMessageWindow()

    ChrTalk(    #1
        0x124,
        (
            "#120F哈哈，看来是机会来了。\x02\x03",

            "在『塔』里也够你辛苦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#260F唔，也不是那样的。\x02\x03",

            "如果再多点时间的话，\x01",
            "就能把他们统统杀掉的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x124,
        (
            "#120F不用，根本不用亲自动手。\x02\x03",

            "如果利用了『环』的力量\x01",
            "那就等同于人类全部死亡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "#260F咦……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x124,
        (
            "#120F思考一下吧，那个教授\x01",
            "掌握了超越人类智力的力量。\x02\x03",

            "玲你也能想象的到，\x01",
            "会有什么样的事情发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#260F嘻嘻……也是。\x02\x03",

            "不管怎么说，教授的性格\x01",
            "是相当的没有道理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x124,
        (
            "#120F到底是我先还是那帮家伙先……\x02\x03",

            "不管是谁能获胜，\x01",
            "答案马上就能揭晓了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90F")

    label("loc_8AC")


    ChrTalk(    #8
        0x10,
        (
            "#260F话说那教授\x01",
            "要操控世界什么的……\x02\x03",

            "嘻嘻……\x01",
            "看来事情像是变得越来越有趣了。\x02",
        )
    )

    Jump("loc_90E")

    label("loc_90E")

    CloseMessageWindow()

    label("loc_90F")

    TalkEnd(0x10)
    Return()

    # Function_7_65D end

    def Function_8_913(): pass

    label("Function_8_913")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B22")
    OP_A2(0x1)

    ChrTalk(    #9
        0x11,
        (
            "#250F唷，看到了吗？\x01",
            "那天空中的巨物。\x02\x03",

            "呵呵呵……\x01",
            "这下，好玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x124,
        (
            "#120F是吗……\x02\x03",

            "不过，这话与我无关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#250F哼……\x01",
            "没劲的家伙。\x02\x03",

            "嗤，如果是这样的话\x01",
            "那小家伙\x01",
            "可就要来撕裂你了。\x02",
        )
    )

    Jump("loc_9F4")

    label("loc_9F4")

    CloseMessageWindow()

    ChrTalk(    #12
        0x124,
        (
            "#120F原来如此……\x01",
            "在『塔』中也出现了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#250F虽然素质不错，\x01",
            "不过，归根到底是执行秘密行动的人……\x02\x03",

            "下次有机会的话，\x01",
            "一定会将其彻底击毁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x124,
        (
            "#120F如果是这样就好了……\x02\x03",

            "不过，那家伙\x01",
            "也有自己的战斗方式。\x02\x03",

            "一定要警惕\x01",
            "慎防那家伙从暗处下手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#250F赫……\x01",
            "这就不用你操心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B77")

    label("loc_B22")


    ChrTalk(    #16
        0x11,
        (
            "#250F下次就提着那小东西的脑袋\x01",
            "给你当礼物了。\x02\x03",

            "呵呵呵……\x01",
            "你就好好期盼着吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B77")

    TalkEnd(0x11)
    Return()

    # Function_8_913 end

    def Function_9_B7B(): pass

    label("Function_9_B7B")

    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BA0")
    SetChrSubChip(0x12, 1)
    Jump("loc_BBB")

    label("loc_BA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB6")
    SetChrSubChip(0x12, 2)
    Jump("loc_BBB")

    label("loc_BB6")

    SetChrSubChip(0x12, 0)

    label("loc_BBB")

    OP_8C(0x12, 180, 0)
    SetChrFlags(0x12, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB2")
    OP_A2(0x2)

    ChrTalk(    #17
        0x12,
        (
            "#240F呵呵，真少见啊。\x01",
            "怎么想起来到我这里来了。\x02\x03",

            "莫非是……\x01",
            "想我了么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x124,
        (
            "#120F快闭嘴……\x02\x03",

            "我不是来和你说这些的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "#240F呵呵，玩笑、玩笑而已。\x02\x03",

            "教授的『福音计划』也\x01",
            "就快要进入最终阶段了……\x02\x03",

            "或许马上就该\x01",
            "轮到你出场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x124,
        (
            "#120F哈哈，恐怕是如此……\x02\x03",

            "……不过，露茜奥拉。\x02\x03",

            "为什么你会一直\x01",
            "协助教授的计划呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#240F呵呵，那是一种缘分。\x02\x03",

            "偶然之间，找到了\x01",
            "自己一直在探寻的东西。\x02\x03",

            "聚集到这里的人们\x01",
            "应该都是一样的缘由吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x124,
        (
            "#120F……也许是这样。\x02\x03",

            "如果能拥有这些找到的东西\x01",
            "那就好了，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#240F好了，不说了……\x01",
            "就此打住吧。\x02\x03",

            "或许是已经太迟了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x124,
        (
            "#120F……………………………………\x02\x03",

            "……不管怎么样\x01",
            "既然已经是涂满鲜血的道路——\x02\x03",

            "那就不要留下任何遗憾地\x01",
            "战斗下去，直到最后。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F17")

    label("loc_EB2")


    ChrTalk(    #25
        0x12,
        (
            "#240F参加教授的计划\x01",
            "也是偶尔的一个缘分所致。\x02\x03",

            "哈哈，聚集在这里的人们\x01",
            "应该都是一样的缘由吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F17")

    SetChrSubChip(0x12, 0)
    TalkEnd(0x12)
    Return()

    # Function_9_B7B end

    def Function_10_F20(): pass

    label("Function_10_F20")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DF")
    OP_A2(0x3)

    ChrTalk(    #26
        0x13,
        (
            "#230F嚯嚯，这可是稀客啊。\x02\x03",

            "大名鼎鼎的剑帝陛下\x01",
            "居然能下榻我们这小庵来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x124,
        (
            "#120F呵呵，到这种时候\x01",
            "还戴着面具……\x02\x03",

            "难道是真的那么害怕\x01",
            "暴露自己的真面目么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x13,
        (
            "#230F呵呵，完全不是如此……\x02\x03",

            "如果说是面具\x01",
            "那您不也是戴着面具么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x124,
        "#120F什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x13,
        (
            "#230F只要是人，不管是谁，一生中\x01",
            "总会以戴着不同的假面具生活着。\x02\x03",

            "您也应该会深有体会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x124,
        "#120F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x13,
        (
            "#230F因此，我时常\x01",
            "只戴着这一个面具。\x02\x03",

            "这才是我的真面目。\x01",
            "而我本身的容貌反而是我的假面具……\x02\x03",

            "难道你不记得\x01",
            "操持着几个假面的你也嘲笑过我么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x124,
        (
            "#120F哈哈，的确是……\x02\x03",

            "你这个样子\x01",
            "多少也有一分道理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x13,
        (
            "#230F没有理念的地方也就没有美――\x02\x03",

            "――这不是能够用简单的道理来说明的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1265")

    label("loc_11DF")


    ChrTalk(    #35
        0x13,
        (
            "#230F只要是人，不管是谁，一生中\x01",
            "总会以戴着不同的假面具生活着。\x02\x03",

            "在笑我之前，先想一想\x01",
            "如果自己的收藏\x01",
            "少了一个的话，会如何呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1265")

    TalkEnd(0x13)
    Return()

    # Function_10_F20 end

    def Function_11_1269(): pass

    label("Function_11_1269")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150A")
    OP_A2(0x4)

    ChrTalk(    #36
        0x14,
        "#1220F你、你……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x124,
        (
            "#120F辛苦你查看了……\x02\x03",

            "……有什么异常么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14,
        (
            "#1220F是，好的！\x02\x03",

            "我、我要为结社\x01",
            "全力完成自己的任务。\x02\x03",

            "从现在开始的新作战\x01",
            "也一定会成功！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x124,
        "#120F呀……什么样的作战啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x14,
        (
            "#1220F哈，是袭击王立学院\x01",
            "的计划！\x02",
        )
    )

    Jump("loc_1381")

    label("loc_1381")

    CloseMessageWindow()

    ChrTalk(    #41
        0x124,
        (
            "#120F袭击学院……？\x02\x03",

            "……是谁的命令？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x14,
        "#1220F呵呵，是肯帕雷拉先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x124,
        (
            "#120F…………………………………\x02\x03",

            "这家伙………到底是在学谁啊!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x14,
        "#1220F到，到底是怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x124,
        (
            "#120F没什么……祈祷你能成功。\x02\x03",

            "不过，尽量把进攻\x01",
            "限制在最低限度。\x02\x03",

            "……为了防备今后的作战\x01",
            "尽量避免过多地消耗战斗力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x14,
        (
            "#1220F哈！　你就放心好了！\x02\x03",

            "那就仔细地瞧一瞧\x01",
            "这基尔巴特的指挥能力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1576")

    label("loc_150A")


    ChrTalk(    #47
        0x14,
        (
            "#1220F一定会让你们瞧瞧，我会使\x01",
            "王立学院袭击作战圆满成功。\x02\x03",

            "那就仔细地瞧一瞧\x01",
            "这基尔巴特的指挥能力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1576")

    TalkEnd(0x14)
    Return()

    # Function_11_1269 end

    def Function_12_157A(): pass

    label("Function_12_157A")

    TalkBegin(0x16)

    ChrTalk(    #48
        0x16,
        "◆与强化猎兵会话（反复进行）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_12_157A end

    def Function_13_15A5(): pass

    label("Function_13_15A5")

    TalkBegin(0x17)

    ChrTalk(    #49
        0x17,
        "◆与强化猎兵会话（反复进行）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_13_15A5 end

    def Function_14_15D0(): pass

    label("Function_14_15D0")

    TalkBegin(0x18)

    ChrTalk(    #50
        0x18,
        "◆与强化猎兵会话（反复进行）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_14_15D0 end

    def Function_15_15FB(): pass

    label("Function_15_15FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(60330, 1000, 52870, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    SetChrPos(0x124, 59900, 1000, 52500, 90)
    SetChrChipByIndex(0x124, 6)
    SetChrSubChip(0x124, 2)
    SetChrFlags(0x124, 0x4)
    OP_4A(0x14, 255)
    Sleep(1000)
    Sleep(500)
    OP_22(0x1C2, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(350, 120, -1, -1)
    SetChrName("男孩子的声音")

    AnonymousTalk(    #51
        (
            "\x07\x0C莱维……\x02\x03",

            "那，如果是莱维……\x02",
        )
    )

    Jump("loc_16C4")

    label("loc_16C4")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240060, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #52
        "\x07\x0C怎么了？约修亚。\x02",
    )

    Jump("loc_1705")

    label("loc_1705")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 120, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #53
        (
            "\x07\x0C我可以先吃便当么？\x02\x03",

            "我的肚子已经\x01",
            "已经饿得瘪瘪的了……\x02",
        )
    )

    Jump("loc_1760")

    label("loc_1760")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 100, -1, -1)
    SetChrName("卡玲")

    AnonymousTalk(    #54
        (
            "\x07\x0C呵呵，不行，约修亚。\x02\x03",

            "不是约好了，\x01",
            "三个人一起吃得么？\x02",
        )
    )

    Jump("loc_17B6")

    label("loc_17B6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 120, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #55
        "\x07\x0C啊，不过……\x02",
    )

    Jump("loc_17E6")

    label("loc_17E6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #56
        (
            "\x07\x0C哈哈，知道啦。\x02\x03",

            "那就请再等10分钟。\x01",
            "然后就开始午饭。\x02",
        )
    )

    Jump("loc_183A")

    label("loc_183A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 120, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #57
        "恩！\x02",
    )

    Jump("loc_1866")

    label("loc_1866")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_23(0x1C2)
    OP_1D(0x4A)
    Sleep(1000)
    OP_AD(0x240061, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #58
        (
            "\x07\x0C那，莱维……\x02\x03",

            "马上就要接受准游击士的考试了，\x01",
            "真的么？\x02",
        )
    )

    Jump("loc_18F3")

    label("loc_18F3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #59
        (
            "\x07\x0C喂喂……\x01",
            "是从谁那里听到的？\x02",
        )
    )

    Jump("loc_1939")

    label("loc_1939")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #60
        (
            "\x07\x0C老头们都在说。\x01",
            "说莱维要去城镇了。\x02",
        )
    )

    Jump("loc_197E")

    label("loc_197E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #61
        (
            "\x07\x0C啊啊…\x02\x03",

            "日子还没有决定。\x01",
            "应该就在最近吧……\x02",
        )
    )

    Jump("loc_19D3")

    label("loc_19D3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #62
        (
            "\x07\x0C是吗……\x02\x03",

            "……如果合格的话，\x01",
            "就会去城镇么？\x02",
        )
    )

    Jump("loc_1A30")

    label("loc_1A30")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #63
        (
            "\x07\x0C怎么了……\x02\x03",

            "你不会是怕寂寞了吧。\x02",
        )
    )

    Jump("loc_1A71")

    label("loc_1A71")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #64
        (
            "\x07\x0C喂喂……说什么呢。\x02\x03",

            "……那，莱维。\x01",
            "让大家一起都去城镇生活如何呀？\x02",
        )
    )

    Jump("loc_1AD8")

    label("loc_1AD8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #65
        "\x07\x0C约修亚……！？\x02",
    )

    Jump("loc_1B05")

    label("loc_1B05")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #66
        (
            "\x07\x0C那样的话\x01",
            "我也可以继续练习剑术……\x02\x03",

            "莱维的话，应该是可以\x01",
            "和卡玲在一起的吧？\x02",
        )
    )

    Jump("loc_1B81")

    label("loc_1B81")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #67
        (
            "\x07\x0C哈哈……这家伙。\x02\x03",

            "要是那样的话，你知道不知道\x01",
            "要有多少米拉才够啊？\x02",
        )
    )

    Jump("loc_1BE3")

    label("loc_1BE3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #68
        (
            "\x07\x0C恩，我觉得\x01",
            "这想法倒也不错，不过……\x02\x03",

            "……果然还是不行么？\x02",
        )
    )

    Jump("loc_1C42")

    label("loc_1C42")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #69
        (
            "\x07\x0C不，没有那回事。\x02\x03",

            "马上肯定有些困难……\x01",
            "什么时候能那样的话就好了。\x02",
        )
    )

    Jump("loc_1CA4")

    label("loc_1CA4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #70
        "\x07\x0C恩！一定会如此的。\x02",
    )

    Jump("loc_1CDA")

    label("loc_1CDA")

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_AE(0x1F4)
    Sleep(2000)
    OP_22(0x87, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x124, 0x0, 0x0, 0x10)
    Sleep(2000)
    OP_22(0x72, 0x0, 0x64)
    Sleep(800)
    OP_22(0x72, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("老人的声音")

    AnonymousTalk(    #71
        (
            "\x07\x0C#2S莱维！\x02\x03",

            "喂，莱维！！\x02",
        )
    )

    Jump("loc_1D54")

    label("loc_1D54")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #72
        (
            "\x07\x0C……怎么了？大爷。\x02\x03",

            "到底怎么回事？\x02",
        )
    )

    Jump("loc_1D97")

    label("loc_1D97")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("老人的声音")

    AnonymousTalk(    #73
        "\x07\x0C#3S快，快跑！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #74
        "\x07\x0C什么……！？\x02",
    )

    Jump("loc_1DEE")

    label("loc_1DEE")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_AD(0x240063, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #75
        "\x07\x0C去，去哪里啊，卡玲姐！\x02",
    )

    Jump("loc_1E3F")

    label("loc_1E3F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("卡玲")

    AnonymousTalk(    #76
        "\x07\x0C少废话，快跟我来！\x02",
    )

    Jump("loc_1E70")

    label("loc_1E70")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #77
        (
            "\x07\x0C两个人都快这么跑！\x02\x03",

            "无论如何尽快跑到邻村去！\x02",
        )
    )

    Jump("loc_1EBD")

    label("loc_1EBD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("卡玲")

    AnonymousTalk(    #78
        "\x07\x0C莱维！？\x02",
    )

    Jump("loc_1EF0")

    label("loc_1EF0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #79
        (
            "\x07\x0C我去搅乱一下他们。\x02\x03",

            "没问题，我的速度\x01",
            "一会儿就能够追上。\x02",
        )
    )

    Jump("loc_1F48")

    label("loc_1F48")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("卡玲")

    AnonymousTalk(    #80
        (
            "\x07\x0C知道了……\x02\x03",

            "……小心！\x02",
        )
    )

    Jump("loc_1F7F")

    label("loc_1F7F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #81
        "\x07\x0C快去吧！\x02",
    )

    Jump("loc_1FB2")

    label("loc_1FB2")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(2000)
    OP_43(0x124, 0x1, 0x0, 0x11)
    WaitChrThread(0x124, 0x1)
    OP_44(0x124, 0xFF)
    Sleep(1000)
    OP_22(0x1CD, 0x0, 0x64)
    Sleep(2000)
    OP_1D(0x5B)
    Sleep(1000)
    OP_AD(0x240065, 0x0, 0x0, 0x12C)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("卡玲")

    AnonymousTalk(    #82
        (
            "\x07\x0C莱、莱维……\x02\x03",

            "一直相信……\x01",
            "你一定回来的。\x02",
        )
    )

    Jump("loc_203E")

    label("loc_203E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #83
        "\x07\x0C卡玲！ 别说话！\x02",
    )

    Jump("loc_206C")

    label("loc_206C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("卡玲")

    AnonymousTalk(    #84
        (
            "\x07\x0C算了……已经迟了。\x02\x03",

            "莱维……\x01",
            "……谢谢你一直照顾到现在。\x02",
        )
    )

    Jump("loc_20D0")

    label("loc_20D0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #85
        "\x07\x0C卡玲！\x02",
    )

    Jump("loc_20FE")

    label("loc_20FE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("卡玲")

    AnonymousTalk(    #86
        (
            "\x07\x0C拜托……\x02\x03",

            "多关照约修亚……\x02",
        )
    )

    Jump("loc_2145")

    label("loc_2145")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #87
        (
            "\x07\x0C恩，我知道！\x02\x03",

            "因此，卡玲……\x02",
        )
    )

    Jump("loc_2182")

    label("loc_2182")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("卡玲")

    AnonymousTalk(    #88
        (
            "\x07\x0C……真好…………\x02\x03",

            "…………………………\x02",
        )
    )

    Jump("loc_21C9")

    label("loc_21C9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #89
        "\x07\x0C卡……卡玲……！？\x02",
    )

    Jump("loc_21FA")

    label("loc_21FA")

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xBB8)
    OP_AE(0xC8)
    OP_23(0x1CD)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #90
        "\x07\x0C#5S卡玲！！\x02",
    )

    Jump("loc_2231")

    label("loc_2231")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(4000)
    FadeToBright(1000, 0)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #91
        0x124,
        "#121F#5P！？\x02",
    )

    CloseMessageWindow()
    Sleep(2000)

    ChrTalk(    #92
        0x124,
        (
            "#124F#5P……呼呼…………\x02\x03",

            "又是这个梦啊……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(5470, 0, 17810, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x124, 8470, 0, 17170, 270)
    SetChrChipByIndex(0x124, 65535)
    SetChrSubChip(0x124, 0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0x1C)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x9, 0)
    OP_70(0x9, 0xF)
    OP_73(0x9)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 3840, 0, 4990, 0)

    def lambda_235C():
        OP_8E(0xFE, 0x10A4, 0x0, 0x4204, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_235C)
    Sleep(300)

    def lambda_237C():
        OP_8E(0xFE, 0x1054, 0x0, 0x3782, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_237C)
    WaitChrThread(0x124, 0x0)
    OP_6F(0x9, 15)
    OP_70(0x9, 0x0)
    WaitChrThread(0x16, 0x0)

    ChrTalk(    #93
        0x16,
        "啊，莱维……\x02",
    )

    CloseMessageWindow()

    def lambda_23C3():
        OP_6D(5560, 0, 17030, 1000)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_23C3)
    OP_8C(0x124, 180, 400)
    WaitChrThread(0x124, 0x0)
    Sleep(300)

    ChrTalk(    #94
        0x124,
        "#121F#5P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x16,
        (
            "教授在圣堂等着你呢。\x02\x03",

            "好像要和你谈谈\x01",
            "今后的作战计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x124,
        "#121F#5P知道了……这就去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x16,
        "是，失陪了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x16, 180, 400)
    Sleep(200)

    def lambda_2485():
        OP_8E(0xFE, 0xF00, 0x0, 0x137E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2485)
    WaitChrThread(0x16, 0x0)
    SetChrPos(0x16, -38630, 0, -68760, 270)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_6D(5470, 0, 17810, 1000)

    ChrTalk(    #98
        0x124,
        (
            "#121F#5P干吧干吧……\x02\x03",

            "没时间想过去的事儿了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_4B(0x14, 255)
    EventEnd(0x0)
    Return()

    # Function_15_15FB end

    def Function_16_250A(): pass

    label("Function_16_250A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_253E")
    OP_22(0x235, 0x0, 0x32)
    Sleep(1000)
    OP_22(0x1F7, 0x0, 0x32)
    Sleep(1000)
    OP_22(0x1F7, 0x0, 0x32)
    Sleep(500)
    OP_22(0x235, 0x0, 0x32)
    Sleep(800)
    Jump("Function_16_250A")

    label("loc_253E")

    Return()

    # Function_16_250A end

    def Function_17_253F(): pass

    label("Function_17_253F")

    OP_24(0x235, 0x32)
    OP_24(0x1F7, 0x32)
    Sleep(300)
    OP_24(0x235, 0x28)
    OP_24(0x1F7, 0x28)
    Sleep(300)
    OP_24(0x235, 0x1E)
    OP_24(0x1F7, 0x1E)
    Sleep(300)
    OP_24(0x235, 0x14)
    OP_24(0x1F7, 0x14)
    Sleep(300)
    OP_24(0x235, 0xA)
    OP_24(0x1F7, 0xA)
    Sleep(300)
    OP_24(0x235, 0x0)
    OP_24(0x1F7, 0x0)
    Sleep(300)
    OP_23(0x235)
    OP_23(0x1F7)
    OP_23(0x87)
    Return()

    # Function_17_253F end

    def Function_18_2597(): pass

    label("Function_18_2597")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x124, 61000, 0, -185610, 0)
    SetChrSubChip(0x124, 0)
    OP_6D(61240, 0, -185600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_20(0xBB8)

    def lambda_25FD():
        OP_6D(60980, 500, -184400, 3000)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_25FD)

    def lambda_2615():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x124, 1, lambda_2615)

    def lambda_262D():
        OP_6B(3120, 3000)
        ExitThread()

    QueueWorkItem(0x124, 2, lambda_262D)

    def lambda_263D():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x124, 3, lambda_263D)
    WaitChrThread(0x124, 0x0)
    OP_21()
    Sleep(300)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x10E)
    OP_22(0x132, 0x0, 0x64)
    Sleep(500)
    OP_73(0x2)

    def lambda_2673():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD3EEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x124, 1, lambda_2673)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/C5401   ._SN", 125, 0, 0)
    IdleLoop()
    OP_64(0x4, 0x1)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_18_2597 end

    def Function_19_26AD(): pass

    label("Function_19_26AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2722")
    EventBegin(0x1)

    ChrTalk(    #99
        0x124,
        (
            "#124F……没有必要再往前去了。\x02\x03",

            "#120F正想要去『圣堂』呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x124, 180, 400)
    OP_90(0x124, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_2722")

    label("loc_2722")

    Return()

    # Function_19_26AD end

    def Function_20_2723(): pass

    label("Function_20_2723")

    Return()

    # Function_20_2723 end

    def Function_21_2724(): pass

    label("Function_21_2724")

    Return()

    # Function_21_2724 end

    def Function_22_2725(): pass

    label("Function_22_2725")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(62950, 0, 50300, 0)
    OP_67(0, 4660, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x40)
    OP_4A(0x14, 255)
    SetChrPos(0x14, 61500, 0, 49000, 90)
    OP_24(0x131, 0x3C)
    Sleep(300)
    OP_24(0x85, 0x64)
    OP_24(0x131, 0x32)
    Sleep(300)
    OP_24(0x85, 0x5A)
    OP_24(0x131, 0x28)
    Sleep(300)
    OP_24(0x85, 0x50)
    OP_24(0x131, 0x1E)
    Sleep(300)
    OP_24(0x85, 0x46)
    OP_24(0x131, 0x14)
    Sleep(300)
    OP_23(0x131)

    def lambda_27E7():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_27E7)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #100
        0x14,
        (
            "#1224F#6P那、那是什么……\x02\x03",

            "那、那是什么呀！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x14, 11)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x14, 0x2)

    def lambda_2859():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2859)
    WaitChrThread(0x14, 0x2)
    OP_22(0x8E, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(400)
    SetChrSubChip(0x14, 3)
    Sleep(100)

    def lambda_2893():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2893)
    WaitChrThread(0x14, 0x2)
    OP_22(0x8E, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(800)

    ChrTalk(    #101
        0x14,
        (
            "#1227F#6P不、不是说……\x01",
            "使用那浮游都市\x01",
            "来控制利贝尔的么？？！\x02\x03",

            "甚至把大陆全境也……\x02\x03",

            "#1225F这，这\x01",
            "不是和说的不一样嘛！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #102
        0x14,
        (
            "#1224F#6P……等、等等哟。\x02\x03",

            "仔细想想的话……\x01",
            "这不过是我随便想象而已。\x01",
            "那样的话一句也……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #103
        0x14,
        "#1227F#3S#6P呜哇啊啊啊！#2S\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x12C)
    CloseMessageWindow()
    ClearChrFlags(0x14, 0x2)
    SetChrChipByIndex(0x14, 5)
    SetChrSubChip(0x14, 0)
    OP_8C(0x14, 315, 600)

    def lambda_2A49():
        OP_6D(61460, 0, 54360, 1500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2A49)

    def lambda_2A61():
        OP_8E(0xFE, 0xE9C0, 0x0, 0xC710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2A61)
    WaitChrThread(0x14, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x19, 59840, 0, 53000, 0)

    def lambda_2A9C():
        OP_96(0xFE, 0xE9C0, 0x2BC, 0xCEA4, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2A9C)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 180, 500)
    Fade(250)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x14, 0x800)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 8)
    Sleep(500)
    OP_99(0x14, 0x8, 0x6, 0x5DC)
    Sleep(300)

    def lambda_2AF2():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2AF2)
    Sleep(1000)

    NpcTalk(    #104
        0x19,
        "基尔巴特",
        (
            "#1228F#5P#30W我讨厌再这样下去了……\x02\x03",

            "让那些人跑掉，\x01",
            "我又要被肯帕雷拉大人折磨了……\x02\x03",

            "还、还落得……\x01",
            "这样一个不明不白的结果……\x02",
        )
    )

    Jump("loc_2BB7")

    label("loc_2BB7")

    CloseMessageWindow()
    Sleep(1000)

    NpcTalk(    #105 op#A op#5
        0x19,
        "基尔巴特",
        "#1224F#5P#20A我、我……\x05\x02",
    )

    Jump("loc_2BF6")

    label("loc_2BF6")

    CloseMessageWindow()

    def lambda_2BFD():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2BFD)
    FadeToDark(3000, 0, -1)
    Sleep(1500)

    NpcTalk(    #106 op#A
        0x19,
        "基尔巴特",
        (
            "#1227F#5P#45A#3S至今为止……\x01",
            "到底都让我们做了一些什么啊！？#2S\x02",
        )
    )

    Jump("loc_2C75")

    label("loc_2C75")

    OP_7C(0x0, 0x96, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(1000)
    OP_0D()
    OP_44(0x19, 0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C5400   ._SN", 125, 0, 0)
    IdleLoop()
    Return()

    # Function_22_2725 end

    def Function_23_2CB1(): pass

    label("Function_23_2CB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(71210, 0, -233330, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(53000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    SetChrPos(0x16, 59760, 0, -186600, 180)
    SetChrPos(0x17, 62240, 0, -186600, 180)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 72500, 0, -234000, 270)
    FadeToBright(1500, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x101A, 0x0)
    ExitThread()
    OP_70(0x1A, 0xF)
    OP_73(0x1A)
    Sleep(500)

    def lambda_2D96():
        OP_8E(0xFE, 0xFDE8, 0x0, 0xFFFC6DF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2D96)
    Sleep(1000)

    def lambda_2DB6():
        OP_6D(62100, -200, -216040, 10000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2DB6)

    def lambda_2DCE():
        OP_67(0, 3500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2DCE)

    def lambda_2DE6():
        OP_6C(30000, 10000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_2DE6)

    def lambda_2DF6():
        OP_6B(3200, 10000)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_2DF6)

    def lambda_2E06():
        OP_6E(434, 10000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_2E06)
    WaitChrThread(0x15, 0x1)

    def lambda_2E1B():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFC7D90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E1B)
    WaitChrThread(0x15, 0x1)

    def lambda_2E3B():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD1E6C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E3B)
    WaitChrThread(0x19, 0x0)
    Fade(500)
    OP_6D(62290, 0, -184300, 0)
    OP_67(0, 4660, -10000, 0)
    OP_6B(3440, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_44(0x15, 0x1)
    OP_0D()
    Sleep(500)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #107
        0x16,
        "#5P肯、肯帕雷拉大人！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x17,
        "#5P没、没事吧！\x02",
    )

    CloseMessageWindow()

    def lambda_2F1D():
        OP_6D(62170, 0, -185780, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2F1D)
    SetChrPos(0x15, 61000, 0, -196000, 0)

    def lambda_2F46():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD19D0, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2F46)

    def lambda_2F61():

        label("loc_2F61")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_2F61")

    QueueWorkItem2(0x16, 2, lambda_2F61)

    def lambda_2F72():

        label("loc_2F72")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_2F72")

    QueueWorkItem2(0x17, 2, lambda_2F72)
    WaitChrThread(0x15, 0x1)
    Sleep(500)

    ChrTalk(    #109
        0x15,
        (
            "#853F#6P哈哈，辛苦了。\x02\x03",

            "#850F不过，这种时候还紧守岗位\x01",
            "是不是太过于认真了？\x02\x03",

            "#851F外面可是很壮观的哦？\x02\x03",

            "可不是花费几百万米拉\x01",
            "就能随便看到的光景啊。\x02\x03",

            "#854F趁现在还来得及，\x01",
            "你们也去参观一下如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x16,
        "#5P难得一见的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x17,
        "#5P我们不能因此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x15,
        (
            "#853F#6P呵呵……\x01",
            "对你们这些被命令束缚的人来说，\x01",
            "的确是有些难度。\x02\x03",

            "#850F算了。\x01",
            "能让我通过这里吗？\x02\x03",

            "我有点琐事需要\x01",
            "前去『圣堂』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x17,
        "#5P咦……\x02",
    )

    Jump("loc_3166")

    label("loc_3166")

    CloseMessageWindow()

    ChrTalk(    #114
        0x16,
        (
            "#5P虽、虽然如此……\x01",
            "#5P即便是肯帕雷拉大人，\x01",
            "没有教授的允许的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x15,
        "#853F#6P啊，如果是说教授，他已经死了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x16,
        "#5P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x17,
        "#5P不、不会吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x15,
        (
            "#852F#6P啊，\x01",
            "觉得我是在胡说八道吗……？\x02\x03",

            "#855F唉，\x01",
            "有点受打击了啊。\x02\x03",

            "#854F好吧，那我就也让你们\x01",
            "和基尔巴特一样\x01",
            "留下愉快的记忆吧。\x02\x03",

            "我想这样的话，\x01",
            "你们应该相信我的话了。\x02",
        )
    )

    Jump("loc_3329")

    label("loc_3329")

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_338C():
        OP_8F(0xFE, 0xE970, 0x0, 0xFFFD2844, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_338C)
    Sleep(100)

    def lambda_33AC():
        OP_8F(0xFE, 0xF320, 0x0, 0xFFFD2844, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_33AC)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)
    Sleep(300)

    ChrTalk(    #119
        0x16,
        "#5P不、不用了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x17,
        (
            "#5P不用您那么费心，\x01",
            "从一开始就是相信您的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x15,
        (
            "#853F#6P那还不到外面去\x01",
            "看看么？\x02\x03",

            "#854F反正命令你们在这里警备的人\x01",
            "已经不在了。\x02",
        )
    )

    Jump("loc_3491")

    label("loc_3491")

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #122
        0x16,
        "#5P#3S承蒙关照！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #123
        0x17,
        "#5P#3S请、请您随意使用！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0x16, 0x2)

    def lambda_351C():
        OP_6D(62170, 0, -192000, 4000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_351C)
    OP_43(0x16, 0x0, 0x0, 0x18)
    Sleep(300)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0x17, 0x2)
    OP_43(0x17, 0x1, 0x0, 0x18)

    def lambda_355D():
        OP_8C(0xFE, 180, 300)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_355D)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x19, 0x0)
    Sleep(1000)

    def lambda_357A():
        OP_6D(62160, 0, -188230, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_357A)
    WaitChrThread(0x19, 0x0)
    Sleep(500)

    ChrTalk(    #124
        0x15,
        (
            "#853F#5P呵呵，他们也没什么用了啊。\x02\x03",

            "#854F但如果只是消除记忆后白白放掉\x01",
            "也有点浪费。\x01",
            "要不，就让我来接管军队吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 0, 400)
    Sleep(300)

    def lambda_3629():
        OP_6D(62160, 0, -186230, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3629)

    def lambda_3641():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD27F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3641)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x19, 0x0)
    Fade(500)
    SetChrPos(0x15, 61000, 0, -185610, 0)
    OP_6D(61000, 500, -184400, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x10E)
    OP_22(0x132, 0x0, 0x64)
    Sleep(500)
    OP_73(0x2)

    def lambda_36DA():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD3EEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_36DA)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_24(0x85, 0x3C)
    Sleep(400)
    OP_24(0x85, 0x37)
    Sleep(400)
    OP_24(0x85, 0x32)
    Sleep(400)
    OP_24(0x85, 0x2D)
    Sleep(400)
    OP_24(0x85, 0x28)
    Sleep(400)
    OP_24(0x85, 0x23)
    Sleep(400)
    OP_24(0x85, 0x1E)
    Sleep(400)
    OP_24(0x85, 0x19)
    Sleep(400)
    OP_24(0x85, 0x14)
    Sleep(400)
    OP_24(0x85, 0xF)
    Sleep(400)
    OP_24(0x85, 0xA)
    Sleep(400)
    OP_23(0x85)
    Sleep(500)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_2CB1 end

    def Function_24_3776(): pass

    label("Function_24_3776")

    OP_8E(0xFE, 0xE6A0, 0x0, 0xFFFD1C14, 0x1770, 0x0)
    OP_8E(0xFE, 0xE6A0, 0x0, 0xFFFCE3E8, 0x1770, 0x0)
    Return()

    # Function_24_3776 end

    SaveToFile()

Try(main)
