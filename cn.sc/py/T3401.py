from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3401   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        '士兵切斯利',                           # 9
        '黛米',                                 # 10
        '士兵儒勒',                             # 11
        '士兵埃克托尔',                         # 12
        '安敦',                                 # 13
        '利库斯',                               # 14
        '利塔街道方向',                         # 15
        '庭园大道方向',                         # 16
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
    )

    DeclNpc(
        X                   = 20790,
        Z                   = 11750,
        Y                   = 6470,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        X                   = 10500,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 10500,
        Z                   = 0,
        Y                   = 3140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 14160,
        Z                   = 13750,
        Y                   = 1650,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 16520,
        Z                   = 11750,
        Y                   = -540,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -37360,
        Z                   = 0,
        Y                   = 960,
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

    DeclNpc(
        X                   = 83520,
        Z                   = 0,
        Y                   = 630,
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
        X                   = -25540,
        Y                   = -1000,
        Z                   = -4310,
        Range               = -27840,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x1F90,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = 15150,
        TriggerZ            = 11750,
        TriggerY            = 1650,
        TriggerRange        = 400,
        ActorX              = 14160,
        ActorZ              = 15250,
        ActorY              = 1650,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_216",          # 00, 0
        "Function_1_342",          # 01, 1
        "Function_2_396",          # 02, 2
        "Function_3_43D",          # 03, 3
        "Function_4_461",          # 04, 4
        "Function_5_485",          # 05, 5
        "Function_6_4A9",          # 06, 6
        "Function_7_4CD",          # 07, 7
        "Function_8_4F1",          # 08, 8
        "Function_9_8D0",          # 09, 9
        "Function_10_AF9",         # 0A, 10
        "Function_11_C22",         # 0B, 11
        "Function_12_C27",         # 0C, 12
        "Function_13_D32",         # 0D, 13
        "Function_14_F74",         # 0E, 14
        "Function_15_1010",        # 0F, 15
        "Function_16_168B",        # 10, 16
        "Function_17_1724",        # 11, 17
        "Function_18_1850",        # 12, 18
    )


    def Function_0_216(): pass

    label("Function_0_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_230")
    ClearChrFlags(0xB, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_64(0x0, 0x1)
    Jump("loc_2CD")

    label("loc_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_24B")
    SetChrPos(0x8, 18040, 11750, -4680, 225)
    Jump("loc_2CD")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_260")
    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_64(0x0, 0x1)
    Jump("loc_2CD")

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_2B7")
    SetChrPos(0x8, 18300, 11750, -10110, 225)
    OP_43(0x8, 0x0, 0x0, 0x3)
    SetChrPos(0xC, 14830, 11750, 6510, 90)
    SetChrPos(0xD, 16120, 11750, 4840, 315)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_64(0x0, 0x1)
    Jump("loc_2CD")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2CD")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_341")
    SetChrPos(0xC, 14830, 11750, 6510, 90)
    SetChrPos(0xD, 16120, 11750, 4840, 315)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x8, 18300, 11750, -10110, 225)
    OP_43(0x8, 0x0, 0x0, 0x3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_A2(0x1413)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_341")

    Return()

    # Function_0_216 end

    def Function_1_342(): pass

    label("Function_1_342")

    OP_16(0x2, 0xFA0, 0xFFFE65D8, 0xFFFE0C00, 0x230056)
    OP_1C(0x2, 0x0, 0x12)
    OP_1C(0x3, 0x0, 0x12)
    OP_1C(0x4, 0x0, 0x12)
    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_395")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_395")

    Return()

    # Function_1_342 end

    def Function_2_396(): pass

    label("Function_2_396")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3C7"),
        (1, "loc_3D3"),
        (2, "loc_3DF"),
        (3, "loc_3EB"),
        (4, "loc_3F7"),
        (5, "loc_403"),
        (6, "loc_40F"),
        (SWITCH_DEFAULT, "loc_41B"),
    )


    label("loc_3C7")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_427")

    label("loc_3D3")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_427")

    label("loc_3DF")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_427")

    label("loc_3EB")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_427")

    label("loc_3F7")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_427")

    label("loc_403")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_427")

    label("loc_40F")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_427")

    label("loc_41B")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_427")

    label("loc_427")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_427")

    label("loc_43C")

    Return()

    # Function_2_396 end

    def Function_3_43D(): pass

    label("Function_3_43D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_460")
    OP_8D(0xFE, 20420, -7160, 16050, -13610, 2000)
    Jump("Function_3_43D")

    label("loc_460")

    Return()

    # Function_3_43D end

    def Function_4_461(): pass

    label("Function_4_461")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_484")
    OP_8D(0xFE, 15300, 14530, 19530, 9890, 2000)
    Jump("Function_4_461")

    label("loc_484")

    Return()

    # Function_4_461 end

    def Function_5_485(): pass

    label("Function_5_485")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A8")
    OP_8D(0xFE, 15160, 2490, 19190, -2240, 2000)
    Jump("Function_5_485")

    label("loc_4A8")

    Return()

    # Function_5_485 end

    def Function_6_4A9(): pass

    label("Function_6_4A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CC")
    OP_8D(0xFE, 30170, 1730, 27910, -3560, 2000)
    Jump("Function_6_4A9")

    label("loc_4CC")

    Return()

    # Function_6_4A9 end

    def Function_7_4CD(): pass

    label("Function_7_4CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F0")
    OP_8D(0xFE, 23750, 7410, 18380, -2820, 2000)
    Jump("Function_7_4CD")

    label("loc_4F0")

    Return()

    # Function_7_4CD end

    def Function_8_4F1(): pass

    label("Function_8_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_502")
    Call(0, 15)
    Return()

    label("loc_502")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_5F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_58B")

    ChrTalk(    #0
        0xFE,
        (
            "希德中校给人的\x01",
            "印象更像是文官，\x01",
            "不过实际上战斗力也十分了得哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "特别是在魔法方面\x01",
            "可是王国军中少数精锐之一。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_58B")


    ChrTalk(    #2
        0xFE,
        (
            "对签字仪式进行警戒的\x01",
            "好像是雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "而且又是希德中校指挥，\x01",
            "可以说是万无一失了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5EE")

    Jump("loc_8CC")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_70A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_67F")

    ChrTalk(    #4
        0xFE,
        (
            "塔顶开始闪光是在\x01",
            "诞辰庆典之后的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "不知何时起开始向天\x01",
            "升起柱子一样的光线来了\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "后来就一直能看到\x01",
            "塔顶上又光亮。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_67F")


    ChrTalk(    #7
        0xFE,
        (
            "从这里能看到托兰特\x01",
            "平原的『红莲之塔』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "最近一直能看到\x01",
            "塔顶有光亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "我向队长也报告过了，\x01",
            "不过还是很在意那是什么光。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_707")

    Jump("loc_8CC")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_76E")

    ChrTalk(    #10
        0xFE,
        (
            "呼，真没办法……\x01",
            "好不容易搞定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "虽然地震很罕见，\x01",
            "不过还是希望不要有第二次了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CC")

    label("loc_76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_7C6")

    ChrTalk(    #12
        0xFE,
        (
            "叫黛米的女孩子\x01",
            "听说见过那个怪家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "她在食堂工作，\x01",
            "要不你们去问问？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CC")

    label("loc_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_809")

    ChrTalk(    #14
        0xFE,
        "你们看看这副样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "希望能在晚饭之前\x01",
            "整理好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CC")

    label("loc_809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_8CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_859")

    ChrTalk(    #16
        0x8,
        "爬城墙可是很危险的啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "得好好提醒一下\x01",
            "那个年轻人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CC")

    label("loc_859")


    ChrTalk(    #18
        0x8,
        (
            "爬城墙可不正常。\x01",
            "真是的，要是掉下来怎么办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "咦！？　难、难道说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "你、你没在想什么\x01",
            "搞怪的事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8CC")

    TalkEnd(0x8)
    Return()

    # Function_8_4F1 end

    def Function_9_8D0(): pass

    label("Function_9_8D0")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_908")

    ChrTalk(    #21
        0xFE,
        (
            "欢迎来到圣海姆门。\x01",
            "有事的话请进来说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF5")

    label("loc_908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_99D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_954")

    ChrTalk(    #22
        0xFE,
        (
            "埃克托尔去帮忙以后\x01",
            "就没回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "是不是先吃饭了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_99A")

    label("loc_954")


    ChrTalk(    #24
        0xFE,
        (
            "地震的善后\x01",
            "总算是结束了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "不过埃克托尔那家伙还没回来。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_99A")

    Jump("loc_AF5")

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_A33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9F6")

    ChrTalk(    #26
        0xFE,
        (
            "门内的大伙儿\x01",
            "都在努力收拾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "我的搭档埃克托尔\x01",
            "也急忙去帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A30")

    label("loc_9F6")


    ChrTalk(    #28
        0xFE,
        "刚才摇得挺厉害。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "好久没像这样\x01",
            "感觉到危险了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A30")

    Jump("loc_AF5")

    label("loc_A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_AF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A6F")

    ChrTalk(    #30
        0xA,
        (
            "欢迎来到圣海姆门！\x01",
            "也欢迎你们来旅游。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF5")

    label("loc_A6F")


    ChrTalk(    #31
        0xA,
        (
            "欢迎来到圣海姆门！\x01",
            "也欢迎你们来旅游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "这里是名叫『亚宁堡』的\x01",
            "古代长城的一部分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "作为旅游名胜，\x01",
            "来参观的人也很多哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_AF5")

    TalkEnd(0xA)
    Return()

    # Function_9_8D0 end

    def Function_10_AF9(): pass

    label("Function_10_AF9")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B5D")

    ChrTalk(    #34
        0xFE,
        (
            "说起来很快就有\x01",
            "条约的签字仪式了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "唉，队长又要在那儿\x01",
            "嚷嚷强化警戒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E")

    label("loc_B5D")


    ChrTalk(    #36
        0xFE,
        (
            "地震好像也\x01",
            "平息下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "旅客和我们都总算\x01",
            "能放心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_B9E")

    Jump("loc_C1E")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_BE0")

    ChrTalk(    #38
        0xB,
        "没事情也没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        "你们可以随意出入。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_BE0")


    ChrTalk(    #40
        0xB,
        "哟，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xB,
        (
            "如果有什么事情\x01",
            "就和里面的队长说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_C1E")

    TalkEnd(0xB)
    Return()

    # Function_10_AF9 end

    def Function_11_C22(): pass

    label("Function_11_C22")

    Call(0, 12)
    Return()

    # Function_11_C22 end

    def Function_12_C27(): pass

    label("Function_12_C27")

    SetChrName("安敦")
    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_CB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C72")

    ChrTalk(    #42
        0xFE,
        (
            "差、差点就\x01",
            "差点没命了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "啊～真吓人……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB3")

    label("loc_C72")


    ChrTalk(    #44
        0xFE,
        (
            "呼～呼……\x01",
            "啊～真吓人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "差、差点就\x01",
            "差点没命了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_CB3")

    Jump("loc_D2E")

    label("loc_CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_D2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CED")

    ChrTalk(    #46
        0xC,
        "再见──！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        "我的青春──！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D2E")

    label("loc_CED")


    ChrTalk(    #48
        0xC,
        "诞辰庆典──！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xC,
        "我最讨厌了───！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xC,
        "哇──！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_D2E")

    TalkEnd(0xC)
    Return()

    # Function_12_C27 end

    def Function_13_D32(): pass

    label("Function_13_D32")

    SetChrName("利库斯")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D51")
    ClearChrFlags(0xD, 0x10)
    Jump("loc_D56")

    label("loc_D51")

    SetChrFlags(0xD, 0x10)

    label("loc_D56")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_E71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_DB4")

    ChrTalk(    #51
        0xFE,
        (
            "这家伙地震的时候\x01",
            "正好在爬城墙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "被震感吓着了，\x01",
            "差点就掉下去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6E")

    label("loc_DB4")


    ChrTalk(    #53
        0xFE,
        (
            "这家伙地震的时候\x01",
            "正好在爬城墙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "被震感吓着了，\x01",
            "差点就掉下去了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xC, 400)

    ChrTalk(    #55
        0xFE,
        (
            "如果地震再稍微大一点，\x01",
            "说不定真的就掉下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "从这一点上来说，安敦，\x01",
            "可以说你算是走运的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_E6E")

    Jump("loc_F70")

    label("loc_E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_F70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F1D")

    ChrTalk(    #57
        0xD,
        (
            "我的搭档安敦在诞辰庆典的时候\x01",
            "向仰慕的女性告白了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        (
            "不过残酷的现实是他被\x01",
            "彻底地拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        (
            "再次来到这里也算\x01",
            "他好像为了断却这个念想就去爬城墙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F70")

    label("loc_F1D")


    ChrTalk(    #60
        0xD,
        (
            "安敦…\x01",
            "那边是蔡斯的方向啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        (
            "如果你恨诞辰庆典的话\x01",
            "至少要面向王都吼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_F70")

    TalkEnd(0xD)
    Return()

    # Function_13_D32 end

    def Function_14_F74(): pass

    label("Function_14_F74")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F87")
    Call(0, 16)

    label("loc_F87")

    OP_6D(29440, 0, 4420, 0)
    OP_67(0, 9960, -10000, 0)
    OP_6B(10000, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    StopSound(0x88B8, 0x61A80, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC09._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_6C(45000, 6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3411   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_F74 end

    def Function_15_1010(): pass

    label("Function_15_1010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102A")
    Call(0, 16)
    FadeToBright(0, 0)

    label("loc_102A")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Fade(1000)
    SetChrPos(0x101, 18120, 11750, -11850, 270)
    SetChrPos(0xF7, 18420, 11750, -13130, 270)
    SetChrPos(0x105, 19340, 11750, -11430, 270)
    SetChrPos(0x104, 19610, 11750, -12770, 270)
    SetChrPos(0x8, 16800, 11750, -12550, 90)
    OP_6D(17660, 11750, -12360, 0)
    OP_67(0, 7800, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(310000, 0)
    OP_6E(423, 0)
    OP_0D()

    ChrTalk(    #62
        0x8,
        "#5P咦……你们是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1006F你就是切斯利先生吧？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_114E")

    ChrTalk(    #64
        0x106,
        (
            "#051F#6P我们是游击士协会的人。\x02\x03",

            "关于刚才的地震\x01",
            "我们有事想问你。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1193")

    label("loc_114E")


    ChrTalk(    #65
        0x103,
        (
            "#020F#6P我们是游击士协会的人。\x02\x03",

            "关于刚才的地震\x01",
            "我们有事想问你。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1193")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05艾丝蒂尔一行询问了关于他\x01",
            "所看到的可疑人物的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #67
        0x8,
        "#5P哦，昨天的事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#5P不，我怎么也不觉得\x01",
            "那和地震有什么关系……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#5P我在这里看到了一个\x01",
            "个子非常高、戴着墨镜的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1002F果然如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x105,
        (
            "#047F在沃尔费堡垒也有人\x01",
            "看到了戴墨镜的男性……\x02\x03",

            "#043F那个人到底做了什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#5P不，他上到这里\x01",
            "眺望了一会儿景色之后\x01",
            "就下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#5P我因为没见过戴墨镜的人，\x01",
            "所以就注意了他一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#5P他也没跟我打招呼，\x01",
            "我也没主动跟他打招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1007F是吗……\x02\x03",

            "#1015F还有没有人\x01",
            "见过那个戴墨镜的男人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "#5P这一点倒是很奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#5P因为我觉得那个人太古怪了，\x01",
            "就把他当作晚饭时的话题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#5P不过其他人都说\x01",
            "没见过他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#5P只有在食堂工作的\x01",
            "叫黛米的女孩子好像见过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x104,
        (
            "#032F#7P唔，这个关卡和沃尔费堡垒\x01",
            "不同，通行的人也很多。\x02\x03",

            "可是目击者却\x01",
            "只有两个人……\x02\x03",

            "#035F让人感觉有点不自然呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_152E")

    ChrTalk(    #81
        0x106,
        (
            "#053F#6P慎重起见，也去跟\x01",
            "那个女孩子打听一下吧？\x02\x03",

            "#050F是食堂的黛米吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_152E")


    ChrTalk(    #82
        0x103,
        (
            "#026F#6P慎重起见，也去跟\x01",
            "那个女孩子打听一下吧？\x02\x03",

            "#020F在食堂工作的黛米是吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1580")


    ChrTalk(    #83
        0x101,
        "#1006F谢谢，你提供的内容很重要。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "#5P能帮上你们就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        "#5P要努力调查哦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(18730, 11750, -12190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 18730, 11750, -12190, 90)
    SetChrPos(0x1, 18730, 11750, -12190, 90)
    SetChrPos(0x2, 18730, 11750, -12190, 90)
    SetChrPos(0x3, 18730, 11750, -12190, 90)
    OP_4B(0x8, 255)
    OP_A2(0x1415)
    OP_28(0x86, 0x1, 0x8)
    OP_28(0x86, 0x1, 0x10)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_1010 end

    def Function_16_168B(): pass

    label("Function_16_168B")

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
        (0, "loc_1705"),
        (1, "loc_170B"),
        (SWITCH_DEFAULT, "loc_1711"),
    )


    label("loc_1705")

    OP_A2(0x1200)
    Jump("loc_1711")

    label("loc_170B")

    OP_A2(0x1201)
    Jump("loc_1711")

    label("loc_1711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_171F")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1723")

    label("loc_171F")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1723")

    Return()

    # Function_16_168B end

    def Function_17_1724(): pass

    label("Function_17_1724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177B")

    ChrTalk(    #86
        0x101,
        (
            "#1002F……这里的调查\x01",
            "还没结束。\x02\x03",

            "赶快\x01",
            "去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_182F")

    label("loc_177B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17DA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1798")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_179F")

    label("loc_1798")

    TurnDirection(0x106, 0x0, 400)

    label("loc_179F")


    ChrTalk(    #87
        0x106,
        (
            "#050F这里的调查\x01",
            "还没结束。\x02\x03",

            "我们赶快去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_182F")

    label("loc_17DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F0")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_17F7")

    label("loc_17F0")

    TurnDirection(0x103, 0x0, 400)

    label("loc_17F7")


    ChrTalk(    #88
        0x103,
        (
            "#020F这里的调查\x01",
            "还没结束。\x02\x03",

            "我们赶快去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182F")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_184F")

    Return()

    # Function_17_1724 end

    def Function_18_1850(): pass

    label("Function_18_1850")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_18_1850 end

    SaveToFile()

Try(main)
