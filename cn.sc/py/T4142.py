from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4142   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4142.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '巴拉尔',                               # 9
        '科蕾蒂',                               # 10
        '彭萨',                                 # 11
        '奈尔',                                 # 12
        '诺蒂亚',                               # 13
        '法尔茨',                               # 14
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01023 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01143 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01023P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01143P._CP',             # 05
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
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
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
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
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -64450,
        Z                   = 0,
        Y                   = 60580,
        Direction           = 1,
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
        X                   = -53860,
        Z                   = 250,
        Y                   = 121340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -59030,
        Z                   = 100,
        Y                   = 59540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1E3",          # 01, 1
        "Function_2_1F5",          # 02, 2
        "Function_3_1FA",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_3B2",          # 05, 5
        "Function_6_5D3",          # 06, 6
        "Function_7_6BC",          # 07, 7
        "Function_8_8FB",          # 08, 8
        "Function_9_94D",          # 09, 9
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Return()

    # Function_0_1E2 end

    def Function_1_1E3(): pass

    label("Function_1_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F4")

    Return()

    # Function_1_1E3 end

    def Function_2_1F5(): pass

    label("Function_2_1F5")

    Call(0, 3)
    Return()

    # Function_2_1F5 end

    def Function_3_1FA(): pass

    label("Function_3_1FA")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                               # 0
            "买东西\x01",                             # 1
            "招牌菜『完熟咖喱饭』　900米拉\x01",      # 2
            "离开\x01",                               # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCB)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_279")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_34E")
    SubMira(900)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06\x07\x02完熟咖喱饭\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x640)
    OP_31(0x1, 0xFD, 0x640)
    OP_31(0x2, 0xFD, 0x640)
    OP_31(0x3, 0xFD, 0x640)
    OP_31(0x4, 0xFD, 0x640)
    OP_31(0x5, 0xFD, 0x640)
    OP_31(0x6, 0xFD, 0x640)
    OP_31(0x7, 0xFD, 0x640)
    OP_31(0x8, 0xFD, 0x640)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_340")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xB)"), scpexpr(EXPR_END)), "loc_316")
    Jump("loc_340")

    label("loc_316")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x02完熟咖喱饭\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_340")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_374")

    label("loc_34E")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_374")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x8)
    Return()

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A0")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_3A0")

    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    # Function_3_1FA end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    Call(0, 5)
    Return()

    # Function_4_3AD end

    def Function_5_3B2(): pass

    label("Function_5_3B2")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                            # 0
            "买东西\x01",                          # 1
            "招牌菜『热海汁』　1200米拉\x01",      # 2
            "离开\x01",                            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCA)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_42E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_533")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4FB")
    SubMira(1200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #3
        "\x06\x07\x02热海汁\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x9C4)
    OP_31(0x1, 0xFD, 0x9C4)
    OP_31(0x2, 0xFD, 0x9C4)
    OP_31(0x3, 0xFD, 0x9C4)
    OP_31(0x4, 0xFD, 0x9C4)
    OP_31(0x5, 0xFD, 0x9C4)
    OP_31(0x6, 0xFD, 0x9C4)
    OP_31(0x7, 0xFD, 0x9C4)
    OP_31(0x8, 0xFD, 0x9C4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x2)"), scpexpr(EXPR_END)), "loc_4C7")
    Jump("loc_4ED")

    label("loc_4C7")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #4
        "\x06\x07\x02热海汁\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_4ED")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_521")

    label("loc_4FB")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_521")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x9)
    Return()

    label("loc_533")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D")
    FadeToBright(300, 0)
    TalkEnd(0x9)
    Return()

    label("loc_54D")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_58D")

    ChrTalk(    #6
        0x9,
        "……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "刚才有没有听见\x01",
            "外面有鸟叫？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CF")

    label("loc_58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_5CF")

    ChrTalk(    #8
        0x9,
        "好了，忙的时间也过去了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "得准备明天的\x01",
            "工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF")

    TalkEnd(0x9)
    Return()

    # Function_5_3B2 end

    def Function_6_5D3(): pass

    label("Function_6_5D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_620")

    ChrTalk(    #10
        0xFE,
        (
            "好，回家\x01",
            "洗个澡吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "一天的紧绷还是要\x01",
            "靠洗澡来消除啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B8")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_6B8")

    ChrTalk(    #12
        0xFE,
        (
            "对了，我在港口工作的\x01",
            "朋友告诉我一些奇怪的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "好像说本来应该没人的仓库\x01",
            "却每晚都发出声音来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "难道……\x01",
            "难道是幽灵！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "怕怕……\x02",
    )

    CloseMessageWindow()

    label("loc_6B8")

    TalkEnd(0xFE)
    Return()

    # Function_6_5D3 end

    def Function_7_6BC(): pass

    label("Function_7_6BC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A8")

    ChrTalk(    #16
        0xB,
        "#143F哟，什么什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1002F奈尔，这附近没\x01",
            "发生什么怪事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        (
            "#140F怪事……\x01",
            "是说什么案子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1002F嗯，比如有什么骚动\x01",
            "或者什么可疑的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "#142F唔～没看到什么\x01",
            "可疑的人。\x02\x03",

            "如果有什么骚动，我们的人\x01",
            "也应该早已听说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1003F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "#143F……你是不是碰到了什么问题？\x02\x03",

            "#141F那我也一起去。\x02\x03",

            "我马上准备一下，\x01",
            "在一楼的大厅等我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1000F啊，嗯、嗯。\x01",
            "不过要快一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "#143F什么？原来是紧急情况啊？\x02\x03",

            "#140F那么\x01",
            "你们赶快先去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1002F嗯，抱歉。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x164A)
    Jump("loc_8F7")

    label("loc_8A8")


    ChrTalk(    #26
        0xB,
        (
            "#140F现场在西街区附近吧？\x02\x03",

            "我一准备好\x01",
            "就去追你们。\x02\x03",

            "你们现在就\x01",
            "赶快先去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F7")

    TalkEnd(0xB)
    Return()

    # Function_7_6BC end

    def Function_8_8FB(): pass

    label("Function_8_8FB")

    TalkBegin(0xFE)

    ChrTalk(    #27
        0xFE,
        (
            "在这种时候只有记者还全体\x01",
            "坚守岗位，真悲哀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "不过这工作很有意义。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_8FB end

    def Function_9_94D(): pass

    label("Function_9_94D")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        "啊～好想快点回家吃饭哟～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_94D end

    SaveToFile()

Try(main)
