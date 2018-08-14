from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3132   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3132.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '玛尔奇娜主管',                         # 9
        '艾玛',                                 # 10
        '东杰',                                 # 11
        '',                                     # 12
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
        'ED6_DT07/CH01210 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01210 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01210P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01210P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
    )

    DeclNpc(
        X                   = -1700,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 192,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 68290,
        Z                   = 0,
        Y                   = 91600,
        Direction           = 90,
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
        X                   = 68100,
        Z                   = 0,
        Y                   = 56310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -1290,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = -1700,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4000,
        TriggerZ            = 0,
        TriggerY            = 4000,
        TriggerRange        = 800,
        ActorX              = -4000,
        ActorZ              = 1000,
        ActorY              = 4000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_18E",          # 01, 1
        "Function_2_18F",          # 02, 2
        "Function_3_1B3",          # 03, 3
        "Function_4_1B8",          # 04, 4
        "Function_5_2EC",          # 05, 5
        "Function_6_3F3",          # 06, 6
        "Function_7_4DD",          # 07, 7
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_18D")

    Return()

    # Function_0_172 end

    def Function_1_18E(): pass

    label("Function_1_18E")

    Return()

    # Function_1_18E end

    def Function_2_18F(): pass

    label("Function_2_18F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B2")
    OP_8D(0xFE, 67200, 90290, 68610, 92730, 2000)
    Jump("Function_2_18F")

    label("loc_1B2")

    Return()

    # Function_2_18F end

    def Function_3_1B3(): pass

    label("Function_3_1B3")

    Call(0, 4)
    Return()

    # Function_3_1B3 end

    def Function_4_1B8(): pass

    label("Function_4_1B8")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_2E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_240")

    ChrTalk(    #0
        0x10,
        (
            "最近这段时间，\x01",
            "从共和国来的客人\x01",
            "好不容易有所增加……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "艾玛却是那副样子，\x01",
            "真担心会不会\x01",
            "给客人添麻烦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8")

    label("loc_240")


    ChrTalk(    #2
        0x10,
        (
            "……刚才我去\x01",
            "储物室看了一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "架子下面\x01",
            "藏了好多油灯。\x02",
        )
    )

    Jump("loc_291")

    label("loc_291")

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "……一定是艾玛干的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "真是的，\x01",
            "买那么多到底打算干什么嘛。\x02",
        )
    )

    Jump("loc_2E4")

    label("loc_2E4")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2E8")

    TalkEnd(0x10)
    Return()

    # Function_4_1B8 end

    def Function_5_2EC(): pass

    label("Function_5_2EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_34F")

    ChrTalk(    #6
        0xFE,
        (
            "就算导力灯无法使用\x01",
            "也绝对没问题……对吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "好，要努力工作哦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EF")

    label("loc_34F")


    ChrTalk(    #8
        0xFE,
        (
            "前些天，\x01",
            "导力灯怎么都点不着，\x01",
            "真是头疼呢。\x02",
        )
    )

    Jump("loc_38C")

    label("loc_38C")

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "所以我吸取教训，\x01",
            "能买多少油灯\x01",
            "就买了多少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "这下就应该可以\x01",
            "绝对放心了……对吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3EF")

    TalkEnd(0xFE)
    Return()

    # Function_5_2EC end

    def Function_6_3F3(): pass

    label("Function_6_3F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_4D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_45D")

    ChrTalk(    #11
        0xFE,
        (
            "嗯，这次应该\x01",
            "不会发生那种麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "商谈似乎\x01",
            "也进展顺利呢。\x02",
        )
    )

    Jump("loc_459")

    label("loc_459")

    CloseMessageWindow()
    Jump("loc_4D9")

    label("loc_45D")


    ChrTalk(    #13
        0xFE,
        (
            "我主要是做\x01",
            "导力器买卖的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "但是，之前来的时候\x01",
            "城里的导力都停了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "结果只好\x01",
            "空手而归了。\x02",
        )
    )

    Jump("loc_4D5")

    label("loc_4D5")

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_4D9")

    TalkEnd(0xFE)
    Return()

    # Function_6_3F3 end

    def Function_7_4DD(): pass

    label("Function_7_4DD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x05　　　　　　　储物室　　　　　　　\x01",
            "      ※非工作人员禁止入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_4DD end

    SaveToFile()

Try(main)
