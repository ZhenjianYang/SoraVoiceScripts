from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2200.x',
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
        '盖尔多那',                             # 9
        '王国军宪兵',                           # 10
        '卢安市·南街区',                       # 11
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
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
    )

    DeclNpc(
        X                   = 98500,
        Z                   = 0,
        Y                   = 17600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 110290,
        Z                   = 1990,
        Y                   = 24010,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 68010,
        Z                   = 0,
        Y                   = 21970,
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


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_127",          # 01, 1
        "Function_2_13F",          # 02, 2
        "Function_3_1E1",          # 03, 3
        "Function_4_35E",          # 04, 4
        "Function_5_663",          # 05, 5
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_126")
    SetChrFlags(0x9, 0x80)

    label("loc_126")

    Return()

    # Function_0_11A end

    def Function_1_127(): pass

    label("Function_1_127")

    OP_16(0x2, 0xFA0, 0xFFFFC180, 0xFFFE5A20, 0x23004A)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_127 end

    def Function_2_13F(): pass

    label("Function_2_13F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E0")
    OP_8E(0xFE, 0x181E6, 0x0, 0x4A60, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x180C4, 0x0, 0x44C0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x17B10, 0x0, 0x42CC, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x17A98, 0x0, 0x48C6, 0xBB8, 0x0)
    OP_8C(0xFE, 120, 400)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xFE)
    Jump("Function_2_13F")

    label("loc_1E0")

    Return()

    # Function_2_13F end

    def Function_3_1E1(): pass

    label("Function_3_1E1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_348")

    label("loc_206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_348")

    label("loc_21F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_348")

    label("loc_238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_348")

    label("loc_251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_348")

    label("loc_26A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_348")

    label("loc_283")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_348")

    label("loc_29C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_348")

    label("loc_2B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_348")

    label("loc_2CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_348")

    label("loc_2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_348")

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_348")

    label("loc_319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_348")

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_348")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_348")

    label("loc_35D")

    Return()

    # Function_3_1E1 end

    def Function_4_35E(): pass

    label("Function_4_35E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D2")

    ChrTalk(    #0
        0xFE,
        (
            "如果下任市长确定了，房屋\x01",
            "就完全属于卢安市民了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "我们士兵也希望\x01",
            "能住进出色的大人物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464")

    label("loc_3D2")

    OP_A2(0x1)

    ChrTalk(    #2
        0xFE,
        (
            "如果下任市长确定了，房屋\x01",
            "就完全属于卢安市民了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "无论哪位候选人胜出\x01",
            "都将是首位平民出身的市长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "这样贵族制的影子\x01",
            "也将被抹去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_464")

    Jump("loc_65F")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_51E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C4")

    ChrTalk(    #5
        0xFE,
        (
            "强化跟协会的合作\x01",
            "是军队全体的改善目标。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "最近军队高层\x01",
            "都这样说了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51B")

    label("loc_4C4")

    OP_A2(0x1)

    ChrTalk(    #7
        0xFE,
        (
            "好像发生了骚动，\x01",
            "不过这边没有异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "如果有什么事\x01",
            "会马上联系游击士协会的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B")

    Jump("loc_65F")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_58D")

    ChrTalk(    #9
        0xFE,
        (
            "这里的女佣们，相当亲切地\x01",
            "拿出茶点款待我们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "伙食也很不错，\x01",
            "真是不想回要塞了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_607")

    label("loc_58D")

    OP_A2(0x1)

    ChrTalk(    #11
        0xFE,
        (
            "这个宅邸现在被\x01",
            "王国军管理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "进出是无所谓，\x01",
            "但府邸内也有贵重物品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "以防万一请不要损坏，\x01",
            "在府邸内请当心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_607")

    Jump("loc_65F")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_65F")

    ChrTalk(    #14
        0xFE,
        (
            "这个宅邸现在\x01",
            "在王国军的管理下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "下任市长选出之后\x01",
            "将作为市政厅使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65F")

    TalkEnd(0xFE)
    Return()

    # Function_4_35E end

    def Function_5_663(): pass

    label("Function_5_663")

    TalkBegin(0xFE)
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6BA")

    ChrTalk(    #16
        0xFE,
        (
            "刚才游击士的大哥\x01",
            "气势汹汹地跑了过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "是发生什么事件了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_90B")

    label("loc_6BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_714")

    ChrTalk(    #18
        0xFE,
        (
            "选定了新市长\x01",
            "我的干劲也倍增了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "幸亏处理庭院树木\x01",
            "和导力器没什么关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90B")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_75F")

    ChrTalk(    #20
        0xFE,
        (
            "呼，我的肚子时钟\x01",
            "说到吃饭时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "待会儿去厨房看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_90B")

    label("loc_75F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_7B7")

    ChrTalk(    #22
        0xFE,
        (
            "唔，难得\x01",
            "士兵大哥们来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "把庭园的树木整理成\x01",
            "士兵的样子也挺好玩的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90B")

    label("loc_7B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7F9")

    ChrTalk(    #24
        0xFE,
        (
            "既然是女王陛下的庭园，\x01",
            "自然就有干劲了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87E")

    label("loc_7F9")

    OP_A2(0x0)

    ChrTalk(    #25
        0xFE,
        (
            "怎么说呢，这房子\x01",
            "好像属于王国军了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "也就是说，我的雇主\x01",
            "变成艾莉茜雅王陛下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "嘿嘿，身为专业人士真是无上光荣啊。\x02",
    )

    CloseMessageWindow()

    label("loc_87E")

    Jump("loc_90B")

    label("loc_881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_90B")

    ChrTalk(    #28
        0xFE,
        (
            "前市长被逮捕\x01",
            "已经过去相当长的一段时间了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "我一直在这里工作，\x01",
            "没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "虽说没有任何命令，\x01",
            "可以毫不介意的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90B")

    TalkEnd(0xFE)
    Return()

    # Function_5_663 end

    SaveToFile()

Try(main)
