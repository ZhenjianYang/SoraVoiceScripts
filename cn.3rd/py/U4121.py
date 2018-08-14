from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4121   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4121.x',
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
        TriggerX            = 117130,
        TriggerZ            = 0,
        TriggerY            = -1810,
        TriggerRange        = 1000,
        ActorX              = 116000,
        ActorZ              = 3000,
        ActorY              = -1500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 86170,
        TriggerZ            = 0,
        TriggerY            = 56850,
        TriggerRange        = 1000,
        ActorX              = 85500,
        ActorZ              = 3000,
        ActorY              = 57000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6080,
        TriggerZ            = 0,
        TriggerY            = -90,
        TriggerRange        = 1000,
        ActorX              = -6080,
        ActorZ              = 1000,
        ActorY              = -90,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_1B8",          # 01, 1
        "Function_2_201",          # 02, 2
        "Function_3_891",          # 03, 3
        "Function_4_8BF",          # 04, 4
        "Function_5_8F2",          # 05, 5
        "Function_6_925",          # 06, 6
        "Function_7_958",          # 07, 7
        "Function_8_9CC",          # 08, 8
        "Function_9_B6D",          # 09, 9
        "Function_10_C23",         # 0A, 10
        "Function_11_CCE",         # 0B, 11
        "Function_12_E73",         # 0C, 12
        "Function_13_F29",         # 0D, 13
        "Function_14_FD4",         # 0E, 14
        "Function_15_FE9",         # 0F, 15
        "Function_16_FFE",         # 10, 16
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (109, "loc_132"),
        (110, "loc_145"),
        (SWITCH_DEFAULT, "loc_158"),
    )


    label("loc_132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_142")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_142")

    Jump("loc_158")

    label("loc_145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_155")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_155")

    Jump("loc_158")

    label("loc_158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_16E")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_1B7")

    label("loc_16E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_184")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 10)
    Jump("loc_1B7")

    label("loc_184")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_19C"),
        (SWITCH_DEFAULT, "loc_1B7"),
    )


    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_1A6")
    Jump("loc_1B7")

    label("loc_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_1B7")

    Return()

    # Function_0_116 end

    def Function_1_1B8(): pass

    label("Function_1_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_1CB")
    OP_B1("U4121_y")
    Jump("loc_1D4")

    label("loc_1CB")

    OP_B1("U4121_n")

    label("loc_1D4")

    OP_82(0x81, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1E7")
    OP_82(0x82, 0x0)
    Jump("loc_1EA")

    label("loc_1E7")

    OP_82(0x83, 0x0)

    label("loc_1EA")

    OP_82(0x84, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1FD")
    OP_82(0x85, 0x0)
    Jump("loc_200")

    label("loc_1FD")

    OP_82(0x86, 0x0)

    label("loc_200")

    Return()

    # Function_1_1B8 end

    def Function_2_201(): pass

    label("Function_2_201")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -230, -500, -7250, 0)
    SetChrPos(0x10F, 960, -500, -7250, 0)
    SetChrPos(0x107, -230, -500, -7250, 0)
    SetChrPos(0x10E, 960, -500, -7250, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-270, -250, -6000, 0)
    OP_67(0, 7960, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_2D8():
        OP_6D(-1810, 0, -1360, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2D8)

    def lambda_2F0():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2F0)

    def lambda_308():
        OP_6B(3360, 3000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_308)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0x107, 0x0, 0x0, 0x5)
    OP_43(0x10E, 0x0, 0x0, 0x6)
    Sleep(1500)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #0
        0x109,
        "#1067F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1445F#6P……谁也不在。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10E,
        (
            "#175F#6P本来还抱有\x01",
            "一丝期望的……\x02\x03",

            "#176F如果这种时候能取得\x01",
            "游击士的协助就再好不过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        (
            "#062F#6P那、那个，\x01",
            "让我查看一下通讯器吧！\x02\x03",

            "说不定可以和其它支部\x01",
            "取得联络！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_470():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_470)
    Sleep(50)

    def lambda_483():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_483)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #4
        0x109,
        "#1060F#5P啊，那就拜托了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x107, -5230, 0, -440, 270)
    SetChrPos(0x109, -5220, 0, -1960, 0)
    SetChrPos(0x10F, -3690, 0, -3170, 315)
    SetChrPos(0x10E, -5380, 0, -3250, 0)
    OP_6D(-6430, 0, -620, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(315000, 0)
    OP_6E(258, 0)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x1, "map\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1500)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #5
        0x107,
        (
            "#561F#5P不、不行……\x02\x03",

            "#063F虽然通讯器还可以工作，\x01",
            "但怎么也接不通……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10E,
        (
            "#178F#6P那再试试雷斯顿\x01",
            "要塞的司令部怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x107,
        (
            "#064F#5P啊，好的……\x01",
            "…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #8
        0x107,
        (
            "#562F#5P不行……\x01",
            "果然还是没有响应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10E,
        "#176F#6P是吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)
    Sleep(500)

    ChrTalk(    #10
        0x10F,
        (
            "#1446F#6P……估计就算打给其它地方\x01",
            "也只会是一样的结果吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        "#1067F#6P啊啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 135, 400)
    Sleep(300)

    ChrTalk(    #12
        0x109,
        (
            "#1063F#5P真是遗憾，\x01",
            "只能我们自己来想办法解决了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x1, 0x0)
    OP_6D(-90, 0, -3480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -90, 0, -3480, 180)
    SetChrPos(0x1, -90, 0, -3480, 180)
    SetChrPos(0x2, -90, 0, -3480, 180)
    SetChrPos(0x3, -90, 0, -3480, 180)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    OP_A2(0x2703)
    OP_28(0x2B, 0x1, 0x10)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_2_201 end

    def Function_3_891(): pass

    label("Function_3_891")


    def lambda_897():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_897)
    OP_8E(0xFE, 0xFFFFFE52, 0x0, 0xFFFFF0EC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_891 end

    def Function_4_8BF(): pass

    label("Function_4_8BF")

    Sleep(300)

    def lambda_8CA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8CA)
    OP_8E(0xFE, 0x316, 0x0, 0xFFFFF128, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_8BF end

    def Function_5_8F2(): pass

    label("Function_5_8F2")

    Sleep(800)

    def lambda_8FD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8FD)
    OP_8E(0xFE, 0xFFFFFD9E, 0xFFFFFF06, 0xFFFFEC82, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_8F2 end

    def Function_6_925(): pass

    label("Function_6_925")

    Sleep(1000)

    def lambda_930():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_930)
    OP_8E(0xFE, 0x2D0, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_925 end

    def Function_7_958(): pass

    label("Function_7_958")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
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

    Jump("loc_9B5")

    label("loc_9B5")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_7_958 end

    def Function_8_9CC(): pass

    label("Function_8_9CC")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 119150, 0, -1320, 270)
    SetChrPos(0x1, 119160, 0, -2640, 270)
    SetChrPos(0x2, 120770, 0, -1370, 270)
    SetChrPos(0x3, 121190, 0, -2760, 270)
    OP_6D(117190, 0, -1720, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA2")
    OP_28(0x4, 0x4, 0x2)
    OP_82(0x82, 0x2)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_AA2")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #14
        (
            "\x07\x05#40W　 汝须将银发之华丽舞者\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B61")
    Call(0, 7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5E")
    Call(0, 9)

    label("loc_B5E")

    Jump("loc_B61")

    label("loc_B61")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_8_9CC end

    def Function_9_B6D(): pass

    label("Function_9_B6D")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)

    def lambda_BD6():
        OP_6B(2750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BD6)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x7, 0, 0x0)
    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_B6D end

    def Function_10_C23(): pass

    label("Function_10_C23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 119150, 0, -1320, 270)
    SetChrPos(0x1, 119160, 0, -2640, 270)
    SetChrPos(0x2, 120770, 0, -1370, 270)
    SetChrPos(0x3, 121190, 0, -2760, 270)
    OP_6D(117190, 0, -1720, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_10_C23 end

    def Function_11_CCE(): pass

    label("Function_11_CCE")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 87660, 0, 57470, 270)
    SetChrPos(0x1, 87780, 0, 55980, 270)
    SetChrPos(0x2, 89360, 0, 57190, 270)
    SetChrPos(0x3, 89250, 0, 56020, 270)
    OP_6D(86850, 0, 56780, 0)
    OP_67(0, 5030, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA4")
    OP_28(0x1C, 0x4, 0x2)
    OP_82(0x85, 0x2)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_DA4")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #15
        (
            "\x07\x05#40W   汝须将无比热爱钓鱼之少女\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E67")
    Call(0, 7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E64")
    Call(0, 12)

    label("loc_E64")

    Jump("loc_E67")

    label("loc_E67")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_11_CCE end

    def Function_12_E73(): pass

    label("Function_12_E73")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    Sleep(500)

    def lambda_EDC():
        OP_6B(3070, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_EDC)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0xC, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_E73 end

    def Function_13_F29(): pass

    label("Function_13_F29")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 87660, 0, 57470, 270)
    SetChrPos(0x1, 87780, 0, 55980, 270)
    SetChrPos(0x2, 89360, 0, 57190, 270)
    SetChrPos(0x3, 89250, 0, 56020, 270)
    OP_6D(86850, 0, 56780, 0)
    OP_67(0, 5030, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_13_F29 end

    def Function_14_FD4(): pass

    label("Function_14_FD4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/U4123   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_14_FD4 end

    def Function_15_FE9(): pass

    label("Function_15_FE9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_15_FE9 end

    def Function_16_FFE(): pass

    label("Function_16_FFE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #16
        "\x07\x05导力通讯似乎无法使用。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_16_FFE end

    SaveToFile()

Try(main)
