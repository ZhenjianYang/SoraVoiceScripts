from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4202   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4202.x',
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
        '艾莉茜雅女王',                         # 9
        '基库',                                 # 10
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02323 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02323P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 2090,
        TriggerZ            = 12000,
        TriggerY            = 67030,
        TriggerRange        = 1000,
        ActorX              = 5244,
        ActorZ              = -10900,
        ActorY              = 81768,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1920,
        TriggerZ            = 12000,
        TriggerY            = 58790,
        TriggerRange        = 4700,
        ActorX              = 1920,
        ActorZ              = 12000,
        ActorY              = 60790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_1E7",          # 02, 2
        "Function_3_1FD",          # 03, 3
        "Function_4_671",          # 04, 4
        "Function_5_A52",          # 05, 5
        "Function_6_A8F",          # 06, 6
        "Function_7_ACC",          # 07, 7
        "Function_8_B09",          # 08, 8
        "Function_9_B46",          # 09, 9
        "Function_10_B5B",         # 0A, 10
        "Function_11_B70",         # 0B, 11
        "Function_12_B85",         # 0C, 12
        "Function_13_B9A",         # 0D, 13
        "Function_14_C85",         # 0E, 14
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_14C")
    Jump("loc_173")

    label("loc_14C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_156")
    Jump("loc_173")

    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_173")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1800, 12000, 67020, 0)

    label("loc_173")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_17F"),
        (SWITCH_DEFAULT, "loc_197"),
    )


    label("loc_17F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_194")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_194")

    Jump("loc_197")

    label("loc_197")

    Return()

    # Function_0_142 end

    def Function_1_198(): pass

    label("Function_1_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AB")
    OP_82(0x80, 0x0)
    OP_64(0x0, 0x1)

    label("loc_1AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D1")
    OP_B1("t4202_y")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    Jump("loc_1DA")

    label("loc_1D1")

    OP_B1("t4202_n")

    label("loc_1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6")
    OP_64(0x1, 0x1)

    label("loc_1E6")

    Return()

    # Function_1_198 end

    def Function_2_1E7(): pass

    label("Function_2_1E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1E7")

    label("loc_1FC")

    Return()

    # Function_2_1E7 end

    def Function_3_1FD(): pass

    label("Function_3_1FD")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_616")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x8,
        (
            "#097F科洛蒂娅，还有\x01",
            "艾丝蒂尔你们……\x02\x03",

            "#090F关于凯诺娜小姐的事\x01",
            "我已经听尤莉亚报告了。\x02\x03",

            "本来她的事\x01",
            "是我应该应对的问题。\x02\x03",

            "艾丝蒂尔小姐，还有诸位，\x01",
            "给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1025F没、没有……\x02\x03",

            "#1000F而且玲……这次的罪犯\x01",
            "也和我有关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#094F嗯，我听说了……\x02\x03",

            "#092F听说这么小的\x01",
            "孩子也是结社的一员\x01",
            "老实说我也很吃惊。\x02\x03",

            "她和巨大机器人的存在\x01",
            "很可能招致市民的混乱，\x01",
            "所以我想先封锁这一消息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3DF")

    ChrTalk(    #3
        0x106,
        (
            "#050F虽然有点不舒服，\x01",
            "不过还是这样比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_418")

    label("loc_3DF")


    ChrTalk(    #4
        0x103,
        (
            "#020F说实话，虽然\x01",
            "有点不舒服，\x01",
            "不过还是这样比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_418")


    ChrTalk(    #5
        0x105,
        (
            "#042F嗯，稍有不慎\x01",
            "也有可能引发\x01",
            "大的国际影响……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1004F这、这么严重啊……\x02\x03",

            "#1009F果然下次见到玲\x01",
            "一定要严肃教育。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#094F对他们的搜查就交给\x01",
            "摩尔根将军和卡西乌斯先生吧。\x02\x03",

            "我也要以我的方式\x01",
            "我们要尽自己所能。\x02\x03",

            "#090F当前我们必须保证\x01",
            "签字仪式的顺利进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1000F女王陛下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#090F艾丝蒂尔，你的担子\x01",
            "也不轻，请努力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1018F是！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(    #11
        0x8,
        "#094F另外……科洛蒂娅。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        "#040F……在。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#090F我期待着你不久之后\x01",
            "会给出的答案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        "#042F是，祖母大人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "#090F那么各位请多加小心。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1651)
    Jump("loc_66D")

    label("loc_616")


    ChrTalk(    #16
        0x8,
        (
            "#090F艾丝蒂尔小姐的担子\x01",
            "虽然辛苦，也请你们多多努力。\x02\x03",

            "科洛蒂娅就拜托\x01",
            "你们照顾了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66D")

    TalkEnd(0x8)
    Return()

    # Function_3_1FD end

    def Function_4_671(): pass

    label("Function_4_671")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 2000, 12000, 67000, 180)
    SetChrPos(0x9, 1110, 12500, 67800, 180)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_6D(2480, 12000, 54000, 0)
    OP_67(0, 10780, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0x108, 0x1, 0x0, 0x8)
    Sleep(100)
    OP_43(0x104, 0x1, 0x0, 0x7)
    FadeToBright(2000, 0)
    WaitChrThread(0x108, 0x1)
    OP_0D()

    NpcTalk(    #17
        0x8,
        "老年妇女的声音",
        (
            "呵呵……\x01",
            "终于来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1004F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        "#044F#6P祖母大人……？\x02",
    )

    CloseMessageWindow()

    def lambda_78C():
        OP_6D(2130, 12000, 66280, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_78C)

    def lambda_7A4():
        OP_67(0, 6260, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A4)

    def lambda_7BC():
        OP_6B(2610, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7BC)

    def lambda_7CC():
        OP_6E(279, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_7CC)
    Sleep(1500)
    OP_43(0x101, 0x0, 0x0, 0x9)
    Sleep(200)
    OP_43(0x105, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_43(0x108, 0x0, 0x0, 0xC)
    Sleep(100)
    OP_43(0x104, 0x0, 0x0, 0xB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #20
        0x9,
        "#311F#1P啾～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1004F#4P咦？基库？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x105,
        (
            "#047F原来如此……\x02\x03",

            "#048F呵呵，基库知道\x01",
            "我们来了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#091F#5P嗯，是它告诉我\x01",
            "你们来了。\x02\x03",

            "#090F欢迎回来，科洛蒂娅。\x02\x03",

            "还有艾丝蒂尔小姐……\x01",
            "谢谢你们能来。\x02\x03",

            "#094F情况我已经从卡西乌斯\x01",
            "先生那里听说了。\x02\x03",

            "真是……发生了不少事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1026F#4P啊……\x02\x03",

            "#1016F嘿嘿，非常感谢您\x01",
            "对我们的担心。\x02\x03",

            "#1006F不过我也找到了前进方向，\x01",
            "科洛丝她们也帮了不少忙。\x02\x03",

            "所以，我没事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#094F#5P是吗……\x02\x03",

            "#090F呵呵，一段时间不见，\x01",
            "你真是变得可靠了。\x02\x03",

            "也欢迎奥利维尔先生\x01",
            "和金先生。\x02\x03",

            "#091F请回房间吧。\x01",
            "红茶已经准备好了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4230   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_4_671 end

    def Function_5_A52(): pass

    label("Function_5_A52")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2740, 12000, 49900, 0)

    def lambda_A6E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A6E)
    OP_8E(0xFE, 0xA3C, 0x2EE0, 0xD2F0, 0x7D0, 0x0)
    Return()

    # Function_5_A52 end

    def Function_6_A8F(): pass

    label("Function_6_A8F")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1630, 12000, 49890, 0)

    def lambda_AAB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AAB)
    OP_8E(0xFE, 0x65E, 0x2EE0, 0xD2F0, 0x7D0, 0x0)
    Return()

    # Function_6_A8F end

    def Function_7_ACC(): pass

    label("Function_7_ACC")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1650, 12000, 49050, 0)

    def lambda_AE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE8)
    OP_8E(0xFE, 0x636, 0x2EE0, 0xCEA4, 0x7D0, 0x0)
    Return()

    # Function_7_ACC end

    def Function_8_B09(): pass

    label("Function_8_B09")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2730, 12000, 49060, 0)

    def lambda_B25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B25)
    OP_8E(0xFE, 0xA3C, 0x2EE0, 0xCEA4, 0x7D0, 0x0)
    Return()

    # Function_8_B09 end

    def Function_9_B46(): pass

    label("Function_9_B46")

    OP_8E(0xFE, 0x9C4, 0x2EE0, 0xFE4B, 0xBB8, 0x0)
    Return()

    # Function_9_B46 end

    def Function_10_B5B(): pass

    label("Function_10_B5B")

    OP_8E(0xFE, 0x528, 0x2EE0, 0xFE4B, 0xBB8, 0x0)
    Return()

    # Function_10_B5B end

    def Function_11_B70(): pass

    label("Function_11_B70")

    OP_8E(0xFE, 0x4D8, 0x2EE0, 0xF8F2, 0xBB8, 0x0)
    Return()

    # Function_11_B70 end

    def Function_12_B85(): pass

    label("Function_12_B85")

    OP_8E(0xFE, 0x992, 0x2EE0, 0xF8CA, 0xBB8, 0x0)
    Return()

    # Function_12_B85 end

    def Function_13_B9A(): pass

    label("Function_13_B9A")

    EventBegin(0x1)

    ChrTalk(    #26
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_BC6():
        OP_6D(-2750, 12000, 67810, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BC6)

    def lambda_BDE():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BDE)

    def lambda_BEE():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_BEE)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C75")
    OP_C0(0xE, 0x2E, 0x852, 0x2EE0, 0x105D6, 0x168, 0x147C, 0xFFFFD56C, 0x13F68)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_C84")

    label("loc_C75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C84")
    EventEnd(0x1)

    label("loc_C84")

    Return()

    # Function_13_B9A end

    def Function_14_C85(): pass

    label("Function_14_C85")

    OP_8C(0x0, 0, 0)
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    OP_8C(0x3, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400CE, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_14_C85 end

    SaveToFile()

Try(main)
