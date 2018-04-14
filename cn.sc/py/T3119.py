from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3119   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3119.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3119   ._SN',
            'ED6_DT21/T3119_1 ._SN',
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
        '拉赛尔博士',                           # 9
        '玛多克工房长',                         # 10
        '特莱斯主任',                           # 11
        '接待处小姐海泽尔',                     # 12
        '威尔姆',                               # 13
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT07/CH01190 ._CH',             # 02
        'ED6_DT07/CH01540 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT07/CH01190P._CP',             # 02
        'ED6_DT07/CH01540P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = -440,
        Z                   = 0,
        Y                   = 10490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 4650,
        Z                   = 1000,
        Y                   = 6180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclEvent(
        X                   = -106990,
        Y                   = 0,
        Z                   = -550,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = -540,
        TriggerZ            = 0,
        TriggerY            = 6300,
        TriggerRange        = 800,
        ActorX              = -540,
        ActorZ              = 900,
        ActorY              = 6300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_243",          # 01, 1
        "Function_2_374",          # 02, 2
        "Function_3_41B",          # 03, 3
        "Function_4_C2D",          # 04, 4
        "Function_5_DB5",          # 05, 5
        "Function_6_147F",         # 06, 6
        "Function_7_2A44",         # 07, 7
        "Function_8_2A93",         # 08, 8
        "Function_9_2AE2",         # 09, 9
        "Function_10_2B31",        # 0A, 10
        "Function_11_2B80",        # 0B, 11
        "Function_12_4043",        # 0C, 12
        "Function_13_40C9",        # 0D, 13
        "Function_14_4115",        # 0E, 14
        "Function_15_592B",        # 0F, 15
        "Function_16_59C4",        # 10, 16
        "Function_17_5A2A",        # 11, 17
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C0")
    Jump("loc_204")

    label("loc_1C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_204")
    SetChrPos(0x8, -480, 0, 10270, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xA, 4650, 1000, 6340, 90)
    SetChrPos(0xC, 2300, 0, 7700, 90)

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_21E")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_242")

    label("loc_21E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_242")
    Event(0, 6)

    label("loc_242")

    Return()

    # Function_0_1B6 end

    def Function_1_243(): pass

    label("Function_1_243")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC")
    OP_6F(0x8, 0)
    OP_72(0x8, 0x10)
    OP_6F(0x5, 29)
    OP_72(0x5, 0x10)
    OP_6F(0x6, 29)
    OP_72(0x6, 0x10)
    OP_6F(0x7, 29)
    OP_72(0x7, 0x10)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_79(0xFF, 0x2)
    OP_7A(0x1F, 0x2)
    OP_7B()
    OP_72(0x13, 0x4)
    OP_72(0x14, 0x4)
    OP_10(0x0, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x4, 0x4)
    OP_64(0x0, 0x1)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_373")

    label("loc_2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_30F")
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_373")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_332")
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_373")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A")
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_373")

    label("loc_35A")

    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_71(0x12, 0x4)

    label("loc_373")

    Return()

    # Function_1_243 end

    def Function_2_374(): pass

    label("Function_2_374")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3A5"),
        (1, "loc_3B1"),
        (2, "loc_3BD"),
        (3, "loc_3C9"),
        (4, "loc_3D5"),
        (5, "loc_3E1"),
        (6, "loc_3ED"),
        (SWITCH_DEFAULT, "loc_3F9"),
    )


    label("loc_3A5")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_405")

    label("loc_3B1")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_405")

    label("loc_3BD")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_405")

    label("loc_3C9")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_405")

    label("loc_3D5")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_405")

    label("loc_3E1")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_405")

    label("loc_3ED")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_405")

    label("loc_3F9")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_405")

    label("loc_405")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_405")

    label("loc_41A")

    Return()

    # Function_2_374 end

    def Function_3_41B(): pass

    label("Function_3_41B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_53A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB")

    ChrTalk(    #0
        0xFE,
        (
            "博士去出差了，\x01",
            "我也不知道他在哪里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "不过他一定在忘我地\x01",
            "研究着这种现象吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "嗯，我们也不能懈怠，\x01",
            "一定要努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "虽然不能做得跟博士一样，\x01",
            "不过应该还是有很多事可以做。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_537")

    label("loc_4EB")


    ChrTalk(    #4
        0xFE,
        (
            "博士也一定在忘我地\x01",
            "研究着现象吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "我们也不能懈怠，\x01",
            "一定要努力……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_537")

    Jump("loc_C29")

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C6")

    ChrTalk(    #6
        0xFE,
        (
            "唉，受不了了……\x01",
            "到底是怎么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "和工房长说的一样，\x01",
            "机械材料都不动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "这种时候\x01",
            "拉赛尔博士要是在的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_614")

    label("loc_5C6")


    ChrTalk(    #9
        0xFE,
        (
            "和工房长说的一样，\x01",
            "机械材料都不动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "呼，拉赛尔博士\x01",
            "要是在的话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_614")

    Jump("loc_C29")

    label("loc_617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_682")

    ChrTalk(    #11
        0xFE,
        (
            "竟然能操纵七耀脉，\x01",
            "真是了不起的技术啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "我们连想都不敢想啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_704")

    label("loc_682")


    ChrTalk(    #13
        0xFE,
        "哟，各位辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "震源的调查\x01",
            "很麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "话虽如此……\x01",
            "竟然能操纵七耀脉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "以我们的知识水平\x01",
            "是无法想象得到的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_704")

    Jump("loc_981")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_75B")

    ChrTalk(    #17
        0xFE,
        (
            "七耀脉的运动\x01",
            "好像还没停止呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "但到底是什么\x01",
            "引发了这样的现象呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_981")

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_85D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7DE")

    ChrTalk(    #19
        0xFE,
        "问题是数据的交接啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "总之得抓紧\x01",
            "进行测试……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "真不愧是拉赛尔博士啊。\x01",
            "一下子就出了这么一个难题啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85A")

    label("loc_7DE")


    ChrTalk(    #22
        0xFE,
        (
            "从外部接收数据，\x01",
            "并且进行即时处理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "虽然不是做不到，\x01",
            "不过也是非常困难的工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "总之得抓紧\x01",
            "进行测试……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_85A")

    Jump("loc_981")

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8C4")

    ChrTalk(    #25
        0xFE,
        (
            "拉赛尔博士……\x01",
            "这次又会怎么样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "一半兴趣、一半恐惧……\x01",
            "现在就是这种心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_915")

    label("loc_8C4")


    ChrTalk(    #27
        0xFE,
        (
            "说起来，拉赛尔博士\x01",
            "好像很忙的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "嗯、嗯～总觉得\x01",
            "有不好的预感……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_915")

    Jump("loc_981")

    label("loc_918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_981")

    ChrTalk(    #29
        0xFE,
        (
            "虽然刚才有地震……\x01",
            "不过好像对『卡佩尔』没有影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "你们有需要的话随时\x01",
            "可以用它进行搜索。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_981")

    Jump("loc_A4A")

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_9E1")

    ChrTalk(    #31
        0xFE,
        "托你们的福，『卡佩尔』状态也很好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "你们有需要的话随时\x01",
            "可以用它进行搜索。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4A")

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_A4A")

    ChrTalk(    #33
        0xFE,
        (
            "虽然刚才有地震……\x01",
            "不过好像对『卡佩尔』没有影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "你们有需要的话随时\x01",
            "可以用它进行搜索。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4A")

    Jump("loc_C29")

    label("loc_A4D")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A98")

    ChrTalk(    #35
        0xFE,
        (
            "哟，是你们啊。\x01",
            "哟～好久不见！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_A98")


    ChrTalk(    #36
        0xFE,
        (
            "哟，是你啊？\x01",
            "哟～好久不见！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB9")


    ChrTalk(    #37
        0x101,
        (
            "#1001F嘿嘿，好久不见了。\x02\x03",

            "#1000F『卡佩尔』的状态如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "嗯，托你们的福，状态很好。\x01",
            "现在看来也没有受到地震的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "如果你们有需要的话随时\x01",
            "可以用它进行搜索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "不管怎样你们是\x01",
            "『卡佩尔』的恩人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB3")

    ChrTalk(    #41
        0x107,
        "#061F啊 ，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCE")

    label("loc_BB3")


    ChrTalk(    #42
        0xFE,
        (
            "你们太有\x01",
            "这个资格了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCE")


    ChrTalk(    #43
        0x101,
        (
            "#1017F嗯、嗯，谢谢你。\x02\x03",

            "那么，有需要的话\x01",
            "请再让我们使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "嗯，我们期待着。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x142F)
    OP_A2(0x0)

    label("loc_C29")

    TalkEnd(0xA)
    Return()

    # Function_3_41B end

    def Function_4_C2D(): pass

    label("Function_4_C2D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(    #45
        0x8,
        (
            "#100F你们赶快去\x01",
            "亚尔摩村吧。\x02\x03",

            "我呆在这里继续分析。\x01",
            "了解到什么的话就赶快联系旅馆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFC")

    label("loc_C98")


    ChrTalk(    #46
        0x8,
        (
            "#100F你们赶快去\x01",
            "亚尔摩村吧。\x02\x03",

            "我在这里继续\x01",
            "解析『卡佩尔』。\x02\x03",

            "了解到什么的话就赶快联系旅馆。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_CFC")

    Jump("loc_DB1")

    label("loc_CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D4F")

    ChrTalk(    #47
        0x8,
        (
            "#100F我们在这里\x01",
            "准备接收数据。\x02\x03",

            "就拜托你们去\x01",
            "设置测量仪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB1")

    label("loc_D4F")


    ChrTalk(    #48
        0x8,
        (
            "#100F哟，怎么样？\x01",
            "测量仪的设置还顺利吗？\x02\x03",

            "今天『卡佩尔』状态不错。\x01",
            "这边的准备也非常顺利。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_DB1")

    TalkEnd(0x8)
    Return()

    # Function_4_C2D end

    def Function_5_DB5(): pass

    label("Function_5_DB5")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_EFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB6")

    ChrTalk(    #49
        0xFE,
        (
            "说不定对这个事件博士\x01",
            "也要负责任呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "说不定是他偷偷做的实验失败了，\x01",
            "使整个王国的导力停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "哈哈……\x01",
            "不、不会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "就、就算是那个人也不会\x01",
            "做这么危险的实验吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "……不、不过也不能这么断言，\x01",
            "这正是可怕的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_EF8")

    label("loc_EB6")


    ChrTalk(    #54
        0xFE,
        (
            "拉、拉赛尔博士\x01",
            "不会与此有关吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "哈哈……\x01",
            "不、不可能的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF8")

    Jump("loc_147B")

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9C")

    ChrTalk(    #56
        0xFE,
        "现在发生的现象……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "好像以前拉赛尔博士\x01",
            "也搞出来过吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "就是说现象持续的过程中\x01",
            "我们是无可奈何的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "……今天就早点回去吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1000")

    label("loc_F9C")


    ChrTalk(    #60
        0xFE,
        (
            "好像以前拉赛尔博士\x01",
            "也搞出来过现在的这个现象吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "就是说现象持续的过程中\x01",
            "我们是无可奈何的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1000")

    Jump("loc_147B")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_10CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_106F")

    ChrTalk(    #62
        0xFE,
        "地震已经好像平息了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "不管怎么样，\x01",
            "希望地面能够稳住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "就算是为了『卡佩尔』。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C8")

    label("loc_106F")


    ChrTalk(    #65
        0xFE,
        (
            "虽然工房长已经发表了说法\x01",
            "地震已经好像平息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "嘿嘿，那个测量\x01",
            "好像起作用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_10C8")

    Jump("loc_147B")

    label("loc_10CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_111E")

    ChrTalk(    #67
        0xFE,
        (
            "呼～工作总算\x01",
            "收拾完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "那～接下来就\x01",
            "交给特莱斯主任吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117F")

    label("loc_111E")


    ChrTalk(    #69
        0xFE,
        (
            "呼～工作总算\x01",
            "开始进行处理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "不过博士很厉害啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "在短期内能构筑起\x01",
            "这样的系统。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_117F")

    Jump("loc_147B")

    label("loc_1182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11E5")

    ChrTalk(    #72
        0xFE,
        (
            "呼，博士真是每每\x01",
            "有惊人之举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "要是早点说的话，\x01",
            "我们就能再轻松一点了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1216")

    label("loc_11E5")


    ChrTalk(    #74
        0xFE,
        "抱歉，现在有点忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "有话一会儿再说。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1216")

    Jump("loc_147B")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_141E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1358")

    ChrTalk(    #76
        0xFE,
        (
            "『卡佩尔』与其他的机械不同\x01",
            "好像必须休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "虽然是我个人的想法，不过我觉得\x01",
            "这恐怕和有没有『记忆』有关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "『卡佩尔』在活动中\x01",
            "会不断更新自己的记忆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "不过没有在工作中重新构成\x01",
            "那些记忆并储存的时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "所以整理记忆就只能\x01",
            "在停止的状态下进行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "……我现在就在写\x01",
            "有关这方面的论文。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141B")

    label("loc_1358")


    ChrTalk(    #82
        0xFE,
        "『卡佩尔』的状态很好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "因为最近让它避开连续\x01",
            "工作而进行定期的休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "『卡佩尔』与其他的机械不同\x01",
            "好像必须休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "定期休息的话状态\x01",
            "就不容易下降。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "真有趣。\x01",
            "就好像生物一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_141B")

    Jump("loc_147B")

    label("loc_141E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_147B")

    ChrTalk(    #87
        0xFE,
        (
            "这个房间在５层，\x01",
            "地震时还是有点摇晃的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "希望『卡佩尔』不要\x01",
            "又因此而闹别扭。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147B")

    TalkEnd(0xC)
    Return()

    # Function_5_DB5 end

    def Function_6_147F(): pass

    label("Function_6_147F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1496")
    Call(0, 15)
    Call(0, 16)

    label("loc_1496")

    OP_4A(0x8, 255)
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x12, 0x4)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x3, 0x3)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(2120, 0, 13780, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -510, 0, 10500, 0)
    SetChrPos(0xA, 4420, 1000, 4220, 90)
    SetChrPos(0x9, 460, 0, 7640, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)

    def lambda_1563():
        OP_6D(1900, 0, 8220, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1563)

    def lambda_157B():
        OP_67(0, 7040, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_157B)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Fade(250)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x4, 0x7)
    OP_0D()
    Sleep(500)
    OP_4A(0xA, 255)
    Sleep(500)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #89
        0xA,
        (
            "拉赛尔博士，\x01",
            "１号连接成功。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#100F#5P看来是的。\x01",
            "情报很快就有了。\x02\x03",

            "#104F嗯嗯……\x01",
            "好像还算稳定。\x02\x03",

            "#102F接着开始进行２号、３号的连接。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    OP_4B(0xA, 255)

    def lambda_1684():
        OP_6D(710, 0, 3390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1684)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x7)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #92
        0x101,
        "#1006F#5P干得不错，干得不错。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1744")

    ChrTalk(    #93
        0x106,
        (
            "#552F#2P真是的……\x01",
            "仍旧是个稀奇古怪的房间啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177F")

    label("loc_1744")


    ChrTalk(    #94
        0x103,
        (
            "#023F#2P怎么说好呢……\x01",
            "这个房间用这一句话就能概括了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177F")

    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_17A1():
        OP_6D(710, 0, 5300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17A1)
    TurnDirection(0x9, 0x101, 400)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1858")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇已经和玛多克重逢的情况下】\x01",      # 0
            "【◇还没和玛多克重逢的情况下】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1843"),
        (1, "loc_1849"),
        (SWITCH_DEFAULT, "loc_184F"),
    )


    label("loc_1843")

    OP_A2(0x1481)
    Jump("loc_184F")

    label("loc_1849")

    OP_A3(0x1481)
    Jump("loc_184F")

    label("loc_184F")

    FadeToBright(300, 0)

    label("loc_1858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A54")

    ChrTalk(    #95
        0x9,
        (
            "#802F#5P哟……\x01",
            "艾丝蒂尔，你来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1004F#6P啊，玛多克工房长。\x02",
    )

    CloseMessageWindow()

    def lambda_18B0():
        OP_6D(710, 0, 6300, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18B0)

    def lambda_18C8():
        OP_8E(0xFE, 0xFFFFFEDE, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18C8)
    Sleep(200)
    SetChrFlags(0x9, 0x4)

    def lambda_18ED():
        OP_8E(0xFE, 0x1F4, 0x0, 0x19E6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18ED)

    def lambda_1908():
        OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x10EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1908)
    Sleep(100)

    def lambda_1928():
        OP_8E(0xFE, 0xFFFFFE84, 0x0, 0xB9A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1928)
    Sleep(200)

    def lambda_1948():
        OP_8E(0xFE, 0xFFFFFA42, 0x0, 0xBCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1948)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x9, 0x1)
    ClearChrFlags(0x9, 0x4)

    ChrTalk(    #97
        0x101,
        (
            "#1025F#6P好久不见。\x01",
            "好像是从诞辰庆典以来就没见过了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#803F#5P嗯，是啊。\x02\x03",

            "#800F听说你遇到了一些事……\x01",
            "还能这么打起精神来真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "谢谢你，工房长先生。\x02\x03",

            "#1011F我们受博士的委托\x01",
            "安放了测量仪……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8D")

    label("loc_1A54")


    ChrTalk(    #100
        0x9,
        "#802F#5P哟，艾丝蒂尔，你们来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1011F#6P嗯，工房长先生。\x02",
    )

    CloseMessageWindow()

    def lambda_1AA1():
        OP_6D(710, 0, 6300, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1AA1)

    def lambda_1AB9():
        OP_8E(0xFE, 0xFFFFFEDE, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1AB9)
    Sleep(200)
    SetChrFlags(0x9, 0x4)

    def lambda_1ADE():
        OP_8E(0xFE, 0x1F4, 0x0, 0x19E6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1ADE)

    def lambda_1AF9():
        OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x10EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1AF9)
    Sleep(100)

    def lambda_1B19():
        OP_8E(0xFE, 0xFFFFFE84, 0x0, 0xB9A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1B19)
    Sleep(200)

    def lambda_1B39():
        OP_8E(0xFE, 0xFFFFFA42, 0x0, 0xBCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1B39)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x9, 0x1)
    ClearChrFlags(0x9, 0x4)

    ChrTalk(    #102
        0x101,
        (
            "#1011F#6P我们受博士的委托\x01",
            "安放了测量仪……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8D")


    ChrTalk(    #103
        0x9,
        (
            "#800F#5P嗯，看来是的。\x02\x03",

            "好像正好刚从各地的\x01",
            "测量仪传来了情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x107,
        (
            "#064F#6P那就是说『卡佩尔』的\x01",
            "调整也结束了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 400)

    ChrTalk(    #105
        0x9,
        (
            "#801F#5P嗯，博士刚让它\x01",
            "运行了专用程序。\x02",
        )
    )

    CloseMessageWindow()
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x8, 0xB)
    OP_4A(0xA, 255)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #106
        0xA,
        "#5P２号、３号的连接也成功了。\x02",
    )

    CloseMessageWindow()

    def lambda_1C9C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C9C)
    Sleep(50)

    def lambda_1CAF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1CAF)
    Sleep(50)

    def lambda_1CC2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CC2)
    Sleep(50)

    def lambda_1CD5():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1CD5)
    Sleep(50)

    def lambda_1CE8():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1CE8)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #107
        0x8,
        "#100F嗯，我们这边也确认好了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    OP_4B(0xA, 255)

    ChrTalk(    #108
        0x8,
        (
            "#101F好好……\x01",
            "哪边都很稳定。\x02\x03",

            "这样一来从１号到３号的\x01",
            "所有测量仪都传来了情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1D98():
        OP_6D(710, 0, 7300, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D98)
    TurnDirection(0x8, 0x101, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #109
        0x8,
        "#103F哟，总算回来了啊。\x02",
    )

    CloseMessageWindow()

    def lambda_1DD9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1DD9)
    Sleep(50)

    def lambda_1DEC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DEC)
    Sleep(50)

    def lambda_1DFF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1DFF)
    Sleep(50)

    def lambda_1E12():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1E12)
    Sleep(50)

    def lambda_1E25():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E25)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #110
        0x8,
        (
            "#101F看，托你们的福\x01",
            "顺利地得到了情报。\x02\x03",

            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1016F#2P哈哈，我们只是\x01",
            "运送了测量仪的零件而已。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F11")

    ChrTalk(    #112
        0x106,
        (
            "#051F而且这件事也是\x01",
            "我们这边请求的。\x02\x03",

            "应该慰劳一下你那个连装置的\x01",
            "启动都负责到底了的孙女啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F72")

    label("loc_1F11")


    ChrTalk(    #113
        0x103,
        (
            "#027F而且这件事也是\x01",
            "我们这边请求的。\x02\x03",

            "应该慰劳一下你那个连装置的\x01",
            "启动都负责到底了的孙女啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F72")

    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x107, 90, 400)

    ChrTalk(    #114
        0x107,
        (
            "#560F#5P没、没什么的～\x01",
            "也不是什么了不起的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#101F不不，\x01",
            "你也很努力了。\x02\x03",

            "传送器的设定也没问题。\x01",
            "情报发送很正常。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)

    ChrTalk(    #116
        0x107,
        (
            "#067F#6P嘿嘿，太好了。\x02\x03",

            "#560F那就是说\x01",
            "准备都完成了？\x02\x03",

            "还有什么需要我帮忙的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#104F没有了，准备已经完成。\x02\x03",

            "#100F我已经给『卡佩尔』设计了程序，\x01",
            "如果七耀脉的运动发生紊乱的话\x01",
            "它会自动开始解析的。\x02\x03",

            "接下来，就只要等待\x01",
            "什么地方再发生地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1007F#2P是吗……\x01",
            "现在可以算是告一段落了。\x02\x03",

            "#1015F不过干等什么地方发生地震\x01",
            "还是让人感觉不自在啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C5")

    ChrTalk(    #119
        0x104,
        (
            "#035F#6P呵呵，是啊。\x02\x03",

            "#030F说不定蔡斯还会发生\x01",
            "大规模的地震。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2202")

    label("loc_21C5")


    ChrTalk(    #120
        0x105,
        (
            "#043F#6P确实是这样。\x02\x03",

            "说不定蔡斯还会发生\x01",
            "大规模的地震。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_222E")

    ChrTalk(    #121
        0x106,
        (
            "#050F对此你们\x01",
            "有什么对策吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2250")

    label("loc_222E")


    ChrTalk(    #122
        0x103,
        (
            "#020F对此你们\x01",
            "有什么对策吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2250")

    OP_8C(0x9, 225, 400)

    ChrTalk(    #123
        0x9,
        (
            "#800F#5P我们姑且已经把\x01",
            "容易倒塌的装置进行了固定。\x02\x03",

            "#803F不过即便如此，要是发生比\x01",
            "上次更厉害的地震就不好办了。\x02\x03",

            "设备的损坏应该是不能避免了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "#100F就是说，这台\x01",
            "『卡佩尔』也是一样的？\x02\x03",

            "因为摇晃而引起误操作\x01",
            "致使实验失败的可能性也很高。\x02\x03",

            "#101F大家都向女神祈祷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1007F#2P啊……\x01",
            "感觉有点不安了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D7")

    ChrTalk(    #126
        0x104,
        (
            "#035F#6P呼，就算是最新技术也\x01",
            "仍然很需要祈求神灵保佑啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2414")

    label("loc_23D7")


    ChrTalk(    #127
        0x105,
        (
            "#045F#6P呼，就算是最新技术也\x01",
            "仍然很需要祈求神灵保佑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2414")

    OP_8C(0x107, 180, 400)

    ChrTalk(    #128
        0x107,
        (
            "#560F#5P嘿嘿，技术人员可是\x01",
            "出奇地有信仰心哦。\x02\x03",

            "我在进行困难的作业时\x01",
            "也经常向女神祈祷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        (
            "#806F#5P确实有点道理。\x02\x03",

            "我在博士首次开发\x01",
            "导力飞船的时候\x01",
            "一天要去三次教会哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        "#102F什么啊，你真是个失礼的家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        (
            "#803F#5P经历过３９次实验失败的话\x01",
            "当然会这么做了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #132
        0x101,
        (
            "#1016F#2P啊哈哈……\x01",
            "从以前开始就有这种感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)

    ChrTalk(    #133
        0x107,
        "#067F#6P嗯……确实如此。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_25E8")

    ChrTalk(    #134
        0x106,
        (
            "#051F不过既然这样的话，\x01",
            "我们去找个地方打发时间吧？\x02\x03",

            "先回一次协会\x01",
            "报告一下也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263F")

    label("loc_25E8")


    ChrTalk(    #135
        0x103,
        (
            "#027F不过既然这样的话，\x01",
            "我们去找个地方打发时间吧？\x02\x03",

            "先回一次协会\x01",
            "报告一下也不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263F")


    ChrTalk(    #136
        0x8,
        (
            "#101F嗯，你们就这么办吧。\x02\x03",

            "有什么动向的话\x01",
            "我们会联络协会的……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x64)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0xC, 0xF)
    Sleep(1500)
    OP_20(0x7D0)
    OP_22(0x9E, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x10, 0x17)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 0, 600)
    OP_8C(0x8, 0, 600)
    OP_8C(0x101, 0, 600)
    OP_8C(0x107, 0, 600)

    ChrTalk(    #137
        0x101,
        "#1020F#2P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x107,
        "#065F#6P莫、莫非……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        (
            "#104F……看来没必要\x01",
            "回协会的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xA, 255)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 270, 600)

    ChrTalk(    #140
        0xA,
        (
            "#5P从１号到３号的所有\x01",
            "测量仪都有了变化！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xA,
        (
            "#5P地下的七耀脉的\x01",
            "运动好像变得活跃了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "#102F嗯，继续\x01",
            "监视屏幕。\x02\x03",

            "如果通讯被阻断就报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        "#5P明白了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 600)
    OP_4B(0xA, 255)
    OP_8C(0x8, 225, 600)

    def lambda_2889():

        label("loc_2889")

        TurnDirection(0x9, 0x8, 400)
        OP_48()
        Jump("loc_2889")

    QueueWorkItem2(0x9, 1, lambda_2889)

    def lambda_289A():
        OP_6D(-590, 0, 6000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_289A)
    OP_8E(0x8, 0xFFFFF95C, 0x0, 0x25B2, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFF95C, 0x0, 0x169E, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFFE20, 0x0, 0x169E, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    OP_44(0x9, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #144
        0x8,
        (
            "#102F#5P即时开始解析\x01",
            "3处的情报……\x02\x03",

            "搜索目前集合了\x01",
            "最大地震波的地点……\x02\x03",

            "#104F座标【12.73，378.02】\x01",
            "哟……原来是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1026F#2P怎、怎样啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "#102F#5P现在已经知道\x01",
            "哪儿在发生地震了。\x02\x03",

            "是雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1020F#2P#3S！！！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A0D")

    ChrTalk(    #148
        0x106,
        "#055F什么！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A20")

    label("loc_2A0D")


    ChrTalk(    #149
        0x103,
        "#024F什么！？\x02",
    )

    CloseMessageWindow()

    label("loc_2A20")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xA, 255)
    OP_4B(0x8, 255)
    OP_4B(0xC, 255)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_147F end

    def Function_7_2A44(): pass

    label("Function_7_2A44")

    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -1120, 0, -1250, 0)
    ClearChrFlags(0x101, 0x80)

    def lambda_2A6B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A6B)
    OP_8E(0x101, 0xFFFFFE98, 0x0, 0x92E, 0x7D0, 0x0)
    OP_8C(0x101, 0, 400)
    Return()

    # Function_7_2A44 end

    def Function_8_2A93(): pass

    label("Function_8_2A93")

    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x107, -1120, 0, -1250, 0)
    ClearChrFlags(0x107, 0x80)

    def lambda_2ABA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2ABA)
    OP_8E(0x107, 0xFFFFF9C0, 0x0, 0x852, 0x7D0, 0x0)
    OP_8C(0x107, 0, 400)
    Return()

    # Function_8_2A93 end

    def Function_9_2AE2(): pass

    label("Function_9_2AE2")

    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF7, -1120, 0, -1250, 0)
    ClearChrFlags(0xF7, 0x80)

    def lambda_2B09():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_2B09)
    OP_8E(0xF7, 0xFFFFFE02, 0x0, 0x38E, 0x7D0, 0x0)
    OP_8C(0xF7, 0, 400)
    Return()

    # Function_9_2AE2 end

    def Function_10_2B31(): pass

    label("Function_10_2B31")

    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF9, -1120, 0, -1250, 0)
    ClearChrFlags(0xF9, 0x80)

    def lambda_2B58():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_2B58)
    OP_8E(0xF9, 0xFFFFF952, 0x0, 0x2E4, 0x7D0, 0x0)
    OP_8C(0xF9, 0, 400)
    Return()

    # Function_10_2B31 end

    def Function_11_2B80(): pass

    label("Function_11_2B80")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B97")
    Call(0, 15)
    Call(0, 16)

    label("loc_2B97")

    OP_22(0x9E, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x12, 0x4)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x10, 0x17)
    OP_4A(0x8, 255)
    OP_6D(-840, 0, 2850, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -290, 0, 4300, 0)
    SetChrPos(0x107, -1430, 0, 4330, 0)
    SetChrPos(0xF7, -380, 0, 2970, 0)
    SetChrPos(0xF9, -1470, 0, 3020, 0)
    SetChrPos(0x8, -480, 0, 5780, 0)
    SetChrPos(0xA, 4420, 1000, 4220, 90)
    SetChrPos(0x9, 500, 0, 6630, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_2CB6():
        OP_6D(-800, 0, 5130, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2CB6)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -1080, 0, -1380, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_2CEF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2CEF)
    OP_8E(0xB, 0xFFFFFC4A, 0x0, 0x5AA, 0xBB8, 0x0)
    OP_0D()

    ChrTalk(    #150
        0xB,
        (
            "工房长！\x01",
            "从雷斯顿要塞收到联络！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "说是就在刚才\x01",
            "发生了中等规模的地震！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(    #152
        0x9,
        "#805F#5P果然如此……\x02",
    )

    CloseMessageWindow()

    def lambda_2D85():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D85)
    Sleep(100)

    def lambda_2D98():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2D98)
    Sleep(50)

    def lambda_2DAB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2DAB)
    Sleep(50)

    def lambda_2DBE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2DBE)
    Sleep(50)

    def lambda_2DD1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2DD1)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #153
        0x101,
        "#1020F#5P受、受害情况怎样！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xB,
        (
            "幸好\x01",
            "没人受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xB,
        (
            "好像是事先\x01",
            "做好了对地震的防范。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#1007F#5P太、太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "#101F#5P不愧是卡西乌斯。\x01",
            "有着万全的危机对策。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x9D, 0x46)
    OP_22(0x9D, 0x0, 0x64)
    OP_23(0x9E)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x18, 0x1B)

    def lambda_2EB4():
        OP_6D(-800, 0, 6500, 800)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2EB4)
    OP_8C(0x8, 0, 500)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #158
        0x8,
        (
            "#102F#6P那么……\x01",
            "这边的解析也完成了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F03():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2F03)
    Sleep(50)

    def lambda_2F16():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F16)
    Sleep(100)

    def lambda_2F29():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2F29)
    Sleep(50)

    def lambda_2F3C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2F3C)
    WaitChrThread(0xF9, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #159
        (
            "\x07\x05拉赛尔博士确认了\x01",
            "显示屏上的解析结果。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #160
        0x8,
        (
            "#102F#6P嗯……让我看看……\x02\x03",

            "#103F哦哦……\x01",
            "这真有意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1002F#2P发、发现什么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #162
        0x8,
        (
            "#100F#5P嗯，别着急。\x02\x03",

            "根据这个解析，地震发生之前，\x01",
            "七耀脉的运动出现了异常。\x02\x03",

            "然后，由于扭曲的运动\x01",
            "集合到要塞地下，\x01",
            "发生了局部性的地震。\x02\x03",

            "因为发生在相当浅的地下，\x01",
            "所以没影响到其他地方。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_30EF")

    ChrTalk(    #163
        0x106,
        "#057F这就是地震的真正原因吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3114")

    label("loc_30EF")


    ChrTalk(    #164
        0x103,
        "#022F这就是地震的真正原因呢……\x02",
    )

    CloseMessageWindow()

    label("loc_3114")


    ChrTalk(    #165
        0x101,
        (
            "#1020F#2P就、就是说……\x02\x03",

            "有人通过操纵七耀脉\x01",
            "引发地震！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3191")

    ChrTalk(    #166
        0x104,
        (
            "#032F#6P呼……\x01",
            "可以称之为『地震兵器』呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C6")

    label("loc_3191")


    ChrTalk(    #167
        0x105,
        (
            "#042F#6P『地震兵器』……\x01",
            "说不定可以这么称呼它。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C6")


    ChrTalk(    #168
        0x8,
        (
            "#102F#5P嗯。\x01",
            "你说得没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x107,
        (
            "#065F#6P可、可是爷爷。\x02\x03",

            "操纵七耀脉的运动这种事\x01",
            "真的有可能做到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        (
            "#805F#5P唔，就算利用最新的土木技术\x01",
            "也应该是不可能做到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "#104F#5P对此我也有同感。\x02\x03",

            "#102F不过，虽然不愿意承认……\x01",
            "可似乎是有人已经做到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1022F#2P好一个挑衅行为……\x02\x03",

            "#1005F博士，你还能推断出一些什么吗！？\x02\x03",

            "比如那个『地震兵器』\x01",
            "被放在哪里什么的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x107,
        "#560F#6P啊……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3366")

    ChrTalk(    #174
        0x106,
        "#051F对！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3375")

    label("loc_3366")


    ChrTalk(    #175
        0x103,
        "#021F对！\x02",
    )

    CloseMessageWindow()

    label("loc_3375")


    ChrTalk(    #176
        0x8,
        (
            "#103F#5P原来如此……\x01",
            "这可真是个盲点呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 600)
    OP_8C(0x9, 225, 400)

    ChrTalk(    #177
        0x8,
        (
            "#102F#6P解析３处七耀脉\x01",
            "运动的扭曲……\x02\x03",

            "如果用逆算的形式\x01",
            "算出扭曲的源头的话……\x02\x03",

            "出来了……\x01",
            "坐标【165.88，-228.35】……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #178
        0x107,
        "#065F#6P咦……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #179
        0x101,
        "#1002F#2P提妲，你认识这地方？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)

    ChrTalk(    #180
        0x107,
        "#065F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #181
        "\x07\x05提妲取出了地图。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS134._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS207._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS208._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS209._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #182
        (
            "\x07\x00#062F座标中心为\x01",
            "蔡斯，单位塞尔矩……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #183
        (
            "\x07\x00#062F从这里往东１２塞尔矩、\x01",
            "往北３７８塞尔矩的地点\x01",
            "是雷斯顿要塞的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #184
        (
            "\x07\x00#062F往东１６５塞尔矩、\x01",
            "往南２２８塞尔矩的地点……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #185
        (
            "\x18\x07\x05从蔡斯往东１６５塞尔矩、\x01",
            "往南２２８塞尔矩的地点是？\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【卡鲁迪亚钟乳洞】\x01",      # 0
            "【红莲之塔】\x01",            # 1
            "【亚尔摩温泉】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_379F"),
        (1, "loc_37DD"),
        (2, "loc_381B"),
        (SWITCH_DEFAULT, "loc_385C"),
    )


    label("loc_379F")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #186
        (
            "\x07\x00#063F啊，不对。\x02\x03",

            "大概是在\x01",
            "这附近……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_385C")

    label("loc_37DD")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #187
        (
            "\x07\x00#063F啊，不对。\x02\x03",

            "大概是在\x01",
            "这附近……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_385C")

    label("loc_381B")

    OP_2B(0x88, 0x2)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #188
        (
            "\x07\x00#063F嗯、嗯。\x02\x03",

            "大概是在\x01",
            "这附近……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_385C")

    label("loc_385C")

    OP_AE(0x1F4)
    Sleep(500)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(300, 50, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #189
        "\x07\x00#1020F啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_38F3")
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #190
        "\x07\x00#555F完全成为盲点了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3925")

    label("loc_38F3")

    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #191
        "\x07\x00#025F完全成为盲点了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3925")

    TurnDirection(0x8, 0x101, 0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D3")

    ChrTalk(    #192
        0x104,
        (
            "#035F#6P亚尔摩村……\x02\x03",

            "#030F看来那个温泉胜地里面\x01",
            "才是真正的『震源』呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A1F")

    label("loc_39D3")


    ChrTalk(    #193
        0x105,
        (
            "#047F#6P亚尔摩村……\x02\x03",

            "#042F看来那个温泉胜地里面\x01",
            "才是真正的『震源』呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A1F")


    ChrTalk(    #194
        0x8,
        (
            "#102F#5P虽然不敢断言，\x01",
            "不过那个可能性看来很高。\x02\x03",

            "你们准备怎么做？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #195
        0x101,
        (
            "#1005F#2P那还用问！\x01",
            "必须马上去调查。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3AC8")

    ChrTalk(    #196
        0x106,
        (
            "#057F嗯……\x01",
            "看来要抓紧了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE8")

    label("loc_3AC8")


    ChrTalk(    #197
        0x103,
        (
            "#022F嗯……\x01",
            "看来要抓紧了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AE8")


    ChrTalk(    #198
        0x8,
        (
            "#104F#5P是吗……\x02\x03",

            "#102F那你们就把\x01",
            "提妲也带去好了。\x02\x03",

            "这孩子的知识和技术\x01",
            "一定会对调查有帮助的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)

    ChrTalk(    #199
        0x107,
        "#560F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)

    ChrTalk(    #200
        0x107,
        "#062F#6P嗯，我一定能帮忙的！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #201
        0x101,
        (
            "#1007F#2P唔……\x01",
            "虽然可能有危险……\x02\x03",

            "#1006F不过有我们保护你的话\x01",
            "应该没问题的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3C3A")

    ChrTalk(    #202
        0x106,
        (
            "#053F真是的……拿你没办法。\x02\x03",

            "#050F喂，小不点。\x01",
            "绝对不要勉强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C6B")

    label("loc_3C3A")


    ChrTalk(    #203
        0x103,
        (
            "#026F是啊……\x02\x03",

            "#020F提妲。\x01",
            "千万不能勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C6B")

    OP_8C(0x107, 180, 400)

    ChrTalk(    #204
        0x107,
        "#062F#5P好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x9,
        (
            "#800F#5P那么就由我来\x01",
            "联系亚尔摩村吧。\x02\x03",

            "如果请毛婆婆帮忙的话\x01",
            "你们的调查也会更加顺利吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #206
        0x101,
        "#1006F#6P嗯，那真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "#800F#5P海泽尔。\x01",
            "准备通讯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xB,
        "遵命。\x02",
    )

    CloseMessageWindow()

    def lambda_3D42():
        OP_6D(-840, 0, 2850, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3D42)

    def lambda_3D5A():

        label("loc_3D5A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3D5A")

    QueueWorkItem2(0x101, 2, lambda_3D5A)

    def lambda_3D6B():

        label("loc_3D6B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3D6B")

    QueueWorkItem2(0x107, 2, lambda_3D6B)

    def lambda_3D7C():

        label("loc_3D7C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3D7C")

    QueueWorkItem2(0xF7, 2, lambda_3D7C)

    def lambda_3D8D():

        label("loc_3D8D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3D8D")

    QueueWorkItem2(0xF9, 2, lambda_3D8D)
    OP_43(0x9, 0x1, 0x0, 0xC)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0xD)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0xF9, 0x2)

    def lambda_3DCB():
        OP_6D(-840, 0, 5130, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3DCB)

    def lambda_3DE3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3DE3)
    Sleep(50)

    def lambda_3DF6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DF6)
    Sleep(50)

    def lambda_3E09():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3E09)
    Sleep(50)

    def lambda_3E1C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3E1C)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #209
        0x8,
        (
            "#102F#5P我在这里\x01",
            "解析『卡佩尔』。\x02\x03",

            "了解到什么的话就会尽快联系旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#1002F#2P嗯，拜托了。\x02\x03",

            "我们如果发现了什么\x01",
            "也会联络中央工房的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x8,
        "#102F#5P嗯，交给你们了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3F0F")

    ChrTalk(    #212
        0x106,
        (
            "#054F好……\x01",
            "那么我们这就去亚尔摩村吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F3B")

    label("loc_3F0F")


    ChrTalk(    #213
        0x103,
        (
            "#024F那么……\x01",
            "我们就这就去亚尔摩村吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F3B")

    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1230, 0, 3450, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -1230, 0, 3450, 17)
    SetChrPos(0x1, -1230, 0, 3450, 17)
    SetChrPos(0x2, -1230, 0, 3450, 17)
    SetChrPos(0x3, -1230, 0, 3450, 17)
    SetChrPos(0x8, -480, 0, 10270, 0)
    OP_0D()
    OP_8C(0x8, 0, 0)
    OP_4B(0x8, 255)
    OP_4B(0xA, 255)
    OP_4B(0xC, 255)
    OP_72(0x2, 0x4)
    OP_71(0x12, 0x4)
    OP_A2(0x1420)
    OP_28(0x88, 0x4, 0x2)
    OP_28(0x88, 0x4, 0x8)
    OP_28(0x88, 0x1, 0x1)
    OP_28(0x85, 0x4, 0x10)
    OP_28(0x86, 0x4, 0x10)
    OP_28(0x87, 0x4, 0x10)
    OP_28(0x70, 0x4, 0x40)
    Sleep(500)
    OP_1D(0xD)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_2B80 end

    def Function_12_4043(): pass

    label("Function_12_4043")

    OP_8E(0x9, 0x3B6, 0x0, 0x17CA, 0x9C4, 0x0)
    OP_8E(0x9, 0x258, 0x0, 0xA5A, 0x9C4, 0x0)
    OP_8E(0x9, 0xFFFFFBBE, 0x0, 0x2E4, 0x9C4, 0x0)
    OP_8E(0x9, 0xFFFFFB32, 0x0, 0xFFFFFE8E, 0x9C4, 0x0)
    OP_20(0xBB8)

    def lambda_409E():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_409E)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0x9, 0xFFFFFB50, 0x0, 0xFFFFF8DA, 0x9C4, 0x0)
    SetChrFlags(0x9, 0x80)
    Return()

    # Function_12_4043 end

    def Function_13_40C9(): pass

    label("Function_13_40C9")

    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xFFFFFB32, 0x0, 0xFFFFFE8E, 0x9C4, 0x0)

    def lambda_40EA():
        OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40EA)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFB50, 0x0, 0xFFFFF8DA, 0x9C4, 0x0)
    SetChrFlags(0xB, 0x80)
    Return()

    # Function_13_40C9 end

    def Function_14_4115(): pass

    label("Function_14_4115")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-200, 0, 7100, 1000)
    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(    #214
        (
            "\x07\x02#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.7.0\x01",
            "Copyright(C)Z.C.F. 1197-1202\x01",
            "MODE:Information Retrieval\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WＯＫ!\x01",
            "#200W　#20W\x01",
            "#1S已连接到数据库。\x01",
            "请选择要搜索的内容。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4226")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58FA")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        55,
        80,
        1,
        "【中央工房关联】　　\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4274"),
        (SWITCH_DEFAULT, "loc_58EA"),
    )


    label("loc_4274")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58DA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        55,
        153,
        1,
        (
            "【设立·沿革】\x01",            # 0
            "【技术一览】\x01",              # 1
            "【关联信息搜索】　　\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_42DD"),
        (1, "loc_4932"),
        (2, "loc_55F8"),
        (SWITCH_DEFAULT, "loc_58CA"),
    )


    label("loc_42DD")


    AnonymousTalk(    #215
        (
            "\x07\x02#1S【Ｓ１１５４】（Ｓ…七耀历）\x01",
            "Ｃ·爱普斯泰恩博士于列曼自治州去世。\x01",
            "【Ｓ１１５５】\x01",
            "Ａ·拉赛尔博士回到利贝尔王国。\x01",
            "回国后提倡普及导力器技术，\x01",
            "但是没得到世人的认可和支持。\x01",
            "【Ｓ１１５７】\x01",
            "拉赛尔博士带领蔡斯的钟表工匠普及导力器。\x01",
            "同年，『蔡斯技术工房』（即之后的中央工房）设立。\x01",
            "【Ｓ１１６０】\x01",
            "埃德佳Ⅲ世在视察蔡斯技术工房后提供巨额资金建设工\x01",
            "房。拉赛尔博士出任首任工房长。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #216
        (
            "\x07\x02#1S【Ｓ１１６２】\x01",
            "埃德佳Ⅲ世去世。艾莉茜雅Ⅱ世即位。\x01",
            "【Ｓ１１６４】\x01",
            "『伦格兰德大桥』落成。\x01",
            "【Ｓ１１６８】\x01",
            "首部导力飞船『加拉托拉巴号』诞生。\x01",
            "（经过３９次飞行实验失败后的产物）\x01",
            "【Ｓ１１７３】\x01",
            "蔡斯技术工房开始对共和国乌尔努社和帝国莱恩福尔特\x01",
            "社输出导力器技术。工房改名为『中央工房』。\x01",
            "【Ｓ１１７５】\x01",
            "飞船公社设立。定期船『林德号』开始服役。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #217
        (
            "\x07\x02#1S【Ｓ１１７７】\x01",
            "定期船『赛希莉亚号』开始服役。\x01",
            "【Ｓ１１７８】\x01",
            "移动工房船『莱普尼兹号』开始服役。\x01",
            "【Ｓ１１８０】\x01",
            "中央工房搬迁（即现在的建筑物）。\x01",
            "开掘卡鲁迪亚平原丘陵的一角，地下工房建成。\x01",
            "【Ｓ１１８２】\x01",
            "拉赛尔工房长退休。\x01",
            "玛多克技术主任出任第二任工房长。\x01",
            "【Ｓ１１８５】\x01",
            "自然科学和医学研究部门设立。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #218
        (
            "\x07\x02#1S【Ｓ１１８７】\x01",
            "客船『埃迪鲁那号』在卡尔瓦德领海沉没。\x01",
            "尤迪斯王太子夫妇去世。\x01",
            "【Ｓ１１９０】\x01",
            "与爱普斯泰恩财团合作，\x01",
            "发表了『导力网络』的构想。\x01",
            "【Ｓ１１９２】\x01",
            "『百日战役』爆发。\x01",
            "中央工房被埃雷波尼亚帝国接管。\x01",
            "拉赛尔博士在雷斯顿要塞开发出警备飞艇，\x01",
            "并将其用于反攻作战中，取得了显赫的战功，\x01",
            "从此警备飞艇作为王国军的主力兵器而被使用。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #219
        (
            "\x07\x02#1S【Ｓ１１９３】\x01",
            "利贝尔王国和埃雷波尼亚帝国缔结和平条约。\x01",
            "战后，王国再次向帝国输出导力器。\x01",
            "【Ｓ１１９７】\x01",
            "导力演算器『卡佩尔』Ver.1完成。\x01",
            "【Ｓ１１９９】\x01",
            "高速巡洋舰『埃尔赛尤』开发工程开始。\x01",
            "【Ｓ１２０２】\x01",
            "高速巡洋舰『埃尔赛尤』竣工，进入试飞阶段。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58D7")

    label("loc_4932")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55E8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49D0")

    Menu(
        2,
        55,
        259,
        1,
        (
            "【导力器】\x01",              # 0
            "【结晶回路】\x01",            # 1
            "【七耀石】\x01",              # 2
            "【导力飞船】\x01",            # 3
            "【导力兵器】\x01",            # 4
            "【战术导力器】\x01",          # 5
            "【游击士协会招牌】\x01",      # 6
        )
    )

    Jump("loc_4A25")

    label("loc_49D0")


    Menu(
        2,
        55,
        259,
        1,
        (
            "【导力器】\x01",          # 0
            "【结晶回路】\x01",        # 1
            "【七耀石】\x01",          # 2
            "【导力飞船】\x01",        # 3
            "【导力兵器】\x01",        # 4
            "【战术导力器】\x01",      # 5
        )
    )


    label("loc_4A25")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4A4D"),
        (1, "loc_4BD6"),
        (2, "loc_4CA0"),
        (3, "loc_4DB8"),
        (4, "loc_4EED"),
        (5, "loc_5062"),
        (6, "loc_5386"),
        (SWITCH_DEFAULT, "loc_55D8"),
    )


    label("loc_4A4D")


    AnonymousTalk(    #220
        (
            "\x07\x02#1S项目：导力器（Orbment）\x01",
            "在半世纪前由Ｃ·爱普斯泰恩博士所发明，是能从七耀\x01",
            "石中提取导力，从而引发各种各样现象的机械装置的总\x01",
            "称。导力器内部的构造和齿轮的运动，使加工七耀石而\x01",
            "成的结晶回路相互干涉，可以引发丰富多彩的现象。导\x01",
            "力器的实用性，除了能产生丰富现象以外，还在于拥有\x01",
            "『经过一段时间内部的导力可以自然恢复』这种特异的\x01",
            "便利性。另外，经济效率也要远远地领先于各种外燃、\x01",
            "内燃引擎设备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E5")

    label("loc_4BD6")


    AnonymousTalk(    #221
        (
            "\x07\x02#1S项目：结晶回路（Quartz）\x01",
            "将七耀石的碎片（耀晶片，Sepith）精制、加工而成的\x01",
            "具有结晶构造的回路。作为能量源的同时，本身还是引\x01",
            "起各种各样现象的装置。但结晶回路必须安装在导力器\x01",
            "内才可以发挥作用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E5")

    label("loc_4CA0")


    AnonymousTalk(    #222
        (
            "\x07\x02#1S项目：七耀石（Septium）\x01",
            "是在大陆全土分布的７种贵重矿石的总称。因被人们称\x01",
            "为『古代的宝石』、『神秘的象征』而变得珍重。近代\x01",
            "一种将体积过小不能成为宝石的碎片（耀晶片）精制加\x01",
            "工制作出结晶回路的技术被发明出来，因此导致七耀石\x01",
            "资源的重要性在大陆诸国之间一夜之间变得十分重要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E5")

    label("loc_4DB8")


    AnonymousTalk(    #223
        (
            "\x07\x02#1S项目：导力飞船\x01",
            "导力飞船可以称得上是导力技术精华凝聚而成的结晶。\x01",
            "集合了用于重力制御的大型飞翔装置和供给大量能量的\x01",
            "导力引擎两大技术，使得如此大的飞船在空中飞行成为\x01",
            "可能。\x01",
            "为了实现高效率的导力传送和十分复杂的船体控制，最\x01",
            "新的飞船大多搭载了高性能的导力演算器。２０亚矩以\x01",
            "下的小型飞船又被称为『飞艇』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E5")

    label("loc_4EED")


    AnonymousTalk(    #224
        (
            "\x07\x02#1S项目：导力兵器\x01",
            "即以导力枪、导力炮作为代表，使用导力技术的兵器体\x01",
            "系。现在已成为大多数国家军队的主力装备。\x01",
            "导力枪枪管内具有能将能量按照螺旋线聚集并高速射出\x01",
            "豆粒大小的金属子弹的构造，与发射火药的枪相比，填\x01",
            "弹量大幅增加，而且还能够调节枪的威力。\x01",
            "导力炮则可以发射封装了能量的炮弹（导力弹）并产生\x01",
            "爆炸，与发射火药的炮相比，其后坐力小，而且也可以\x01",
            "自由调节威力大小。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E5")

    label("loc_5062")


    AnonymousTalk(    #225
        (
            "\x07\x02#1S项目：战术导力器\x01",
            "可以发动导力魔法的导力器。大小和怀表差不多，内部\x01",
            "构造则相当精致优雅。\x01",
            "战术导力器具有安装结晶回路后能够提高持有者能力的\x01",
            "设计，使内部结晶回路与持有者达到同步，引发出『共\x01",
            "鸣现象』，以代替传统释放魔法所需的复杂的齿轮和驱\x01",
            "动装置，使持有者能够发动各种导力魔法。\x01",
            "而且，根据复数结晶回路属性和势能的组合不同，持有\x01",
            "者能够使用的导力魔法也会发生变化，具有相当的灵活\x01",
            "性。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #226
        (
            "\x07\x02#1S追加：新型战术导力器\x01",
            "作为战术导力器的开发者，爱普斯泰恩财团对过去的型号进\x01",
            "行大幅改良，并且成功投入实用的新规格战术导力器。和过\x01",
            "去只有六个结晶回路插槽的旧型号相比，这种新型号则具备\x01",
            "了七个结晶回路插槽，可以实现更为灵活的结晶回路组合。\x01",
            "新型号不仅使可以使用的魔法变得多元化，而且使其威力也\x01",
            "得到了飞跃性的提升。但是，由于新型号和过去型号的基本\x01",
            "构造有很大的不同，新型战术导力器也有着无法互换结晶回\x01",
            "路的缺陷。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E5")

    label("loc_5386")

    OP_A2(0x4)
    OP_28(0x6C, 0x1, 0x8)

    AnonymousTalk(    #227
        (
            "\x07\x02#1S内容：游击士协会招牌\x01",
            "这就是英俊潇洒的怪盗绅士布卢布兰凭借其天才般的超级无\x01",
            "敌手腕从傻瓜般的超级无能游击士协会之一的蔡斯支部的檐\x01",
            "头偷走的金属招牌。虽然没什么经济价值，不过给予协会相\x01",
            "关人员的打击是无穷的，正在读此文的诸位想必也强烈地感\x01",
            "受到了屈辱吧。好了，闲话到此为止。该是时候给出下一个\x01",
            "提示了。\x01\x02",

            "　\x07\x02\x01",
            "　　┌──────────────────┐　　\x01",
            "　　│　　　　第３把钥匙再次位于市内。　　│　\x01",
            "　　│      抬头看那『尖帽子三兄弟』吧。  │　　\x01",
            "　　└──────────────────┘\x01",
            "　※另外，这个记录会自动删除。　　　　\x01",
            "　　所以再次极力推荐诸位赶快做好应做的笔记！　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E5")

    label("loc_55D8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55E5")

    label("loc_55E5")

    Jump("loc_4932")

    label("loc_55E8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_58D7")

    label("loc_55F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58BA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        55,
        255,
        1,
        (
            "【内燃引擎设备】\x01",      # 0
            "【汽油】\x01",              # 1
            "【运输车】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5655"),
        (1, "loc_572E"),
        (2, "loc_57CD"),
        (SWITCH_DEFAULT, "loc_58AA"),
    )


    label("loc_5655")


    AnonymousTalk(    #228
        (
            "\x07\x02#1S项目：内燃引擎设备\x01",
            "在机关装置内燃烧燃料以获得能量的动力源。与导力机\x01",
            "关相比经济效率低下，而且还会产生噪音、废气等各种\x01",
            "问题，因此已经停止开发和生产。\x01\x01",
            "『内燃引擎设备』\x01",
            "库存量：１台\x01",
            "管理责任人：格斯塔夫维修长\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58B7")

    label("loc_572E")


    AnonymousTalk(    #229
        (
            "\x07\x02#1S项目：汽油\x01",
            "将天然产生的液态碳氢化合物（石油）分馏、精制而成\x01",
            "的液体。常作为内燃引擎设备的燃料以及工业生产的溶\x01",
            "剂使用。\x01\x01",
            "储备量：无（已向共和国订购）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58B7")

    label("loc_57CD")

    OP_28(0x29, 0x1, 0x8000)

    AnonymousTalk(    #230
        (
            "\x07\x02#1S项目：运输车\x01",
            "使用导力引擎驱动的各种车辆的总称。因为乘坐的舒适\x01",
            "度较差，速度也很慢，所以基本不用于客运方面，而主\x01",
            "要用来进行中短距离的货物运输。\x01\x01",
            "『运输车用驱动导力器』\x01",
            "库存量：不明\x01",
            "保管地点：地下工场搬入口\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58B7")

    label("loc_58AA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B7")

    label("loc_58B7")

    Jump("loc_55F8")

    label("loc_58BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_58D7")

    label("loc_58CA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58D7")

    label("loc_58D7")

    Jump("loc_4274")

    label("loc_58DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jump("loc_58F7")

    label("loc_58EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58F7")

    label("loc_58F7")

    Jump("loc_4226")

    label("loc_58FA")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5928")
    Call(1, 0)
    OP_A3(0x4)

    label("loc_5928")

    EventEnd(0x1)
    Return()

    # Function_14_4115 end

    def Function_15_592B(): pass

    label("Function_15_592B")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_59A5"),
        (1, "loc_59AB"),
        (SWITCH_DEFAULT, "loc_59B1"),
    )


    label("loc_59A5")

    OP_A2(0x1200)
    Jump("loc_59B1")

    label("loc_59AB")

    OP_A2(0x1201)
    Jump("loc_59B1")

    label("loc_59B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_59BF")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_59C3")

    label("loc_59BF")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_59C3")

    Return()

    # Function_15_592B end

    def Function_16_59C4(): pass

    label("Function_16_59C4")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_59FE")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_5A18")

    label("loc_59FE")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_5A18")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_16_59C4 end

    def Function_17_5A2A(): pass

    label("Function_17_5A2A")

    SetPlaceName(0x9A)
    Return()

    # Function_17_5A2A end

    SaveToFile()

Try(main)
