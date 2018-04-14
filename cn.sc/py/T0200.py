from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0200   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0200.x',
        MapIndex            = 12,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0200_1 ._SN',
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
        '克劳斯市长',                           # 9
        '士兵库雷',                             # 10
        '乌鸦',                                 # 11
        '基蒂',                                 # 12
        '洛连特市街区',                         # 13
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
        'ED6_DT07/CH02350 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT27/CH03870 ._CH',             # 02
        'ED6_DT27/CH03871 ._CH',             # 03
        'ED6_DT27/CH03005 ._CH',             # 04
        'ED6_DT07/CH01770 ._CH',             # 05
        'ED6_DT26/CH20311 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02350P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT27/CH03870P._CP',             # 02
        'ED6_DT27/CH03871P._CP',             # 03
        'ED6_DT27/CH03005P._CP',             # 04
        'ED6_DT07/CH01770P._CP',             # 05
        'ED6_DT26/CH20311P._CP',             # 06
    )

    DeclNpc(
        X                   = 8700,
        Z                   = 3650,
        Y                   = 2510,
        Direction           = 270,
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
        X                   = 7070,
        Z                   = 450,
        Y                   = 1530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 7640,
        Z                   = 0,
        Y                   = 11140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4940,
        Z                   = 0,
        Y                   = 6680,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -20690,
        Z                   = 0,
        Y                   = -180,
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


    DeclActor(
        TriggerX            = 8130,
        TriggerZ            = 0,
        TriggerY            = -13900,
        TriggerRange        = 1000,
        ActorX              = 8130,
        ActorZ              = 2100,
        ActorY              = -13700,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_1FB",          # 01, 1
        "Function_2_283",          # 02, 2
        "Function_3_299",          # 03, 3
        "Function_4_4A6",          # 04, 4
        "Function_5_6B3",          # 05, 5
        "Function_6_81D",          # 06, 6
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE")
    ClearChrFlags(0xB, 0x80)

    label("loc_1BE")

    Jump("loc_1D2")

    label("loc_1C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D2")
    ClearChrFlags(0x8, 0x80)

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E3")
    ClearChrFlags(0x9, 0x80)

    label("loc_1E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1FA")
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x3)

    label("loc_1FA")

    Return()

    # Function_0_1A6 end

    def Function_1_1FB(): pass

    label("Function_1_1FB")

    OP_16(0x2, 0xFA0, 0xFFFE36F8, 0xFFFE0C00, 0x230002)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_238")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_24D")

    label("loc_238")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_24D")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_271")
    OP_65(0x0, 0x1)

    label("loc_271")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_282")
    SoundLoad(347)
    SoundLoad(140)

    label("loc_282")

    Return()

    # Function_1_1FB end

    def Function_2_283(): pass

    label("Function_2_283")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_298")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_283")

    label("loc_298")

    Return()

    # Function_2_283 end

    def Function_3_299(): pass

    label("Function_3_299")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 5590, 13090, 9980, 9010, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A5")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46E")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_354")

    def lambda_338():

        label("loc_338")

        OP_97(0xFE, 0x28D2, 0x4272, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_338")

    QueueWorkItem2(0xFE, 1, lambda_338)
    Jump("loc_373")

    label("loc_354")


    def lambda_35A():

        label("loc_35A")

        OP_97(0xFE, 0x28D2, 0x4272, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_35A")

    QueueWorkItem2(0xFE, 1, lambda_35A)

    label("loc_373")

    SetChrChipByIndex(0xFE, 2)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    OP_22(0x15B, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C4")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BC")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_3C4")

    label("loc_3BC")

    Sleep(15)
    Jump("loc_38C")

    label("loc_3C4")

    OP_44(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 7640, 0, 11140, 270)

    label("loc_3E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46B")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4650), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4650), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4650), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4650), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_463")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 3)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 5590, 13090, 9980, 9010, 0)
    Jump("loc_46B")

    label("loc_463")

    Sleep(500)
    Jump("loc_3E3")

    label("loc_46B")

    Jump("loc_4A2")

    label("loc_46E")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2")

    def lambda_48A():
        OP_8D(0xFE, 5590, 13090, 9980, 9010, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48A)

    label("loc_4A2")

    Jump("loc_2CD")

    label("loc_4A5")

    Return()

    # Function_3_299 end

    def Function_4_4A6(): pass

    label("Function_4_4A6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_5CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_52E")

    ChrTalk(    #0
        0x8,
        (
            "#602F这里对艾丝蒂尔\x01",
            "来说就像是自己家的院子一样吧。\x02\x03",

            "不过，还是不能\x01",
            "掉以轻心啊。\x02\x03",

            "雾很浓，\x01",
            "什么东西都看不清楚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB")

    label("loc_52E")


    ChrTalk(    #1
        0x8,
        (
            "#602F雾确实比昨天\x01",
            "更加浓了。\x02\x03",

            "艾丝蒂尔你们去\x01",
            "疏导市民避难吧。\x02\x03",

            "王国军的警备部队\x01",
            "也要来了。\x01",
            "离城市较远的人们还没有防备，\x02\x03",

            "请将他们疏导\x01",
            "到安全场所吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5CB")

    Jump("loc_6AF")

    label("loc_5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_6AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_61E")

    ChrTalk(    #2
        0x8,
        (
            "#602F雾确实比昨天\x01",
            "更加浓了。\x02\x03",

            "要出城的话\x01",
            "可一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AF")

    label("loc_61E")


    ChrTalk(    #3
        0x8,
        (
            "#602F噢，是艾丝蒂尔吗。\x01",
            "这么早就开始工作，真辛苦啊。\x02\x03",

            "雾确实比昨天\x01",
            "更加浓了。\x02\x03",

            "如果要出城的话\x01",
            "一定要小心啊。\x02\x03",

            "雾很浓，\x01",
            "什么东西都看不清楚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AF")

    TalkEnd(0x8)
    Return()

    # Function_4_4A6 end

    def Function_5_6B3(): pass

    label("Function_5_6B3")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_729")

    ChrTalk(    #4
        0xFE,
        (
            "阿斯顿队长是个了不起的军人，\x01",
            "但也有洛克那种部下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "呼，我完全可以体会\x01",
            "阿斯顿队长的辛劳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB")

    label("loc_729")


    ChrTalk(    #6
        0xFE,
        (
            "阿斯顿队长是个了不起的军人，\x01",
            "但也有洛克那种部下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "……真是的，身为士兵\x01",
            "却完全没有自觉性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "呼，我完全可以体会\x01",
            "阿斯顿队长的辛劳。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_7BB")

    Jump("loc_819")

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_819")

    ChrTalk(    #9
        0xFE,
        (
            "阿斯顿队长好像是个\x01",
            "很优秀的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "听说原来他在王都部队，\x01",
            "果然名不虚传啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_819")

    TalkEnd(0x9)
    Return()

    # Function_5_6B3 end

    def Function_6_81D(): pass

    label("Function_6_81D")

    TalkBegin(0xB)

    ChrTalk(    #11
        0xFE,
        (
            "有商品要\x01",
            "送来市长的宅邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "虽然事情已经结束了，\x01",
            "但院子很漂亮……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "虽然必须要快回到店里去，\x01",
            "但却不由自主的想多留一会儿呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_6_81D end

    SaveToFile()

Try(main)
