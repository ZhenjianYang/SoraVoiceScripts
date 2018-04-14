from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0110   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0110.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0110_1 ._SN',
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
        '鲁克',                                 # 9
        '鲁克',                                 # 10
        '玛茜婆婆',                             # 11
        '帕特',                                 # 12
        '雷特拉',                               # 13
        '赛拉',                                 # 14
        '阿斯顿队长',                           # 15
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
        'ED6_DT07/CH01160 ._CH',             # 00
        'ED6_DT07/CH01110 ._CH',             # 01
        'ED6_DT07/CH01060 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01310 ._CH',             # 05
        'ED6_DT26/CH20330 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01160P._CP',             # 00
        'ED6_DT07/CH01110P._CP',             # 01
        'ED6_DT07/CH01060P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01310P._CP',             # 05
        'ED6_DT26/CH20330P._CP',             # 06
    )

    DeclNpc(
        X                   = 54480,
        Z                   = 0,
        Y                   = 163580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 55200,
        Z                   = 100,
        Y                   = 159950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51750,
        Z                   = 0,
        Y                   = 163200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 56170,
        Z                   = 0,
        Y                   = 161420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 93320,
        Z                   = 0,
        Y                   = 162900,
        Direction           = 0,
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
        X                   = 58080,
        Z                   = 0,
        Y                   = 198250,
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
        X                   = 49300,
        Z                   = 0,
        Y                   = 161100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 94990,
        TriggerZ            = 0,
        TriggerY            = 166570,
        TriggerRange        = 800,
        ActorX              = 95120,
        ActorZ              = 1400,
        ActorY              = 165990,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_2E1",          # 01, 1
        "Function_2_32B",          # 02, 2
        "Function_3_4A8",          # 03, 3
        "Function_4_BA0",          # 04, 4
        "Function_5_D37",          # 05, 5
        "Function_6_F39",          # 06, 6
        "Function_7_17E1",         # 07, 7
        "Function_8_1CF0",         # 08, 8
        "Function_9_1CF7",         # 09, 9
        "Function_10_1E99",        # 0A, 10
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_22D")
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E")
    SetChrPos(0xB, 55510, 0, 163460, 270)
    Jump("loc_22A")

    label("loc_20E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219")
    Jump("loc_22A")

    label("loc_219")

    SetChrPos(0xB, 55510, 0, 163460, 270)

    label("loc_22A")

    Jump("loc_2D2")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_237")
    Jump("loc_2D2")

    label("loc_237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_272")
    SetChrPos(0xA, 55120, 0, 161430, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 92380, 0, 161500, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x9, 4)
    Jump("loc_2D2")

    label("loc_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, 55120, 0, 161430, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x9, 4)
    Jump("loc_2D2")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2BC")
    SetChrPos(0xD, 88100, 0, 162410, 270)
    Jump("loc_2D2")

    label("loc_2BC")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 49230, 0, 165600, 0)

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E0")
    OP_A3(0x10F0)
    Event(0, 9)

    label("loc_2E0")

    Return()

    # Function_0_1E6 end

    def Function_1_2E1(): pass

    label("Function_1_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2EB")
    Jump("loc_317")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2FC")
    OP_6F(0x2, 15)
    Jump("loc_317")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_30D")
    OP_6F(0x2, 15)
    Jump("loc_317")

    label("loc_30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_317")
    Jump("loc_317")

    label("loc_317")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_32A")
    OP_65(0x0, 0x1)

    label("loc_32A")

    Return()

    # Function_1_2E1 end

    def Function_2_32B(): pass

    label("Function_2_32B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_492")

    label("loc_350")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_492")

    label("loc_369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_492")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_492")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_492")

    label("loc_3B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_492")

    label("loc_3CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_492")

    label("loc_3E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_492")

    label("loc_3FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_492")

    label("loc_418")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_492")

    label("loc_431")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_492")

    label("loc_44A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_492")

    label("loc_463")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_492")

    label("loc_47C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_492")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_492")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_492")

    label("loc_4A7")

    Return()

    # Function_2_32B end

    def Function_3_4A8(): pass

    label("Function_3_4A8")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_4FA")

    ChrTalk(    #0
        0xFE,
        "唉，鲁克回来得真晚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "这种时候还这样，\x01",
            "小孩子真是不懂事哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9C")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD")

    ChrTalk(    #2
        0xFE,
        (
            "今天早上，火炉点不着了，\x01",
            "不过以为只是故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "去了梅尔达斯工房后，\x01",
            "发现现在到处都是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "这大概是\x01",
            "遭到女神的报应了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "一定是在斥责我们\x01",
            "不应该太过于享乐。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_613")

    label("loc_5BD")


    ChrTalk(    #6
        0xFE,
        (
            "导力器的事，\x01",
            "大概是遭到女神的报应了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "一定是在斥责我们\x01",
            "不应该太过于享乐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_613")

    Jump("loc_B9C")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_81C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_662")

    ChrTalk(    #8
        0xFE,
        (
            "那料理的事\x01",
            "不太清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "不好意思，请去问别人吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_819")

    label("loc_662")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68D")
    Call(1, 0)
    Jump("loc_819")

    label("loc_68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_73B")

    ChrTalk(    #10
        0xFE,
        (
            "我家的鲁克啊，\x01",
            "终于醒来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "这下又能看着他\x01",
            "和阿斯顿一起练剑了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "这样看来\x01",
            "小孩的教育怎么样还真是次要的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "总之只要那孩子健康\x01",
            "就是我的幸福。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_819")

    label("loc_73B")


    ChrTalk(    #14
        0xFE,
        "哎呀，是游击士们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "我家的鲁克\x01",
            "终于醒来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "已经完全恢复了呢。\x01",
            "现在已经出去玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "真是的，也不想想\x01",
            "自己多让人担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "不过也算了……\x01",
            "今天就不唠叨他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "那孩子醒来了。\x01",
            "现在这样就足够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_819")

    Jump("loc_B9C")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_89E")

    ChrTalk(    #20
        0xFE,
        (
            "刚才，他爸爸阿斯顿\x01",
            "也回了一趟家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "看了看鲁克的情况\x01",
            "又回去警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "就不能找别人\x01",
            "暂代一下任务吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_943")

    label("loc_89E")


    ChrTalk(    #23
        0xFE,
        (
            "刚才，他爸爸阿斯顿\x01",
            "也回了一趟家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "看了看鲁克的情况\x01",
            "又回去警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "我知道公事很重要，\x01",
            "但他还是有点逞强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "阿斯顿他呀……\x01",
            "其实应该非常担心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_943")

    Jump("loc_B9C")

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9A5")

    ChrTalk(    #27
        0xFE,
        (
            "帕特也来了。\x01",
            "已经可以出去玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "要是平时的你，\x01",
            "应该早就跳起来了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A40")

    label("loc_9A5")

    SetChrName("玛茜婆婆")

    ChrTalk(    #29
        0xFE,
        (
            "鲁克啊……\x01",
            "已经到早上了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "好了，起来啦。\x01",
            "今天雾也很大哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "帕特也来了……\x01",
            "随时都可以出去玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "喂，鲁克……\x01",
            "早点起来……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A40")

    Jump("loc_B9C")

    label("loc_A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AB9")

    ChrTalk(    #33
        0xFE,
        (
            "鲁克那淘气的样子\x01",
            "到底像谁呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "这个样子，教他剑的\x01",
            "阿斯顿也够辛苦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "一定相当\x01",
            "棘手吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B50")

    label("loc_AB9")


    ChrTalk(    #36
        0xFE,
        (
            "鲁克那淘气的样子\x01",
            "到底像谁呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "早饭也不吃\x01",
            "就飞奔出去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "好不容易开始学剑，\x01",
            "却一点都没长进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "他爸爸阿斯顿以前\x01",
            "可是很安分的孩子。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B50")

    Jump("loc_B9C")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_B9C")

    ChrTalk(    #40
        0xFE,
        (
            "哎呀，鲁克\x01",
            "去哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "真是的……\x01",
            "马上就要吃午饭了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9C")

    TalkEnd(0xA)
    Return()

    # Function_3_4A8 end

    def Function_4_BA0(): pass

    label("Function_4_BA0")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 3)), scpexpr(EXPR_END)), "loc_C05")

    ChrTalk(    #42
        0xFE,
        (
            "据说，从现在起王国军\x01",
            "就要进行大规模的组织改革了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "我们也快要忙起来喽。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D33")

    label("loc_C05")


    ChrTalk(    #44
        0xFE,
        "啊，这不是艾丝蒂尔吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "何时回到洛连特的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#000F刚刚才到的，阿斯顿先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "是吗，你回来了\x01",
            "我家鲁克一定会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "鲁克最近，总是\x01",
            "缠着我要学剑术呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "还以为突然怎么了呢，\x01",
            "问他理由也不说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "可能因为我常常不在家，\x01",
            "怎么和儿子交流还真是伤脑筋啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "哈哈，真难为情了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1033)

    label("loc_D33")

    TalkEnd(0xE)
    Return()

    # Function_4_BA0 end

    def Function_5_D37(): pass

    label("Function_5_D37")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D8F")

    ChrTalk(    #52
        0xB,
        (
            "吃完晚饭\x01",
            "我再去找鲁克。\x02\x03",

            "如果我去了，鲁克一定\x01",
            "也会想出去玩的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E33")

    label("loc_D8F")


    ChrTalk(    #53
        0xB,
        (
            "我本来是\x01",
            "和鲁克在一起的……\x02\x03",

            "但是被妈妈\x01",
            "硬拖回来了。\x02\x03",

            "不过，吃完晚饭\x01",
            "我会再去看他的。\x02\x03",

            "如果我在，鲁克一定\x01",
            "也会想出去玩的吧？\x02\x03",

            "顺利的话，\x01",
            "说不定会醒过来哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_E33")

    Jump("loc_F35")

    label("loc_E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_F35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_E84")

    ChrTalk(    #54
        0xB,
        (
            "鲁克虽然没醒来，\x01",
            "但表情好像挺开心的。\x02\x03",

            "一定在做美梦吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F35")

    label("loc_E84")


    ChrTalk(    #55
        0xB,
        (
            "啊，艾丝蒂尔姐姐……\x02\x03",

            "到了早上\x01",
            "鲁克还没起来啊。\x02\x03",

            "玛茜婆婆的声音\x01",
            "好像也听不到……\x02\x03",

            "……不过啊，姐姐。\x02\x03",

            "鲁克的睡脸……\x01",
            "看起来好像很开心呢。\x02\x03",

            "因为鲁克他，\x01",
            "一定在做美梦吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_F35")

    TalkEnd(0xB)
    Return()

    # Function_5_D37 end

    def Function_6_F39(): pass

    label("Function_6_F39")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_FD2")

    ChrTalk(    #56
        0xFE,
        (
            "我妻子赛拉和儿子帕特\x01",
            "现在正打算去参加婚礼哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "这时候举行婚礼\x01",
            "真是不合时宜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "不过，正因为这样\x01",
            "更要祝福他们\x01",
            "新婚生活幸福呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DD")

    label("loc_FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109F")

    ChrTalk(    #59
        0xFE,
        (
            "呀，导力器居然停了，\x01",
            "真令人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "正读着喜欢的书，\x01",
            "突然就变得漆黑一片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "以为是故障去了工房，\x01",
            "结果说原因不明……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "再加上那个出现在空中的岛，\x01",
            "总有点不吉利的预感啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_10E4")

    label("loc_109F")


    ChrTalk(    #63
        0xFE,
        (
            "导力器不能用的原因\x01",
            "好像还不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "总有点不吉利的预感啊……\x02",
    )

    CloseMessageWindow()

    label("loc_10E4")

    Jump("loc_17DD")

    label("loc_10E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1304")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1187")

    ChrTalk(    #65
        0xFE,
        (
            "看来食谱\x01",
            "已经找到了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "传统料理能够复活，\x01",
            "我个人也是非常期待呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "可以的话真想加进\x01",
            "亚班特酒馆的例牌菜单啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1301")

    label("loc_1187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E7")

    ChrTalk(    #68
        0xFE,
        (
            "食谱册应该\x01",
            "放在哪个书架上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "不好意思\x01",
            "你们自己找找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1301")

    label("loc_11E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1212")
    Call(1, 1)
    Jump("loc_1301")

    label("loc_1212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1262")

    ChrTalk(    #70
        0xFE,
        (
            "帕特和鲁克一起\x01",
            "飞奔出去了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "不管怎样，鲁克\x01",
            "醒来了就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1301")

    label("loc_1262")


    ChrTalk(    #72
        0xFE,
        (
            "帕特和鲁克一起\x01",
            "飞奔出去了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "不管怎样，鲁克\x01",
            "醒来了就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "不过，雾散天晴的同时\x01",
            "那孩子就醒了过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "……这几天的事情\x01",
            "真是难以理解啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1301")

    Jump("loc_17DD")

    label("loc_1304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_136B")

    ChrTalk(    #76
        0xFE,
        (
            "在雾中行走之时，\x01",
            "骑士也忘记了使命……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "看到现在的洛连特，\x01",
            "真让人想起这传说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1446")

    label("loc_136B")


    ChrTalk(    #78
        0xFE,
        (
            "前来警备的士兵们，\x01",
            "对这雾也很困惑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "如此浓雾……\x01",
            "简直像是中世纪文学中\x01",
            "所描绘的神秘森林一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "在雾中前进之时，\x01",
            "勇敢的骑士们也迷失了方向，\x01",
            "最后连使命也忘记了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "看到现在的洛连特，\x01",
            "真让人想起这传说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1446")

    Jump("loc_17DD")

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_154F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14B7")

    ChrTalk(    #82
        0xFE,
        "今天是互不侵犯条约的签字议式吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "应该是值得纪念的一天，\x01",
            "但却总是没有祝贺的心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154C")

    label("loc_14B7")


    ChrTalk(    #84
        0xFE,
        "今天是互不侵犯条约的签字议式吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "明明是值得纪念的一天，\x01",
            "城市被不吉利的雾所覆盖啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "再加上鲁克他们的事，\x01",
            "怎么也没有了祝贺的心情。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_154C")

    Jump("loc_17DD")

    label("loc_154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_16D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(    #87
        0xFE,
        (
            "以前这一带\x01",
            "也常有旅行艺人来表演。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "最近是没见过了，\x01",
            "还真想再去看看啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D5")

    label("loc_15B0")


    ChrTalk(    #89
        0xFE,
        "哎呀～今天的雾可真厉害。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "湿气会伤书本，\x01",
            "因此急急忙忙开始整理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "结果偶然发现了\x01",
            "令人怀念的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "……居然是１０年以前看\x01",
            "旅行艺人表演的票呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "作为跟妻子的首次约会纪念\x01",
            "被夹在书里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "哎呀，回想起来。\x01",
            "那时候的赛拉可真漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "不，不过……\x01",
            "当然现在也很漂亮。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_16D5")

    Jump("loc_17DD")

    label("loc_16D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_17DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_174C")

    ChrTalk(    #96
        0xFE,
        (
            "政变的时候\x01",
            "遭到他国侵略，\x01",
            "这在历史上也经常发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "担心帝国会不会攻过来，\x01",
            "总是心惊胆战的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DD")

    label("loc_174C")


    ChrTalk(    #98
        0xFE,
        (
            "理查德上校的政变\x01",
            "是相当严重的事件吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "政变的时候\x01",
            "遭到他国侵略，\x01",
            "这在历史上也经常发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "总是担心帝国会不会攻过\x01",
            "来，心惊胆战的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_17DD")

    TalkEnd(0xC)
    Return()

    # Function_6_F39 end

    def Function_7_17E1(): pass

    label("Function_7_17E1")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_18E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_185B")

    ChrTalk(    #101
        0xFE,
        (
            "看到帕特他们就在想，\x01",
            "是不是我也该和老公一起出去转转呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "呵呵，像以前那样\x01",
            "约会一下也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DF")

    label("loc_185B")


    ChrTalk(    #103
        0xFE,
        (
            "鲁克也醒了过来，\x01",
            "总算能放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "难得雾散了天也晴了，\x01",
            "是不是去约约老公看看呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "呵呵，像以前那样\x01",
            "约会一下也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_18DF")

    Jump("loc_1CEC")

    label("loc_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1996")

    ChrTalk(    #106
        0xFE,
        (
            "虽然不大好……\x01",
            "还是把帕特带回家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "因为这个事件的原因\x01",
            "还不清楚吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "如果是什么病\x01",
            "连这孩子都会遭到牵连。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "虽然对不住玛茜婆婆，\x01",
            "但保护孩子是父母的责任。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEC")

    label("loc_1996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_19ED")

    ChrTalk(    #110
        0xFE,
        (
            "帕特一起床\x01",
            "就去看鲁克了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "真不希望这孩子\x01",
            "再遭遇到那种事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_19ED")


    ChrTalk(    #112
        0xFE,
        (
            "帕特一起床\x01",
            "就去看鲁克了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "虽然明白他的担心，\x01",
            "但也不能连早饭也不吃啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "真怕连那孩子\x01",
            "也会倒下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "希望别变成\x01",
            "鲁克那样……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1A7C")

    Jump("loc_1CEC")

    label("loc_1A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 2)), scpexpr(EXPR_END)), "loc_1B11")

    ChrTalk(    #116
        0xFE,
        (
            "我老公真是的，\x01",
            "又在翻看旧书了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "而且从刚才开始\x01",
            "就一直看着那些旧纸片傻笑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "……是不是湿气太重\x01",
            "连脑袋里都发霉了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE9")

    label("loc_1B11")


    ChrTalk(    #119
        0xFE,
        (
            "我老公真是的，\x01",
            "又在翻看旧书了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "一时冲动买下的书\x01",
            "还真是存了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "反正要扔掉，\x01",
            "送人还不至于浪费。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "所以，给。\x01",
            "这个给你。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #123
        "\x07\x00得到了\x1F\x3F\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23F, 1)
    OP_A2(0x10BA)

    label("loc_1BE9")

    Jump("loc_1CEC")

    label("loc_1BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_1CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C6E")

    ChrTalk(    #124
        0xFE,
        (
            "那孩子和鲁克\x01",
            "一起玩挺让人担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "但和我老公在一起\x01",
            "也不大放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "要能再找个\x01",
            "出色点的人看着就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEC")

    label("loc_1C6E")


    ChrTalk(    #127
        0xFE,
        (
            "最近，帕特经常和老公\x01",
            "一起看书呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "书是精神食粮，\x01",
            "对那孩子也是好事吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "就是担心会不会\x01",
            "受些什么奇怪的影响。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1CEC")

    TalkEnd(0xD)
    Return()

    # Function_7_17E1 end

    def Function_8_1CF0(): pass

    label("Function_8_1CF0")

    TalkBegin(0x8)
    TalkEnd(0x8)
    Return()

    # Function_8_1CF0 end

    def Function_9_1CF7(): pass

    label("Function_9_1CF7")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x9, 255)
    OP_6F(0x2, 15)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, 55200, 100, 159950, 180)
    SetChrPos(0xA, 55120, 0, 161430, 180)
    SetChrPos(0xB, 56170, 0, 161420, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x9, 6)
    SetChrSubChip(0x9, 4)
    OP_6D(51920, 350, 164390, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    def lambda_1DBB():
        OP_6D(54630, 350, 161690, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1DBB)
    FadeToBright(1000, 0)
    Sleep(2500)
    SetChrSubChip(0x9, 5)
    Sleep(200)
    OP_4A(0xB, 255)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0xE, 90, 400)
    OP_43(0xB, 0x1, 0x0, 0xA)
    Sleep(300)

    def lambda_1E35():
        OP_8E(0xFE, 0xC5F8, 0x0, 0x26F7A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1E35)
    WaitChrThread(0xE, 0x0)

    def lambda_1E55():
        OP_8E(0xFE, 0xD0A2, 0x0, 0x27042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1E55)
    WaitChrThread(0xE, 0x0)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0131   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1CF7 end

    def Function_10_1E99(): pass

    label("Function_10_1E99")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EC1")
    OP_95(0xB, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    Jump("Function_10_1E99")

    label("loc_1EC1")

    Return()

    # Function_10_1E99 end

    SaveToFile()

Try(main)
