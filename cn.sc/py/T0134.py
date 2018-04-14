from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0134   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0134.x',
        MapIndex            = 3,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0134_1 ._SN',
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
        '迪拜恩教区长',                         # 9
        '克劳斯市长',                           # 10
        '修女梅',                               # 11
        '矿工皮尔姆',                           # 12
        '矿工海涅',                             # 13
        '阿鲁姆',                               # 14
        '艾娅莉',                               # 15
        '目标用照相机',                         # 16
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH02350 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01500 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH02350P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01500P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
    )

    DeclNpc(
        X                   = -14740,
        Z                   = 0,
        Y                   = 43530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16830,
        Z                   = 0,
        Y                   = 42890,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 55350,
        Z                   = 0,
        Y                   = 46550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 56050,
        Z                   = 0,
        Y                   = 40700,
        Direction           = 358,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 64000,
        Z                   = 0,
        Y                   = 47270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 64000,
        Z                   = 0,
        Y                   = 48170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_234",          # 01, 1
        "Function_2_235",          # 02, 2
        "Function_3_3B2",          # 03, 3
        "Function_4_53A",          # 04, 4
        "Function_5_587",          # 05, 5
        "Function_6_623",          # 06, 6
        "Function_7_720",          # 07, 7
        "Function_8_96E",          # 08, 8
        "Function_9_A1F",          # 09, 9
        "Function_10_124F",        # 0A, 10
        "Function_11_12EB",        # 0B, 11
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20D")
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_21C")

    label("loc_20D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_21C")
    ClearChrFlags(0xE, 0x10)

    label("loc_21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_233")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 9)

    label("loc_233")

    Return()

    # Function_0_1DA end

    def Function_1_234(): pass

    label("Function_1_234")

    Return()

    # Function_1_234 end

    def Function_2_235(): pass

    label("Function_2_235")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_39C")

    label("loc_25A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_39C")

    label("loc_273")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_39C")

    label("loc_28C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_39C")

    label("loc_2A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_39C")

    label("loc_2BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_39C")

    label("loc_2D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_39C")

    label("loc_2F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_39C")

    label("loc_309")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_39C")

    label("loc_322")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_39C")

    label("loc_33B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_39C")

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_39C")

    label("loc_36D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_39C")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_39C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_39C")

    label("loc_3B1")

    Return()

    # Function_2_235 end

    def Function_3_3B2(): pass

    label("Function_3_3B2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_43F")

    ChrTalk(    #0
        0x8,
        (
            "我也想尽快联络\x01",
            "王都的大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "那边文献也很丰富，\x01",
            "也有了解各地地方病的神父。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "说不定能找到\x01",
            "什么治疗的线索。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536")

    label("loc_43F")


    ChrTalk(    #3
        0x8,
        (
            "教会秘传的苏醒法\x01",
            "都没用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "说明此次的昏睡事件不是\x01",
            "由药物和疾病引起的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "总之我准备先再查阅一遍\x01",
            "手头的医学书，\x01",
            "老实说我也不是很期待有什么结果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "呼，看来还是尽快\x01",
            "联络王都的大圣堂比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "等归纳好病例的报告\x01",
            "就赶紧准备吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_536")

    TalkEnd(0x8)
    Return()

    # Function_3_3B2 end

    def Function_4_53A(): pass

    label("Function_4_53A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_583")

    ChrTalk(    #8
        0xFE,
        "空之女神啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "希望被睡眠迷住了的大家\x01",
            "能够赶快醒来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_583")

    TalkEnd(0xA)
    Return()

    # Function_4_53A end

    def Function_5_587(): pass

    label("Function_5_587")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_61F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5D0")

    ChrTalk(    #10
        0xFE,
        (
            "深深感谢女神保佑我\x01",
            "今天的工作也安全地完成了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61F")

    label("loc_5D0")


    ChrTalk(    #11
        0xFE,
        (
            "多亏了女神，\x01",
            "今天的工作也安全地完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "请您明天也能\x01",
            "保佑我们……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_61F")

    TalkEnd(0xB)
    Return()

    # Function_5_587 end

    def Function_6_623(): pass

    label("Function_6_623")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_71C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_685")

    ChrTalk(    #13
        0xFE,
        (
            "皮尔姆那家伙……\x01",
            "要祈祷到什么时候？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "他怎么不想想\x01",
            "我还在旁边等着呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71C")

    label("loc_685")


    ChrTalk(    #15
        0xFE,
        (
            "皮尔姆那家伙……\x01",
            "要祈祷到什么时候？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "他怎么不想想\x01",
            "我还在旁边等着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "啊～太晚的话\x01",
            "酒馆要关门了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "……真是的，我一个人\x01",
            "去吃算了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_71C")

    TalkEnd(0xC)
    Return()

    # Function_6_623 end

    def Function_7_720(): pass

    label("Function_7_720")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_76D")

    ChrTalk(    #19
        0xFE,
        "啊啊～艾娅莉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_93F")

    label("loc_76D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7D5")

    ChrTalk(    #20
        0xFE,
        (
            "那么，游击士。\x01",
            "戒指的事拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "要是有什么情况\x01",
            "请再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C5")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_823")

    ChrTalk(    #22
        0xFE,
        (
            "那么，游击士。\x01",
            "戒指的事拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "要是有什么情况\x01",
            "请再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C5")

    label("loc_823")

    OP_A2(0x4)

    ChrTalk(    #24
        0xFE,
        "啊，游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "怎、怎么样了？\x01",
            "调查进行得如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1015F嗯，还在继续啊。\x02\x03",

            "也许再等一会\x01",
            "就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "那、那样啊…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "嗯，明白了。\x01",
            "我会一直等的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C5")

    Jump("loc_93F")

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_93F")

    ChrTalk(    #29
        0xFE,
        "今天也看不见星星……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "不过只要有你在，\x01",
            "我就一点儿也不寂寞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "因为我所寻找的星星\x01",
            "就是你啊，艾娅莉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93F")

    Jump("loc_96A")

    label("loc_942")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_966")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_95F")
    Call(1, 1)
    Jump("loc_963")

    label("loc_95F")

    Call(1, 0)

    label("loc_963")

    Jump("loc_96A")

    label("loc_966")

    Call(1, 3)

    label("loc_96A")

    TalkEnd(0xD)
    Return()

    # Function_7_720 end

    def Function_8_96E(): pass

    label("Function_8_96E")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_98B")

    ChrTalk(    #32
        0xFE,
        "阿鲁姆……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1B")

    label("loc_98B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9ED")

    ChrTalk(    #33
        0xFE,
        "我们在这里等着。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "虽然是很艰难的委托，\x01",
            "但请努力坚持一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_A1B")

    ChrTalk(    #35
        0xFE,
        (
            "呵呵，阿鲁姆\x01",
            "你真是个浪漫主义者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1B")

    TalkEnd(0xE)
    Return()

    # Function_8_96E end

    def Function_9_A1F(): pass

    label("Function_9_A1F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3F")
    Call(0, 10)
    FadeToBright(0, 0)
    Call(0, 11)

    label("loc_A3F")

    OP_44(0x8, 0x0)
    SetChrPos(0x8, -17390, 0, 42890, 90)
    SetChrPos(0x101, -15830, 0, 42280, 270)
    SetChrPos(0x103, -15950, 0, 43470, 270)
    SetChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABE")
    SetChrPos(0x9, -15850, 0, 45570, 180)
    SetChrPos(0xF8, -14610, 0, 43470, 270)
    SetChrPos(0xF9, -14600, 0, 42200, 270)
    Jump("loc_AF1")

    label("loc_ABE")

    SetChrPos(0x9, -16020, 0, 45150, 180)
    SetChrPos(0xF8, -14600, 0, 42200, 270)
    SetChrPos(0xF9, -14610, 0, 43470, 270)

    label("loc_AF1")

    TurnDirection(0xF8, 0x8, 0)
    TurnDirection(0xF9, 0x8, 0)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-16630, 3000, 43560, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(-16630, 0, 43560, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #36
        0x8,
        (
            "#5P各位病人的家里都去看了一遍，\x01",
            "果然所有人的症状都一致……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#5P呼吸也很稳定，\x01",
            "瞳孔也没有异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#5P几乎就像是睡着了一样，\x01",
            "所以应该不会立即恶化吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "#603F是、是吗……\x01",
            "可以说是不幸中的万幸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#5P可是这么一直沉睡下去的话\x01",
            "体力肯定会不支的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "#5P得赶紧想出\x01",
            "对策来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "#602F嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1003F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_CC3():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_CC3)
    Sleep(100)

    def lambda_CD6():
        TurnDirection(0xF9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_CD6)
    Sleep(100)
    TurnDirection(0x103, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D32")

    ChrTalk(    #44
        0x107,
        (
            "#065F#4P姐、姐姐，你没事吧？\x02\x03",

            "你的脸色好像很差……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E33")

    label("loc_D32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6E")

    ChrTalk(    #45
        0x106,
        (
            "#552F#4P喂……你没事吧？\x02\x03",

            "脸色这么差？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E33")

    label("loc_D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB3")

    ChrTalk(    #46
        0x104,
        (
            "#032F#4P咦？你没事吧？\x02\x03",

            "脸色好像相当\x01",
            "不好呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E33")

    label("loc_DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFC")

    ChrTalk(    #47
        0x105,
        (
            "#043F#4P艾丝蒂尔……\x01",
            "那个，你没事吧？\x02\x03",

            "你脸色很差。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E33")

    label("loc_DFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E33")

    ChrTalk(    #48
        0x108,
        (
            "#572F#4P喂，你没事吧？\x02\x03",

            "脸色很差啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E33")

    TurnDirection(0x101, 0xF8, 400)

    ChrTalk(    #49
        0x101,
        (
            "#1026F#5P啊，嗯……\x02\x03",

            "#1007F想不到连伊莉莎的妈妈和\x01",
            "鲁克也会倒下来……\x02\x03",

            "……所以感到有点吃惊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#524F#2P艾丝蒂尔……\x02\x03",

            "如果觉得不舒服\x01",
            "你也可以返回协会？\x02\x03",

            "还是说回家歇着？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #51
        0x101,
        (
            "#1025F#6P不……\x01",
            "不能泄气。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    def lambda_F26():
        TurnDirection(0x103, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F26)

    def lambda_F34():
        TurnDirection(0xF9, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F34)
    TurnDirection(0xF8, 0x8, 400)
    Sleep(500)

    ChrTalk(    #52
        0x101,
        (
            "#1002F#6P那么，教区长先生，\x01",
            "昏睡的原因知道了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        "#5P很遗憾，现在还不能确定……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#5P不过，连教会秘传的苏醒法\x01",
            "也没起作用，\x01",
            "应该不是毒和疾病造成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#5P如果一定要说的话，\x01",
            "好像是灵魂被某种东西囚禁了……\x01",
            "给人的印象就是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1002F#6P灵魂被某种东西囚禁……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x103,
        "#522F#4P……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #58
        0x103,
        (
            "#022F#2P总之还是先走访一下\x01",
            "昏睡者的家比较好。\x02\x03",

            "他们究竟是在\x01",
            "何种情况下进入昏睡状态的……\x02\x03",

            "通过询问家属这方面的情况，\x01",
            "说不定能发现些什么。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #59
        0x101,
        (
            "#1004F#6P啊……\x02\x03",

            "#1002F嗯，明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "#603F艾丝蒂尔，雪拉扎德。\x02",
    )

    CloseMessageWindow()

    def lambda_1170():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1170)
    Sleep(100)

    def lambda_1183():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1183)
    Sleep(100)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #61
        0x9,
        (
            "#602F洛连特市政府正式委托\x01",
            "协会调查此次的事件。\x02\x03",

            "希望你们能查出原因，\x01",
            "消除大家的不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1006F#6P嗯……请放心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        "#020F#6P我们会尽一份薄力的。\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0101   ._SN", 117, 0, 0)
    IdleLoop()
    Return()

    # Function_9_A1F end

    def Function_10_124F(): pass

    label("Function_10_124F")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_12CC"),
        (1, "loc_12D2"),
        (SWITCH_DEFAULT, "loc_12D8"),
    )


    label("loc_12CC")

    OP_A2(0x1200)
    Jump("loc_12D8")

    label("loc_12D2")

    OP_A2(0x1201)
    Jump("loc_12D8")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_12E6")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_12EA")

    label("loc_12E6")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_12EA")

    Return()

    # Function_10_124F end

    def Function_11_12EB(): pass

    label("Function_11_12EB")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_11_12EB end

    SaveToFile()

Try(main)
