from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5507   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5507.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        TriggerX            = 5300,
        TriggerZ            = 0,
        TriggerY            = 9990,
        TriggerRange        = 800,
        ActorX              = 5670,
        ActorZ              = 1500,
        ActorY              = 10510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_DF",           # 01, 1
        "Function_2_F7",           # 02, 2
        "Function_3_979",          # 03, 3
        "Function_4_F51",          # 04, 4
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE")
    Event(0, 2)

    label("loc_DE")

    Return()

    # Function_0_CE end

    def Function_1_DF(): pass

    label("Function_1_DF")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE2758, 0x2300A4)
    OP_1B(0x1, 0x0, 0x3)
    Return()

    # Function_1_DF end

    def Function_2_F7(): pass

    label("Function_2_F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 950, 0, 25250, 180)
    SetChrPos(0x102, 2360, 0, 25120, 180)
    SetChrPos(0xF0, 1230, 0, 26610, 180)
    SetChrPos(0xF1, 2670, 0, 26530, 180)
    OP_6D(2700, 3000, -24000, 0)
    OP_67(0, 14750, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(89000, 0)
    OP_6E(428, 0)

    def lambda_18A():
        OP_6D(2700, 3000, 13000, 12000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18A)

    def lambda_1A2():
        OP_67(0, 12710, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A2)

    def lambda_1BA():
        OP_6B(2930, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1BA)

    def lambda_1CA():
        OP_6E(428, 9000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CA)
    StopSound(0x88B8, 0x27100, 0x0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_1F1():
        OP_8E(0xFE, 0xFFFFFA1A, 0x0, 0x339A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F1)
    Sleep(200)

    def lambda_211():
        OP_8E(0xFE, 0xFFFFFFF6, 0x0, 0x32E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_211)
    Sleep(130)

    def lambda_231():
        OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x3994, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_231)
    Sleep(150)

    def lambda_251():
        OP_8E(0xFE, 0x122, 0x0, 0x389A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_251)
    Sleep(1000)
    Fade(1000)
    StopSound(0x88B8, 0x30D40, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x102, 0x2)
    OP_6D(1500, 0, -2430, 0)
    OP_67(0, 12990, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(45000, 0)
    OP_6E(427, 0)

    def lambda_2D0():
        OP_6D(-350, 2000, 10660, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2D0)

    def lambda_2E8():
        OP_6B(3800, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2E8)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)
    Fade(1000)
    StopSound(0x88B8, 0x1FBD0, 0x0)
    OP_6D(520, 0, 15250, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(45000, 0)
    OP_6E(337, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D1")

    ChrTalk(    #0
        0x10A,
        (
            "#1310F#5P哇，好漂亮……！\x02\x03",

            "#819F和我们训练的时候\x01",
            "感觉完全不同……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_526")

    label("loc_3D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_407")

    ChrTalk(    #1
        0x107,
        "#560F#5P哇啊……好漂亮！\x02",
    )

    CloseMessageWindow()
    Jump("loc_526")

    label("loc_407")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_440")

    ChrTalk(    #2
        0x105,
        "#1168F#5P这……真是漂亮啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_526")

    label("loc_440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47D")

    ChrTalk(    #3
        0x10B,
        (
            "#415F#5P哦……\x01",
            "真是相当漂亮呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_526")

    label("loc_47D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B9")

    ChrTalk(    #4
        0x104,
        (
            "#1540F#5P哈……\x01",
            "这真是漂亮啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_526")

    label("loc_4B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F1")

    ChrTalk(    #5
        0x10E,
        "#171F#5P哦……这真是漂亮。\x02",
    )

    CloseMessageWindow()
    Jump("loc_526")

    label("loc_4F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_526")

    ChrTalk(    #6
        0x108,
        "#070F#5P嗯，这真是漂亮啊。\x02",
    )

    CloseMessageWindow()

    label("loc_526")


    ChrTalk(    #7
        0x102,
        (
            "#1504F#5P………………………………\x02\x03",

            "#1502F的确很漂亮……\x01",
            "不过不觉得有点奇怪吗？\x02\x03",

            "这种针叶树一般\x01",
            "不会有红叶的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1065F#6P不，\x01",
            "针叶树里应该也有叶子会变红的种类。\x02\x03",

            "#1067F叫做什么来着……\x01",
            "莉丝应该会更清楚吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1500F#5P原来如此……\x01",
            "是我多心了吗。\x02\x03",

            "#1503F不，但是……\x01",
            "在宿舍的土地上种的树，\x01",
            "应该也和这里的是同一品种。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E5")
    OP_A2(0x2)

    ChrTalk(    #10
        0x10D,
        (
            "#270F#5P唔……\x01",
            "那边可是郁郁葱葱的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88A")

    label("loc_6E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72B")
    OP_A2(0x7)

    ChrTalk(    #11
        0x108,
        (
            "#072F#5P唔……\x01",
            "记得那边可是绿色的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88A")

    label("loc_72B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_773")
    OP_A2(0x1)

    ChrTalk(    #12
        0x10E,
        (
            "#178F#5P那边的树\x01",
            "应该是郁郁葱葱的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88A")

    label("loc_773")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BA")
    OP_A2(0x6)

    ChrTalk(    #13
        0x104,
        (
            "#1542F#5P唔……\x01",
            "那边可是郁郁葱葱的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88A")

    label("loc_7BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_802")
    OP_A2(0x3)

    ChrTalk(    #14
        0x10B,
        (
            "#212F#5P那边可是完全\x01",
            "没有红叶的样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88A")

    label("loc_802")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_847")
    OP_A2(0x5)

    ChrTalk(    #15
        0x105,
        (
            "#1162F#5P……那边可是\x01",
            "没有红叶的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88A")

    label("loc_847")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88A")
    OP_A2(0x0)

    ChrTalk(    #16
        0x107,
        (
            "#062F#5P那、那边\x01",
            "可是完全没有红叶吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_903")

    ChrTalk(    #17
        0x109,
        (
            "#1065F#6P嗯……\x01",
            "不管怎么说，\x01",
            "这里都是不正常的地方。\x02\x03",

            "#1063F提高警惕前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_962")

    label("loc_903")


    ChrTalk(    #18
        0x109,
        (
            "#1065F#6P嗯……\x01",
            "不管怎么说，\x01",
            "这里都是不正常的地方。\x02\x03",

            "#1063F提高警惕前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_962")

    OP_A2(0x2906)
    OP_28(0x33, 0x1, 0x1)
    OP_28(0x33, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_F7 end

    def Function_3_979(): pass

    label("Function_3_979")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_99C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9AD")

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_9AD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9AD")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_9D2"),
        (1, "loc_A01"),
        (2, "loc_A30"),
        (SWITCH_DEFAULT, "loc_A5F"),
    )


    label("loc_9D2")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_A5F")

    label("loc_A01")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_A5F")

    label("loc_A30")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_A5F")

    label("loc_A5F")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E01")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_ABF"),
        (1, "loc_AEB"),
        (2, "loc_B28"),
        (SWITCH_DEFAULT, "loc_B7A"),
    )


    label("loc_ABF")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_B7A")

    label("loc_AEB")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_B7A")

    label("loc_B28")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_B7A")

    label("loc_B7A")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BA4"),
        (1, "loc_C38"),
        (2, "loc_CCE"),
        (3, "loc_D64"),
        (SWITCH_DEFAULT, "loc_DFE"),
    )


    label("loc_BA4")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_C03")

    label("loc_C03")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C25"),
        (1, "loc_C32"),
        (SWITCH_DEFAULT, "loc_C35"),
    )


    label("loc_C25")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C35")

    label("loc_C32")

    Jump("loc_C35")

    label("loc_C35")

    Jump("loc_DFE")

    label("loc_C38")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #20
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_C99")

    label("loc_C99")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CBB"),
        (1, "loc_CC8"),
        (SWITCH_DEFAULT, "loc_CCB"),
    )


    label("loc_CBB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCB")

    label("loc_CC8")

    Jump("loc_CCB")

    label("loc_CCB")

    Jump("loc_DFE")

    label("loc_CCE")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #21
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_D2F")

    label("loc_D2F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D51"),
        (1, "loc_D5E"),
        (SWITCH_DEFAULT, "loc_D61"),
    )


    label("loc_D51")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D61")

    label("loc_D5E")

    Jump("loc_D61")

    label("loc_D61")

    Jump("loc_DFE")

    label("loc_D64")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #22
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_DC9")

    label("loc_DC9")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DEB"),
        (1, "loc_DF8"),
        (SWITCH_DEFAULT, "loc_DFB"),
    )


    label("loc_DEB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFB")

    label("loc_DF8")

    Jump("loc_DFB")

    label("loc_DFB")

    Jump("loc_DFE")

    label("loc_DFE")

    Jump("loc_A94")

    label("loc_E01")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_E1A"),
        (1, "loc_E4E"),
        (2, "loc_E82"),
        (3, "loc_EB6"),
        (SWITCH_DEFAULT, "loc_EEA"),
    )


    label("loc_E1A")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_EEA")

    label("loc_E4E")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_EEA")

    label("loc_E82")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_EEA")

    label("loc_EB6")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_EEA")

    label("loc_EEA")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F0C"),
        (1, "loc_F2C"),
        (2, "loc_F38"),
        (3, "loc_F44"),
        (SWITCH_DEFAULT, "loc_F50"),
    )


    label("loc_F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F20")
    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F29")

    label("loc_F20")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_F29")

    Jump("loc_F50")

    label("loc_F2C")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F50")

    label("loc_F38")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_F50")

    label("loc_F44")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_F50")

    label("loc_F50")

    Return()

    # Function_3_979 end

    def Function_4_F51(): pass

    label("Function_4_F51")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #23
        "\x07\x05【圣科洛瓦森林】\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #24
        (
            "\x07\x05除了游击队员训练以外，\x01",
            "这里也适合进行生存训练。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_F51 end

    SaveToFile()

Try(main)
