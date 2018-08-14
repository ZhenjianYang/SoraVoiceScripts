from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3110   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3110.x',
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
        '露依赛',                               # 9
        '乌缇',                                 # 10
        '鲁特尔',                               # 11
        '索黛丽娅',                             # 12
        '斯坦因',                               # 13
        '',                                     # 14
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
    )

    DeclNpc(
        X                   = 60,
        Z                   = 0,
        Y                   = 26440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -1760,
        Z                   = 4000,
        Y                   = 23400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 24940,
        Z                   = 0,
        Y                   = 520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4040,
        Z                   = 0,
        Y                   = 3790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 48200,
        Z                   = 0,
        Y                   = 23060,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    ScpFunction(
        "Function_0_17A",          # 00, 0
        "Function_1_1A0",          # 01, 1
        "Function_2_1A1",          # 02, 2
        "Function_3_31E",          # 03, 3
        "Function_4_342",          # 04, 4
        "Function_5_366",          # 05, 5
        "Function_6_409",          # 06, 6
        "Function_7_4D2",          # 07, 7
        "Function_8_618",          # 08, 8
        "Function_9_709",          # 09, 9
    )


    def Function_0_17A(): pass

    label("Function_0_17A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_19F")

    Return()

    # Function_0_17A end

    def Function_1_1A0(): pass

    label("Function_1_1A0")

    Return()

    # Function_1_1A0 end

    def Function_2_1A1(): pass

    label("Function_2_1A1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_308")

    label("loc_1C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_308")

    label("loc_1DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_308")

    label("loc_1F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_308")

    label("loc_211")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_308")

    label("loc_22A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_308")

    label("loc_243")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_308")

    label("loc_25C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_308")

    label("loc_275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_308")

    label("loc_28E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_308")

    label("loc_2A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C0")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_308")

    label("loc_2C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_308")

    label("loc_2D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_308")

    label("loc_2F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_308")

    label("loc_31D")

    Return()

    # Function_2_1A1 end

    def Function_3_31E(): pass

    label("Function_3_31E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_341")
    OP_8D(0xFE, 25620, 1830, 23470, -690, 1000)
    Jump("Function_3_31E")

    label("loc_341")

    Return()

    # Function_3_31E end

    def Function_4_342(): pass

    label("Function_4_342")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_365")
    OP_8D(0xFE, 48200, 23060, 51000, 22330, 1000)
    Jump("Function_4_342")

    label("loc_365")

    Return()

    # Function_4_342 end

    def Function_5_366(): pass

    label("Function_5_366")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3CA")

    ChrTalk(    #0
        0xFE,
        (
            "为什么谁都\x01",
            "不来叫醒我啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "啊～伤脑筋……\x01",
            "这次找什么借口才好啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405")

    label("loc_3CA")


    ChrTalk(    #2
        0xFE,
        "……咦，都中午了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "糟糕，又睡过头了！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_405")

    TalkEnd(0xFE)
    Return()

    # Function_5_366 end

    def Function_6_409(): pass

    label("Function_6_409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_4CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_47B")

    ChrTalk(    #4
        0xFE,
        (
            "这一星期里只有被乌尔斯先生\x01",
            "叫醒的两天没有迟到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "虽然确实很懒，\x01",
            "但也要自觉点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE")

    label("loc_47B")


    ChrTalk(    #6
        0xFE,
        (
            "唉，姐姐真的\x01",
            "没办法自己起床啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "姐姐……\x01",
            "真是没用啊。\x02",
        )
    )

    Jump("loc_4CA")

    label("loc_4CA")

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_4CE")

    TalkEnd(0xFE)
    Return()

    # Function_6_409 end

    def Function_7_4D2(): pass

    label("Function_7_4D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_56D")

    ChrTalk(    #8
        0xFE,
        (
            "其实我对飞翔引擎的原理\x01",
            "了解得不是很清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "也不能随便\x01",
            "就做个应付差事的说明……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "还是重新学习一下\x01",
            "比较好吗…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_614")

    label("loc_56D")


    ChrTalk(    #11
        0xFE,
        (
            "我的工作是\x01",
            "飞艇交易……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "不过最近客户向我提出了\x01",
            "如果导力停止飞艇会不会坠落的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "嗯……嗯嗯……\x01",
            "我记得就算引擎停止，\x01",
            "应该也不会马上坠落的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_614")

    TalkEnd(0xFE)
    Return()

    # Function_7_4D2 end

    def Function_8_618(): pass

    label("Function_8_618")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_680")

    ChrTalk(    #14
        0xFE,
        "最近老公都留在家里呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "呵呵，\x01",
            "我这么辛苦做饭终于有回报了呢。\x02",
        )
    )

    Jump("loc_67C")

    label("loc_67C")

    CloseMessageWindow()
    Jump("loc_705")

    label("loc_680")


    ChrTalk(    #16
        0xFE,
        (
            "老公因为商谈工作\x01",
            "经常到外地出差……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "不过最近却\x01",
            "常常回家来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "呵呵，\x01",
            "我这么辛苦做饭终于有回报了呢。\x02",
        )
    )

    Jump("loc_701")

    label("loc_701")

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_705")

    TalkEnd(0xFE)
    Return()

    # Function_8_618 end

    def Function_9_709(): pass

    label("Function_9_709")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_7EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_77F")

    ChrTalk(    #19
        0xFE,
        (
            "那种东西\x01",
            "最终调整工作是最难的。\x02",
        )
    )

    Jump("loc_74C")

    label("loc_74C")

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "我以前也是技师，\x01",
            "制作者的辛苦我很明白。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EC")

    label("loc_77F")


    ChrTalk(    #21
        0xFE,
        (
            "加鲁诺的新型枪\x01",
            "好像终于要产品化了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "听说现在正在\x01",
            "进行最终调整呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "嗯，真令人期待啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_7EC")

    TalkEnd(0xFE)
    Return()

    # Function_9_709 end

    SaveToFile()

Try(main)
