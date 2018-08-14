from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4241   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4241.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        '升降梯',                               # 9
        '',                                     # 10
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 100,
        TriggerY            = -60610,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 900,
        ActorY              = -60610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_EE",           # 00, 0
        "Function_1_120",          # 01, 1
        "Function_2_133",          # 02, 2
        "Function_3_8ED",          # 03, 3
        "Function_4_914",          # 04, 4
        "Function_5_940",          # 05, 5
        "Function_6_96C",          # 06, 6
        "Function_7_998",          # 07, 7
        "Function_8_9AB",          # 08, 8
        "Function_9_D9D",          # 09, 9
        "Function_10_1190",        # 0A, 10
        "Function_11_14A0",        # 0B, 11
    )


    def Function_0_EE(): pass

    label("Function_0_EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_10F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F")
    Event(0, 10)

    label("loc_11F")

    Return()

    # Function_0_EE end

    def Function_1_120(): pass

    label("Function_1_120")

    OP_B1("U4241_1")
    OP_10(0x1, 0x0)
    OP_71(0x201, 0x0)
    ExitThread()
    Return()

    # Function_1_120 end

    def Function_2_133(): pass

    label("Function_2_133")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -780, 0, -77630, 0)
    SetChrPos(0x10F, 460, 0, -77990, 0)
    SetChrPos(0xF0, -780, 0, -77630, 0)
    SetChrPos(0xF1, 460, 0, -77990, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(160, 1350, -61500, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)

    def lambda_1F2():
        OP_6D(1100, 0, -67410, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1F2)

    def lambda_20A():
        OP_67(0, 5830, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_20A)

    def lambda_222():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_222)

    def lambda_232():
        OP_6E(280, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_232)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        (
            "#1444F#5P这里……\x01",
            "这个是升降梯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10E,
        (
            "#173F#6P是啊，\x01",
            "可以降到地下５００亚矩的遗迹……\x02\x03",

            "#178F……奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        "#1067F#5P嗯……的确。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_403")

    ChrTalk(    #3
        0x10D,
        "#270F#6P有什么不对劲的地方吗？\x02",
    )

    CloseMessageWindow()

    def lambda_362():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_362)
    Sleep(100)
    OP_8C(0x10F, 225, 400)
    Sleep(300)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #4
        0x109,
        (
            "#1063F#5P我第一次来利贝尔的时候，\x01",
            "是尤莉亚小姐带领我\x01",
            "到这个地方的……\x02\x03",

            "那个时候这个房间\x01",
            "并不像现在这样散乱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545")

    label("loc_403")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43E")

    ChrTalk(    #5
        0x102,
        "#1504F#6P有什么不对劲吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A1")

    label("loc_43E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_470")

    ChrTalk(    #6
        0x107,
        "#064F#6P怎、怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A1")

    label("loc_470")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A1")

    ChrTalk(    #7
        0x10B,
        "#213F#6P有什么奇怪的？\x02",
    )

    CloseMessageWindow()

    label("loc_4A1")


    def lambda_4A7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4A7)
    Sleep(100)
    OP_8C(0x10F, 225, 400)
    Sleep(300)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #8
        0x109,
        (
            "#1063F#5P我第一次来利贝尔的时候，\x01",
            "是尤莉亚小姐带领我\x01",
            "到这个地方的……\x02\x03",

            "那个时候这个房间\x01",
            "并不像现在这样散乱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_545")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F5")

    ChrTalk(    #9
        0x10E,
        (
            "#176F#6P嗯，据我所知，\x01",
            "这里在整理好之后\x01",
            "就应该被锁上了。\x02\x03",

            "#178F话说回来，\x01",
            "这种气氛……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_631")

    ChrTalk(    #10
        0x102,
        (
            "#1503F#6P简直就如同\x01",
            "政变事件那时一样……\x02\x03",

            "#1502F的确有这样的印象呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C5")

    label("loc_631")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C5")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x107,
        (
            "#065F#6P虽、虽然\x01",
            "我有些记不清了……\x02\x03",

            "不过确实和政变事件中\x01",
            "大家在这里集合的时候一样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C5")


    ChrTalk(    #12
        0x10E,
        "#176F#6P啊……我也有这样的印象。\x02",
    )

    CloseMessageWindow()
    Jump("loc_78A")

    label("loc_6F5")


    ChrTalk(    #13
        0x10E,
        (
            "#176F#6P嗯，据我所知，\x01",
            "这里在整理好之后\x01",
            "就应该被锁上了。\x02\x03",

            "#178F……话说回来……\x02\x03",

            "简直就如同政变事件的情景\x01",
            "又再现眼前一般。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78A")


    ChrTalk(    #14
        0x10F,
        (
            "#1802F#5P时光倒流……\x01",
            "是这个意思吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10E,
        (
            "#175F#6P不，就算再怎么说\x01",
            "这也是不可能的事。\x02\x03",

            "如果只是单纯搞错了还好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1063F#5P…………………………………\x02\x03",

            "#1065F……总之，\x01",
            "我们只有相信那个亡灵的引导\x01",
            "继续前进了。\x02\x03",

            "#1060F我们做好准备\x01",
            "到地下去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10E,
        "#172F#6P好……！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x271C)
    OP_28(0x2D, 0x1, 0x100)
    OP_28(0x2E, 0x4, 0x4)
    OP_28(0x2E, 0x4, 0x8)
    OP_28(0x2E, 0x1, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_133 end

    def Function_3_8ED(): pass

    label("Function_3_8ED")


    def lambda_8F3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F3)
    OP_8E(0xFE, 0xFFFFFC9A, 0x0, 0xFFFEF656, 0x7D0, 0x0)
    Return()

    # Function_3_8ED end

    def Function_4_914(): pass

    label("Function_4_914")

    Sleep(100)

    def lambda_91F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91F)
    OP_8E(0xFE, 0x280, 0x0, 0xFFFEF624, 0x7D0, 0x0)
    Return()

    # Function_4_914 end

    def Function_5_940(): pass

    label("Function_5_940")

    Sleep(900)

    def lambda_94B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_94B)
    OP_8E(0xFE, 0xFFFFFB78, 0x0, 0xFFFEEF80, 0x7D0, 0x0)
    Return()

    # Function_5_940 end

    def Function_6_96C(): pass

    label("Function_6_96C")

    Sleep(900)

    def lambda_977():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_977)
    OP_8E(0xFE, 0x78, 0x0, 0xFFFEEF26, 0x7D0, 0x0)
    Return()

    # Function_6_96C end

    def Function_7_998(): pass

    label("Function_7_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 5)), scpexpr(EXPR_END)), "loc_9A6")
    Call(0, 9)
    Jump("loc_9AA")

    label("loc_9A6")

    Call(0, 8)

    label("loc_9AA")

    Return()

    # Function_7_998 end

    def Function_8_9AB(): pass

    label("Function_8_9AB")

    EventBegin(0x0)
    Fade(500)
    SetChrBattleFlags(0x109, 0x20)
    SetChrBattleFlags(0x10F, 0x20)
    SetChrBattleFlags(0xF0, 0x20)
    SetChrBattleFlags(0xF1, 0x20)
    OP_89(0x109, -90, 100, -61250, 0)
    OP_89(0x10F, 750, 100, -62230, 0)
    OP_89(0xF0, -1230, 100, -62300, 0)
    OP_89(0xF1, -280, 100, -63320, 0)
    OP_6D(400, 100, -61120, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05要启动升降梯吗？\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9A")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "启动\x01",        # 0
            "不启动\x01",      # 1
        )
    )

    Jump("loc_ABC")

    label("loc_ABC")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AE4"),
        (SWITCH_DEFAULT, "loc_D8A"),
    )


    label("loc_AE4")

    OP_22(0x9C, 0x0, 0x64)
    OP_71(0x401, 0x0)
    ExitThread()
    Sleep(1000)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 0, 0, -62000, 0)
    OP_48()

    def lambda_B11():
        OP_67(0, 6000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B11)

    def lambda_B29():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B29)
    OP_22(0xF7, 0x0, 0x64)
    OP_22(0x68, 0x1, 0x64)

    def lambda_B43():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B43)
    Sleep(300)

    def lambda_B63():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B63)
    Sleep(500)

    def lambda_B83():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B83)
    Sleep(800)

    def lambda_BA3():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BA3)
    Sleep(1000)

    def lambda_BC3():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BC3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x10, 0xFF)
    OP_A1(0x10, 0x2)
    SetChrPos(0x10, 0, 170000, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_48()
    OP_6A(0x10)
    OP_67(0, 7410, -10000, 0)
    OP_6B(1980, 0)
    OP_6C(36000, 0)
    OP_6E(450, 0)
    OP_89(0x109, -290, 190100, 470, 0)
    OP_89(0x10F, 510, 190100, -670, 0)
    OP_89(0xF0, -1180, 190100, -570, 0)
    OP_89(0xF1, -370, 190100, -1410, 0)
    Sleep(500)

    def lambda_C99():
        OP_67(0, 11400, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C99)

    def lambda_CB1():
        OP_6B(1310, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CB1)

    def lambda_CC1():
        OP_6C(55000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CC1)

    def lambda_CD1():
        OP_6E(776, 10000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_CD1)

    def lambda_CE1():
        OP_8F(0xFE, 0x0, 0xEA60, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_CE1)
    Sleep(300)
    FadeToBright(2000, 0)
    WaitChrThread(0x10, 0x0)
    FadeToDark(2000, 0, -1)

    def lambda_D19():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_D19)
    OP_24(0x68, 0x5A)
    Sleep(400)
    OP_24(0x68, 0x55)
    Sleep(400)
    OP_24(0x68, 0x50)
    Sleep(400)
    OP_24(0x68, 0x4B)
    Sleep(400)
    OP_24(0x68, 0x46)
    Sleep(400)
    OP_24(0x68, 0x41)
    Sleep(400)
    OP_24(0x68, 0x3C)
    Sleep(400)
    OP_23(0x68)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4300   ._SN", 101, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D97")

    label("loc_D8A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D97")

    label("loc_D97")

    Jump("loc_A8B")

    label("loc_D9A")

    EventEnd(0x0)
    Return()

    # Function_8_9AB end

    def Function_9_D9D(): pass

    label("Function_9_D9D")

    EventBegin(0x0)
    Fade(500)
    SetChrBattleFlags(0x0, 0x20)
    SetChrBattleFlags(0x1, 0x20)
    SetChrBattleFlags(0x2, 0x20)
    SetChrBattleFlags(0x3, 0x20)
    OP_89(0x0, -90, 100, -61250, 0)
    OP_89(0x1, 750, 100, -62230, 0)
    OP_89(0x2, -1230, 100, -62300, 0)
    OP_89(0x3, -280, 100, -63320, 0)
    OP_6D(400, 100, -61120, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05要启动升降梯吗？\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118D")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "启动\x01",        # 0
            "不启动\x01",      # 1
        )
    )

    Jump("loc_EAE")

    label("loc_EAE")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ED6"),
        (SWITCH_DEFAULT, "loc_117D"),
    )


    label("loc_ED6")

    OP_22(0x9C, 0x0, 0x64)
    OP_71(0x401, 0x0)
    ExitThread()
    Sleep(1000)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 0, 0, -62000, 0)
    OP_48()

    def lambda_F03():
        OP_67(0, 6000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_F03)

    def lambda_F1B():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F1B)
    OP_22(0xF7, 0x0, 0x64)
    OP_22(0x68, 0x1, 0x64)

    def lambda_F35():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F35)
    Sleep(300)

    def lambda_F55():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F55)
    Sleep(500)

    def lambda_F75():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F75)
    Sleep(800)

    def lambda_F95():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F95)
    Sleep(1000)

    def lambda_FB5():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_FB5)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x0, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x10, 0xFF)
    OP_A1(0x10, 0x2)
    SetChrPos(0x10, 0, 170000, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_48()
    OP_6A(0x10)
    OP_67(0, 7410, -10000, 0)
    OP_6B(1980, 0)
    OP_6C(36000, 0)
    OP_6E(450, 0)
    OP_89(0x0, -290, 190100, 470, 0)
    OP_89(0x1, 510, 190100, -670, 0)
    OP_89(0x2, -1180, 190100, -570, 0)
    OP_89(0x3, -370, 190100, -1410, 0)
    Sleep(500)

    def lambda_108B():
        OP_67(0, 11400, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_108B)

    def lambda_10A3():
        OP_6B(1310, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10A3)

    def lambda_10B3():
        OP_6C(55000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_10B3)

    def lambda_10C3():
        OP_6E(776, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_10C3)

    def lambda_10D3():
        OP_8F(0xFE, 0x0, 0xEA60, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_10D3)
    Sleep(300)
    FadeToBright(2000, 0)
    Sleep(5000)
    FadeToDark(2000, 0, -1)

    def lambda_110B():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_110B)
    OP_24(0x68, 0x5A)
    Sleep(400)
    OP_24(0x68, 0x55)
    Sleep(400)
    OP_24(0x68, 0x50)
    Sleep(400)
    OP_24(0x68, 0x4B)
    Sleep(400)
    OP_24(0x68, 0x46)
    Sleep(400)
    OP_24(0x68, 0x41)
    Sleep(400)
    OP_24(0x68, 0x3C)
    Sleep(400)
    OP_23(0x68)
    OP_0D()
    OP_44(0x10, 0x0)
    NewScene("ED6_DT21/M4300   ._SN", 101, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_118A")

    label("loc_117D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_118A")

    label("loc_118A")

    Jump("loc_E7D")

    label("loc_118D")

    EventEnd(0x0)
    Return()

    # Function_9_D9D end

    def Function_10_1190(): pass

    label("Function_10_1190")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_A1(0x10, 0x2)
    SetChrPos(0x10, 0, 70000, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_48()
    OP_6A(0x10)
    OP_67(0, 11400, -10000, 0)
    OP_6B(1310, 0)
    OP_6C(55000, 0)
    OP_6E(776, 0)
    SetChrBattleFlags(0x0, 0x20)
    SetChrBattleFlags(0x1, 0x20)
    SetChrBattleFlags(0x2, 0x20)
    SetChrBattleFlags(0x3, 0x20)
    OP_89(0x0, -290, 90100, 470, 0)
    OP_89(0x1, 510, 90100, -670, 0)
    OP_89(0x2, -1180, 90100, -570, 0)
    OP_89(0x3, -370, 90100, -1410, 0)
    Sleep(500)

    def lambda_1260():
        OP_67(0, 7410, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1260)

    def lambda_1278():
        OP_6B(1980, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1278)

    def lambda_1288():
        OP_6C(36000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1288)

    def lambda_1298():
        OP_6E(450, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1298)
    OP_43(0x10, 0x3, 0x0, 0xB)

    def lambda_12AF():
        OP_8F(0xFE, 0x0, 0x27100, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_12AF)
    Sleep(300)
    FadeToBright(2000, 0)
    Sleep(5000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_6A(0xFF)
    OP_44(0x0, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x2)
    OP_44(0x0, 0x3)
    ClearMapFlags(0x10)
    Sleep(300)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 0, -10000, -62000, 0)
    OP_48()
    Sleep(100)
    SetChrBattleFlags(0x0, 0x20)
    SetChrBattleFlags(0x1, 0x20)
    SetChrBattleFlags(0x2, 0x20)
    SetChrBattleFlags(0x3, 0x20)
    OP_89(0x0, -90, -5100, -61450, 0)
    OP_89(0x1, 750, -5100, -62430, 0)
    OP_89(0x2, -1230, -5100, -62500, 0)
    OP_89(0x3, -280, -5100, -63520, 0)
    OP_6D(400, 100, -61120, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    def lambda_13BF():
        OP_67(0, 8000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_13BF)

    def lambda_13D7():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13D7)
    FadeToBright(1000, 0)

    def lambda_13F0():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13F0)
    Sleep(1000)

    def lambda_1410():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1410)
    Sleep(800)

    def lambda_1430():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1430)
    Sleep(600)

    def lambda_1450():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1450)
    Sleep(300)

    def lambda_1470():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1470)
    WaitChrThread(0x10, 0x1)
    OP_22(0xF7, 0x0, 0x64)
    OP_23(0x68)
    OP_72(0x401, 0x0)
    ExitThread()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_10_1190 end

    def Function_11_14A0(): pass

    label("Function_11_14A0")

    OP_22(0x68, 0x1, 0x0)
    Sleep(100)
    OP_24(0x68, 0xA)
    Sleep(100)
    OP_24(0x68, 0x14)
    Sleep(100)
    OP_24(0x68, 0x1E)
    Sleep(100)
    OP_24(0x68, 0x28)
    Sleep(100)
    OP_24(0x68, 0x32)
    Sleep(100)
    OP_24(0x68, 0x3C)
    Sleep(100)
    OP_24(0x68, 0x46)
    Sleep(100)
    OP_24(0x68, 0x50)
    Sleep(100)
    OP_24(0x68, 0x5A)
    Sleep(100)
    OP_24(0x68, 0x64)
    Return()

    # Function_11_14A0 end

    SaveToFile()

Try(main)
