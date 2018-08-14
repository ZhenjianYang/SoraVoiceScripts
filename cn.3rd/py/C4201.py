from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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


    DeclActor(
        TriggerX            = 123780,
        TriggerZ            = 0,
        TriggerY            = 19220,
        TriggerRange        = 1000,
        ActorX              = 122910,
        ActorZ              = 1500,
        ActorY              = 19200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103870,
        TriggerZ            = 0,
        TriggerY            = 24400,
        TriggerRange        = 1000,
        ActorX              = 103830,
        ActorZ              = 1500,
        ActorY              = 24960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 136410,
        TriggerZ            = 0,
        TriggerY            = -112150,
        TriggerRange        = 1000,
        ActorX              = 137180,
        ActorZ              = 1500,
        ActorY              = -112180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 128250,
        TriggerZ            = 0,
        TriggerY            = -152730,
        TriggerRange        = 1000,
        ActorX              = 127270,
        ActorZ              = 1500,
        ActorY              = -152920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 130400,
        TriggerZ            = 0,
        TriggerY            = -145890,
        TriggerRange        = 3000,
        ActorX              = 130400,
        ActorZ              = 3000,
        ActorY              = -145890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_15F",          # 01, 1
        "Function_2_208",          # 02, 2
        "Function_3_21E",          # 03, 3
        "Function_4_12FE",         # 04, 4
        "Function_5_132D",         # 05, 5
        "Function_6_132E",         # 06, 6
        "Function_7_132F",         # 07, 7
        "Function_8_1346",         # 08, 8
        "Function_9_146C",         # 09, 9
        "Function_10_1592",        # 0A, 10
        "Function_11_16B8",        # 0B, 11
        "Function_12_17DE",        # 0C, 12
        "Function_13_1850",        # 0D, 13
        "Function_14_1A05",        # 0E, 14
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Return()

    # Function_0_15E end

    def Function_1_15F(): pass

    label("Function_1_15F")

    OP_6F(0x0, 0)
    OP_6F(0x3, 0)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E")
    OP_1B(0x0, 0x0, 0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 6)), scpexpr(EXPR_END)), "loc_19A")
    OP_6F(0x0, 240)
    OP_6F(0x3, 120)
    Jump("loc_19E")

    label("loc_19A")

    OP_65(0x4, 0x1)

    label("loc_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0")
    OP_6F(0x1, 0)
    Jump("loc_1B7")

    label("loc_1B0")

    OP_6F(0x1, 60)

    label("loc_1B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9")
    OP_6F(0x2, 0)
    Jump("loc_1D0")

    label("loc_1C9")

    OP_6F(0x2, 60)

    label("loc_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2")
    OP_6F(0x4, 0)
    Jump("loc_1E9")

    label("loc_1E2")

    OP_6F(0x4, 60)

    label("loc_1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB")
    OP_6F(0x5, 0)
    Jump("loc_202")

    label("loc_1FB")

    OP_6F(0x5, 60)

    label("loc_202")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_15F end

    def Function_2_208(): pass

    label("Function_2_208")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_208")

    label("loc_21D")

    Return()

    # Function_2_208 end

    def Function_3_21E(): pass

    label("Function_3_21E")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(129300, 0, -151840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 129199, 0, -152700, 270)
    SetChrPos(0x151, 129199, 0, -151240, 225)
    Sleep(1000)

    ChrTalk(    #0
        0x151,
        (
            "#1653F好像不动呢……\x02\x03",

            "#1656F嗯……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x151, 135, 400)
    Sleep(600)
    OP_8C(0x151, 315, 400)
    Sleep(600)

    ChrTalk(    #1
        0x103,
        "#1648F别出声。\x02",
    )

    CloseMessageWindow()

    def lambda_2F8():
        OP_8E(0xFE, 0x1F630, 0x0, 0xFFFDAB84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2F8)

    def lambda_313():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_313)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05雪拉扎德取下装置下面的石头，\x01",
            "将一只手伸进去。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_22(0x73, 0x0, 0x64)
    Sleep(300)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x64, 0x0, 0x64)
    OP_6F(0x3, 65)
    OP_70(0x3, 0x78)
    OP_73(0x3)
    OP_6F(0x3, 120)
    Sleep(500)
    OP_6D(128919, 0, -146150, 2000)
    OP_22(0xD0, 0x0, 0x64)
    OP_70(0x0, 0xF0)
    Sleep(200)

    def lambda_3DD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_3DD)
    Sleep(100)

    def lambda_3F0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3F0)
    OP_73(0x0)
    OP_6F(0x0, 240)
    OP_6D(129300, 0, -151840, 2000)

    ChrTalk(    #3
        0x151,
        (
            "#1653F#1P啊………………\x02\x03",

            "#1651F好厉害……\x01",
            "呵呵，真令人感动！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#1646F嗯，\x01",
            "跟开金库类似啦。\x02\x03",

            "#1648F………………我说。\x02\x03",

            "对这种事\x01",
            "还是不要太憧憬的好。\x02",
        )
    )

    Jump("loc_4DD")

    label("loc_4DD")

    CloseMessageWindow()

    def lambda_4E4():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_4E4)
    Sleep(300)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    def lambda_513():
        OP_6B(2600, 10000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_513)

    ChrTalk(    #5
        0x151,
        "#1653F雪拉扎德小姐……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x103,
        "#1648F……这种技术……\x02",
    )

    CloseMessageWindow()

    def lambda_56B():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_56B)
    OP_20(0xFA0)
    FadeToDark(2000, 0, -1)
    OP_24(0x1CD, 0x5A)
    Sleep(300)
    OP_24(0x1CD, 0x50)
    Sleep(300)
    OP_24(0x1CD, 0x46)
    Sleep(300)
    OP_24(0x1CD, 0x3C)
    Sleep(300)
    OP_24(0x1CD, 0x32)
    Sleep(300)
    OP_24(0x1CD, 0x28)
    Sleep(300)
    OP_24(0x1CD, 0x1E)
    Sleep(300)
    OP_24(0x1CD, 0x14)
    Sleep(300)
    OP_23(0x1CD)
    OP_21()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x18\x07\x0C#40W不知道会比较幸福。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_21()
    OP_22(0x173, 0x0, 0x64)
    Sleep(4000)
    OP_1D(0x1A)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x18\x07\x0C#40W这条街充满臭水沟的味道。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x18\x07\x0C#40W即使在贫民区也是遭人嫌恶之所。\x01",
            "流浪者不是被抓入牢狱\x01",
            "就是被赶出城市。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #10
        "\x18\x07\x0C#40W还有像废物般被抛弃的孩子。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x18\x07\x0C#40W在这堆积了几十年尘埃的街上，\x01",
            "我为了生存不择手段。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1200)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x18\x07\x0C#40W几乎是看到什么就拿什么。\x01",
            "从小就养成了顺手牵羊的恶习。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x18\x07\x0C#40W即使如此也难以糊口。\x01",
            "因为这里有些人就靠\x01",
            "抢夺我们这种人的金钱为生。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #14
        "\x18\x07\x0C#40W最可靠的手段就是闯空门，开金库。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x18\x07\x0C#40W与贫民区仅一河之隔的高级住宅区，\x01",
            "可以从地下水路潜入。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x18\x07\x0C#40W饥肠辘辘地潜进去，\x01",
            "使出在懂事之前就学会的伎俩。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x18\x07\x0C#40W窍门在于，\x01",
            "不要把金库里的东西洗劫一空。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x18\x07\x0C#40W而是一次次地拿走\x01",
            "物主难以察觉的小数额。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #19
        "\x18\x07\x0C#40W一根针就能取得足够生活十天的米拉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x18\x07\x0C#40W尝到了甜头就会每天都去。\x01",
            "还痴心妄想开始存钱。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x18\x07\x0C#40W……结果还是被贫民区的男人们全部抢走，\x01",
            "并把我踢打到吐血。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #22
        "\x18\x07\x0C#40W所有人都是『为了生存』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x1C9, 0x1, 0xA)
    Sleep(300)
    OP_24(0x1C9, 0x14)
    Sleep(300)
    OP_24(0x1C9, 0x1E)
    Sleep(300)
    OP_24(0x1C9, 0x28)
    Sleep(300)
    OP_24(0x1C9, 0x32)
    Sleep(300)
    OP_24(0x1C9, 0x3C)
    Sleep(300)
    OP_24(0x1C9, 0x46)
    Sleep(300)
    OP_24(0x1C9, 0x50)
    Sleep(300)
    OP_24(0x1C9, 0x5A)
    OP_C5(0x0, 0xFE00, 0xFE00, 0x200, 0x200, 0x140, 0xF0, 0x400, 0x400, 0x0, 0x0, 0x400, 0x400, 0xFFFFFF, 0x0, "C_VIS353._CH")
    OP_C6(0x0, 0x1, 800, 800, 0)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    OP_43(0x103, 0x3, 0x0, 0x4)
    Sleep(4500)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x18\x07\x0C#40W所有人都这么说着，装出拼命的姿态，\x01",
            "却都选择着最轻松的生存方式。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x18\x07\x0C#40W这毫无生气的城市生产着肮脏的人类。\x01",
            "而我也是其中之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #25
        "\x18\x07\x0C#40W多少次想放弃。多少次祈祷能够放弃。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x18\x07\x0C#40W我憎恶持续着这种生活的自己，\x01",
            "更憎恶无法放弃这种生活的自己。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 8947848, 2000, 0)
    Sleep(200)
    OP_24(0x1C9, 0x50)
    Sleep(200)
    OP_24(0x1C9, 0x3C)
    Sleep(200)
    OP_24(0x1C9, 0x28)
    Sleep(200)
    OP_24(0x1C9, 0x14)
    Sleep(200)
    OP_23(0x1C9)
    OP_C7(0x0, 0x0, 0x3)
    OP_44(0x103, 0x3)
    OP_C7(0x1, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(    #27
        "\x18\x07\x0C#40W我就是不想再回到那种生活才当上了游击士。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #28
        "\x18\x07\x0C#40W…………我害怕得不行。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x18\x07\x0C#40W将自己从那条街上拯救出来的戏团消失了，\x01",
            "让我走上正道的人们消失了，\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #30
        "\x18\x07\x0C#40W……难道我又要重回那种生活吗。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #31
        "\x18\x07\x0C#40W因为我终究是贫民区出身的。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x18\x07\x0C#40W无论如何打扮，\x01",
            "无论装得多亲切。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #33
        "\x18\x07\x0C#40W我………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #34
        "\x18\x07\x0C#40W――――总有一天，还是得回那条街。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #35
        "\x18\x07\x0C#40W……所以，我必须坚强地活下去。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x18\x07\x0C#40W什么职业都无所谓。\x01",
            "只要全身心投入，过正当的生活。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x18\x07\x0C#40W不再回想过去。\x01",
            "不屈服于丑陋的自己。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #38
        "\x18\x07\x0C#40W即使孤独一人，也要坚强地活下去。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #39
        "\x18\x07\x0C#40W坚强、坚强……比任何人都坚强……！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #40
        "\x18\x07\x0C#40W……但是，结果怎样呢。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #41
        (
            "\x18\x07\x0C#40W我是不是做得够好呢。#5500W　\x01",
            "#40W……露茜奥拉姐姐………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(127220, 0, -150380, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 126600, 0, -151000, 270)
    SetChrPos(0x151, 128639, 0, -151000, 270)
    OP_C4(0x1, 0x800)
    OP_20(0x1388)

    def lambda_1015():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1015)
    FadeToBright(5000, 0)
    Sleep(300)
    OP_22(0x1CD, 0x1, 0xA)
    Sleep(300)
    OP_24(0x1CD, 0x14)
    Sleep(300)
    OP_24(0x1CD, 0x1E)
    Sleep(300)
    OP_24(0x1CD, 0x28)
    Sleep(300)
    OP_24(0x1CD, 0x32)
    Sleep(300)
    OP_24(0x1CD, 0x3C)
    Sleep(300)
    OP_24(0x1CD, 0x46)
    Sleep(300)
    OP_24(0x1CD, 0x50)
    Sleep(300)
    OP_24(0x1CD, 0x5A)
    Sleep(300)
    OP_24(0x1CD, 0x64)
    OP_0D()
    WaitChrThread(0x103, 0x2)
    Sleep(300)

    ChrTalk(    #42
        0x151,
        (
            "#1653F#2P雪拉扎德小姐……？\x02\x03",

            "怎么了，一脸失落的表情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        (
            "#1648F…………没什么。\x02\x03",

            "#1646F（只要完成这个委托，\x01",
            "  正游击士的推荐信就齐了。）\x02\x03",

            "（……我也能当上正游击士了。）\x02\x03",

            "（绝不再怨天尤人。\x01",
            "  我……要坚强地活下去！）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 400)
    Sleep(300)

    ChrTalk(    #44
        0x103,
        "#1648F走吧。\x02",
    )

    CloseMessageWindow()

    def lambda_11C4():
        OP_8E(0xFE, 0x225C4, 0x0, 0xFFFDB228, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11C4)

    def lambda_11DF():

        label("loc_11DF")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_11DF")

    QueueWorkItem2(0x151, 2, lambda_11DF)

    def lambda_11F0():
        OP_8F(0xFE, 0x1F67F, 0x0, 0xFFFDAD78, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_11F0)
    WaitChrThread(0x151, 0x1)
    Sleep(1000)

    ChrTalk(    #45
        0x151,
        (
            "#1653F#3P啊，等等！？\x02\x03",

            "雪拉扎德小姐！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x151, 0x2)

    def lambda_1252():
        OP_8E(0xFE, 0x1FB6C, 0x0, 0xFFFDB228, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1252)
    WaitChrThread(0x151, 0x1)

    def lambda_1272():
        OP_8E(0xFE, 0x225C4, 0x0, 0xFFFDB228, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1272)
    WaitChrThread(0x151, 0x1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #46
        "\x18\x07\x0C#40W只要完成这个委托……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x50, 0xFE, 0x0)
    OP_64(0x5, 0x1)
    OP_64(0x4, 0x1)
    OP_C4(0x1, 0x800)
    OP_A2(0x2F4E)
    NewScene("ED6_DT21/C4203   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_3_21E end

    def Function_4_12FE(): pass

    label("Function_4_12FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_132C")
    OP_C6(0x0, 0x2, -360000, 250000, 0)
    OP_C7(0x0, 0x0, 0x2)
    OP_C6(0x0, 0x2, 0, 0, 0)
    Jump("Function_4_12FE")

    label("loc_132C")

    Return()

    # Function_4_12FE end

    def Function_5_132D(): pass

    label("Function_5_132D")

    Return()

    # Function_5_132D end

    def Function_6_132E(): pass

    label("Function_6_132E")

    Return()

    # Function_6_132E end

    def Function_7_132F(): pass

    label("Function_7_132F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (112, "loc_133F"),
        (114, "loc_1342"),
        (SWITCH_DEFAULT, "loc_1345"),
    )


    label("loc_133F")

    Jump("loc_1345")

    label("loc_1342")

    Jump("loc_1345")

    label("loc_1345")

    Return()

    # Function_7_132F end

    def Function_8_1346(): pass

    label("Function_8_1346")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_13BA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    Jump("loc_139F")

    label("loc_139F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF0)
    Jump("loc_1428")

    label("loc_13BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x05\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1409")

    label("loc_1409")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1428")

    Jump("loc_145E")

    label("loc_142B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_145E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1346 end

    def Function_9_146C(): pass

    label("Function_9_146C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1551")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_14E0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x00得到了\x1F\x03\x02\x07\x00。\x02",
    )

    Jump("loc_14C5")

    label("loc_14C5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF1)
    Jump("loc_154E")

    label("loc_14E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #51
        (
            "宝箱里装有\x1F\x03\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x03\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_152F")

    label("loc_152F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_154E")

    Jump("loc_1584")

    label("loc_1551")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1584")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_146C end

    def Function_10_1592(): pass

    label("Function_10_1592")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1677")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_1606")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x00得到了\x1F\x03\x02\x07\x00。\x02",
    )

    Jump("loc_15EB")

    label("loc_15EB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF2)
    Jump("loc_1674")

    label("loc_1606")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #54
        (
            "宝箱里装有\x1F\x03\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x03\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1655")

    label("loc_1655")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_1674")

    Jump("loc_16AA")

    label("loc_1677")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_16AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1592 end

    def Function_11_16B8(): pass

    label("Function_11_16B8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_172C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x00得到了\x1F\x03\x02\x07\x00。\x02",
    )

    Jump("loc_1711")

    label("loc_1711")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF3)
    Jump("loc_179A")

    label("loc_172C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #57
        (
            "宝箱里装有\x1F\x03\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x03\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_177B")

    label("loc_177B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_179A")

    Jump("loc_17D0")

    label("loc_179D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #58
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_17D0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_16B8 end

    def Function_12_17DE(): pass

    label("Function_12_17DE")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05把手被固定得很牢，动不了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184F")
    Call(0, 3)

    label("loc_184F")

    Return()

    # Function_12_17DE end

    def Function_13_1850(): pass

    label("Function_13_1850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1898")

    ChrTalk(    #60
        0x103,
        (
            "#1640F附近应该有开关装置的。\x01",
            "找找吧。\x02",
        )
    )

    Jump("loc_1894")

    label("loc_1894")

    CloseMessageWindow()
    Jump("loc_1A01")

    label("loc_1898")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x103, 132300, 0, -145380, 255)
    SetChrPos(0x151, 133360, 0, -145880, 255)
    OP_0D()

    def lambda_18C8():
        OP_6D(133140, 0, -144700, 2000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18C8)

    def lambda_18E0():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_18E0)

    def lambda_18F8():
        OP_6C(18000, 2000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_18F8)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #61
        0x151,
        (
            "#1650F穿过这里\x01",
            "好像就进入西街区了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x103,
        (
            "#1646F#1P附近应该有开关装置的。\x02\x03",

            "……找找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x151,
        (
            "#1650F……………………\x01",
            "感觉……#3960W #20W \x02\x03",

            "#1651F好浪漫哦㈱\x02",
        )
    )

    Jump("loc_19CA")

    label("loc_19CA")

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #64
        0x103,
        "#1644F#1P………哪有！？\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x0)
    EventEnd(0x5)

    label("loc_1A01")

    TalkEnd(0xFF)
    Return()

    # Function_13_1850 end

    def Function_14_1A05(): pass

    label("Function_14_1A05")

    EventBegin(0x1)
    NewScene("ED6_DT21/C4200   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1A05 end

    SaveToFile()

Try(main)
