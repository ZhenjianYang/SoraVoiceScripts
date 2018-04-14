from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4131   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '卡兰大主教',                           # 9
        '利瓦尔牧师',                           # 10
        '修女诺雅',                             # 11
        '希丝娜',                               # 12
        '阿加特',                               # 13
        '雪拉扎德',                             # 14
        '礼拜者',                               # 15
        '礼拜者',                               # 16
        '礼拜者',                               # 17
        '礼拜者',                               # 18
        '礼拜者',                               # 19
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
        'ED6_DT07/CH01670 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01033 ._CH',             # 03
        'ED6_DT07/CH00050 ._CH',             # 04
        'ED6_DT07/CH00020 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
        'ED6_DT07/CH01010 ._CH',             # 07
        'ED6_DT07/CH01143 ._CH',             # 08
        'ED6_DT07/CH01160 ._CH',             # 09
        'ED6_DT07/CH01220 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01670P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01033P._CP',             # 03
        'ED6_DT07/CH00050P._CP',             # 04
        'ED6_DT07/CH00020P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
        'ED6_DT07/CH01010P._CP',             # 07
        'ED6_DT07/CH01143P._CP',             # 08
        'ED6_DT07/CH01160P._CP',             # 09
        'ED6_DT07/CH01220P._CP',             # 0A
    )

    DeclNpc(
        X                   = -50,
        Z                   = 1000,
        Y                   = 20410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2870,
        Z                   = 1000,
        Y                   = 18870,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -71360,
        Z                   = 0,
        Y                   = 3640,
        Direction           = 82,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3190,
        Z                   = 150,
        Y                   = 10800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 910,
        Z                   = 0,
        Y                   = 14450,
        Direction           = 260,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 910,
        Z                   = 0,
        Y                   = 14450,
        Direction           = 260,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3890,
        Z                   = 1000,
        Y                   = 17280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2690,
        Z                   = 1000,
        Y                   = 17280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3990,
        Z                   = 150,
        Y                   = 4660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4970,
        Z                   = 0,
        Y                   = 5260,
        Direction           = 210,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -5300,
        Z                   = 0,
        Y                   = 7270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = 200,
        TriggerZ            = 1000,
        TriggerY            = 17890,
        TriggerRange        = 400,
        ActorX              = -50,
        ActorZ              = 2500,
        ActorY              = 20410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74990,
        TriggerZ            = 0,
        TriggerY            = 66030,
        TriggerRange        = 800,
        ActorX              = -74990,
        ActorZ              = 1000,
        ActorY              = 66030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_3C0",          # 01, 1
        "Function_2_3E6",          # 02, 2
        "Function_3_3EB",          # 03, 3
        "Function_4_987",          # 04, 4
        "Function_5_E22",          # 05, 5
        "Function_6_11AE",         # 06, 6
        "Function_7_1350",         # 07, 7
        "Function_8_13B6",         # 08, 8
        "Function_9_141C",         # 09, 9
        "Function_10_1527",        # 0A, 10
        "Function_11_1651",        # 0B, 11
        "Function_12_1772",        # 0C, 12
        "Function_13_186E",        # 0D, 13
        "Function_14_198A",        # 0E, 14
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2DE")
    SetChrPos(0xA, -132010, 0, 6440, 340)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_3BF")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_31B")
    SetChrPos(0xA, -132010, 0, 6440, 340)
    SetChrPos(0xE, 3250, 0, 13250, 344)
    SetChrPos(0xF, 4130, 0, 13250, 347)
    Jump("loc_3BF")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_369")
    SetChrPos(0x9, -132010, 0, 6440, 340)
    SetChrPos(0xA, -75250, 0, 3670, 275)
    SetChrPos(0xE, 3250, 0, 13250, 344)
    SetChrPos(0xF, 4130, 0, 13250, 347)
    Jump("loc_3BF")

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x9, -132010, 0, 6440, 340)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2")
    SetChrPos(0xA, -540, 0, 14500, 103)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3AD")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3B2")

    label("loc_3AD")

    ClearChrFlags(0xD, 0x80)

    label("loc_3B2")

    Jump("loc_3BF")

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3BF")
    Jump("loc_3BF")

    label("loc_3BF")

    Return()

    # Function_0_2AA end

    def Function_1_3C0(): pass

    label("Function_1_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DC")
    OP_B1("t4131_y")
    Jump("loc_3E5")

    label("loc_3DC")

    OP_B1("t4131_n")

    label("loc_3E5")

    Return()

    # Function_1_3C0 end

    def Function_2_3E6(): pass

    label("Function_2_3E6")

    Call(0, 3)
    Return()

    # Function_2_3E6 end

    def Function_3_3EB(): pass

    label("Function_3_3EB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_44B")

    ChrTalk(    #0
        0x8,
        "开始了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "很遗憾，这次的事件\x01",
            "并非女神的试练……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "……………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_983")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D")

    ChrTalk(    #3
        0x8,
        (
            "在阻止特务兵这一观点上\x01",
            "可以说他是正确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "可不管怎么说，任务\x01",
            "都是回收古代遗物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "泼出去的水\x01",
            "收不回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "虽说是迫不得已，\x01",
            "但也必须责罚他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "当然，他……\x01",
            "凯文神父应该是有思想准备的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5B2")

    label("loc_52D")


    ChrTalk(    #8
        0x8,
        (
            "在阻止特务兵这一观点上\x01",
            "可以说他是正确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "可不管怎么说，他的任务\x01",
            "都是回收古代遗物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "虽说是迫不得已，\x01",
            "但也必须责罚他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B2")

    Jump("loc_983")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_628")

    ChrTalk(    #11
        0x8,
        (
            "……穿白色礼服的少女？\x01",
            "不，没来过这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "我记得几天前有个\x01",
            "和父母一起来过的\x01",
            "女孩子是这身打扮……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_983")

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_741")

    ChrTalk(    #13
        0x8,
        (
            "刚才历史资料馆有来\x01",
            "问过关于他们发现的\x01",
            "古代遗物的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "教会确实有义务回收、\x01",
            "调查古代遗物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "教会中也确实有\x01",
            "这方面的专门组织。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "原因在于\x01",
            "教会的中立性，\x01",
            "也只能这么说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "不过资料馆收到的\x01",
            "古代遗物已经失去了力量，\x01",
            "不属于要回收的对象。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7C1")

    label("loc_741")


    ChrTalk(    #18
        0x8,
        (
            "教会确实有义务回收、\x01",
            "调查古代遗物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "教会中也确实有\x01",
            "这方面的专门组织。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "原因在于\x01",
            "教会的中立性，\x01",
            "也只能这么说了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C1")

    Jump("loc_983")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_875")

    ChrTalk(    #21
        0x8,
        (
            "这座大圣堂和利贝尔王室\x01",
            "有悠久的渊源。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "签字仪式的事儿也\x01",
            "顺势承担下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "但是教会的本质说到底都是中立的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "唯一能做的就是\x01",
            "一边向女神祈祷一边关注。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_983")

    label("loc_875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94C")
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #25
        0x8,
        (
            "哟，莫非你\x01",
            "就是那个人说的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1015F……那个人？\x02\x03",

            "#1016F我在这里应该\x01",
            "没有熟人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "呵呵，女神\x01",
            "帮助那些帮助自己的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "愿你走上正确的道路。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_983")

    label("loc_94C")


    ChrTalk(    #29
        0x8,
        (
            "女神帮助那些帮助自己的人……\x01",
            "愿你走上正确的道路。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_983")

    TalkEnd(0x8)
    Return()

    # Function_3_3EB end

    def Function_4_987(): pass

    label("Function_4_987")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4F")

    ChrTalk(    #30
        0xFE,
        (
            "刚才有两个\x01",
            "可疑的男人把给凯文\x01",
            "神父的东西放下就走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "虽然东西不大，\x01",
            "可是包装得很严实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "大主教大人要我马上\x01",
            "呈交给凯文神父，我就照办了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "里面到底是什么呢？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_AB0")

    label("loc_A4F")


    ChrTalk(    #34
        0xFE,
        (
            "刚才有两个\x01",
            "可疑的男人把给凯文\x01",
            "神父的东西放下就走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "虽然东西不大，\x01",
            "可是包装得很严实。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB0")

    Jump("loc_E1E")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B54")

    ChrTalk(    #36
        0xFE,
        (
            "关于『星杯骑士团』，\x01",
            "我也不是很了解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "就算是大主教大人也不是\x01",
            "全部都了解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "在骑士团的职务的关系下，\x01",
            "可能这样也是\x01",
            "不得已的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_BA8")

    label("loc_B54")


    ChrTalk(    #39
        0xFE,
        (
            "关于『星杯骑士团』，\x01",
            "我也不是很了解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "就算是大主教大人也不是\x01",
            "全部都了解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA8")

    Jump("loc_E1E")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_C02")

    ChrTalk(    #41
        0xFE,
        "哎呀，你好像有烦恼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "空之女神啊，请你指引\x01",
            "他们所迷失的道路吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1E")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C63")

    ChrTalk(    #43
        0xFE,
        (
            "刚才傍晚的弥撒\x01",
            "做完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "对了，我看到了\x01",
            "那个游击士，\x01",
            "是不是发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1E")

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_CFE")

    ChrTalk(    #45
        0xFE,
        (
            "这次从总部派来的那个\x01",
            "凯文神父真是个奇怪的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "作为神职者来说看上去略显轻薄，\x01",
            "我都有点担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "莫非巡回神父中有很多\x01",
            "那样的人吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1E")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB1")

    ChrTalk(    #48
        0xFE,
        (
            "前几天我去圣海姆门的时候，\x01",
            "碰到了那场地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "虽说好歹是平息了，\x01",
            "不过蔡斯的人们现在\x01",
            "应该也还抱有不安吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "因为地震毫无预兆，\x01",
            "不知何时就会发生。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_E1E")

    label("loc_DB1")


    ChrTalk(    #51
        0xFE,
        (
            "虽说好歹是平息了，\x01",
            "不过蔡斯的人们现在\x01",
            "应该也还抱有不安吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "因为地震毫无预兆，\x01",
            "不知何时就会发生。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1E")

    TalkEnd(0xFE)
    Return()

    # Function_4_987 end

    def Function_5_E22(): pass

    label("Function_5_E22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EB8")

    ChrTalk(    #53
        0xFE,
        (
            "凯文神父和大主教大人\x01",
            "说话到很晚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "后来就马上出去了……\x01",
            "还没有回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "看来这次的事大主教大人和\x01",
            "凯文神父似乎知道一些什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11AA")

    label("loc_EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_F32")

    ChrTalk(    #56
        0xFE,
        (
            "在昨晚的事件中有很多亲卫队\x01",
            "士兵受伤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "啊，空之女神爱德丝啊……\x01",
            "请保佑那些勇敢而又有气节的人们吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11AA")

    label("loc_F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_F9D")

    ChrTalk(    #58
        0xFE,
        (
            "有封信是给\x01",
            "凯文神父的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "可他本人却还没\x01",
            "返回大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "真是的……\x01",
            "到底去了哪儿呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11AA")

    label("loc_F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_1000")

    ChrTalk(    #61
        0xFE,
        (
            "刚才有游击士\x01",
            "来向我打听情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "不过已经回去了，\x01",
            "估计应该到协会了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1027")

    label("loc_1000")


    ChrTalk(    #63
        0xFE,
        (
            "那家人我记得，\x01",
            "给人很深的印象……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1027")

    Jump("loc_11AA")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D6")

    ChrTalk(    #64
        0xFE,
        (
            "上次我碰到了\x01",
            "巡回神父凯文先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "虽然大主教大人说巡回\x01",
            "神父的工作很辛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "不过凯文先生\x01",
            "完全没给人那样的印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "这工作真的很累吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_112E")

    label("loc_10D6")


    ChrTalk(    #68
        0xFE,
        (
            "虽然大主教大人说巡回\x01",
            "神父的工作很辛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "不过凯文先生\x01",
            "完全没给人那样的印象。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112E")

    Jump("loc_11AA")

    label("loc_1131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_11AA")

    ChrTalk(    #70
        0xFE,
        (
            "呼，终于\x01",
            "圣歌集的修理结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "自从修女艾伦\x01",
            "消失以后\x01",
            "我就变得很忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "希望能早点找到\x01",
            "接替她的人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AA")

    TalkEnd(0xFE)
    Return()

    # Function_5_E22 end

    def Function_6_11AE(): pass

    label("Function_6_11AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11E2")

    ChrTalk(    #73
        0xFE,
        (
            "这种时候真的该\x01",
            "向女神献上祈祷……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134C")

    label("loc_11E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1219")

    ChrTalk(    #74
        0xFE,
        (
            "空之女神啊！\x01",
            "希望这座城市能重获安宁……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134C")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1247")

    ChrTalk(    #75
        0xFE,
        "祈祷是让人心情平静的最佳方式。\x02",
    )

    CloseMessageWindow()
    Jump("loc_134C")

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(    #76
        0xFE,
        (
            "刚才历史资料馆的\x01",
            "馆长来了这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "给大主教大人看了一样东西，\x01",
            "那是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134C")

    label("loc_12A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1308")

    ChrTalk(    #78
        0xFE,
        (
            "希望互不侵犯条约能让帝国和\x01",
            "共和国的人们友好相处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "空之女神……请引导我们……\x02",
    )

    CloseMessageWindow()
    Jump("loc_134C")

    label("loc_1308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_134C")

    ChrTalk(    #80
        0xFE,
        "哎呀，你们也是来祈祷的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "空之女神永远\x01",
            "守护着我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134C")

    TalkEnd(0xFE)
    Return()

    # Function_6_11AE end

    def Function_7_1350(): pass

    label("Function_7_1350")

    TalkBegin(0xFE)

    ChrTalk(    #82
        0xC,
        (
            "#050F艾丝蒂尔，你那边的\x01",
            "询问已经结束了吗？\x02\x03",

            "我这边还要花点时间，\x01",
            "完了的话就回协会等我吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1350 end

    def Function_8_13B6(): pass

    label("Function_8_13B6")

    TalkBegin(0xFE)

    ChrTalk(    #83
        0xD,
        (
            "#020F艾丝蒂尔，你那边的\x01",
            "询问已经结束了吗？\x02\x03",

            "我这边还要花点时间，\x01",
            "完了的话就回协会等我吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_13B6 end

    def Function_9_141C(): pass

    label("Function_9_141C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1429")
    Jump("loc_1523")

    label("loc_1429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1460")

    ChrTalk(    #84
        0xFE,
        (
            "要让心情平静，\x01",
            "祈祷是最好的方式，奶奶。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1523")

    label("loc_1460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_148F")

    ChrTalk(    #85
        0xFE,
        (
            "喂，奶奶。\x01",
            "你到底在祈求些什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1523")

    label("loc_148F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C6")

    ChrTalk(    #86
        0xFE,
        (
            "彩色玻璃……\x01",
            "在夕阳下显得更加美丽。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1523")

    label("loc_14C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_14F5")

    ChrTalk(    #87
        0xFE,
        (
            "哎呀，说起来\x01",
            "这玻璃窗还真漂亮。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1523")

    label("loc_14F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1523")

    ChrTalk(    #88
        0xFE,
        (
            "喂，奶奶。\x01",
            "格兰赛尔的教堂真宽敞。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1523")

    TalkEnd(0xFE)
    Return()

    # Function_9_141C end

    def Function_10_1527(): pass

    label("Function_10_1527")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1534")
    Jump("loc_164D")

    label("loc_1534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1569")

    ChrTalk(    #89
        0xFE,
        (
            "是啊，老头子……\x01",
            "这也是女神的恩惠啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164D")

    label("loc_1569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(    #90
        0xFE,
        "呵呵，我得保密。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "因为人们说愿望\x01",
            "说出来就不灵了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164D")

    label("loc_15B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DC")

    ChrTalk(    #92
        0xFE,
        "是啊，很有幻想的美感……\x02",
    )

    CloseMessageWindow()
    Jump("loc_164D")

    label("loc_15DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1607")

    ChrTalk(    #93
        0xFE,
        (
            "老头子，这个\x01",
            "叫彩色玻璃哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164D")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_164D")

    ChrTalk(    #94
        0xFE,
        "呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "这么宽敞的地方，可以把\x01",
            "我们家都装进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164D")

    TalkEnd(0xFE)
    Return()

    # Function_10_1527 end

    def Function_11_1651(): pass

    label("Function_11_1651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_165E")
    Jump("loc_176E")

    label("loc_165E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1695")

    ChrTalk(    #96
        0xFE,
        (
            "女神啊……求你保佑我们兄弟\x01",
            "一路平安吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176E")

    label("loc_1695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_16CE")

    ChrTalk(    #97
        0xFE,
        (
            "……嗯，我知道了。\x01",
            "再给我一点时间好不好？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176E")

    label("loc_16CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1701")

    ChrTalk(    #98
        0xFE,
        (
            "女神啊……\x01",
            "请饶恕我弟弟的言行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176E")

    label("loc_1701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1744")

    ChrTalk(    #99
        0xFE,
        "好了，首先合上眼睛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "然后把手放在\x01",
            "胸前祈祷。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176E")

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_176E")

    ChrTalk(    #101
        0xFE,
        (
            "啊，你真是……稍微\x01",
            "老实一点！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1651 end

    def Function_12_1772(): pass

    label("Function_12_1772")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_177F")
    Jump("loc_186A")

    label("loc_177F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_17A5")

    ChrTalk(    #102
        0xFE,
        "我说，我们早点回去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_186A")

    label("loc_17A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_17ED")

    ChrTalk(    #103
        0xFE,
        (
            "你说好今天要\x01",
            "陪我玩的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "可不能在女神面前\x01",
            "撒谎哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186A")

    label("loc_17ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1824")

    ChrTalk(    #105
        0xFE,
        (
            "已经傍晚了啊……\x01",
            "弥撒真是像在上刑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186A")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_184F")

    ChrTalk(    #106
        0xFE,
        (
            "不嘛不嘛～！\x01",
            "我绝不要祈祷～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186A")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_186A")

    ChrTalk(    #107
        0xFE,
        "教堂太无聊了～\x02",
    )

    CloseMessageWindow()

    label("loc_186A")

    TalkEnd(0xFE)
    Return()

    # Function_12_1772 end

    def Function_13_186E(): pass

    label("Function_13_186E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_187B")
    Jump("loc_1986")

    label("loc_187B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_18A4")

    ChrTalk(    #108
        0xFE,
        (
            "女神，感谢您\x01",
            "保佑我们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1986")

    label("loc_18A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_18D5")

    ChrTalk(    #109
        0xFE,
        (
            "女神，今天也请您\x01",
            "保佑我们安康……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1986")

    label("loc_18D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(    #110
        0xFE,
        (
            "刚才，傍晚的弥撒\x01",
            "结束了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1986")

    label("loc_1902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1952")

    ChrTalk(    #111
        0xFE,
        (
            "大圣堂的庄严肃穆\x01",
            "真是感人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "今后是不是该\x01",
            "认真地来教堂呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1986")

    label("loc_1952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1986")

    ChrTalk(    #113
        0xFE,
        (
            "这就是格兰赛尔大圣堂……\x01",
            "果然名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1986")

    TalkEnd(0xFE)
    Return()

    # Function_13_186E end

    def Function_14_198A(): pass

    label("Function_14_198A")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #114
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_198A end

    SaveToFile()

Try(main)
