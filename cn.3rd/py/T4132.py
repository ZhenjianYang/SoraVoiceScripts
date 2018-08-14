from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4132   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4132.x',
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
        '福立兹',                               # 9
        '尼尔森',                               # 10
        '',                                     # 11
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
    )

    DeclNpc(
        X                   = 6940,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 166,
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
        X                   = -24500,
        Z                   = 0,
        Y                   = 113310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 7060,
        TriggerZ            = 0,
        TriggerY            = 1700,
        TriggerRange        = 800,
        ActorX              = 6940,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 4890,
        TriggerRange        = 800,
        ActorX              = 7000,
        ActorZ              = 1000,
        ActorY              = 4890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_143",          # 01, 1
        "Function_2_14D",          # 02, 2
        "Function_3_152",          # 03, 3
        "Function_4_245",          # 04, 4
        "Function_5_602",          # 05, 5
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Return()

    # Function_0_142 end

    def Function_1_143(): pass

    label("Function_1_143")

    OP_B1("t4132_n")
    Return()

    # Function_1_143 end

    def Function_2_14D(): pass

    label("Function_2_14D")

    Call(0, 3)
    Return()

    # Function_2_14D end

    def Function_3_152(): pass

    label("Function_3_152")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C1")

    ChrTalk(    #0
        0x10,
        (
            "前几天有一些\x01",
            "穿黑衣的人来过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "好像是在找人呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "唔，有点不放心啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_223")

    label("loc_1C1")


    ChrTalk(    #3
        0x10,
        "哦？客人，要住店吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "十分抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "本酒店的入住手续\x01",
            "是从三点以后开始办理的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_223")

    Jump("loc_241")

    label("loc_226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_230")
    Jump("loc_241")

    label("loc_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_23A")
    Jump("loc_241")

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_241")

    label("loc_241")

    TalkEnd(0x10)
    Return()

    # Function_3_152 end

    def Function_4_245(): pass

    label("Function_4_245")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_5E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EB, 1)), scpexpr(EXPR_END)), "loc_3C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D4")

    ChrTalk(    #6
        0xFE,
        (
            "这么说来，\x01",
            "刚才有一些奇怪的男人来过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "感觉好像很凶恶……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "……不，不会吧………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BD")

    label("loc_2D4")


    ChrTalk(    #9
        0xFE,
        (
            "我和别人\x01",
            "约在这里见面。\x02",
        )
    )

    Jump("loc_303")

    label("loc_303")

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "顺便也打算\x01",
            "在利贝尔采访一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "因为利贝尔王国\x01",
            "可是以击退强国埃雷波尼亚\x01",
            "而闻名的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "其『底蕴』\x01",
            "到底在哪里呢…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "呵呵，我很有兴趣。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3BD")

    Jump("loc_5E0")

    label("loc_3C0")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #14
        0xFE,
        "哦，你们是……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    Sleep(300)

    ChrTalk(    #15
        0xFE,
        (
            "这脚步声我没听过。\x01",
            "是第一次见面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        (
            "#1643F嗯、嗯。\x01",
            "应该是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x151,
        (
            "#1653F请问，难道说……\x02\x03",

            "#1650F您的眼睛\x01",
            "不方便吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "嗯嗯，正是这样。\x01",
            "我双目完全失明了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "不过……真是有趣的组合啊。\x01",
            "其中一位是游击士吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0xFE,
        (
            "哈哈，我知道的。\x01",
            "感觉很像我认识的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "失去了光芒，\x01",
            "反而能清楚地看到原本看不见的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x103,
        "#1643F哎～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x151,
        "#1650F是这样吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F59)

    label("loc_5E0")

    Jump("loc_5FE")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_5ED")
    Jump("loc_5FE")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_5F7")
    Jump("loc_5FE")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_5FE")

    label("loc_5FE")

    TalkEnd(0xFE)
    Return()

    # Function_4_245 end

    def Function_5_602(): pass

    label("Function_5_602")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #24
        (
            "\x07\x05　　　　　　　事务室\x01",
            "※无关人员请勿入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_602 end

    SaveToFile()

Try(main)
