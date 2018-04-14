from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4134   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4134.x',
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
        '修女艾伦',                             # 9
        '卡兰大主教',                           # 10
        '利瓦尔牧师',                           # 11
        '修女诺雅',                             # 12
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
        'ED6_DT07/CH01410 ._CH',             # 00
        'ED6_DT07/CH01400 ._CH',             # 01
        'ED6_DT07/CH01670 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01410P._CP',             # 00
        'ED6_DT07/CH01400P._CP',             # 01
        'ED6_DT07/CH01670P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -50,
        Z                   = 1000,
        Y                   = 20410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -132010,
        Z                   = 0,
        Y                   = 6440,
        Direction           = 340,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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


    ScpFunction(
        "Function_0_166",          # 00, 0
        "Function_1_167",          # 01, 1
        "Function_2_179",          # 02, 2
        "Function_3_17E",          # 03, 3
        "Function_4_3B4",          # 04, 4
        "Function_5_3FC",          # 05, 5
    )


    def Function_0_166(): pass

    label("Function_0_166")

    Return()

    # Function_0_166 end

    def Function_1_167(): pass

    label("Function_1_167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_178")

    Return()

    # Function_1_167 end

    def Function_2_179(): pass

    label("Function_2_179")

    Call(0, 3)
    Return()

    # Function_2_179 end

    def Function_3_17E(): pass

    label("Function_3_17E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D")
    TurnDirection(0x9, 0x109, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x9,
        "这不是凯文神父吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        "半夜三更的，有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1060F大主教，这附近\x01",
            "有什么异样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        "？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "不，没发生什么\x01",
            "怪事啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #5
        0x109,
        (
            "#1063F呼，艾丝蒂尔。\x01",
            "看来不在这一带……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #6
        0x101,
        "#1002F嗯、嗯。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x9, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #7
        0x9,
        (
            "对了，凯文神父，\x01",
            "在那份报告中提及的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1064F啊，不好意思。\x02\x03",

            "#1066F现在有点紧急情况，\x01",
            "我正在赶时间。\x02\x03",

            "关于那件事的详细内容，\x01",
            "我以后再向你汇报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "唔，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "那你就小心行事吧。\x01",
            "愿你们走在正确的道路上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        "#1062F多谢！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1645)
    Jump("loc_3B0")

    label("loc_38D")


    ChrTalk(    #12
        0x9,
        (
            "怎么了？\x01",
            "你们不是在赶时间吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0")

    TalkEnd(0x9)
    Return()

    # Function_3_17E end

    def Function_4_3B4(): pass

    label("Function_4_3B4")

    TalkBegin(0xFE)

    ChrTalk(    #13
        0xFE,
        (
            "还要准备签字仪式，\x01",
            "今天会开门到很晚哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "有什么困扰吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_3B4 end

    def Function_5_3FC(): pass

    label("Function_5_3FC")

    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        (
            "……修女的一天\x01",
            "始于祈祷，终于祈祷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "早晚的祈祷都\x01",
            "各要进行２小时哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "啊，空之女神啊，\x01",
            "今天也很顺利……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_3FC end

    SaveToFile()

Try(main)
