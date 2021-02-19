from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4138   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4138.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '达维尔大使',                           # 9
        '穆拉',                                 # 10
        '巴克雷书记官',                         # 11
        '杰拉尔德',                             # 12
        '阿尔夫参事官',                         # 13
        '卡米拉',                               # 14
        '尼赞',                                 # 15
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
        'ED6_DT27/CH03713 ._CH',             # 00
        'ED6_DT27/CH03570 ._CH',             # 01
        'ED6_DT07/CH01560 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01350 ._CH',             # 05
        'ED6_DT07/CH01570 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT27/CH03713P._CP',             # 00
        'ED6_DT27/CH03570P._CP',             # 01
        'ED6_DT07/CH01560P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01350P._CP',             # 05
        'ED6_DT07/CH01570P._CP',             # 06
    )

    DeclNpc(
        X                   = 1190,
        Z                   = 300,
        Y                   = 75010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -4180,
        Z                   = 0,
        Y                   = 66110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 55300,
        Z                   = 0,
        Y                   = 59890,
        Direction           = 93,
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
        X                   = 53760,
        Z                   = 0,
        Y                   = 65280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -49800,
        Z                   = 0,
        Y                   = 13300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -48940,
        Z                   = 1000,
        Y                   = 64599,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 1040,
        TriggerZ            = 4000,
        TriggerY            = 32049,
        TriggerRange        = 800,
        ActorX              = 1040,
        ActorZ              = 4500,
        ActorY              = 32049,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42830,
        TriggerZ            = 1000,
        TriggerY            = 61060,
        TriggerRange        = 600,
        ActorX              = -42830,
        ActorZ              = 2000,
        ActorY              = 61060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42800,
        TriggerZ            = 1000,
        TriggerY            = 59460,
        TriggerRange        = 600,
        ActorX              = -42800,
        ActorZ              = 2000,
        ActorY              = 59460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_2CE",          # 01, 1
        "Function_2_315",          # 02, 2
        "Function_3_492",          # 03, 3
        "Function_4_CED",          # 04, 4
        "Function_5_D1A",          # 05, 5
        "Function_6_EBF",          # 06, 6
        "Function_7_1264",         # 07, 7
        "Function_8_15C7",         # 08, 8
        "Function_9_1925",         # 09, 9
        "Function_10_1D83",        # 0A, 10
        "Function_11_2702",        # 0B, 11
        "Function_12_37E2",        # 0C, 12
        "Function_13_382A",        # 0D, 13
        "Function_14_3872",        # 0E, 14
        "Function_15_38BA",        # 0F, 15
        "Function_16_3902",        # 10, 16
        "Function_17_398A",        # 11, 17
        "Function_18_39AF",        # 12, 18
        "Function_19_39E8",        # 13, 19
        "Function_20_3A25",        # 14, 20
        "Function_21_3B64",        # 15, 21
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_255")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_252")
    SetChrPos(0xA, 5740, 0, 75240, 87)

    label("loc_252")

    Jump("loc_2AD")

    label("loc_255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_27C")
    SetChrPos(0xA, 2430, 0, 76110, 180)
    Jump("loc_2AD")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 2)), scpexpr(EXPR_END)), "loc_29C")
    SetChrPos(0x9, 54220, 0, 7400, 90)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2AD")

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_2A6")
    Jump("loc_2AD")

    label("loc_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2AD")

    label("loc_2AD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2B9"),
        (SWITCH_DEFAULT, "loc_2CD"),
    )


    label("loc_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_2CA")

    Jump("loc_2CD")

    label("loc_2CD")

    Return()

    # Function_0_22E end

    def Function_1_2CE(): pass

    label("Function_1_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EE")
    OP_B1("t4138_y")
    Jump("loc_2F7")

    label("loc_2EE")

    OP_B1("t4138_n")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30F")
    OP_64(0x0, 0x1)
    OP_71(0x2, 0x10)
    Jump("loc_314")

    label("loc_30F")

    OP_72(0x2, 0x10)

    label("loc_314")

    Return()

    # Function_1_2CE end

    def Function_2_315(): pass

    label("Function_2_315")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_47C")

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_47C")

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_47C")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_47C")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_47C")

    label("loc_39E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_47C")

    label("loc_3B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_47C")

    label("loc_3D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E9")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_47C")

    label("loc_3E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_47C")

    label("loc_402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_47C")

    label("loc_41B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_47C")

    label("loc_434")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_47C")

    label("loc_44D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_47C")

    label("loc_466")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_47C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_491")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_47C")

    label("loc_491")

    Return()

    # Function_2_315 end

    def Function_3_492(): pass

    label("Function_3_492")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x2, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B7")
    SetChrSubChip(0x8, 1)
    Jump("loc_4BC")

    label("loc_4B7")

    SetChrSubChip(0x8, 2)

    label("loc_4BC")

    OP_8C(0x8, 180, 0)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_81F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 6)), scpexpr(EXPR_END)), "loc_50C")

    ChrTalk(    #0
        0x8,
        (
            "#1100F至、至少，\x01",
            "想让通信恢复……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F")

    label("loc_50C")


    ChrTalk(    #1
        0x8,
        (
            "#1102F呜唔唔唔……\x02\x03",

            "那最后的通信到底是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1000F您好，大使先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#1101F哦哦，诸位是……\x01",
            "来得正好。\x02\x03",

            "#1100F关于现在的状况\x01",
            "了解到什么了吗？\x02\x03",

            "无论怎样细微的事都行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1011F真，真突然啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#1101F导力器竟然全部\x01",
            "停止真是前所未闻的事。\x02\x03",

            "#1100F这样下去别说\x01",
            "和本国取得联络，\x01",
            "即使平常的业务也做不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1015F嗯～话虽这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1042F恕我直言大使阁下……\x02\x03",

            "这样的话去格兰赛尔城\x01",
            "询问看看怎样呢？\x02\x03",

            "#1040F那位艾莉茜雅女王\x01",
            "说不定已经采取了\x01",
            "适当的策略了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#1101F这，这当然已经试过了。\x02\x03",

            "#1100F但是，格兰赛尔城内\x01",
            "仍然是相当混乱的情况。\x02\x03",

            "催促了几次\x01",
            "至今还未收到\x01",
            "艾莉茜雅女王的回答。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1004F哎呀呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#1100F至、至少，\x01",
            "想让通信恢复……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1011F（……『零力场发生器』\x01",
            "　不能交给他吧？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#1042F（当然了。）\x02\x03",

            "（装置的数量有限……\x01",
            "　现在只有忍耐了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20DE)

    label("loc_81F")

    Jump("loc_CE4")

    label("loc_822")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 3)), scpexpr(EXPR_END)), "loc_8D0")

    ChrTalk(    #13
        0x8,
        (
            "#1100F……你们特地\x01",
            "前来这里，\x01",
            "请让我表示谢意。\x02\x03",

            "多亏你们，对我国的\x01",
            "不当怀疑确实消释了。\x02\x03",

            "虽说是小事，\x01",
            "但因这种事有损\x01",
            "帝国的威信绝非我本意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7E")

    label("loc_8D0")


    ChrTalk(    #14
        0x8,
        (
            "#1100F唔……奥利维尔。\x02\x03",

            "还有前几天的那几位游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x104,
        "#031F贵安，大使殿下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#1100F哼……今天又在\x01",
            "游手好闲啊。\x02\x03",

            "穆拉不在\x01",
            "你就放羊了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        "#030F呼，你还是那么严厉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#1100F……今天到底有什么事？\x02\x03",

            "要是恐吓信的事\x01",
            "我已经收到报告了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1011F咦，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#1102F啊啊，犯人似乎是\x01",
            "王国军特务兵的逃兵。\x02\x03",

            "#1100F就像我说的，不是\x01",
            "帝国关系者所为吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1015F（嗯～虽说正确\x01",
            "　说来也不是特务兵……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AAC")

    ChrTalk(    #22
        0x106,
        (
            "#053F（嗯，没必要在这里\x01",
            "　说出实话引人不安吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEA")

    label("loc_AAC")


    ChrTalk(    #23
        0x103,
        (
            "#020F（嗯，在这里就算说实话\x01",
            "　也只会让事情变得更复杂。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEA")


    ChrTalk(    #24
        0x8,
        (
            "#1100F……你们特地\x01",
            "前来这里，\x01",
            "请让我表示谢意。\x02\x03",

            "多亏你们，对我国的\x01",
            "不当怀疑确实消释了。\x02\x03",

            "虽说是小事，\x01",
            "但因这种事有损\x01",
            "帝国的威信绝非我本意。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165B)

    label("loc_B7E")

    Jump("loc_CE4")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C15")

    ChrTalk(    #25
        0x8,
        (
            "#1100F帝国内的协会支部\x01",
            "似乎接连受到什么人的袭击\x01",
            "情报已经传来了。\x02\x03",

            "考虑到组织的性格，\x01",
            "必定有什么目的吧。\x02\x03",

            "要努力不输给他们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4")

    label("loc_C15")


    ChrTalk(    #26
        0x8,
        (
            "#1100F唔，游击士\x01",
            "看来也是很辛苦的工作啊。\x02\x03",

            "这么说来，几个月前……\x02\x03",

            "帝国内的协会支部\x01",
            "似乎接连受到什么人的袭击\x01",
            "情报已经传来了。\x02\x03",

            "#1102F考虑到组织的性格，\x01",
            "必定有什么目的吧。\x02\x03",

            "#1100F要努力不输给他们啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CE4")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_3_492 end

    def Function_4_CED(): pass

    label("Function_4_CED")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 2)), scpexpr(EXPR_END)), "loc_D16")

    ChrTalk(    #27
        0x9,
        "#270F怎么了，忘了东西吗？\x02",
    )

    CloseMessageWindow()

    label("loc_D16")

    TalkEnd(0x9)
    Return()

    # Function_4_CED end

    def Function_5_D1A(): pass

    label("Function_5_D1A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D8C")

    ChrTalk(    #28
        0xFE,
        (
            "导力停止发生之前\x01",
            "好像收到过本国奇怪的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "大使问起这个的时候，\x01",
            "通讯似乎就断了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8C")

    Jump("loc_EBB")

    label("loc_D8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_DDE")

    ChrTalk(    #30
        0xFE,
        "唔，奇怪啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "柏斯的穆拉\x01",
            "没有发来定时联络……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBB")

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E3A")

    ChrTalk(    #32
        0xFE,
        (
            "不过寻找恐吓信的犯人\x01",
            "是相当辛苦的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "如果能帮上忙就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_EBB")

    label("loc_E3A")


    ChrTalk(    #34
        0xFE,
        (
            "不过寻找恐吓信的犯人\x01",
            "是相当辛苦的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "无论怎么说，那个内容\x01",
            "就等于完全没有线索一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "如果能帮上忙就好了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_EBB")

    TalkEnd(0xA)
    Return()

    # Function_5_D1A end

    def Function_6_EBF(): pass

    label("Function_6_EBF")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F36")

    ChrTalk(    #37
        0xFE,
        (
            "大使殿下从本国\x01",
            "收到的最后的联络\x01",
            "是怎样的内容？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "『别动是怎么回事！』\x01",
            "像是这样的怒吼……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F36")

    Jump("loc_1260")

    label("loc_F39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_109F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FB2")

    ChrTalk(    #39
        0xFE,
        (
            "合并自治州的时候，\x01",
            "宰相阁下的指挥相当漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "哎呀，导力铁路的整备\x01",
            "就是因为这个啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109C")

    label("loc_FB2")


    ChrTalk(    #41
        0xFE,
        (
            "在跟自治州的纠纷中，\x01",
            "宰相阁下的指挥相当漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "配置在广大领土上的战力\x01",
            "由导力铁路暂时向国境集中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "闪电战取得胜利后\x01",
            "又将各部队很快返回守备地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "导力铁路的整备\x01",
            "就是因为这个啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "是是，我们祖国\x01",
            "已经毫无空隙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_109C")

    Jump("loc_1260")

    label("loc_109F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_1122")

    ChrTalk(    #46
        0xFE,
        (
            "奥斯本宰相阁下\x01",
            "原本是军部出身的政治家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "成为宰相\x01",
            "大概是１０年前吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "以惊人的速度\x01",
            "出人头地令人印象深刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1260")

    label("loc_1122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_11A7")

    ChrTalk(    #49
        0xFE,
        (
            "离利贝尔的国境最近的\x01",
            "帝国城镇被称为帕尔姆镇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "我就是那个帕鲁姆出身的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "离柏斯很近，\x01",
            "返回故乡很方便。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1260")

    label("loc_11A7")


    ChrTalk(    #52
        0xFE,
        (
            "离利贝尔的国境最近的\x01",
            "帝国城镇被称为帕尔姆镇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "我就是那个帕鲁姆出身的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "离柏斯很近，\x01",
            "返回故乡很方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "相反去帝都\x01",
            "更费时间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "帝国没有定期船，\x01",
            "只能换乘铁路。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1260")

    TalkEnd(0xB)
    Return()

    # Function_6_EBF end

    def Function_7_1264(): pass

    label("Function_7_1264")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12E3")

    ChrTalk(    #57
        0xFE,
        (
            "那个湖上浮现的\x01",
            "物体是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "这个现象帝国也\x01",
            "发生了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "什么都不清楚的\x01",
            "状态很令人不安啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E3")

    Jump("loc_15C3")

    label("loc_12E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_135B")

    ChrTalk(    #60
        0xFE,
        (
            "犯人若是共和国的人，\x01",
            "我帝国无法沉默下去了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "反之亦然。\x01",
            "条约缔结也有影响啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1415")

    label("loc_135B")


    ChrTalk(    #62
        0xFE,
        (
            "虽然这么说\x01",
            "可能不太好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "但知道骚动的犯人\x01",
            "是原王国军，松了口气的\x01",
            "该是艾莉茜雅女王吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "这若是共和国的人，\x01",
            "我帝国无法沉默下去了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "反之亦然。\x01",
            "条约缔结也有影响啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1415")

    Jump("loc_15C3")

    label("loc_1418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_154A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1487")

    ChrTalk(    #66
        0xFE,
        (
            "艾莉茜雅女王活用\x01",
            "导力技术的政策就是绝妙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "如果她有难题……\x01",
            "那还是继任者的问题吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1547")

    label("loc_1487")


    ChrTalk(    #68
        0xFE,
        (
            "利贝尔王国\x01",
            "成为所谓的缓冲国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "缓冲国就是在大国之间，\x01",
            "抵御互相矛盾的国家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "缓冲国为了保持独立，\x01",
            "要与周围的势力相称\x01",
            "必须不懈努力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "互不侵犯条约或许也有\x01",
            "均衡势力的目的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1547")

    Jump("loc_15C3")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_15C3")

    ChrTalk(    #72
        0xFE,
        "呀，这不是奥利维尔吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "竟然去了温泉\x01",
            "真令人羡慕啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "我为了准备签字仪式\x01",
            "可是连日工作到筋疲力尽啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C3")

    TalkEnd(0xC)
    Return()

    # Function_7_1264 end

    def Function_8_15C7(): pass

    label("Function_8_15C7")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1668")

    ChrTalk(    #75
        0xFE,
        (
            "在帝国的爸爸\x01",
            "和妈妈是否平安呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "前几天，回国的奥利维尔先生\x01",
            "是否还好好地活着？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "这样的状况下和国家\x01",
            "联络不上真是令人不安啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1668")

    Jump("loc_1921")

    label("loc_166B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1921")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_16D1")

    ChrTalk(    #78
        0xFE,
        (
            "喂喂，奥利维尔先生，\x01",
            "请别打扰我工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "别看大使那样\x01",
            "其实很爱干净的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_1731")

    ChrTalk(    #80
        0xFE,
        (
            "……奥利维尔先生，\x01",
            "可别太戏弄大使哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "他被宰相虐待，最近\x01",
            "头发都变得稀薄了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_1731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1921")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 4)), scpexpr(EXPR_END)), "loc_17C3")

    ChrTalk(    #82
        0xFE,
        "客人和穆拉先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "呵呵，奥利维尔先生\x01",
            "真正喜欢的是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x104,
        (
            "#030F想知道吗？\x01",
            "说来话长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1019F真是的，算了啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_17C3")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x104, 400)
    Sleep(600)

    ChrTalk(    #86
        0xFE,
        (
            "哎呀，奥利维尔先生……\x01",
            "真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "这些是您的客人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x104,
        (
            "#035F唔，的确是客人\x01",
            "也因为一起旅行……\x02\x03",

            "#030F是共同渡过连玫瑰也自愧不如\x01",
            "的甘美浓厚时光的亲密关系啊。\x02\x03",

            "#037F对吧，艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "那么，穆拉先生\x01",
            "就被抛弃了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1019F头、头痛……\x02\x03",

            "穆拉先生的辛苦\x01",
            "我似乎能够明白一点了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165C)

    label("loc_1921")

    TalkEnd(0xD)
    Return()

    # Function_8_15C7 end

    def Function_9_1925(): pass

    label("Function_9_1925")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_19A8")

    ChrTalk(    #92
        0xFE,
        "金光闪耀的浮游物体吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "那种东西，到现在为止\x01",
            "见所未见闻所未闻呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "总之只能说是让人毛骨悚然。\x02",
    )

    CloseMessageWindow()

    label("loc_19A8")

    Jump("loc_1D7F")

    label("loc_19AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1A59")

    ChrTalk(    #95
        0xFE,
        (
            "埃雷波尼亚帝国有限制\x01",
            "出版物什么的要经过严格检查哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "是不是适合国风的内容，\x01",
            "有没有大不敬的内容……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "其实我在帝国\x01",
            "也担任这样的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B16")

    label("loc_1A59")


    ChrTalk(    #98
        0xFE,
        (
            "听说利贝尔王国承认\x01",
            "国民的言论自由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "埃雷波尼亚帝国有限制\x01",
            "出版物什么的要经过严格检查哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "是不是适合国风的内容，\x01",
            "有没有大不敬的内容……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "其实我在帝国\x01",
            "也担任这样的工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1B16")

    Jump("loc_1D7F")

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_1CEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 0)), scpexpr(EXPR_END)), "loc_1BBD")

    ChrTalk(    #102
        0xFE,
        (
            "因此我推荐的书\x01",
            "该是『红耀石』小说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "作者是哪里人不太清楚，\x01",
            "不过应该是帝国出身吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "不是在帝都住过一阵子\x01",
            "应该描写不出那种风格吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEC")

    label("loc_1BBD")


    ChrTalk(    #105
        0xFE,
        "这，这本书……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "不是在埃雷波尼亚\x01",
            "禁止发行的吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "谁，谁把这种东西\x01",
            "放进书架的呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2F)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C4E")

    ChrTalk(    #108
        0x130,
        "#274F（…………………………）\x02",
    )

    CloseMessageWindow()

    label("loc_1C4E")


    ChrTalk(    #109
        0xFE,
        (
            "如果被达维尔大使知道\x01",
            "可就够受的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "对，对了，就是你。\x01",
            "快把这本书拿走！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #111
        "\x07\x00得到了\x1F\x3D\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23D, 1)
    OP_A2(0x10B8)

    label("loc_1CEC")

    Jump("loc_1D7F")

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1D7F")

    ChrTalk(    #112
        0xFE,
        (
            "这个房间的书全部\x01",
            "都是利贝尔出版的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "要了解别的国家，\x01",
            "首先要从文化开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "你们可以随便读，\x01",
            "不过一定要放回到原来的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7F")

    TalkEnd(0xE)
    Return()

    # Function_9_1925 end

    def Function_10_1D83(): pass

    label("Function_10_1D83")

    EventBegin(0x0)
    OP_6D(910, 4000, 27010, 0)
    OP_67(0, 10110, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(45000, 0)
    OP_6E(453, 0)
    SetChrPos(0x104, 1590, 0, 4140, 0)
    SetChrPos(0x101, 430, 0, 4150, 0)
    SetChrPos(0x105, 210, 0, 2710, 0)
    SetChrPos(0x108, 1520, 0, 2840, 0)

    def lambda_1E0C():
        OP_6D(970, 0, 5940, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E0C)

    def lambda_1E24():
        OP_67(0, 10110, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E24)
    OP_C8(0x200, 0x46, "C_PLAC12._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(1490, 0, 4150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #115
        0x108,
        (
            "#073F喔……\x01",
            "这真是华丽的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1011F#6P呜哇～……\x02\x03",

            "毫不逊色于卡尔瓦德大使馆\x01",
            "豪华气氛的内部装潢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x105,
        (
            "#047F壮丽而强有力的氛围……\x02\x03",

            "#048F用帝国风情的装饰品\x01",
            "装饰起来的内部装潢看起来很协调呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x104,
        (
            "#030F呼，因为这里是\x01",
            "显耀帝国威光的舞台嘛。\x02\x03",

            "#035F遗憾的是工作人员\x01",
            "似乎稍稍相形见绌。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 60)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 12690, 0, 5860, 270)
    OP_4A(0x9, 255)

    NpcTalk(    #119
        0x9,
        "男人的声音",
        (
            "#3P干嘛说这\x01",
            "危险的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_208B():

        label("loc_208B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_208B")

    QueueWorkItem2(0x104, 2, lambda_208B)

    def lambda_209C():

        label("loc_209C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_209C")

    QueueWorkItem2(0x101, 2, lambda_209C)
    Sleep(200)

    def lambda_20B2():

        label("loc_20B2")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_20B2")

    QueueWorkItem2(0x108, 2, lambda_20B2)

    def lambda_20C3():

        label("loc_20C3")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_20C3")

    QueueWorkItem2(0x105, 2, lambda_20C3)
    OP_6D(10750, 0, 5950, 2000)

    def lambda_20E5():
        OP_8E(0xFE, 0x35C, 0x0, 0x1568, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_20E5)

    def lambda_2100():
        OP_6D(990, 0, 4480, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2100)
    OP_71(0x3, 0x10)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    OP_8C(0x9, 180, 400)
    OP_44(0x104, 0x2)
    OP_44(0x101, 0x2)
    OP_44(0x108, 0x2)
    OP_44(0x105, 0x2)
    OP_8C(0x104, 0, 0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #120
        0x104,
        (
            "#031F#6P哦哦，亲爱的朋友啊！\x02\x03",

            "好久不见呢。\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "#274F#5P你这家伙……\x02\x03",

            "我那样嘱咐你\x01",
            "要告诉我你到了哪里的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x104,
        (
            "#037F#6P呼，这也算是爱的私奔吧。\x02\x03",

            "正因为分开了\x01",
            "才会有积累的感情嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        (
            "#276F#5P……艾丝蒂尔，谢谢你。\x02\x03",

            "看来这个轻佻的大赖皮蛋\x01",
            "给你添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "嗯，也没什么啦。\x02\x03",

            "#1006F还算比较安分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "#272F#5P嗯，那个怪人\x01",
            "暂且不管……\x02\x03",

            "#277F你们来帝国大使馆\x01",
            "好像有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1002F#6P啊，嗯。\x02\x03",

            "其实，是有些事情\x01",
            "想问问这里的大使……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #127
        (
            "\x07\x05说明为了询问恐吓信\x01",
            "前来会见帝国大使的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #128
        0x9,
        (
            "#273F#5P那个恐吓信啊……\x02\x03",

            "#270F我也很在意\x01",
            "但没想到协会也行动了。\x02\x03",

            "是王国军的委托吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1006F#6P姑且算是吧……\x02\x03",

            "不过我们打算尽可能\x01",
            "以中立的立场来调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        (
            "#277F#5P呵呵，想得真周到。\x02\x03",

            "那么，由我来\x01",
            "向达维尔大使介绍吧。\x02\x03",

            "那个轻佻的大赖皮蛋\x01",
            "应该不能够相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1004F#6P咦，可以吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x108,
        "#071F呀，帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x105,
        "#041F#6P非常感谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 225, 400)

    ChrTalk(    #134
        0x104,
        (
            "#036F#5P嗯……\x01",
            "我就那么不可信？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #135
        0x101,
        (
            "#1004F#6P哎……\x01",
            "你以为可信！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x108,
        (
            "#070F嗯，要是你来介绍\x01",
            "看来会导致多余的误解。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 45, 400)

    ChrTalk(    #137
        0x105,
        (
            "#045F#6P嗯……\x01",
            "抱歉了，奥利维尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x104,
        "#034F#5P（啜泣啜泣……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        "#272F#5P贤明的判断。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x105, 0, 400)
    OP_8C(0x104, 0, 400)

    ChrTalk(    #140
        0x9,
        (
            "#277F#5P达维尔大使\x01",
            "在2楼的办公室。\x02\x03",

            "我去确认一下\x01",
            "你们稍等片刻吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1006F#6P嗯，ＯＫ。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    def lambda_264F():
        OP_6D(6830, 0, 8520, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_264F)

    def lambda_2667():

        label("loc_2667")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2667")

    QueueWorkItem2(0x104, 2, lambda_2667)

    def lambda_2678():

        label("loc_2678")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2678")

    QueueWorkItem2(0x101, 2, lambda_2678)

    def lambda_2689():

        label("loc_2689")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2689")

    QueueWorkItem2(0x108, 2, lambda_2689)

    def lambda_269A():

        label("loc_269A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_269A")

    QueueWorkItem2(0x105, 2, lambda_269A)
    OP_8E(0x9, 0x2242, 0x0, 0x1EE6, 0xBB8, 0x0)
    OP_8E(0x9, 0x2454, 0x7D0, 0x3AF2, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_6D(1020, 0, 3870, 2000)
    OP_44(0x104, 0x2)
    OP_44(0x101, 0x2)
    OP_44(0x108, 0x2)
    OP_44(0x105, 0x2)
    OP_72(0x2, 0x10)
    OP_65(0x0, 0x1)
    OP_A2(0x1620)
    EventEnd(0x0)
    Return()

    # Function_10_1D83 end

    def Function_11_2702(): pass

    label("Function_11_2702")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 1500, 4000, 29410, 0)
    SetChrPos(0x101, 320, 4000, 29600, 0)
    SetChrPos(0x108, 1380, 4000, 28080, 0)
    SetChrPos(0x105, -110, 4000, 28000, 0)
    OP_6D(920, 4000, 30680, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(    #142
        0x101,
        (
            "#1015F#6P嗯……\x01",
            "这里是办公室吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x104,
        (
            "#031F#2P呼，没错。\x02\x03",

            "那么就华丽地闯入\x01",
            "吓大使殿下一跳吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #144
        0x101,
        (
            "#1019F#6P会被穆拉先生\x01",
            "暴扁的哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    Sleep(1000)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 1020, 4000, 32900, 180)
    ClearChrFlags(0x9, 0x80)
    OP_8C(0x101, 0, 400)

    def lambda_286F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_286F)
    OP_8E(0x9, 0x384, 0xFA0, 0x79EA, 0x7D0, 0x0)

    ChrTalk(    #145
        0x9,
        (
            "#277F#5P久等了。\x01",
            "大使说可以见你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1006F#6P啊，嗯。\x01",
            "那么就有劳了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28E4():
        OP_8E(0xFE, 0x96A, 0xFA0, 0x7A08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_28E4)
    WaitChrThread(0x9, 0x0)
    OP_8C(0x9, 270, 400)
    OP_43(0x101, 0x0, 0x0, 0x11)
    Sleep(500)
    OP_43(0x104, 0x0, 0x0, 0x11)
    Sleep(300)
    OP_43(0x105, 0x0, 0x0, 0x11)
    Sleep(600)
    OP_43(0x108, 0x0, 0x0, 0x11)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x2F, 0xFF, 0xFF)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x130, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6D(450, 0, 67280, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_29AE():
        OP_6D(1760, 0, 73830, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29AE)
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(600)
    OP_43(0x104, 0x1, 0x0, 0xD)
    Sleep(600)
    OP_43(0x105, 0x1, 0x0, 0xE)
    Sleep(600)
    OP_43(0x108, 0x1, 0x0, 0xF)
    Sleep(600)
    OP_43(0x130, 0x1, 0x0, 0x10)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_0D()

    ChrTalk(    #147
        0x8,
        (
            "#1100F#5P欢迎光临\x01",
            "埃雷波尼亚大使馆。\x02\x03",

            "我是驻利贝尔大使\x01",
            "达维尔·克莱纳赫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1011F#6P嗯，我是游击士协会的\x01",
            "艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x108,
        (
            "#070F#4P金·瓦赛克。\x01",
            "同是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x105,
        (
            "#040F杰尼丝王立学院２年级生，\x01",
            "我叫科洛丝·琳希。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x104,
        (
            "#031F还有爱与和平的使者，\x01",
            "奥利维尔·朗海姆！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "#1102F#5P哼……是你啊。\x02\x03",

            "#1100F听说你去了亚尔摩村\x01",
            "就行踪不明了啊。\x02\x03",

            "太让穆拉\x01",
            "担心可不行哦。\x02\x03",

            "当然还有我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x104,
        "#035F呼，您真是严厉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "#1100F#5P别提这个了……\x02\x03",

            "你们似乎是来问\x01",
            "那个恐吓信的事吧。\x02\x03",

            "想知道些什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#1002F#6P嗯，那么\x01",
            "我们就单刀直入地问了。\x02\x03",

            "大使对威胁者\x01",
            "有线索吗？\x02\x03",

            "譬如帝国内\x01",
            "反对条约缔结的势力什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#1102F#5P哈哈，你说话真直啊。\x02\x03",

            "#1100F不过很不巧\x01",
            "我完全没有线索。\x02\x03",

            "皇帝陛下对条约缔结\x01",
            "也相当积极。\x02\x03",

            "而且异端不规矩之人等\x01",
            "怎么可能出现在我帝国？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1007F#6P这、这样断言\x01",
            "真是直截了当啊……\x02\x03",

            "#1015F那么大使先生认为\x01",
            "是帝国以外的人做的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "#1100F#5P当然，必然是这样吧。\x02\x03",

            "很可能是卡尔瓦德附近的\x01",
            "在野党势力在作祟吧。\x02\x03",

            "愚民政治的弊病就在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x108,
        (
            "#073F#4P这我觉得难说。\x02\x03",

            "#070F的确共和国的执政党\x01",
            "和在野党总是对立的……\x02\x03",

            "但哪怕条约缔结被阻止了\x01",
            "我也不认为会变成总统的责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#1102F#5P哼，详情我可不知道。\x02\x03",

            "#1100F能肯定的，只有威胁者\x01",
            "不可能是帝国的人这件事。\x02\x03",

            "知道这个不就够了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1015F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x105,
        (
            "#047F#4P……那个，达维尔大使。\x02\x03",

            "#042F奥斯本宰相阁下\x01",
            "对于互不侵犯条约，\x01",
            "是持什么样的态度呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #163
        0x8,
        "#1101F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x130, 225, 400)
    Sleep(200)

    ChrTalk(    #164
        0x130,
        "#273F#5P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x104,
        (
            "#035F呼呼……\x01",
            "相当尖锐的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1016F#6P嗯……\x01",
            "那个奥斯本大人是……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x104,
        (
            "#030F帝国政府的代表，\x01",
            "铁血宰相奥斯本。\x02\x03",

            "『国家的稳定要靠铁血』\x01",
            "毫不忌讳公开如此宣称的人。\x02\x03",

            "#035F在帝国全土铺设导力铁道\x01",
            "武力合并几个自治州\x01",
            "嗯，总之是精力充沛的政治家。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #168
        0x101,
        "#1004F#5P有，有这种人啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #169
        0x8,
        (
            "#1103F#5P喂，我说奥利维尔！\x02\x03",

            "对于本国的宰相，\x01",
            "不许使用带批判性的言词！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #170
        0x104,
        (
            "#035F呼～\x01",
            "其实没有批判的意思。\x02\x03",

            "#030F只是，如果再合作点儿\x01",
            "也不会不合适吧？\x02\x03",

            "之前，共和国的爱尔莎大使\x01",
            "也说了很多情况……\x02\x03",

            "他们可是合作多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        "#1101F#5P什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x104,
        (
            "#034F这样下去埃雷波尼亚帝国\x01",
            "的度量就会被人怀疑了……\x02\x03",

            "这我可不能忍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        "#1101F#5P唔唔唔……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x130, 270, 400)

    ChrTalk(    #174
        0x130,
        (
            "#276F#2P达维尔大使。\x02\x03",

            "关于这件事\x01",
            "没有什么情报好隐瞒的。\x02\x03",

            "直率说明情况\x01",
            "也没有什么问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "#1102F#5P……哼，好吧。\x02\x03",

            "#1100F关于之前的问题……\x01",
            "和陛下一样，奥斯本宰相\x01",
            "对条约缔结也非常积极。\x02\x03",

            "听说反而是宰相\x01",
            "向陛下进言的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x105,
        "#044F#4P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x104,
        "#030F哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1015F#6P嗯，这么说果然\x01",
            "还是以新型引擎为目标吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#1102F#5P不，他向陛下进言似乎\x01",
            "是在新型引擎的事情出来之前。\x02\x03",

            "#1100F嗯，事情就是如此\x01",
            "我也少了奇怪的压力\x01",
            "说实话倒是松了口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x108,
        (
            "#074F#4P唔，原来如此啊……\x02\x03",

            "#070F这样看来帝国关系者\x01",
            "无辜的可能性似乎很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#1007F#6P嗯，似乎是这样。\x02\x03",

            "#1006F大使先生，非常感谢您能\x01",
            "告诉我们这些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x8,
        (
            "#1101F#5P哼、哼……怎么样。\x01",
            "我一开始就说了吧。\x02\x03",

            "要找犯人\x01",
            "就赶快去别处吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1004F#6P啊，稍等一下！\x02\x03",

            "#1015F嗯，其实还有\x01",
            "一件事想问……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #184
        "\x07\x05关于玲的父母，试着询问了达维尔大使。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #185
        0x8,
        (
            "#1102F#5P是吗……\x01",
            "那真是可怜。\x02\x03",

            "#1100F唔～帝国商人的话时常\x01",
            "会来这个大使馆……\x02\x03",

            "不过说到克洛斯贝尔的\x01",
            "贸易商倒是真的没印象。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #186
        0x8,
        "#1100F#5P穆拉怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x130,
        (
            "#272F#2P不……\x01",
            "我也没有记忆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1015F#6P这样啊……\x02\x03",

            "#1007F嗯～这边\x01",
            "看来也是前途多难啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #189
        0x8,
        (
            "#1100F#5P不过竟然要同时寻找\x01",
            "恐吓犯和迷路孩子的亲人……\x02\x03",

            "虽然是老调重弹\x01",
            "还请你们加油不要放弃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#1006F#6P啊……是！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x130, 225, 400)
    Sleep(400)

    ChrTalk(    #191
        0x130,
        "#277F#5P那么，我送你们到门口吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(700, 0, 70010, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 700, 0, 70010, 180)
    SetChrPos(0x1, 700, 0, 70010, 180)
    SetChrPos(0x2, 700, 0, 70010, 180)
    SetChrPos(0x3, 700, 0, 70010, 180)
    SetChrPos(0x130, 700, 0, 70010, 180)
    OP_71(0x2, 0x10)
    OP_64(0x0, 0x1)
    OP_A2(0x1621)
    OP_28(0x8B, 0x2, 0x20)
    OP_28(0x8B, 0x1, 0x40)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_2702 end

    def Function_12_37E2(): pass

    label("Function_12_37E2")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_3809():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3809)
    OP_8E(0xFE, 0x406, 0x0, 0x11990, 0x7D0, 0x0)
    Return()

    # Function_12_37E2 end

    def Function_13_382A(): pass

    label("Function_13_382A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_3851():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3851)
    OP_8E(0xFE, 0xFFFFFF2E, 0x0, 0x11756, 0x7D0, 0x0)
    Return()

    # Function_13_382A end

    def Function_14_3872(): pass

    label("Function_14_3872")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_3899():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3899)
    OP_8E(0xFE, 0x73A, 0x0, 0x116B6, 0x7D0, 0x0)
    Return()

    # Function_14_3872 end

    def Function_15_38BA(): pass

    label("Function_15_38BA")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_38E1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38E1)
    OP_8E(0xFE, 0x24E, 0x0, 0x11472, 0x7D0, 0x0)
    Return()

    # Function_15_38BA end

    def Function_16_3902(): pass

    label("Function_16_3902")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_3929():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3929)
    OP_8E(0xFE, 0xFFFFFFBA, 0x0, 0xFF45, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_8E(0xFE, 0xCB2, 0x0, 0x10F90, 0x9C4, 0x0)
    OP_8E(0xFE, 0xCB2, 0x0, 0x11EFE, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_3902 end

    def Function_17_398A(): pass

    label("Function_17_398A")

    OP_8E(0xFE, 0x3CA, 0xFA0, 0x82D2, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_398A end

    def Function_18_39AF(): pass

    label("Function_18_39AF")

    OP_8E(0xFE, 0x302, 0xFA0, 0x7A58, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3CA, 0xFA0, 0x82D2, 0xBB8, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_39AF end

    def Function_19_39E8(): pass

    label("Function_19_39E8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #192
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_19_39E8 end

    def Function_20_3A25(): pass

    label("Function_20_3A25")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #193
        "\x07\x05书架上有『红耀石』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【读第１卷】\x01",      # 0
            "【读第２卷】\x01",      # 1
            "【读第３卷】\x01",      # 2
            "【读第４卷】\x01",      # 3
            "【读第５卷】\x01",      # 4
            "【读第６卷】\x01",      # 5
            "【放弃】\x01",          # 6
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B06")
    OP_B8(0x212, 0x0)

    label("loc_3B06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B18")
    OP_B8(0x213, 0x0)

    label("loc_3B18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2A")
    OP_B8(0x214, 0x0)

    label("loc_3B2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B3C")
    OP_B8(0x215, 0x0)

    label("loc_3B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4E")
    OP_B8(0x216, 0x0)

    label("loc_3B4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B60")
    OP_B8(0x217, 0x0)

    label("loc_3B60")

    TalkEnd(0xFF)
    Return()

    # Function_20_3A25 end

    def Function_21_3B64(): pass

    label("Function_21_3B64")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #194
        "\x07\x05书架上有『红耀石』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【读第７卷】\x01",      # 0
            "【读第８卷】\x01",      # 1
            "【读第９卷】\x01",      # 2
            "【读第10卷】\x01",      # 3
            "【读最终卷】\x01",      # 4
            "【放弃】\x01",          # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C38")
    OP_B8(0x218, 0x0)

    label("loc_3C38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4A")
    OP_B8(0x219, 0x0)

    label("loc_3C4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5C")
    OP_B8(0x21A, 0x0)

    label("loc_3C5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C6E")
    OP_B8(0x21B, 0x0)

    label("loc_3C6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C80")
    OP_B8(0x21C, 0x0)

    label("loc_3C80")

    TalkEnd(0xFF)
    Return()

    # Function_21_3B64 end

    SaveToFile()

Try(main)
