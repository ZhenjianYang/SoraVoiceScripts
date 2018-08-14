from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2811   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2811.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '德波拉',                               # 9
        '利库斯',                               # 10
        '露西',                                 # 11
        '目标用照相机',                         # 12
        '',                                     # 13
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
        'ED6_DT07/CH01130 ._CH',             # 00
        'ED6_DT26/CH20783 ._CH',             # 01
        'ED6_DT07/CH02690 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01130P._CP',             # 00
        'ED6_DT26/CH20783P._CP',             # 01
        'ED6_DT07/CH02690P._CP',             # 02
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
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
        X                   = -4900,
        Z                   = 140,
        Y                   = -4650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 30860,
        Z                   = 0,
        Y                   = 57160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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


    DeclActor(
        TriggerX            = 29620,
        TriggerZ            = 0,
        TriggerY            = 60000,
        TriggerRange        = 1000,
        ActorX              = 29620,
        ActorZ              = 1500,
        ActorY              = 60000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_1A6",          # 01, 1
        "Function_2_1A7",          # 02, 2
        "Function_3_324",          # 03, 3
        "Function_4_329",          # 04, 4
        "Function_5_3F4",          # 05, 5
        "Function_6_4C0",          # 06, 6
        "Function_7_718",          # 07, 7
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_1A5")

    Return()

    # Function_0_18A end

    def Function_1_1A6(): pass

    label("Function_1_1A6")

    Return()

    # Function_1_1A6 end

    def Function_2_1A7(): pass

    label("Function_2_1A7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_30E")

    label("loc_1CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E5")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_30E")

    label("loc_1E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_30E")

    label("loc_1FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_217")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_30E")

    label("loc_217")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_30E")

    label("loc_230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_30E")

    label("loc_249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_30E")

    label("loc_262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_30E")

    label("loc_27B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_30E")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_30E")

    label("loc_2AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_30E")

    label("loc_2C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_30E")

    label("loc_2DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_30E")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_30E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_323")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_30E")

    label("loc_323")

    Return()

    # Function_2_1A7 end

    def Function_3_324(): pass

    label("Function_3_324")

    Call(0, 4)
    Return()

    # Function_3_324 end

    def Function_4_329(): pass

    label("Function_4_329")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_3F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_393")

    ChrTalk(    #0
        0x10,
        (
            "感觉\x01",
            "看起来没什么精神嘛。\x02",
        )
    )

    Jump("loc_360")

    label("loc_360")

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "我们这里开到很晚的，\x01",
            "肚子饿了就来吃吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F0")

    label("loc_393")


    ChrTalk(    #2
        0x10,
        (
            "今天学生会的孩子们\x01",
            "好像待到很晚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "我们这里开到很晚的。\x01",
            "肚子饿了就来吃吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3F0")

    TalkEnd(0x10)
    Return()

    # Function_4_329 end

    def Function_5_3F4(): pass

    label("Function_5_3F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_4BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44B")

    ChrTalk(    #4
        0xFE,
        (
            "这么低的价格就\x01",
            "能品尝到美味的饭菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "当学生也不错呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BC")

    label("loc_44B")


    ChrTalk(    #6
        0xFE,
        (
            "（嚼嚼……）\x01",
            "………嗯，美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "上课之后午睡了一下\x01",
            "结果完全睡过头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "现在正要去吃晚饭呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_4BC")

    TalkEnd(0xFE)
    Return()

    # Function_5_3F4 end

    def Function_6_4C0(): pass

    label("Function_6_4C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 2)), scpexpr(EXPR_END)), "loc_52D")

    ChrTalk(    #9
        0x12,
        (
            "#1790F已经进入宵禁时间了呢。\x02\x03",

            "科洛丝，\x01",
            "你也早点回去为好。\x02",
        )
    )

    Jump("loc_529")

    label("loc_529")

    CloseMessageWindow()
    Jump("loc_714")

    label("loc_52D")


    ChrTalk(    #10
        0x105,
        (
            "#043F啊，露西学姐……\x02\x03",

            "一直工作到\x01",
            "这么晚吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "#1790F嗯嗯，稍微拖久了点……\x02\x03",

            "刚刚才做完。\x01",
            "得赶快回去才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        "#049F啊，是…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x12,
        (
            "#1792F科洛丝，怎么了？\x02\x03",

            "好像没什么精神……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        (
            "#047F不…………\x01",
            "没什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x12,
        (
            "#1794F…………是吗……\x02\x03",

            "#1790F宵禁时间已经开始了\x01",
            "你也早点回去才是哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x105,
        (
            "#043F是…………\x02\x03",

            "#049F（不过，现在…………\x01",
            "  ……我不想回去……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F7A)

    label("loc_714")

    TalkEnd(0xFE)
    Return()

    # Function_6_4C0 end

    def Function_7_718(): pass

    label("Function_7_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_79E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "爬上屋顶看看\x01",      # 0
            "不上去\x01",            # 1
        )
    )

    Jump("loc_75F")

    label("loc_75F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79B")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2800   ._SN", 130, 0, 0)
    IdleLoop()
    Jump("loc_79B")

    label("loc_79B")

    Jump("loc_834")

    label("loc_79E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05窗外有根绳子垂下。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #18
        0x105,
        (
            "#047F…………………………\x02\x03",

            "这个好像一直\x01",
            "延伸到屋顶上呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_834")

    TalkEnd(0xFF)
    Return()

    # Function_7_718 end

    SaveToFile()

Try(main)
