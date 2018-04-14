from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2330   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2330.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2330   ._SN',
            'ED6_DT21/T2330_1 ._SN',
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
        '雷克斯',                               # 9
        '卡拉',                                 # 10
        '达里奥',                               # 11
        '奥维德',                               # 12
        '梅尔茨',                               # 13
        '王国军士兵',                           # 14
        '酒瓶',                                 # 15
        '酒瓶',                                 # 16
        '酒杯满',                               # 17
        '酒杯空',                               # 18
        '酒瓶',                                 # 19
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
        'ED6_DT07/CH01563 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01760 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT07/CH01300 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
        'ED6_DT07/CH01563P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01760P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT07/CH01300P._CP',             # 07
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 43210,
        Direction           = 270,
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
        X                   = -37500,
        Z                   = 0,
        Y                   = 44500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -37480,
        Z                   = 200,
        Y                   = 39900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 0,
        Y                   = 2330,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = -30680,
        Z                   = 0,
        Y                   = 44805,
        Direction           = 90,
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
        X                   = -2200,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 284,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -37820,
        Z                   = 750,
        Y                   = 38730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966085,
        ChipIndex           = 0x5,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37470,
        Z                   = 750,
        Y                   = 38480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966085,
        ChipIndex           = 0x5,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37530,
        Z                   = 750,
        Y                   = 39070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37260,
        Z                   = 750,
        Y                   = 38950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65542,
        ChipIndex           = 0x6,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37010,
        Z                   = 800,
        Y                   = 38560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900549,
        ChipIndex           = 0x5,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -37020,
        TriggerZ            = 0,
        TriggerY            = 42970,
        TriggerRange        = 400,
        ActorX              = -37500,
        ActorZ              = 1500,
        ActorY              = 44500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26870,
        TriggerZ            = 0,
        TriggerY            = 42820,
        TriggerRange        = 400,
        ActorX              = -25500,
        ActorZ              = 1500,
        ActorY              = 43210,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_2D6",          # 01, 1
        "Function_2_2D7",          # 02, 2
        "Function_3_2DC",          # 03, 3
        "Function_4_975",          # 04, 4
        "Function_5_97A",          # 05, 5
        "Function_6_F1E",          # 06, 6
        "Function_7_14B5",         # 07, 7
        "Function_8_1571",         # 08, 8
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C4")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_2D5")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D5")
    ClearChrFlags(0xC, 0x80)

    label("loc_2D5")

    Return()

    # Function_0_292 end

    def Function_1_2D6(): pass

    label("Function_1_2D6")

    Return()

    # Function_1_2D6 end

    def Function_2_2D7(): pass

    label("Function_2_2D7")

    Call(0, 3)
    Return()

    # Function_2_2D7 end

    def Function_3_2DC(): pass

    label("Function_3_2DC")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                 # 0
            "买东西\x01",                               # 1
            "招牌菜『魅惑海鲜烧串』　600米拉\x01",      # 2
            "离开\x01",                                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35D")
    OP_0D()
    OP_A9(0x70)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_35D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_434")
    SubMira(600)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06\x07\x02魅惑海鲜烧串\x07\x00已经品尝了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x258)
    OP_31(0x1, 0xFD, 0x258)
    OP_31(0x2, 0xFD, 0x258)
    OP_31(0x3, 0xFD, 0x258)
    OP_31(0x4, 0xFD, 0x258)
    OP_31(0x5, 0xFD, 0x258)
    OP_31(0x6, 0xFD, 0x258)
    OP_31(0x7, 0xFD, 0x258)
    OP_31(0x8, 0xFD, 0x258)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_426")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x1)"), scpexpr(EXPR_END)), "loc_3FA")
    Jump("loc_426")

    label("loc_3FA")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x02魅惑海鲜烧串\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_426")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_45A")

    label("loc_434")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_45A")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x8)
    Return()

    label("loc_46C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47D")
    TalkEnd(0x8)
    Return()

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_50C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8")

    ChrTalk(    #3
        0x8,
        (
            "受了伤的士兵\x01",
            "似乎也好多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "反正警备艇也不能飞，\x01",
            "现在还是希望他们好好休息。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_509")

    label("loc_4E8")


    ChrTalk(    #5
        0x8,
        (
            "受了伤的士兵\x01",
            "似乎也好多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_509")

    Jump("loc_971")

    label("loc_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A0")

    ChrTalk(    #6
        0x8,
        (
            "呀，欢迎。\x01",
            "欢迎光临『白之木莲亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "进货虽然困难，\x01",
            "里面还是和平时一样营业呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "因为在这种时候，\x01",
            "想帮村民的忙嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5F2")

    label("loc_5A0")


    ChrTalk(    #9
        0x8,
        (
            "进货虽然困难，\x01",
            "不过，还是尽力在营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "这还多亏在村里\x01",
            "采摘了许多食材呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F2")

    Jump("loc_971")

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 6)), scpexpr(EXPR_END)), "loc_829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_64C")

    ChrTalk(    #11
        0x8,
        (
            "这次选举\x01",
            "我们店是投票所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "承蒙大家关照\x01",
            "我们也会努力干好的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_826")

    label("loc_64C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_688")

    ChrTalk(    #13
        0x8,
        (
            "就快到是市长选举了，\x01",
            "该投票给谁呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_712")

    label("loc_688")

    OP_A2(0x0)

    ChrTalk(    #14
        0x8,
        (
            "就快到是市长选举了，\x01",
            "那么，该投票给谁呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "旅游业的发展是令人高兴，\x01",
            "不过卢安还是港口城市嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "港口萧条了\x01",
            "应该不大好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_712")

    Jump("loc_826")

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_786")

    ChrTalk(    #17
        0x8,
        (
            "呀，莫非\x01",
            "去看风车小屋了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "看了那景色的客人\x01",
            "必定会再来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "那里的风景\x01",
            "就是那么好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_826")

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7D4")

    ChrTalk(    #20
        0x8,
        (
            "要吃饭的话\x01",
            "推荐新菜单哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "在我们这里是最受欢迎了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_826")

    label("loc_7D4")

    OP_A2(0x0)

    ChrTalk(    #22
        0x8,
        (
            "欢迎光临『白之木莲亭』。\x01",
            "现在推荐新菜单哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "在我们这里是最受欢迎了。\x02",
    )

    CloseMessageWindow()

    label("loc_826")

    Jump("loc_971")

    label("loc_829")

    OP_A2(0x122E)
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #24
        0x8,
        (
            "欢迎光临『白之木莲亭』。\x01",
            "没见过的脸呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "……不过，想一想\x01",
            "又好像有见过的印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "以前来过吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1011F啊，还记得吗？\x02\x03",

            "时间比较久了，\x01",
            "以前在这里买过便当哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "哦，是这样吗。\x01",
            "那么试试新菜单怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "是我们这里现在\x01",
            "最受欢迎的料理哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1018F哟～那倒是很令人期待。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "肚子饿了的话\x01",
            "请务必试试。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_971")

    TalkEnd(0x8)
    Return()

    # Function_3_2DC end

    def Function_4_975(): pass

    label("Function_4_975")

    Call(0, 5)
    Return()

    # Function_4_975 end

    def Function_5_97A(): pass

    label("Function_5_97A")

    TalkBegin(0x9)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_997")
    OP_A9(0x6F)
    TalkEnd(0x9)
    Return()

    label("loc_997")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A8")
    TalkEnd(0x9)
    Return()

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2E")

    ChrTalk(    #32
        0x9,
        (
            "警备艇好像还在海岸\x01",
            "停靠着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        (
            "导力器不能动的话，\x01",
            "确实没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "那样的话倒不如\x01",
            "大家都来村里的好……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_A76")

    label("loc_A2E")


    ChrTalk(    #35
        0x9,
        (
            "警备艇好像还在海岸\x01",
            "停靠着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "导力器不能动的话，\x01",
            "确实没办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A76")

    Jump("loc_F1A")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0F")

    ChrTalk(    #37
        0x9,
        (
            "２楼的士兵\x01",
            "是迫降的警备艇中的成员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "村子被袭击的时候\x01",
            "是他们保护了我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "虽然伤得不重，\x01",
            "但热情招待他是理所当然的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_B59")

    label("loc_B0F")


    ChrTalk(    #40
        0x9,
        (
            "乘坐警备艇的士兵\x01",
            "保护了村子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "登上船撤退的时候\x01",
            "发生了那个现象。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B59")

    Jump("loc_F1A")

    label("loc_B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BC3")

    ChrTalk(    #42
        0x9,
        (
            "哎呀，市长官邸现在\x01",
            "不是戴尔蒙家的所有物了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "嗯～那样\x01",
            "应该联络哪里才好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C41")

    label("loc_BC3")

    OP_A2(0x1)

    ChrTalk(    #44
        0x9,
        (
            "那位客人，真的\x01",
            "是戴尔蒙家的管家吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "要是那样，得联络那里\x01",
            "前来迎接他才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "喝得那么醉，\x01",
            "一个人可回不去啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C41")

    Jump("loc_F1A")

    label("loc_C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CA6")

    ChrTalk(    #47
        0x9,
        (
            "那位客人\x01",
            "终于开始\x01",
            "说胡话了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "『我不是我！』\x01",
            "……之类的话都说出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D25")

    label("loc_CA6")

    OP_A2(0x1)

    ChrTalk(    #49
        0x9,
        (
            "那位客人\x01",
            "终于开始\x01",
            "说胡话了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "『我不是我！』什么的\x01",
            "话都说出来了，真是没救了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "呼，还是不要\x01",
            "再拿酒出来了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D25")

    Jump("loc_F1A")

    label("loc_D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D8D")

    ChrTalk(    #52
        0x9,
        (
            "那个客人这么消沉，\x01",
            "有些可怜的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "也许真的是\x01",
            "戴尔蒙家的管家也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFD")

    label("loc_D8D")

    OP_A2(0x1)

    ChrTalk(    #54
        0x9,
        (
            "嗯～那个客人。\x01",
            "有些可怜的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "自己说自己是\x01",
            "戴尔蒙家的管家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "看那个样子\x01",
            "说不定是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFD")

    Jump("loc_F1A")

    label("loc_E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E86")

    ChrTalk(    #57
        0x9,
        (
            "那边酩酊大醉的人\x01",
            "好像是戴尔蒙家的管家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "不过，那样的话\x01",
            "他说的事却很奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "喝了那么多\x01",
            "也难怪会这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1A")

    label("loc_E86")

    OP_A2(0x1)

    ChrTalk(    #60
        0x9,
        (
            "那边有个酩酊大醉的\x01",
            "客人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "那个人\x01",
            "好像是戴尔蒙家的管家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1004F咦？真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "不知道是不是真的。\x01",
            "只不过，他本人是那样说的哟。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1A")

    TalkEnd(0x9)
    Return()

    # Function_5_97A end

    def Function_6_F1E(): pass

    label("Function_6_F1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_11B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 5)), scpexpr(EXPR_END)), "loc_FAA")

    ChrTalk(    #64
        0xFE,
        (
            "呜～……抽泣……\x01",
            "那、那不是我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "屋里的女佣们看到的……\x01",
            "那、那个管家达里奥不是我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "呜呜～……抽泣……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B1")

    label("loc_FAA")

    OP_A2(0x1425)

    ChrTalk(    #67
        0xFE,
        "呜咿～……抽泣……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "呜～…………\x01",
            "那、那不是我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x105,
        (
            "#042F………………………………\x02\x03",

            "#042F（艾丝蒂尔……）\x02\x03",

            "（这位…………\x01",
            "　是戴尔蒙家的管家。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1002F（嗯……\x01",
            "是那家伙说的人吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x104,
        "#032F（唔，好像是呢。）\x02",
    )

    CloseMessageWindow()

    def lambda_1094():
        TurnDirection(0xF7, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1094)

    def lambda_10A2():
        TurnDirection(0x104, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10A2)
    TurnDirection(0x101, 0xFE, 400)
    Sleep(250)

    ChrTalk(    #72
        0xFE,
        (
            "呜呜～……那，那……\x01",
            "那不是我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "女佣们看见的我……\x01",
            "管家达里奥不是我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "呜呜～……抽泣……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1002F（……………………）\x02\x03",

            "（那家伙说的事……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1188")

    ChrTalk(    #76
        0x103,
        (
            "#022F（嗯嗯……\x01",
            "好像是真的呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B1")

    label("loc_1188")


    ChrTalk(    #77
        0x106,
        (
            "#050F（啊啊……\x01",
            "　好像不是唬人的。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B1")

    Jump("loc_14B1")

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_12AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1227")

    ChrTalk(    #78
        0xFE,
        (
            "抽泣……\x01",
            "谁、谁来听我说啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "市长官邸的那个我……\x01",
            "抽泣……不是我！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "呜～……抽泣……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_1227")

    OP_A2(0x2)

    ChrTalk(    #81
        0xFE,
        (
            "呜～……抽泣……\x01",
            "呜呜～……相信我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "市长官邸那个我……\x01",
            "抽泣……不是我！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "只、只能这样……\x01",
            "呜～……考虑了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A7")

    Jump("loc_14B1")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_13B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1334")

    ChrTalk(    #84
        0xFE,
        (
            "呜～……抽泣……\x01",
            "很、很奇怪啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "得到休假的我……\x01",
            "怎、怎么会在屋子里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "抽泣……那、那么……\x01",
            "就有两个我！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B4")

    label("loc_1334")

    OP_A2(0x2)

    ChrTalk(    #87
        0xFE,
        (
            "呜～……抽泣……\x01",
            "说、说起来很奇怪啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "我、我得到休假……\x01",
            "不在……宅邸的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "抽泣……为何大家\x01",
            "都、都说我在！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B4")

    Jump("loc_14B1")

    label("loc_13B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_14B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1430")

    ChrTalk(    #90
        0xFE,
        (
            "老……老爷被逮捕什么的……\x01",
            "肯、肯定搞错了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "我不在的时候……\x01",
            "到、到底发生了什么…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_1430")

    OP_A2(0x2)

    ChrTalk(    #92
        0xFE,
        "呜～……抽泣……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "老……老爷被逮捕什么的……\x01",
            "肯、肯定搞错了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "我不在的时候……\x01",
            "到、到底发生了什么…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B1")

    TalkEnd(0xFE)
    Return()

    # Function_6_F1E end

    def Function_7_14B5(): pass

    label("Function_7_14B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_14C2")
    Jump("loc_156D")

    label("loc_14C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_156D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_150C")

    ChrTalk(    #95
        0xFE,
        "这里的便当很好吃。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "是工作空闲时的\x01",
            "小小乐趣哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156D")

    label("loc_150C")

    OP_A2(0x3)

    ChrTalk(    #97
        0xFE,
        "啊，大家辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "我正好来这里\x01",
            "消灭通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "近来魔兽变得很强\x01",
            "说实话真是棘手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156D")

    TalkEnd(0xFE)
    Return()

    # Function_7_14B5 end

    def Function_8_1571(): pass

    label("Function_8_1571")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1696")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1639")

    ChrTalk(    #100
        0xFE,
        (
            "虽然伤势没有大碍，\x01",
            "可以返回船上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "不过宿驿的人们很亲切，\x01",
            "总觉得有点盛情难却啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "感觉因为这事故\x01",
            "体会到了自己的使命呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "这样保护人们\x01",
            "就是我们士兵的任务啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1693")

    label("loc_1639")


    ChrTalk(    #104
        0xFE,
        (
            "与宿驿的人们互相接触\x01",
            "体会到了自己的使命呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "这样保护人们\x01",
            "就是我们士兵的任务啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1693")

    Jump("loc_1780")

    label("loc_1696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172E")

    ChrTalk(    #106
        0xFE,
        (
            "航行中的警备艇全导力\x01",
            "都下降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "由于高度低\x01",
            "才偶然得救……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "由于迫降的冲击，\x01",
            "我身上青一块紫一块的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "好痛痛痛……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1780")

    label("loc_172E")


    ChrTalk(    #110
        0xFE,
        (
            "航行中的警备艇全导力\x01",
            "都下降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "由于迫降的冲击\x01",
            "我身上也是青一块紫一块。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1780")

    TalkEnd(0xD)
    Return()

    # Function_8_1571 end

    SaveToFile()

Try(main)
