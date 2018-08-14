from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4406   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4406.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        ' ',                                    # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 3500,
        Y                   = -1000,
        Z                   = -6930,
        Range               = 7780,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x177A,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = -19450,
        TriggerZ            = 0,
        TriggerY            = -15500,
        TriggerRange        = 1000,
        ActorX              = -20540,
        ActorZ              = -500,
        ActorY              = -17840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20540,
        TriggerZ            = -700,
        TriggerY            = -17840,
        TriggerRange        = 1000,
        ActorX              = -19600,
        ActorZ              = 500,
        ActorY              = -14960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23370,
        TriggerZ            = -560,
        TriggerY            = -22430,
        TriggerRange        = 1000,
        ActorX              = -23370,
        ActorZ              = 200,
        ActorY              = -22430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_1B7",          # 01, 1
        "Function_2_200",          # 02, 2
        "Function_3_811",          # 03, 3
        "Function_4_83E",          # 04, 4
        "Function_5_86B",          # 05, 5
        "Function_6_898",          # 06, 6
        "Function_7_8C5",          # 07, 7
        "Function_8_98E",          # 08, 8
        "Function_9_E1B",          # 09, 9
        "Function_10_EFF",         # 0A, 10
        "Function_11_F57",         # 0B, 11
        "Function_12_FA1",         # 0C, 12
        "Function_13_FDD",         # 0D, 13
        "Function_14_100B",        # 0E, 14
        "Function_15_10EF",        # 0F, 15
        "Function_16_1147",        # 10, 16
        "Function_17_1191",        # 11, 17
        "Function_18_11CD",        # 12, 18
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Return()

    # Function_0_1B6 end

    def Function_1_1B7(): pass

    label("Function_1_1B7")

    OP_16(0x2, 0xFA0, 0xFFFE3AE0, 0xFFFE69C0, 0x23006D)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_1E1")
    OP_B1("U4406_y")
    Jump("loc_1EA")

    label("loc_1E1")

    OP_B1("U4406_n")

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB")
    OP_72(0x1002, 0x0)
    ExitThread()
    Jump("loc_1FF")

    label("loc_1FB")

    OP_64(0x2, 0x1)

    label("loc_1FF")

    Return()

    # Function_1_1B7 end

    def Function_2_200(): pass

    label("Function_2_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 1)), scpexpr(EXPR_END)), "loc_208")
    Return()

    label("loc_208")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257")
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 225, 400)

    ChrTalk(    #0
        0x109,
        "#1079F什……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_381")

    label("loc_257")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2")
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 225, 400)

    ChrTalk(    #1
        0x10F,
        "#1444F哎……\x02",
    )

    CloseMessageWindow()
    Jump("loc_381")

    label("loc_2A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 225, 400)

    ChrTalk(    #2
        0x107,
        "#065F咦……\x02",
    )

    CloseMessageWindow()
    Jump("loc_381")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_338")
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10E, 225, 400)

    ChrTalk(    #3
        0x10E,
        "#173F哎……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_381")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381")
    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 225, 400)

    ChrTalk(    #4
        0x10D,
        "#273F嗯……？\x02",
    )

    CloseMessageWindow()

    label("loc_381")

    Sleep(300)

    def lambda_38C():
        OP_6D(-22380, 290, -22070, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_38C)

    def lambda_3A4():
        OP_67(0, 7900, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A4)

    def lambda_3BC():
        OP_6B(3070, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3BC)

    def lambda_3CC():
        OP_6C(224000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3CC)

    def lambda_3DC():
        OP_6E(420, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_3DC)
    WaitChrThread(0x109, 0x1)
    SetChrPos(0x10F, 910, 0, -55320, 0)
    SetChrPos(0xF0, -910, 0, -55370, 0)
    SetChrPos(0xF1, -20, 0, -56270, 0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Sleep(1000)

    def lambda_445():
        OP_6D(-21370, 0, -16740, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_445)

    def lambda_45D():
        OP_67(0, 5800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_45D)

    def lambda_475():
        OP_6B(3070, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_475)

    def lambda_485():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_485)

    def lambda_495():
        OP_6E(355, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_495)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FD")

    ChrTalk(    #5
        0x107,
        (
            "#065F#6P『山猫号』……\x01",
            "为什么在这里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_543")

    label("loc_4FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_543")

    ChrTalk(    #6
        0x10D,
        (
            "#270F#6P『山猫号』……\x01",
            "为什么会在这种地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_543")


    ChrTalk(    #7
        0x10F,
        (
            "#1443F#6P……果然，\x01",
            "是你们见过的飞艇呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1065F#5P是和『埃尔赛尤』一样，\x01",
            "在那个事件中登上浮游都市的\x01",
            "空贼团的飞艇……\x02\x03",

            "#1063F不过我听说\x01",
            "他们现在已经洗手不干了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_685")

    ChrTalk(    #9
        0x10E,
        (
            "#176F#6P事件之后，\x01",
            "他们受到了陛下的恩赦，\x01",
            "被无罪释放了。\x02\x03",

            "#175F现在应该是在经营\x01",
            "飞艇运输业……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_718")

    label("loc_685")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_718")

    ChrTalk(    #10
        0x10D,
        (
            "#272F#6P他们在事件之后，\x01",
            "他们受到了艾莉茜雅女王的恩赦，\x01",
            "已经是清白之身了。\x02\x03",

            "我听说他们现在\x01",
            "正在经营飞艇运输业……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_718")


    ChrTalk(    #11
        0x109,
        "#1840F#5P哈，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1446F#6P……原来如此。\x02\x03",

            "#1802F不过，这艘飞艇\x01",
            "为什么会在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1067F#5P难不成是因为\x01",
            "运输上的业务\x01",
            "而来到格兰赛尔……\x02\x03",

            "#1060F算了，\x01",
            "总之我们先进去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2709)
    OP_28(0x2C, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_200 end

    def Function_3_811(): pass

    label("Function_3_811")

    SetChrPos(0xFE, -12370, 0, -6360, 219)
    OP_8E(0xFE, 0xFFFFB5C8, 0x0, 0xFFFFCB9E, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_811 end

    def Function_4_83E(): pass

    label("Function_4_83E")

    SetChrPos(0xFE, -12390, 0, -4230, 215)
    OP_8E(0xFE, 0xFFFFB0C8, 0x0, 0xFFFFCCC0, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_83E end

    def Function_5_86B(): pass

    label("Function_5_86B")

    SetChrPos(0xFE, -10060, 0, -4480, 222)
    OP_8E(0xFE, 0xFFFFB866, 0x0, 0xFFFFD210, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_86B end

    def Function_6_898(): pass

    label("Function_6_898")

    SetChrPos(0xFE, -10090, 0, -2450, 227)
    OP_8E(0xFE, 0xFFFFB24E, 0x0, 0xFFFFD2CE, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_898 end

    def Function_7_8C5(): pass

    label("Function_7_8C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 4)), scpexpr(EXPR_END)), "loc_932")
    TalkBegin(0xFF)
    Sleep(300)
    OP_22(0x73, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05门上的锁打开了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x270D)
    OP_64(0x2, 0x1)
    OP_71(0x1002, 0x0)
    ExitThread()
    TalkEnd(0xFF)
    Jump("loc_98D")

    label("loc_932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_941")
    Call(0, 8)
    Jump("loc_98D")

    label("loc_941")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_98D")

    Return()

    # Function_7_8C5 end

    def Function_8_98E(): pass

    label("Function_8_98E")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, -23040, -610, -21760, 180)
    SetChrPos(0x10F, -21410, -170, -21530, 270)
    SetChrPos(0xF0, -20040, -240, -20880, 270)
    SetChrPos(0xF1, -20670, -450, -19630, 225)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-23140, -610, -22300, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #17
        0x109,
        (
            "#1841F#6P喂喂，不是开玩笑吧。\x02\x03",

            "#1063F本来还想着可能会有人在里面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1803F#6P…………………………………\x02\x03",

            "#1440F……要把门强行撞开吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #19
        0x109,
        (
            "#1061F#2P说的也是──\x02\x01",

            "#1063F喂，都说不要用过激的手段了！\x02\x03",

            "你就不能从别的方面\x01",
            "思考一下吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2C")

    ChrTalk(    #20
        0x107,
        (
            "#560F#6P而且我觉得飞艇的门\x01",
            "应该是非常坚固的。\x02\x03",

            "要想把它破坏\x01",
            "也许没那么简单……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C90")

    label("loc_C2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C90")

    ChrTalk(    #21
        0x10D,
        (
            "#272F#6P而且飞艇的门\x01",
            "应该是相当坚固的。\x02\x03",

            "#270F不可能轻易被破坏掉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C90")

    OP_8C(0x10F, 45, 400)
    Sleep(300)

    ChrTalk(    #22
        0x10F,
        "#1447F#5P嗯，当然是开玩笑的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1068F#2P（看你的眼神\x01",
            "  就是认真的……）\x02\x03",

            "#1060F算了，\x01",
            "也许在别处可以找到钥匙。\x02\x03",

            "我们一会儿再过来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-20660, -170, -21090, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -20660, -170, -21090, 0)
    SetChrPos(0x1, -20660, -170, -21090, 0)
    SetChrPos(0x2, -20660, -170, -21090, 0)
    SetChrPos(0x3, -20660, -170, -21090, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x270A)
    OP_28(0x2C, 0x1, 0x8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_98E end

    def Function_9_E1B(): pass

    label("Function_9_E1B")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0xD)
    OP_43(0x1, 0x1, 0x0, 0xC)
    OP_43(0x2, 0x1, 0x0, 0xB)
    OP_43(0x3, 0x1, 0x0, 0xA)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_E1B end

    def Function_10_EFF(): pass

    label("Function_10_EFF")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_EFF end

    def Function_11_F57(): pass

    label("Function_11_F57")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_F57 end

    def Function_12_FA1(): pass

    label("Function_12_FA1")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_12_FA1 end

    def Function_13_FDD(): pass

    label("Function_13_FDD")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_FDD end

    def Function_14_100B(): pass

    label("Function_14_100B")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x12)
    OP_43(0x1, 0x1, 0x0, 0x11)
    OP_43(0x2, 0x1, 0x0, 0x10)
    OP_43(0x3, 0x1, 0x0, 0xF)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_100B end

    def Function_15_10EF(): pass

    label("Function_15_10EF")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_15_10EF end

    def Function_16_1147(): pass

    label("Function_16_1147")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_1147 end

    def Function_17_1191(): pass

    label("Function_17_1191")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_17_1191 end

    def Function_18_11CD(): pass

    label("Function_18_11CD")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_18_11CD end

    SaveToFile()

Try(main)
