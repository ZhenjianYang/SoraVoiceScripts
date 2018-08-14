from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4165   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4165.x',
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


    DeclActor(
        TriggerX            = -84930,
        TriggerZ            = 0,
        TriggerY            = -60800,
        TriggerRange        = 1000,
        ActorX              = -84930,
        ActorZ              = 2000,
        ActorY              = -60800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 78570,
        TriggerZ            = 0,
        TriggerY            = -63260,
        TriggerRange        = 1000,
        ActorX              = 77000,
        ActorZ              = 3000,
        ActorY              = -63000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11940,
        TriggerZ            = 0,
        TriggerY            = 6010,
        TriggerRange        = 1000,
        ActorX              = -11940,
        ActorZ              = 1000,
        ActorY              = 6010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 87000,
        TriggerZ            = 0,
        TriggerY            = 42860,
        TriggerRange        = 800,
        ActorX              = 87000,
        ActorZ              = 1000,
        ActorY              = 42860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -87000,
        TriggerZ            = 0,
        TriggerY            = 42860,
        TriggerRange        = 800,
        ActorX              = -87000,
        ActorZ              = 1000,
        ActorY              = 42860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_1A2",          # 01, 1
        "Function_2_1D5",          # 02, 2
        "Function_3_90F",          # 03, 3
        "Function_4_936",          # 04, 4
        "Function_5_95D",          # 05, 5
        "Function_6_984",          # 06, 6
        "Function_7_9AB",          # 07, 7
        "Function_8_A17",          # 08, 8
        "Function_9_CAF",          # 09, 9
        "Function_10_D23",         # 0A, 10
        "Function_11_DAA",         # 0B, 11
        "Function_12_1148",        # 0C, 12
        "Function_13_11FE",        # 0D, 13
        "Function_14_12A9",        # 0E, 14
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_174")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_1A1")

    label("loc_174")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A1")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_1A1")

    Return()

    # Function_0_15E end

    def Function_1_1A2(): pass

    label("Function_1_1A2")

    OP_72(0x1001, 0x0)
    ExitThread()
    OP_1B(0x3, 0x0, 0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_1BE")

    OP_82(0x84, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1D1")
    OP_82(0x85, 0x0)
    Jump("loc_1D4")

    label("loc_1D1")

    OP_82(0x86, 0x0)

    label("loc_1D4")

    Return()

    # Function_1_1A2 end

    def Function_2_1D5(): pass

    label("Function_2_1D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -410, 0, -2500, 0)
    SetChrPos(0x10F, 1030, 0, -2420, 0)
    SetChrPos(0xF0, -410, 0, -2500, 0)
    SetChrPos(0xF1, 1030, 0, -2420, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-1070, 0, 16059, 0)
    OP_67(0, 7910, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(315000, 0)
    OP_6E(322, 0)

    def lambda_294():
        OP_6D(-730, 0, 4500, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_294)

    def lambda_2AC():
        OP_67(0, 6550, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2AC)

    def lambda_2C4():
        OP_6B(2850, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_2C4)

    def lambda_2D4():
        OP_6E(284, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_2D4)
    FadeToBright(1000, 0)
    Sleep(3000)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(500)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    Sleep(400)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    Sleep(600)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1444F#6P……这里是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1060F#5P『格兰竞技场』……\x01",
            "也就是王立竞技场。\x02\x03",

            "据说是召开武术大会\x01",
            "和其它各种活动的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_485")

    ChrTalk(    #2
        0x10E,
        (
            "#170F#6P去年的武术大会\x01",
            "就是在这里举办的，\x01",
            "金先生和艾丝蒂尔他们取得了优胜呢。\x02\x03",

            "今年由于发生了很多事情，\x01",
            "还没有举办大会的预定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        "#1078F#5P哎，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_60A")

    label("loc_485")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_544")

    ChrTalk(    #4
        0x10D,
        (
            "#272F#6P那个赖皮蛋和艾丝蒂尔他们\x01",
            "参加了去年的大会对吧。\x02\x03",

            "#276F当我注意到的时候\x01",
            "已经是决出优胜之后的事了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1066F#5P哈哈……\x01",
            "真是出乎意料啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60A")

    label("loc_544")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60A")

    ChrTalk(    #6
        0x107,
        (
            "#560F#6P去年的武术大会\x01",
            "艾丝蒂尔姐姐他们也参加了，\x01",
            "而且取得了优胜哦。\x02\x03",

            "阿加特大哥哥\x01",
            "也一直十分后悔\x01",
            "自己没能参加呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        "#1066F#5P哈哈，果然是阿加特的作风啊。\x02",
    )

    CloseMessageWindow()

    label("loc_60A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83E")
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x109, 0x10B, 400)
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1060F#5P对了，\x01",
            "乔丝特你们好像也参加了武术大会吧？\x02\x03",

            "我听艾丝蒂尔\x01",
            "他们说起过。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A2():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6A2)

    def lambda_6B0():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_6B0)

    def lambda_6BE():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_6BE)
    TurnDirection(0x10B, 0x109, 400)
    Sleep(300)

    ChrTalk(    #9
        0x10B,
        (
            "#416F#6P……是啊。\x02\x03",

            "只不过以罪犯的身份参加\x01",
            "实在不是什么令人愉快的回忆。\x02\x03",

            "#216F……等一下，我说。\x02\x03",

            "你怎么能就这样\x01",
            "随便称呼我呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1064F#5P哎，你不喜欢吗？\x02\x03",

            "#1068F不过称呼全名太见外了，\x01",
            "叫亲昵一点又容易被当成恋人。\x02\x03",

            "#1066F啊，\x01",
            "不过如果你愿意的话，\x01",
            "那我就——\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10B,
        (
            "#214F#6P哎呀，真是的！\x01",
            "随你便好了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83E")


    ChrTalk(    #12
        0x10F,
        (
            "#1440F#5P…………………………………\x02\x03",

            "#1446F……不管怎么说，\x01",
            "这里好像有什么东西蠢蠢欲动。\x02\x03",

            "如果要调查里面的话，\x01",
            "最好小心一点为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        "#1060F#5P嗯，说的也是。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2712)
    OP_28(0x2C, 0x1, 0x200)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_1D5 end

    def Function_3_90F(): pass

    label("Function_3_90F")


    def lambda_915():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_915)
    OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0x105E, 0x7D0, 0x0)
    Return()

    # Function_3_90F end

    def Function_4_936(): pass

    label("Function_4_936")


    def lambda_93C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93C)
    OP_8E(0xFE, 0x348, 0x0, 0xF64, 0x7D0, 0x0)
    Return()

    # Function_4_936 end

    def Function_5_95D(): pass

    label("Function_5_95D")


    def lambda_963():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_963)
    OP_8E(0xFE, 0xFFFFFD08, 0x0, 0xA50, 0x7D0, 0x0)
    Return()

    # Function_5_95D end

    def Function_6_984(): pass

    label("Function_6_984")


    def lambda_98A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_98A)
    OP_8E(0xFE, 0x406, 0x0, 0x8A2, 0x7D0, 0x0)
    Return()

    # Function_6_984 end

    def Function_7_9AB(): pass

    label("Function_7_9AB")

    EventBegin(0x1)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05上着锁，无法通过。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_9AB end

    def Function_8_A17(): pass

    label("Function_8_A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE6")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(1024)
    Sleep(500)
    Jump("loc_AE9")

    label("loc_AE6")

    TalkBegin(0xFF)

    label("loc_AE9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_B13")

    label("loc_B13")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7E")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_B78")

    label("loc_B78")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B95"),
        (1, "loc_C10"),
        (2, "loc_C3F"),
        (SWITCH_DEFAULT, "loc_C6E"),
    )


    label("loc_B95")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7B")

    label("loc_C10")

    OP_A9(0x17)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_C3C")

    label("loc_C3C")

    Jump("loc_C7B")

    label("loc_C3F")

    OP_A9(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_C6B")

    label("loc_C6B")

    Jump("loc_C7B")

    label("loc_C6E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7B")

    label("loc_C7B")

    Jump("loc_B26")

    label("loc_C7E")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAB")
    OP_A2(0x2587)
    EventEnd(0x1)
    Jump("loc_CAE")

    label("loc_CAB")

    TalkEnd(0xFF)

    label("loc_CAE")

    Return()

    # Function_8_A17 end

    def Function_9_CAF(): pass

    label("Function_9_CAF")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_D0C")

    label("loc_D0C")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_9_CAF end

    def Function_10_D23(): pass

    label("Function_10_D23")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x1F\x3D\x03\x07\x00奉上，\x01",
            "打开『门』吗？\x18\x02",
        )
    )

    Jump("loc_D57")

    label("loc_D57")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_D93")

    label("loc_D93")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_10_D23 end

    def Function_11_DAA(): pass

    label("Function_11_DAA")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 79700, 0, -62570, 270)
    SetChrPos(0x1, 79520, 0, -63940, 270)
    SetChrPos(0x2, 81380, 0, -62830, 270)
    SetChrPos(0x3, 81460, 0, -64090, 270)
    OP_6D(78510, 0, -63230, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E80")
    OP_28(0x21, 0x4, 0x2)
    OP_82(0x85, 0x2)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_E80")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_F69")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1C")

    AnonymousTalk(    #20
        (
            "\x07\x05#40W      道路既已打开……\x01",
            "#500W\x01",
            "#40W　　请携带挑战者之『证』\x01",
            "　   穿越此『门』吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F66")

    label("loc_F1C")


    AnonymousTalk(    #21
        (
            "\x07\x05#40W      道路既已打开……\x01",
            "#500W\x01",
            "#40W　    穿越此『门』吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F66")

    Jump("loc_109B")

    label("loc_F69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1033")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE5")

    AnonymousTalk(    #22
        (
            "\x07\x05#40W      道路既已打开……\x01",
            "#500W\x01",
            "#40W　　请携带挑战者之『证』\x01",
            "　   穿越此『门』吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1030")

    label("loc_FE5")


    AnonymousTalk(    #23
        (
            "\x07\x05#40W      道路既已打开……\x01",
            "#500W\x01",
            "#40W　   穿越此『门』吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1030")

    Jump("loc_109B")

    label("loc_1033")


    AnonymousTalk(    #24
        (
            "\x07\x05#40W　汝须将无法撼动之巨汉拳手\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109B")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_10D1")
    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CE")
    Call(0, 12)

    label("loc_10CE")

    Jump("loc_113C")

    label("loc_10D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_10F3")
    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F0")
    Call(0, 12)

    label("loc_10F0")

    Jump("loc_113C")

    label("loc_10F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1127")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1124")
    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1121")
    Call(0, 12)

    label("loc_1121")

    Jump("loc_1124")

    label("loc_1124")

    Jump("loc_113C")

    label("loc_1127")

    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113C")
    Call(0, 12)

    label("loc_113C")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_11_DAA end

    def Function_12_1148(): pass

    label("Function_12_1148")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x8)
    Sleep(500)

    def lambda_11B1():
        OP_6B(2750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_11B1)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x10, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1148 end

    def Function_13_11FE(): pass

    label("Function_13_11FE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 79700, 0, -62570, 270)
    SetChrPos(0x1, 79520, 0, -63940, 270)
    SetChrPos(0x2, 81380, 0, -62830, 270)
    SetChrPos(0x3, 81460, 0, -64090, 270)
    OP_6D(78510, 0, -63230, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_13_11FE end

    def Function_14_12A9(): pass

    label("Function_14_12A9")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_14_12A9 end

    SaveToFile()

Try(main)
