from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3115   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3115.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '玛多克工房长',                         # 9
        '康丝坦茨',                             # 10
        '米优',                                 # 11
        '格斯塔夫维修长',                       # 12
        '雨果',                                 # 13
        '普罗梅笛',                             # 14
        '拉赛尔博士',                           # 15
        '露依赛',                               # 16
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
        'ED6_DT07/CH02620 ._CH',             # 00
        'ED6_DT07/CH02623 ._CH',             # 01
        'ED6_DT07/CH01230 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH02440 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH01430 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02620P._CP',             # 00
        'ED6_DT07/CH02623P._CP',             # 01
        'ED6_DT07/CH01230P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH02440P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH01430P._CP',             # 08
    )

    DeclNpc(
        X                   = 4380,
        Z                   = 0,
        Y                   = 2370,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -107400,
        Z                   = 0,
        Y                   = -90,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -104390,
        Z                   = 0,
        Y                   = 8560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -103940,
        Z                   = 0,
        Y                   = 98950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -102540,
        Z                   = 0,
        Y                   = 97610,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -103430,
        Z                   = 0,
        Y                   = 108150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 2430,
        Z                   = 0,
        Y                   = 2850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -102520,
        Z                   = 0,
        Y                   = 96150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_34C",          # 01, 1
        "Function_2_3BB",          # 02, 2
        "Function_3_1979",         # 03, 3
        "Function_4_19B2",         # 04, 4
        "Function_5_1A31",         # 05, 5
        "Function_6_1E1E",         # 06, 6
        "Function_7_2368",         # 07, 7
        "Function_8_281F",         # 08, 8
        "Function_9_2F22",         # 09, 9
        "Function_10_343A",        # 0A, 10
        "Function_11_37FB",        # 0B, 11
        "Function_12_3C30",        # 0C, 12
        "Function_13_3F98",        # 0D, 13
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 3)), scpexpr(EXPR_END)), "loc_1FE")
    ClearChrFlags(0xB, 0x10)

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25F")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 1)
    SetChrPos(0x8, 2430, 200, 5330, 180)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0xD, -103580, 0, 99360, 180)
    ClearChrFlags(0xF, 0x80)
    OP_8C(0xF, 270, 0)
    ClearChrFlags(0xF, 0x10)
    OP_8C(0xC, 270, 0)
    Jump("loc_341")

    label("loc_25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2C8")
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 1)
    SetChrPos(0x8, 2430, 200, 5330, 180)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, -104980, 0, 640, 0)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -104980, 0, 1980, 180)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_341")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2F7")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -103480, 0, 99640, 180)
    Jump("loc_341")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_324")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x10)
    OP_8C(0xC, 180, 0)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_341")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_341")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x10)
    OP_8C(0xC, 180, 0)
    ClearChrFlags(0xF, 0x80)

    label("loc_341")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_1F2 end

    def Function_1_34C(): pass

    label("Function_1_34C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    OP_6F(0x0, 29)
    OP_72(0x0, 0x10)
    OP_6F(0x1, 29)
    OP_72(0x1, 0x10)
    OP_6F(0x2, 29)
    OP_72(0x2, 0x10)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_79(0xFF, 0x2)
    OP_7A(0x18, 0x2)
    OP_7A(0x19, 0x2)
    OP_7A(0x1A, 0x2)
    OP_7B()
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)

    label("loc_3BA")

    Return()

    # Function_1_34C end

    def Function_2_3BB(): pass

    label("Function_2_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C0")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_456")
    Jump("loc_498")

    label("loc_456")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_472")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_498")

    label("loc_472")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48E")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_498")

    label("loc_48E")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_498")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jump("loc_4C3")

    label("loc_4C0")

    TalkBegin(0x8)

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_6E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_696")

    ChrTalk(    #0
        0x8,
        (
            "#802F喔喔，是你们吗……\x02\x03",

            "温泉的泵\x01",
            "修理好了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_561")

    ChrTalk(    #1
        0x107,
        "#061F是的，已经修理好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1006F嗯，现在随时\x01",
            "都可以去泡温泉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD")

    label("loc_561")


    ChrTalk(    #3
        0x101,
        (
            "#1006F嗯，现在随时\x01",
            "都可以去泡温泉了。\x02\x03",

            "#1015F嗯，这全是提妲\x01",
            "的功劳啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AD")


    ChrTalk(    #4
        0x8,
        (
            "#801F噢噢！那可太让人高兴了。\x02\x03",

            "等工作告一段落之后\x01",
            "我要赶快去看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1049F嗯嗯，偶尔\x01",
            "也要好好休息一下。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_664")

    ChrTalk(    #6
        0x107,
        (
            "#560F说的对啊。\x02\x03",

            "不管是什么机械\x01",
            "也都要定期维护的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_664")


    ChrTalk(    #7
        0x8,
        (
            "#801F哈哈，多谢忠告。\x01",
            "我会牢记在心的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_6DE")

    label("loc_696")


    ChrTalk(    #8
        0x8,
        (
            "#800F水泵的修理\x01",
            "真是辛苦你们了。\x02\x03",

            "#806F呵，早点去温泉里\x01",
            "泡一泡吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DE")

    Jump("loc_195F")

    label("loc_6E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_754")

    ChrTalk(    #9
        0x8,
        (
            "#802F喔喔……\x01",
            "艾丝蒂尔，约修亚。\x02\x03",

            "还有提妲也……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x107,
        "#067F嘿嘿，我们回来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_77A")

    label("loc_754")


    ChrTalk(    #11
        0x8,
        (
            "#802F喔喔……\x01",
            "艾丝蒂尔，约修亚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77A")


    ChrTalk(    #12
        0x101,
        "#1000F工房长先生，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        "#1040F好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#801F嗯，平安回来了\x01",
            "就比什么都好。\x02\x03",

            "博士的发明品\x01",
            "还有用吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1011F那个发生器吗？\x02\x03",

            "#1001F当然啊，帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1040F王国军可能比我们\x01",
            "更加感激你们吧。\x02\x03",

            "在通讯系统恢复之前\x01",
            "各个据点都已经完全被孤立了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#801F呵呵，原来如此。\x02\x03",

            "看来这东西充分发挥了\x01",
            "预想中的效果啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1015F嗯，这虽然很好，\x01",
            "不过……\x02\x03",

            "#1002F工房长先生，\x01",
            "……中央工房现在怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_968")

    ChrTalk(    #19
        0x107,
        (
            "#063F这、这么漆黑一团…\x01",
            "实在没办法再继续研究了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_993")

    label("loc_968")


    ChrTalk(    #20
        0x102,
        (
            "#1043F像现在这种状况\x01",
            "什么也干不了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_993")


    ChrTalk(    #21
        0x8,
        (
            "#805F啊啊……\x01",
            "很严峻的状况啊。\x02\x03",

            "现在的问题堆积如山，\x01",
            "已经都忙不过来了。\x02\x03",

            "不过我们能做的也只有\x01",
            "尽力解决了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1007F是吗，真是不得了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1040F要是有什么我们可以帮忙的事\x01",
            "请一定别客气啊。\x02\x03",

            "遇到什么困难的话\x01",
            "和协会联络就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#800F嗯，谢谢啦。\x01",
            "你们也要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20CD)
    Jump("loc_D43")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_END)), "loc_BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B86")

    ChrTalk(    #25
        0x8,
        (
            "#802F喔喔，这不是艾丝蒂尔吗。\x02\x03",

            "汽油已经拿到了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1006F嗯，拿到了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#1040F介绍信……\x01",
            "还麻烦您，真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#801F哪里哪里～这是应当的。\x02\x03",

            "那么，修理水泵的事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_BDB")

    label("loc_B86")


    ChrTalk(    #29
        0x8,
        (
            "#800F修理水泵的事\x01",
            "就拜托你们了。\x02\x03",

            "我也很喜欢温泉呢，\x01",
            "修理设施的事就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDB")

    Jump("loc_D43")

    label("loc_BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C87")

    ChrTalk(    #30
        0x8,
        (
            "#800F介绍信里已经写清\x01",
            "的负责人就可以了。\x02\x03",

            "如果汽油已经送到的话，\x01",
            "要交给你们了。\x02\x03",

            "街道的路灯都已经熄灭了，\x01",
            "现在哪条路都很危险。\x02\x03",

            "路上要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_CDC")

    label("loc_C87")


    ChrTalk(    #31
        0x8,
        (
            "#800F介绍信里已经写清\x01",
            "的负责人就可以了。\x02\x03",

            "如果汽油已经送到的话，\x01",
            "要交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDC")

    Jump("loc_D43")

    label("loc_CDF")


    ChrTalk(    #32
        0x8,
        (
            "#805F虽然很想早点开始研究，\x01",
            "但现在问题堆积如山。\x02\x03",

            "#806F呼～总之还是\x01",
            "先把这些文件整理一下吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D43")

    Jump("loc_195F")

    label("loc_D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 2)), scpexpr(EXPR_END)), "loc_DEA")

    ChrTalk(    #33
        0x8,
        (
            "#800F我已经以自己的名义\x01",
            "发表了有关地震的安全宣言。\x02\x03",

            "现在最重要的就是\x01",
            "消除市民们的不安。\x02\x03",

            "要去王都的话，\x01",
            "路上一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEE")

    label("loc_DEA")

    Call(0, 5)

    label("loc_DEE")

    Jump("loc_109C")

    label("loc_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_EC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E4A")

    ChrTalk(    #34
        0x8,
        (
            "#800F那么亚尔摩村那边\x01",
            "就先让我去把事情做个说明。\x02\x03",

            "那么，多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBE")

    label("loc_E4A")


    ChrTalk(    #35
        0x8,
        (
            "#800F那么亚尔摩村那边\x01",
            "就先让我去把事情做个说明。\x02\x03",

            "等你们过去以后毛婆婆\x01",
            "会尽力帮你们忙的。\x02\x03",

            "那么，多加小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_EBE")

    Jump("loc_109C")

    label("loc_EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F5C")

    ChrTalk(    #36
        0x8,
        (
            "#800F拉赛尔博士的头脑\x01",
            "在关键的时刻\x01",
            "才能体现出真正的价值。\x02\x03",

            "正因如此才会\x01",
            "被称作天才吧。\x02\x03",

            "#806F哈，博士的才能有时\x01",
            "也会引起『天灾』呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC4")

    label("loc_F5C")


    ChrTalk(    #37
        0x8,
        (
            "#800F这次的地震太奇妙了。\x01",
            "研究者对此也很有兴趣呢。\x02\x03",

            "如果拉赛尔博士的实验\x01",
            "能成为突破口就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FC4")

    Jump("loc_109C")

    label("loc_FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1048")

    ChrTalk(    #38
        0x8,
        (
            "#800F刚收到联络，\x01",
            "好像连圣海姆门那里\x01",
            "也遭遇了地震。\x02\x03",

            "不过从这里完全\x01",
            "感觉不到摇晃。\x02\x03",

            "看来这次地震\x01",
            "好像有点特别呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109C")

    label("loc_1048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_109C")

    ChrTalk(    #39
        0x8,
        (
            "#800F市内的情报收集\x01",
            "由我去做吧。\x02\x03",

            "近来街道也很危险，\x01",
            "路上要小心谨慎哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109C")

    Jump("loc_1195")

    label("loc_109F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_10FC")

    ChrTalk(    #40
        0x8,
        (
            "#800F中央工房也会全力\x01",
            "配合协会的调查。\x02\x03",

            "虽然很麻烦，\x01",
            "不过还是要请你们多帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1195")

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1141")

    ChrTalk(    #41
        0x8,
        (
            "#800F拉赛尔博士\x01",
            "正在找你们。\x02\x03",

            "是不是应该回\x01",
            "协会看看？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1195")

    label("loc_1141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1195")

    ChrTalk(    #42
        0x8,
        (
            "#800F市内的情报收集\x01",
            "由我去做吧。\x02\x03",

            "近来街道也很危险，\x01",
            "路上要小心谨慎哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1195")

    Jump("loc_195F")

    label("loc_1198")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_133B")

    ChrTalk(    #43
        0x8,
        "#801F啊，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x106, 400)

    ChrTalk(    #44
        0x8,
        "#801F阿加特也在啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        "#051F你好，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1006F工房长先生，好久不见。\x01",
            "好像是从诞辰庆典以来就没见过了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #47
        0x8,
        (
            "#801F嗯，是啊。\x02\x03",

            "听说你遇到了很多事……\x01",
            "还能这么打起精神来真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "谢谢你，工房长先生。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1338")

    ChrTalk(    #49
        0x8,
        (
            "#800F你们好像会为了协助\x01",
            "蔡斯支部而逗留一阵子。\x02\x03",

            "有你们在我就放心了。\x01",
            "请你们多帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1338")

    Jump("loc_155D")

    label("loc_133B")


    ChrTalk(    #50
        0x8,
        (
            "#801F哟……\x01",
            "艾丝蒂尔，你来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1006F工房长先生，好久不见。\x01",
            "好像是从诞辰庆典以来就没见过了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#801F嗯，是啊。\x02\x03",

            "听说你遇到了很多事……\x01",
            "还能这么打起精神来真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "谢谢你，工房长先生。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #54
        0x8,
        "#802F请问这位是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1006F嗯，她是雪拉姐……\x01",
            "支部的前辈…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        (
            "#020F我是洛连特支部的游击士，\x01",
            "雪拉扎德·哈维。\x02\x03",

            "虽然可能是短期的\x01",
            "麻烦您了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_14EF")

    ChrTalk(    #57
        0x8,
        (
            "#801F艾丝蒂尔的前辈啊。\x01",
            "也请你多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155D")

    label("loc_14EF")


    ChrTalk(    #58
        0x8,
        (
            "#801F也请你多关照。\x02\x03",

            "#800F你们好像会为了协助\x01",
            "蔡斯支部而逗留一阵子。\x02\x03",

            "我也代表整个城市\x01",
            "期待着你们的表现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_164D")

    ChrTalk(    #59
        0x8,
        (
            "#800F听说你们已经开始\x01",
            "协助拉赛尔博士的实验了。\x02\x03",

            "中央工房也会全力\x01",
            "配合协会的调查。\x02\x03",

            "虽然很麻烦，\x01",
            "不过还是要请你们多帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 3)

    ChrTalk(    #60
        0x8,
        (
            "#800F嗯，如果有什么不方便的地方\x01",
            "就立即联络我们吧。\x02\x03",

            "那么，你们也要当心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1006F嗯，再见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1959")

    label("loc_164D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_17A2")
    Call(0, 3)

    ChrTalk(    #62
        0x101,
        "#1006F我们会尽全力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#802F说起来，拉赛尔博士\x01",
            "好像在找你们。\x02\x03",

            "据说是完成了一个什么准备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1004F哦，原来是这样啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1716")

    ChrTalk(    #65
        0x106,
        (
            "#052F是不是应该先回\x01",
            "仔细看着指南针前进啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173A")

    label("loc_1716")


    ChrTalk(    #66
        0x103,
        (
            "#027F是不是应该先回\x01",
            "确认一下？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173A")


    ChrTalk(    #67
        0x8,
        (
            "#800F嗯，这样比较好。\x02\x03",

            "#806F呼，虽然很麻烦，\x01",
            "不过还是请你们继续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1016F嗯、嗯，那么再见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1959")

    label("loc_17A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1959")
    Call(0, 3)

    ChrTalk(    #69
        0x101,
        (
            "#1006F嗯，我们会尽力的。\x02\x03",

            "说起来，工房长先生你好像\x01",
            "也在帮助协会吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #70
        0x8,
        (
            "#800F嗯，刚才的地震之后\x01",
            "收到了雾香的联络。\x02\x03",

            "她让我收集地震前后\x01",
            "有没有发生过可疑情况的情报。\x02\x03",

            "#806F我刚开始弄，\x01",
            "并没有什么成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F是吗……\x01",
            "嗯，结果也不会那么快就出来吧。\x02\x03",

            "#1000F我们也马上要去\x01",
            "沃尔费堡垒调查了……\x02\x03",

            "工房长先生请继续\x01",
            "做市内的调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#800F嗯，一有发现\x01",
            "我就会联络协会的。\x02\x03",

            "艾丝蒂尔你们也要小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1006F嗯，再见。\x02",
    )

    CloseMessageWindow()

    label("loc_1959")

    OP_A2(0x1481)
    OP_A2(0x0)

    label("loc_195F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1975")
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Jump("loc_1978")

    label("loc_1975")

    TalkEnd(0x8)

    label("loc_1978")

    Return()

    # Function_2_3BB end

    def Function_3_1979(): pass

    label("Function_3_1979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_199A")

    ChrTalk(    #74
        0x106,
        "#051F嗯，请放心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B1")

    label("loc_199A")


    ChrTalk(    #75
        0x103,
        "#525F嗯，请放心。\x02",
    )

    CloseMessageWindow()

    label("loc_19B1")

    Return()

    # Function_3_1979 end

    def Function_4_19B2(): pass

    label("Function_4_19B2")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 2)), scpexpr(EXPR_END)), "loc_1A29")

    ChrTalk(    #76
        0xE,
        (
            "#100F看来那个『结社』的技术力量\x01",
            "已经高得没话说了。\x02\x03",

            "嗯，好久没碰到\x01",
            "这么有挑战性的研究课题了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2D")

    label("loc_1A29")

    Call(0, 5)

    label("loc_1A2D")

    TalkEnd(0xE)
    Return()

    # Function_4_19B2 end

    def Function_5_1A31(): pass

    label("Function_5_1A31")

    OP_4A(0xE, 255)

    ChrTalk(    #77
        0x8,
        "#802F哟，这不是艾丝蒂尔你们吗。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)

    ChrTalk(    #78
        0xE,
        "#103F还没有出发吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1000F嗯，稍微有点事。\x02\x03",

            "#1015F……不过你们好像在谈话？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "#100F嗯，王国军那边送来了\x01",
            "调查报告书。\x02\x03",

            "是有关那个投影装置的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1011F投影装置……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B56")

    ChrTalk(    #82
        0x106,
        (
            "#050F就是在卢安的敌人使用的\x01",
            "那个制造幻影的装置吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8E")

    label("loc_1B56")


    ChrTalk(    #83
        0x103,
        (
            "#022F就是在卢安的敌人使用的\x01",
            "那个制造幻影的装置吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8E")


    ChrTalk(    #84
        0xE,
        (
            "#104F嗯，就是你们\x01",
            "告诉我的那个。\x02\x03",

            "#102F因为它是研究『福音』\x01",
            "所不可或缺的资料。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x101, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C04")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1C09")

    label("loc_1C04")

    SetChrSubChip(0xFE, 2)

    label("loc_1C09")

    OP_8C(0x8, 180, 0)
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #85
        0x8,
        (
            "#800F本来我正要去询问军方，\x01",
            "不过他们倒先把报告书送来了。\x02\x03",

            "我刚才立即看了一遍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1004F哟～调查报告都\x01",
            "已经完成啦。\x02\x03",

            "看来军方对『结社』的调查\x01",
            "也相当卖力呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1CF0")

    ChrTalk(    #87
        0x106,
        (
            "#053F嗯，当然也肯定\x01",
            "有做记号吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D16")

    label("loc_1CF0")


    ChrTalk(    #88
        0x103,
        (
            "#026F嗯，当然也肯定\x01",
            "有做记号吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D16")


    ChrTalk(    #89
        0xE,
        (
            "#100F我也准备倾注全力在\x01",
            "『福音』的解析上。\x02\x03",

            "#100F那么，提妲就\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D6C():
        TurnDirection(0xF7, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1D6C)
    TurnDirection(0x101, 0xE, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1DA0")

    ChrTalk(    #90
        0x106,
        "#051F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBD")

    label("loc_1DA0")


    ChrTalk(    #91
        0x103,
        "#020F嗯，请交给我们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1DBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF4")

    ChrTalk(    #92
        0x107,
        (
            "#560F嗯……\x01",
            "爷爷你们也要好好的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E16")

    label("loc_1DF4")


    ChrTalk(    #93
        0x101,
        "#1006F嗯……你们也要好好的。\x02",
    )

    CloseMessageWindow()

    label("loc_1E16")

    OP_4B(0xE, 255)
    OP_A2(0x1642)
    Return()

    # Function_5_1A31 end

    def Function_6_1E1E(): pass

    label("Function_6_1E1E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E3C")
    OP_A2(0x4)

    label("loc_1E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDA")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在上半部完成过QST046、QST047、QST048其中之一】\x01",      # 0
            "【◇在上半部没完成过其中任何一个】\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1ECE"),
        (1, "loc_1ED4"),
        (SWITCH_DEFAULT, "loc_1EDA"),
    )


    label("loc_1ECE")

    OP_A2(0x4)
    Jump("loc_1EDA")

    label("loc_1ED4")

    OP_A3(0x4)
    Jump("loc_1EDA")

    label("loc_1EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1F00")
    Call(0, 8)
    Jump("loc_215A")

    label("loc_1F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1FCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F5B")

    ChrTalk(    #94
        0xFE,
        (
            "那个新人现在在\x01",
            "研究室里干活儿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "反正那孩子做事\x01",
            "一定很得要领。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FCC")

    label("loc_1F5B")


    ChrTalk(    #96
        0xFE,
        (
            "事务工作的实习\x01",
            "大家都是从帮资料室工作\x01",
            "来开始积累经验的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "不过像我这样\x01",
            "起点直接成终点的人\x01",
            "也是有的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1FCC")

    Jump("loc_215A")

    label("loc_1FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_20AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2046")

    ChrTalk(    #98
        0xFE,
        (
            "那个新人好像是\x01",
            "通过关系进入工房的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "不过我们这边是能力至上主义，\x01",
            "是如何进来的并不构成问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A7")

    label("loc_2046")


    ChrTalk(    #100
        0xFE,
        "那个新人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "好像是以前我们这儿\x01",
            "一个工匠的孙女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "就是说……\x01",
            "是通过关系进来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_20A7")

    Jump("loc_215A")

    label("loc_20AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_215A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2117")

    ChrTalk(    #103
        0xFE,
        (
            "我们这儿也有有前途的\x01",
            "新人被分配进来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "虽然有点傻傻的，\x01",
            "不过劳动能力很令人期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215A")

    label("loc_2117")


    ChrTalk(    #105
        0xFE,
        (
            "唉，地震真是\x01",
            "太讨厌了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "赶快让新人\x01",
            "来整理倒塌的书吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_215A")

    Jump("loc_21AD")

    label("loc_215D")


    ChrTalk(    #107
        0xFE,
        (
            "现在交给新人在做，\x01",
            "没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "不过如果碰到问题的话\x01",
            "还是要拜托你们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AD")

    Jump("loc_2364")

    label("loc_21B0")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #109
        0xFE,
        "哎呀，我说怎么这么面熟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "你是以前帮我\x01",
            "找过书的人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1016F啊～我想起来了。\x02\x03",

            "#1007F好、好像那是一段\x01",
            "很不容易的过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "呵呵，放心好了。\x01",
            "暂时没有要委托的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "正好有个新人被分配过来了，\x01",
            "现在杂物就交给那孩子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1000F哟～挺好的嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "嗯，暂时是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "如果有什么事她做不好\x01",
            "我还是会拜托协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "到时候\x01",
            "还请你们帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#1006F嗯，你放心好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "嗯，请多关照。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x142C)
    OP_A2(0x2)

    label("loc_2364")

    TalkEnd(0x9)
    Return()

    # Function_6_1E1E end

    def Function_7_2368(): pass

    label("Function_7_2368")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CA")

    ChrTalk(    #120
        0xFE,
        "啊，真无聊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "必须到５楼\x01",
            "去拿资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "呜～……\x01",
            "真讨厌爬楼梯。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2416")

    label("loc_23CA")


    ChrTalk(    #123
        0xFE,
        (
            "没有电梯的话\x01",
            "连回收资料也很麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "真是的～明天\x01",
            "要不要感冒一下呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2416")

    Jump("loc_281B")

    label("loc_2419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_24EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A3")

    ChrTalk(    #125
        0xFE,
        (
            "这么暗的话\x01",
            "书的标题也看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "真是的～让我\x01",
            "怎么工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "前辈也不知道去什么地方了，\x01",
            "我也早点回去吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_24E7")

    label("loc_24A3")


    ChrTalk(    #128
        0xFE,
        (
            "这么暗的话\x01",
            "书的标题也看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "真是的～让我\x01",
            "怎么工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E7")

    Jump("loc_281B")

    label("loc_24EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_24F8")
    Call(0, 8)
    Jump("loc_281B")

    label("loc_24F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_2691")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 5)), scpexpr(EXPR_END)), "loc_255B")

    ChrTalk(    #130
        0xFE,
        (
            "呼～这边结束以后\x01",
            "就要去研究室了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "为了提升第一印象\x01",
            "就要保持可爱的笑容～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268E")

    label("loc_255B")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)
    Sleep(400)

    ChrTalk(    #132
        0xFE,
        "啊～提妲，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        (
            "#060F啊，米优小姐。\x01",
            "工作感觉怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "好像都是在做一些杂事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "反正是实习，\x01",
            "也没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x107,
        (
            "#067F嘿嘿，大家开始时\x01",
            "都要先从小事做起的。\x02\x03",

            "不过米优小姐\x01",
            "一定没问题的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "谢谢你，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "我也有目标，\x01",
            "所以我会努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x107,
        "#061F嗯，请你加油。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1435)

    label("loc_268E")

    Jump("loc_281B")

    label("loc_2691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_26F8")

    ChrTalk(    #140
        0xFE,
        (
            "嗯～搞定这个以后\x01",
            "就要去研究室了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "第一印象很重要，\x01",
            "出门的时候总要保持微笑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2755")

    label("loc_26F8")


    ChrTalk(    #142
        0xFE,
        (
            "我的目标很明确，\x01",
            "就是成为工房的接待处小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "我一定会通过踏实的努力\x01",
            "来实现它的～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2755")

    Jump("loc_281B")

    label("loc_2758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_281B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_27B4")

    ChrTalk(    #144
        0xFE,
        "现在我正在进行业务实习。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "呼，一天到晚就是整理书籍，\x01",
            "我受不了了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_281B")

    label("loc_27B4")


    ChrTalk(    #146
        0xFE,
        (
            "唉～你们看看。\x01",
            "这是因为刚才的地震倒塌的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "与其责怪地震，倒不如说\x01",
            "是不干活儿的前辈造成的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_281B")

    TalkEnd(0xA)
    Return()

    # Function_7_2368 end

    def Function_8_281F(): pass

    label("Function_8_281F")

    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2848"),
        (1, "loc_2909"),
        (2, "loc_29CE"),
        (3, "loc_2B28"),
        (4, "loc_2C39"),
        (5, "loc_2DDD"),
        (SWITCH_DEFAULT, "loc_2F19"),
    )


    label("loc_2848")


    ChrTalk(    #148
        0xA,
        "所以呢，前辈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        (
            "我真的能成为\x01",
            "接待处小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x9,
        (
            "我都说了，你问我还不如\x01",
            "靠自己努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x9,
        (
            "不是挺好吗？\x01",
            "有目标是好事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x9,
        (
            "能够让人对未来充满憧憬的\x01",
            "工作真是太棒了。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F19")

    label("loc_2909")


    ChrTalk(    #153
        0x9,
        "不过海泽尔可是个劲敌呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "处处都受到\x01",
            "工房长的信赖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "海泽尔小姐\x01",
            "年纪不小了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        (
            "我觉得还是年轻又活跃的人\x01",
            "更能受到大家的喜爱～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "如果我穿得漂亮点\x01",
            "那胜利绝对是我的。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F19")

    label("loc_29CE")


    ChrTalk(    #158
        0xA,
        (
            "说起来，海泽尔小姐\x01",
            "还没结婚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x9,
        "嗯，还是独身。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        (
            "我和海泽尔一样\x01",
            "都还是单身呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #161
        0xA,
        "啊，是吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        (
            "哈哈，前辈～\x01",
            "那样不会有压力吗～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        (
            "男人就是易耗品……\x01",
            "好一点的也就是耐久度高的消耗品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x9,
        (
            "和那些消耗品定终身契约\x01",
            "岂不是更有压力吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #165
        0xA,
        "已、已经无药可救了～\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F19")

    label("loc_2B28")


    ChrTalk(    #166
        0xA,
        (
            "对了，我刚才\x01",
            "去了４楼的实验室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        (
            "前辈你不是说\x01",
            "有好男人的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        (
            "不过那个白衣男人好像\x01",
            "战战兢兢的，一副没用的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        "你说的是蒂亚利吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        "不是还有一个人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        "啊，还有一个人～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        "唉，我白努力了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x9,
        (
            "快要到午饭时间了，\x01",
            "雷伊可能出去了。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F19")

    label("loc_2C39")


    ChrTalk(    #174
        0x9,
        (
            "说起午饭，\x01",
            "我肚子倒也饿起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x9,
        (
            "要不要去『福格尔』？\x01",
            "今天就我来请客吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        "哇～我太喜欢前辈了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "对了，说起『福格尔』，\x01",
            "那边的男服务员也不错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        "咦，你不知道？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "那个男服务员正在和\x01",
            "我们这儿的女研究员交往哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #180
        0xA,
        (
            "啊───噢……\x01",
            "挺打击人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x9,
        (
            "鲁伊泽你认识吗？\x01",
            "在年轻人当中属于最有前途的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "外表虽然只能打５０分，\x01",
            "不过考试能够拿那个分数两倍的类型。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F19")

    label("loc_2DDD")


    ChrTalk(    #183
        0xA,
        (
            "唔～工房的人是不是\x01",
            "比较重视内涵呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        "那方面的倾向确实很强。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x9,
        (
            "如果工作不能得到认可\x01",
            "谁都不会正眼瞧你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        (
            "如果成为接待处小姐\x01",
            "会不会变得受欢迎～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        (
            "反正比呆在资料室\x01",
            "要好很多吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xA,
        (
            "是吗～果然还是\x01",
            "只有靠努力了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        (
            "好～一定要成为\x01",
            "接待处小姐～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xA,
        (
            "然后要猎取外观也ＯＫ的\x01",
            "研究员的心～\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F19")

    label("loc_2F19")

    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    Return()

    # Function_8_281F end

    def Function_9_2F22(): pass

    label("Function_9_2F22")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 3)), scpexpr(EXPR_END)), "loc_3181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_302A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2FAA")

    ChrTalk(    #191
        0xB,
        (
            "#690F新型引擎的换装工程\x01",
            "预定在雷斯顿要塞进行。\x02\x03",

            "让王都的『埃尔赛尤』返航，\x01",
            "我们则派工程船过去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3027")

    label("loc_2FAA")


    ChrTalk(    #192
        0xB,
        (
            "#690F很快新型引擎就能\x01",
            "搭载到『埃尔赛尤』上面了。\x02\x03",

            "必须赶快确定\x01",
            "换装工程的计划了。\x02\x03",

            "所以我最近也要\x01",
            "一直呆在中央工房。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3027")

    Jump("loc_30BE")

    label("loc_302A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_307F")

    ChrTalk(    #193
        0xB,
        (
            "#690F不过说起来地震\x01",
            "倒是很久没碰上了。\x02\x03",

            "总之没什么大损失\x01",
            "真是万幸了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BE")

    label("loc_307F")


    ChrTalk(    #194
        0xB,
        (
            "#690F嗯，我这边的招呼你们已经打过了。\x02\x03",

            "快点去见见小提妲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30BE")

    Jump("loc_317E")

    label("loc_30C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3126")

    ChrTalk(    #195
        0xB,
        (
            "#691F有你们在真是\x01",
            "以一敌万。\x02\x03",

            "如果有什么需要的话\x01",
            "拜托了。\x02\x03",

            "到那时请一定多关照啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317E")

    label("loc_3126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_317E")

    ChrTalk(    #196
        0xB,
        (
            "#691F小提妲热烈欢迎你们啊……\x01",
            "哈哈，也难怪。\x02\x03",

            "因为小提妲那丫头\x01",
            "很想念你啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_317E")

    Jump("loc_3436")

    label("loc_3181")


    ChrTalk(    #197
        0x101,
        "#1018F啊，维修长先生！\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xB)
    TurnDirection(0xB, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_31FF")

    ChrTalk(    #198
        0xB,
        (
            "#692F哟……\x01",
            "这不是艾丝蒂尔吗！\x02\x03",

            "#691F好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3236")

    label("loc_31FF")


    ChrTalk(    #199
        0xB,
        (
            "#692F哟……\x01",
            "这不是艾丝蒂尔吗！\x02\x03",

            "#691F好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3236")


    ChrTalk(    #200
        0x101,
        (
            "#1001F嘿嘿，好久不见！\x01",
            "维修长先生看起来也很精神呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        "#691F怎么？这次又是工作？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1006F嗯，我们接到了蔡斯\x01",
            "支部的支援请求。\x02\x03",

            "所以要在这里\x01",
            "工作一阵子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xB,
        (
            "#691F哦，那真令人安心。\x02\x03",

            "那我就不客气了，\x01",
            "有什么事的话就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#1001F嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_338A")
    TurnDirection(0xB, 0x107, 400)

    ChrTalk(    #205
        0xB,
        (
            "#691F小提妲也在\x01",
            "努力帮助博士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x107,
        "#060F哦，我明白！\x02",
    )

    CloseMessageWindow()
    Jump("loc_342B")

    label("loc_338A")


    ChrTalk(    #207
        0xB,
        (
            "#691F说起来，你们去见过\x01",
            "博士了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1011F嗯，刚去了。\x02\x03",

            "#1008F受、受到了提妲的\x01",
            "热烈欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xB,
        (
            "#693F哈哈，那是肯定的。\x02\x03",

            "因为小提妲那丫头\x01",
            "很想念你啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342B")

    OP_A2(0x1483)
    OP_A2(0x6)
    ClearChrFlags(0xB, 0x10)

    label("loc_3436")

    TalkEnd(0xB)
    Return()

    # Function_9_2F22 end

    def Function_10_343A(): pass

    label("Function_10_343A")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34EC")

    ChrTalk(    #210
        0xFE,
        (
            "我们这些技术人员虽然\x01",
            "在研究如何应对这种现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "不过越想越觉得这种\x01",
            "现象很异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "现在只能对事实\x01",
            "感到目瞪口呆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "根本想不出\x01",
            "有什么对策。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3542")

    label("loc_34EC")


    ChrTalk(    #214
        0xFE,
        (
            "现在只能对该现象的\x01",
            "异常性感到震惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "超过了人类智慧的力量……\x01",
            "只能这么想了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3542")

    Jump("loc_37F7")

    label("loc_3545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_366F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3612")

    ChrTalk(    #216
        0xFE,
        (
            "实在想不到事态\x01",
            "会发展成这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "『埃尔赛尤』的性能评价\x01",
            "已经告一段落，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "因为读取数据这种事\x01",
            "没有导力器也能完成。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "而且现在对这种现象\x01",
            "进行研究才是当务之急。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_366C")

    label("loc_3612")


    ChrTalk(    #220
        0xFE,
        (
            "实在想不到事态\x01",
            "会发展成这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "『埃尔赛尤』的性能评价\x01",
            "已经告一段落，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_366C")

    Jump("loc_37F7")

    label("loc_366F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_36E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_36DC")

    ChrTalk(    #222
        0xFE,
        (
            "插头的检查结束以后\x01",
            "请立即做登船准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "如果没有足够时间准备的话\x01",
            "一定会丢三落四的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E0")

    label("loc_36DC")

    Call(0, 13)

    label("loc_36E0")

    Jump("loc_37F7")

    label("loc_36E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_37F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_374C")

    ChrTalk(    #224
        0xFE,
        (
            "很快『埃尔赛尤』上就要\x01",
            "搭载新型引擎了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "我们准备前往雷斯顿要塞，\x01",
            "在那里施工。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F7")

    label("loc_374C")


    ChrTalk(    #226
        0xFE,
        (
            "不久『埃尔赛尤』上就要\x01",
            "搭载新型引擎了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "现在维修长正在\x01",
            "确定工程的次序。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "刚才的地震没造成\x01",
            "什么损失真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "如果使工程的准备\x01",
            "推迟的话就不好办了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_37F7")

    TalkEnd(0xC)
    Return()

    # Function_10_343A end

    def Function_11_37FB(): pass

    label("Function_11_37FB")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_38E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B1")

    ChrTalk(    #230
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "怎么想都想\x01",
            "不明白。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "那个空中的浮游物体……\x01",
            "以及这回的停止现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "将两者结合的话应该\x01",
            "能发现一些什么的……\x01",
            "不过就是想不通那是什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_38E0")

    label("loc_38B1")


    ChrTalk(    #234
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "不行啊……\x01",
            "果然还是无法说明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E0")

    Jump("loc_3C2C")

    label("loc_38E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39B4")

    ChrTalk(    #236
        0xFE,
        (
            "现在的情况是所有的\x01",
            "导力器都失去了导力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "以前也有过类似的事件，\x01",
            "所以我尝试进行了理论上的解析……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "不过很遗憾，大部分\x01",
            "还是没能理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "可能拉赛尔博士\x01",
            "已经掌握了一些什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3A06")

    label("loc_39B4")


    ChrTalk(    #240
        0xFE,
        (
            "对我们来说这种现象\x01",
            "现在还是一个大谜团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "目前根本无法从\x01",
            "理论上来阐明它。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A06")

    Jump("loc_3C2C")

    label("loc_3A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3AB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3A6F")

    ChrTalk(    #242
        0xFE,
        (
            "我正在整理\x01",
            "地震的数据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "多亏了拉赛尔博士，\x01",
            "『卡佩尔』里储存着\x01",
            "庞大的记录。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AAD")

    label("loc_3A6F")


    ChrTalk(    #244
        0xFE,
        "咦，有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "大家刚刚出发\x01",
            "前往了雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3AAD")

    Jump("loc_3C2C")

    label("loc_3AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3B1D")

    ChrTalk(    #246
        0xFE,
        (
            "拉赛尔博士好像也在\x01",
            "就地震进行调查呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "嗯，博士没问题的。\x01",
            "即便是从石头里\x01",
            "也能找出线索吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C2C")

    label("loc_3B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3B80")

    ChrTalk(    #248
        0xFE,
        (
            "现在还不知道\x01",
            "刚才的地震的震源。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "有可能是由于某种\x01",
            "特别的原因引发的地震。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C2C")

    label("loc_3B80")


    ChrTalk(    #250
        0xFE,
        (
            "关于刚才的地震\x01",
            "我查看了一下测量仪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "这……还真是一次不寻常的地震啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "和过去的所有地震\x01",
            "都完全没有相似之处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "有可能是由于某种\x01",
            "特别的原因引发的地震。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3C2C")

    TalkEnd(0xD)
    Return()

    # Function_11_37FB end

    def Function_12_3C30(): pass

    label("Function_12_3C30")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CA9")

    ChrTalk(    #254
        0xFE,
        "唔，导力停止现象啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "我、我理论\x01",
            "方面不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "呆在这里可能\x01",
            "也只是添乱……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    TalkEnd(0xF)
    SetChrFlags(0xFE, 0x10)
    Return()

    label("loc_3CA9")


    ChrTalk(    #257
        0xFE,
        "唔，导力停止现象啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "(……装作在思考的样子。)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F94")

    label("loc_3CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D77")

    ChrTalk(    #259
        0xFE,
        (
            "据说『埃尔赛尤』降落在\x01",
            "水中以后安然无恙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "无论如何总算让人松了一口气。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "我从心底里感谢那些\x01",
            "保护了船的船员们。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_3DCA")

    label("loc_3D77")


    ChrTalk(    #262
        0xFE,
        (
            "据说『埃尔赛尤』降落在\x01",
            "水中以后安然无恙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        "无论如何总算让人松了一口气。\x02",
    )

    CloseMessageWindow()

    label("loc_3DCA")

    Jump("loc_3F94")

    label("loc_3DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3E48")

    ChrTalk(    #264
        0xFE,
        "好，登船准备完成。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "大概乌尔斯会照顾\x01",
            "我妹妹乌缇的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "果然还是应该找一个\x01",
            "会做家务的男朋友啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EFB")

    label("loc_3E48")


    ChrTalk(    #267
        0xFE,
        (
            "嗯，图纸全部打包\x01",
            "放在箱子里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "导力系统的图纸\x01",
            "由雨果负责……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "为了预备紧急的空腹状态\x01",
            "还准备了点心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        "……嗯，准备完成！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "好，现在随时\x01",
            "可以乘工程船了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3EFB")

    Jump("loc_3F94")

    label("loc_3EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3F94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3F90")

    ChrTalk(    #272
        0xFE,
        (
            "呼～检查结束以后终于\x01",
            "要乘工程船出发了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "为了装配『埃尔赛尤』的引擎，\x01",
            "竟然和我们交换……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "好、好像还没\x01",
            "回过神来～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F94")

    label("loc_3F90")

    Call(0, 13)

    label("loc_3F94")

    TalkEnd(0xF)
    Return()

    # Function_12_3C30 end

    def Function_13_3F98(): pass

    label("Function_13_3F98")

    OP_4A(0xC, 255)
    OP_4A(0xF, 255)

    ChrTalk(    #275
        0xF,
        (
            "『埃尔赛尤』的工程需要的\x01",
            "备件都准备好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xF,
        (
            "接下来就是接受检查，\x01",
            "然后搬进工程船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xC,
        (
            "好，露依赛就负责\x01",
            "插头的检查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xC,
        (
            "因为那是你设计的，\x01",
            "比让其他人做要来的准确。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xF,
        "好，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xC,
        (
            "我和维修长一起\x01",
            "去看一下飞船坪的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 255)
    OP_4B(0xF, 255)
    OP_A2(0x8)
    OP_A2(0xB)
    Return()

    # Function_13_3F98 end

    SaveToFile()

Try(main)
