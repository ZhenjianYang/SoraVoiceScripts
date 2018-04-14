from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C2102_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '',                                     # 8
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_536",          # 01, 1
        "Function_2_989",          # 02, 2
        "Function_3_99B",          # 03, 3
        "Function_4_9C6",          # 04, 4
        "Function_5_9F1",          # 05, 5
        "Function_6_A1C",          # 06, 6
        "Function_7_A47",          # 07, 7
        "Function_8_A99",          # 08, 8
        "Function_9_AEF",          # 09, 9
        "Function_10_BA4",         # 0A, 10
        "Function_11_11CC",        # 0B, 11
        "Function_12_1D27",        # 0C, 12
        "Function_13_1DB6",        # 0D, 13
        "Function_14_22CB",        # 0E, 14
        "Function_15_2336",        # 0F, 15
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Call(1, 7)
    FadeToBright(2000, 0)
    Call(1, 8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #0
        0x101,
        "#1004F#4P啊……！？\x02",
    )

    CloseMessageWindow()
    Call(1, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_18D")

    ChrTalk(    #1
        0x101,
        "#1020F#2P真、真的在动……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_156")

    ChrTalk(    #2
        0x106,
        "#057F……和委托人说的一样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A")

    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_18A")

    ChrTalk(    #3
        0x103,
        "#022F……原来如此，和委托人说的一样呢。\x02",
    )

    CloseMessageWindow()

    label("loc_18A")

    Jump("loc_253")

    label("loc_18D")


    ChrTalk(    #4
        0x101,
        "#1020F#2P好、好像在动啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_201")

    ChrTalk(    #5
        0x106,
        (
            "#052F……是古代文明的遗物呢。\x02\x03",

            "我记得它的功能应该是使机能停止的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253")

    label("loc_201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_253")

    ChrTalk(    #6
        0x103,
        (
            "#022F……是古代文明的遗物呢。\x02\x03",

            "我记得它的功能应该是使得机能停止的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_39F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_2CB")

    ChrTalk(    #7
        0x104,
        (
            "#031F不过这光真有神秘感。\x02\x03",

            "嗯，可以让人感受到古人的睿智呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x127,
        (
            "#151F嗯嗯～\x01",
            "太漂亮了⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326")

    label("loc_2CB")


    ChrTalk(    #9
        0x104,
        (
            "#031F原来是古代的装置啊。\x02\x03",

            "嗯，怪不得它会发出神秘的光呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x127,
        (
            "#151F嗯嗯～\x01",
            "太漂亮了⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326")

    TurnDirection(0x101, 0x127, 400)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        (
            "#1007F#2P怎、怎么还在说些无关紧要的话。\x02\x03",

            "#2P不过，现在看上去\x01",
            "倒是没什么危险。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459")

    label("loc_39F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_407")

    ChrTalk(    #12
        0x101,
        (
            "#1015F#2P可是，为什么这种东西\x01",
            "会莫名启动呢……\x02\x03",

            "#2P不过，现在看上去\x01",
            "倒是没什么危险。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459")

    label("loc_407")


    ChrTalk(    #13
        0x101,
        (
            "#1020F#2P那、那东西为什么会动啊？\x02\x03",

            "#1015F不过，现在看上去\x01",
            "倒是没什么危险……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4AF")

    ChrTalk(    #14
        0x106,
        (
            "#050F嗯，虽然如此，\x01",
            "也不能掉以轻心。\x02\x03",

            "谁都不知道接下来可能会发生什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_50A")

    ChrTalk(    #15
        0x103,
        (
            "#022F嗯，虽然如此，\x01",
            "还是不要掉以轻心比较好。\x02\x03",

            "谁都不知道接下来可能会发生什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50A")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #16
        0x101,
        "#1002F……嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x66, 0x1, 0x2000)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_536(): pass

    label("Function_1_536")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Call(1, 7)
    FadeToBright(2000, 0)
    Call(1, 8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #17
        0x101,
        "#1004F#4P啊……！？\x02",
    )

    CloseMessageWindow()

    label("loc_595")

    Call(1, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C7")

    ChrTalk(    #18
        0x101,
        "#1020F#2P真、真的在动……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E8")

    label("loc_5C7")


    ChrTalk(    #19
        0x101,
        "#1002F#2P果然在活动着呢……\x02",
    )

    CloseMessageWindow()

    label("loc_5E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_61C")

    ChrTalk(    #20
        0x106,
        "#057F……和听说的一样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_64C")

    label("loc_61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_64C")

    ChrTalk(    #21
        0x103,
        "#022F……原来如此，和听说的一样呢。\x02",
    )

    CloseMessageWindow()

    label("loc_64C")


    ChrTalk(    #22
        0x104,
        (
            "#031F不过这光真有神秘感。\x02\x03",

            "嗯，可以让人感受到古人的睿智呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x127,
        (
            "#151F嗯嗯～\x01",
            "太漂亮了⊙\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x127, 400)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x101,
        (
            "#1007F#2P怎、怎么还在说些无关紧要的话。\x02\x03",

            "#2P快点拍摄完后马上撤退吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_750")

    ChrTalk(    #25
        0x106,
        (
            "#552F按我说的办。\x01",
            "这里的气氛让人不想久留。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78B")

    label("loc_750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_78B")

    ChrTalk(    #26
        0x103,
        (
            "#025F的确如此。\x01",
            "这可不是一个让人想久留的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78B")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #27
        0x101,
        "#1015F#2P那么，从哪里开始拍呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E0")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_82E")

    ChrTalk(    #28
        0x106,
        (
            "#050F……和听说的一样。\x02\x03",

            "虽然看上去没什么危险，\x01",
            "不过还是赶快拍照吧。\x02\x03",

            "……这里的气氛让人不想久留。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AB")

    label("loc_82E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8AB")

    ChrTalk(    #29
        0x103,
        (
            "#022F……原来如此，和听说的一样呢。\x02\x03",

            "虽然看上去没什么危险，\x01",
            "不过还是赶快拍照吧。\x02\x03",

            "这可不是一个让人想久留的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AB")


    ChrTalk(    #30
        0x101,
        (
            "#1002F#2P嗯……\x02\x03",

            "#1015F那么，从哪里开始拍呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E0")

    OP_59()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #31
        "\x07\x05※拍摄照片时要使用『#15I导力照相机』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #32
        (
            "\x07\x05※移动到想拍摄的地方，\x01",
            "  请在Camp界面的[Items]标签里\x01",
            "  点选『#15I导力照相机』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_28(0x66, 0x1, 0x1000)
    OP_28(0x66, 0x1, 0x2000)
    EventEnd(0x0)
    Return()

    # Function_1_536 end

    def Function_2_989(): pass

    label("Function_2_989")

    OP_6D(70, 0, 8320, 2000)
    Return()

    # Function_2_989 end

    def Function_3_99B(): pass

    label("Function_3_99B")

    SetChrPos(0xFE, 600, -1000, -5960, 0)
    Sleep(400)
    OP_90(0xFE, 0x258, 0x0, 0x1770, 0x7D0, 0x0)
    Return()

    # Function_3_99B end

    def Function_4_9C6(): pass

    label("Function_4_9C6")

    SetChrPos(0xFE, -100, -1000, -5960, 0)
    Sleep(400)
    OP_90(0xFE, 0xFFFFFF9C, 0x0, 0x1450, 0x7D0, 0x0)
    Return()

    # Function_4_9C6 end

    def Function_5_9F1(): pass

    label("Function_5_9F1")

    SetChrPos(0xFE, 400, -1000, -5960, 0)
    Sleep(400)
    OP_90(0xFE, 0x190, 0x0, 0x1068, 0x7D0, 0x0)
    Return()

    # Function_5_9F1 end

    def Function_6_A1C(): pass

    label("Function_6_A1C")

    SetChrPos(0xFE, -300, -1000, -5960, 0)
    Sleep(400)
    OP_90(0xFE, 0xFFFFFED4, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_6_A1C end

    def Function_7_A47(): pass

    label("Function_7_A47")

    SetChrPos(0x101, 600, -10000, -5960, 0)
    SetChrPos(0xF7, -600, -10000, -5960, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A98")
    SetChrPos(0x104, 600, -10000, -6960, 0)
    SetChrPos(0x127, -600, -10000, -6960, 0)

    label("loc_A98")

    Return()

    # Function_7_A47 end

    def Function_8_A99(): pass

    label("Function_8_A99")

    OP_43(0x101, 0x1, 0x1, 0x3)
    Sleep(750)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AB6")
    OP_43(0x106, 0x1, 0x1, 0x4)
    Jump("loc_AC4")

    label("loc_AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AC4")
    OP_43(0x103, 0x1, 0x1, 0x4)

    label("loc_AC4")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE9")
    OP_43(0x104, 0x1, 0x1, 0x5)
    Sleep(750)
    OP_43(0x127, 0x1, 0x1, 0x6)

    label("loc_AE9")

    WaitChrThread(0x101, 0x1)
    Return()

    # Function_8_A99 end

    def Function_9_AEF(): pass

    label("Function_9_AEF")

    OP_6D(-160, 950, 12910, 4000)
    Sleep(2000)
    OP_43(0x101, 0x2, 0x1, 0x2)

    def lambda_B12():
        OP_90(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B12)
    Sleep(100)

    def lambda_B32():
        OP_90(0xF7, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_B32)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B94")
    Sleep(100)

    def lambda_B5F():
        OP_90(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B5F)
    Sleep(100)

    def lambda_B7F():
        OP_90(0x127, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_B7F)

    label("loc_B94")

    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    Return()

    # Function_9_AEF end

    def Function_10_BA4(): pass

    label("Function_10_BA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB1")
    Return()

    label("loc_BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD4")
    Return()

    label("loc_BD4")

    SetMapFlags(0x80)
    OP_C2()
    Sleep(30)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)
    OP_8B(0x0, 0xFFFFFF2E, 0x3D40, 0x0)
    OP_8B(0x1, 0xFFFFFF2E, 0x3D40, 0x0)
    OP_8B(0x2, 0xFFFFFF2E, 0x3D40, 0x0)
    OP_8B(0x3, 0xFFFFFF2E, 0x3D40, 0x0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C41")
    OP_51(0x9, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_C41")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C5A")
    OP_51(0xA, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_C5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C73")
    OP_51(0xB, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_C73")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D06")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD7")

    ChrTalk(    #33
        0x101,
        "#1015F从这里拍的话有柱子挡着。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D03")

    label("loc_CD7")


    ChrTalk(    #34
        0x101,
        "#1015F从那里拍的话可能会被柱子挡到……\x02",
    )

    CloseMessageWindow()

    label("loc_D03")

    EventEnd(0x3)
    Return()

    label("loc_D06")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DA1")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D68")

    ChrTalk(    #35
        0x101,
        (
            "#1003F这个角度有点不好。\x02\x03",

            "得再靠近正面一点拍摄……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9E")

    label("loc_D68")


    ChrTalk(    #36
        0x101,
        (
            "#1007F这个角度有点不好。\x02\x03",

            "得再靠近正面一点拍摄。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9E")

    EventEnd(0x3)
    Return()

    label("loc_DA1")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x361A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x42C1D80), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_E79")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E42")

    ChrTalk(    #37
        0x101,
        (
            "#1007F距离有点太近了。\x02\x03",

            "可能得再下来一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E76")

    label("loc_E42")


    ChrTalk(    #38
        0x101,
        (
            "#1007F距离有点太近了。\x02\x03",

            "可能再下来一点比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E76")

    EventEnd(0x3)
    Return()

    label("loc_E79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0xBEBC200), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EFE")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECF")

    ChrTalk(    #39
        0x101,
        (
            "#1015F………………………………\x02\x03",

            "有点太远了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFB")

    label("loc_ECF")


    ChrTalk(    #40
        0x101,
        (
            "#1015F从那里拍的话……\x02\x03",

            "有点太远了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFB")

    EventEnd(0x3)
    Return()

    label("loc_EFE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F13")
    OP_A2(0x0)
    Jump("loc_1033")

    label("loc_F13")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F27")
    OP_A2(0x1)
    Jump("loc_1033")

    label("loc_F27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FA9")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A")

    ChrTalk(    #41
        0x101,
        (
            "#1015F………………………………\x02\x03",

            "有点太远了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA6")

    label("loc_F7A")


    ChrTalk(    #42
        0x101,
        (
            "#1015F从那里拍的话……\x02\x03",

            "有点太远了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA6")

    EventEnd(0x3)
    Return()

    label("loc_FA9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1838), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1033")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFC")

    ChrTalk(    #43
        0x101,
        (
            "#1007F距离有点太近了。\x02\x03",

            "不再下来一点可能不行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1030")

    label("loc_FFC")


    ChrTalk(    #44
        0x101,
        (
            "#1007F距离有点太近了。\x02\x03",

            "不再下来一点可能不行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1030")

    EventEnd(0x3)
    Return()

    label("loc_1033")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1069")

    ChrTalk(    #45
        0x101,
        (
            "#1015F嗯……\x01",
            "从这里会比较好吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1135")

    label("loc_1069")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109E")

    ChrTalk(    #46
        0x106,
        (
            "#050F喂，艾丝蒂尔。\x01",
            "这里怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1105")

    label("loc_109E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D3")

    ChrTalk(    #47
        0x103,
        (
            "#020F艾丝蒂尔。\x01",
            "从这里拍怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1105")

    label("loc_10D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1105")

    ChrTalk(    #48
        0x104,
        (
            "#030F艾丝蒂尔。\x01",
            "从这里拍怎么样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1105")

    OP_8B(0x101, 0x0, 0x3192, 0x1F4)

    ChrTalk(    #49
        0x101,
        (
            "#1011F啊，嗯……\x01",
            "确实比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1135")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【从这里拍摄】\x01",      # 0
            "【找其他地方】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119B")
    Call(1, 11)
    Jump("loc_11C4")

    label("loc_119B")


    ChrTalk(    #50
        0x101,
        (
            "#1015F……再找找\x01",
            "别的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)
    OP_A3(0x1)

    label("loc_11C4")

    EventEnd(0x3)
    ClearMapFlags(0x80)
    Return()

    # Function_10_BA4 end

    def Function_11_11CC(): pass

    label("Function_11_11CC")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_51(0x101, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1262")
    OP_8C(0x101, 45, 0)
    SetChrPos(0xF7, -11490, 250, 4670, 0)
    TurnDirection(0xF7, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_125F")
    SetChrPos(0x104, -13060, 250, 3460, 0)
    SetChrPos(0x127, -11130, 250, 2970, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x127, 0x101, 0)

    label("loc_125F")

    Jump("loc_1324")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12C8")
    OP_8C(0x101, 315, 0)
    SetChrPos(0xF7, 12340, 250, 4740, 338)
    TurnDirection(0xF7, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12C5")
    SetChrPos(0x104, 13400, 250, 3860, 338)
    SetChrPos(0x127, 11220, 250, 3250, 338)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x127, 0x101, 0)

    label("loc_12C5")

    Jump("loc_1324")

    label("loc_12C8")

    OP_8C(0x101, 0, 0)
    SetChrPos(0xF7, 1050, 0, 500, 0)
    TurnDirection(0xF7, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1324")
    SetChrPos(0x104, 270, 0, -1000, 0)
    SetChrPos(0x127, -850, 0, 0, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x127, 0x101, 0)

    label("loc_1324")

    OP_69(0x101, 0x0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        (
            "#1006F……好，就在这儿了。\x02\x03",

            "#1018F那么～我要拍了哦～\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 15)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D1")

    ChrTalk(    #52
        0x127,
        "#151F小艾～加油～⊙\x02",
    )

    CloseMessageWindow()

    label("loc_13D1")

    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x101, 1)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x101)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D07")
    Fade(250)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x127, 400)
    OP_51(0x8, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x8, 0x3E8)

    ChrTalk(    #53
        0x127,
        "#153F咦～要放弃吗～？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_14A7")

    ChrTalk(    #54
        0x106,
        "#052F怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C1")

    label("loc_14A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_14C1")

    ChrTalk(    #55
        0x103,
        "#023F怎么了？\x02",
    )

    CloseMessageWindow()

    label("loc_14C1")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #56
        0x101,
        (
            "#1015F不，我想想觉得\x01",
            "没必要一定得让我来拍。\x02\x03",

            "虽说是偶然，不过难得有\x01",
            "专家和我们在一起。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF7, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1562")

    ChrTalk(    #57
        0x106,
        "#051F原来是这么回事啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1582")

    label("loc_1562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1582")

    ChrTalk(    #58
        0x103,
        "#021F哦，这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1582")


    ChrTalk(    #59
        0x101,
        (
            "#1011F拜托朵洛希了……\x02\x03",

            "帮我们拍摄应该没关系吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_15F3")

    ChrTalk(    #60
        0x106,
        (
            "#051F嗯，没问题。\x02\x03",

            "你没自信的话就拜托她吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162B")

    label("loc_15F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_162B")

    ChrTalk(    #61
        0x103,
        (
            "#027F嗯，没关系。\x02\x03",

            "你没自信的话就拜托她吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_162B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【拜托朵洛希】\x01",      # 0
            "【自己拍摄】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B81")
    TurnDirection(0x101, 0x127, 400)

    ChrTalk(    #62
        0x101,
        (
            "#1000F……那么，朵洛希。\x02\x03",

            "可以拜托你来拍吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x127,
        (
            "#151F当然没问题！\x02\x03",

            "就让我全力以赴地来拍摄吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1017F嘿嘿，谢谢。\x02\x03",

            "那么我把相机给你。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_180C")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x127, 0, 0, 4000, 0)
    SetChrPos(0x101, -50, 0, 1280, 0)
    SetChrPos(0xF7, 1050, 0, 500, 0)
    TurnDirection(0xF7, 0x127, 0)
    SetChrPos(0x104, 270, 0, -1000, 0)
    TurnDirection(0x104, 0x127, 0)
    OP_69(0x127, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #65
        0x127,
        "#151F那我就开始啰～⊙\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x127, 16)
    OP_0D()
    Call(1, 14)

    ChrTalk(    #66
        0x127,
        (
            "#153F嘿嘿，很棒的表情～\x02\x03",

            "#151F来，茄～～子㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Jump("loc_19CD")

    label("loc_180C")


    def lambda_1812():
        OP_69(0x127, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1812)

    def lambda_1820():

        label("loc_1820")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1820")

    QueueWorkItem2(0xF7, 1, lambda_1820)

    def lambda_1831():

        label("loc_1831")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1831")

    QueueWorkItem2(0x104, 1, lambda_1831)

    def lambda_1842():

        label("loc_1842")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1842")

    QueueWorkItem2(0x127, 1, lambda_1842)
    OP_8E(0x101, 0xFFFFFCAE, 0x0, 0x500, 0x7D0, 0x0)
    TurnDirection(0x101, 0x127, 400)
    WaitChrThread(0xF7, 0x2)
    OP_44(0xF7, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x127, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #67
        "把\x1F\x32\x02\x07\x00交给了朵洛希。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)

    ChrTalk(    #68
        0x127,
        "#150F那么我要开始了！\x02",
    )

    CloseMessageWindow()

    def lambda_18E6():

        label("loc_18E6")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_18E6")

    QueueWorkItem2(0x101, 1, lambda_18E6)
    OP_94(0x0, 0x101, 0x10E, 0x320, 0x7D0, 0x0)

    def lambda_1906():
        OP_6D(0, 0, 4000, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1906)

    def lambda_191E():

        label("loc_191E")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_191E")

    QueueWorkItem2(0xF7, 1, lambda_191E)

    def lambda_192F():

        label("loc_192F")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_192F")

    QueueWorkItem2(0x104, 1, lambda_192F)
    OP_8E(0x127, 0xFFFFFCAE, 0x0, 0x500, 0x7D0, 0x0)
    OP_8E(0x127, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_8C(0x127, 0, 400)
    OP_44(0xF7, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x104, 0x1)
    WaitChrThread(0xF7, 0x2)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x127, 16)
    OP_0D()
    Call(1, 14)

    ChrTalk(    #69
        0x127,
        (
            "#153F嘿嘿，很棒的表情～\x02\x03",

            "#151F那我开始了～来，茄子㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    label("loc_19CD")

    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x127, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    SetChrChipByIndex(0x127, 65535)
    OP_8C(0x127, 180, 400)
    Sleep(1000)

    ChrTalk(    #70
        0x127,
        (
            "#151F让你们久等了～\x02\x03",

            "我觉得拍得很有韵味哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1016F真、真像你的风格～\x02",
    )

    CloseMessageWindow()

    def lambda_1A86():
        OP_6D(-850, 0, 1280, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1A86)

    def lambda_1A9E():

        label("loc_1A9E")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1A9E")

    QueueWorkItem2(0x101, 1, lambda_1A9E)

    def lambda_1AAF():

        label("loc_1AAF")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1AAF")

    QueueWorkItem2(0xF7, 1, lambda_1AAF)

    def lambda_1AC0():

        label("loc_1AC0")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1AC0")

    QueueWorkItem2(0x104, 1, lambda_1AC0)
    OP_8E(0x127, 0xFFFFFCAE, 0x0, 0x500, 0x7D0, 0x0)
    TurnDirection(0x127, 0x101, 400)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x104, 0x1)
    WaitChrThread(0xF7, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #72
        "\x1F\x32\x02\x07\x00归还了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #73
        0x101,
        (
            "#1001F嗯，不过还是要谢谢你。\x02\x03",

            "好了，这样拍摄的任务就完成了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x66, 0x1, 0x8)
    Jump("loc_1D04")

    label("loc_1B81")


    ChrTalk(    #74
        0x101,
        (
            "#1015F……虽然这么想，\x01",
            "不过还是由我来拍吧。\x02\x03",

            "因为这是我自己接下的工作。\x01",
            "必须靠自己坚持到底才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x127,
        (
            "#150F嗯，难得有这个机会，\x01",
            "还是让小艾来拍比较好。\x02\x03",

            "毕竟把这么棒的模特儿\x01",
            "让给别人来拍，也太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1007F抱歉，朵洛希。\x01",
            "搞得这么大动干戈的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8B(0x101, 0xFFFFFF2E, 0x3D40, 0x190)

    ChrTalk(    #77
        0x101,
        (
            "#1002F好，重新准备。\x02\x03",

            "再次集中精力来拍摄照片了～\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 15)
    OP_0D()
    Sleep(400)
    Fade(250)
    SetChrSubChip(0x101, 1)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(1000)
    Call(1, 12)
    OP_28(0x66, 0x1, 0x4)

    label("loc_1D04")

    Jump("loc_1D11")

    label("loc_1D07")

    Call(1, 12)
    OP_28(0x66, 0x1, 0x4)

    label("loc_1D11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_1D20")
    Call(1, 15)

    label("loc_1D20")

    Call(1, 13)
    EventEnd(0x0)
    Return()

    # Function_11_11CC end

    def Function_12_1D27(): pass

    label("Function_12_1D27")

    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x101, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Fade(250)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(400)

    ChrTalk(    #78
        0x101,
        "#1018F好，拍摄完毕。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_12_1D27 end

    def Function_13_1DB6(): pass

    label("Function_13_1DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1DF5")

    ChrTalk(    #79
        0x106,
        (
            "#050F那么马上回城里吧。\x02\x03",

            "待在这里也没什么用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3F")

    label("loc_1DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1E3F")

    ChrTalk(    #80
        0x103,
        (
            "#020F那么马上回城里吧。\x02\x03",

            "一直待在这种地方也没什么太大的意义。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3F")

    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(400)

    ChrTalk(    #81
        0x101,
        "#1004F咦？要回去了？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1EB0")

    ChrTalk(    #82
        0x106,
        (
            "#052F嗯，是这么打算的……\x02\x03",

            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE6")

    label("loc_1EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1EE6")

    ChrTalk(    #83
        0x103,
        (
            "#023F嗯，是这么打算的……\x02\x03",

            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE6")


    ChrTalk(    #84
        0x101,
        (
            "#1015F倒是没有什么问题……\x02\x03",

            "不过难得来到这里，\x01",
            "马上回去的话是不是有点可惜？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F92")

    ChrTalk(    #85
        0x106,
        (
            "#051F咦，怎么了？\x01",
            "你还想探索这座塔吗？\x02\x03",

            "如果你有这个想法\x01",
            "我就陪你一起去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDF")

    label("loc_1F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1FDF")

    ChrTalk(    #86
        0x103,
        (
            "#027F咦，想探索这座塔吗？\x02\x03",

            "如果你这么想的话，\x01",
            "我倒是没什么问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FDF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【马上返回卢安】\x01",            # 0
            "【探索完塔之后再返回】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_215F")

    ChrTalk(    #87
        0x101,
        (
            "#1007F抱歉，还是算了吧。\x02\x03",

            "首先要把照片的工作\x01",
            "完成才行。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_20CB")

    ChrTalk(    #88
        0x106,
        (
            "#053F啊啊，是啊。\x02\x03",

            "#050F好，直接返回城里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20FF")

    label("loc_20CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_20FF")

    ChrTalk(    #89
        0x103,
        (
            "#020F嗯，是啊。\x02\x03",

            "那么，直接返回城里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2137")

    ChrTalk(    #90
        0x104,
        "#031F嗯，那么走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x127,
        "#151F好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_2137")


    ChrTalk(    #92
        0x101,
        "#1006F嗯！　我们走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2153")

    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_22CA")

    label("loc_215F")


    ChrTalk(    #93
        0x101,
        (
            "#1006F嗯，还是想先去\x01",
            "探索一下哟。\x02\x03",

            "这里也有很多挺厉害的魔兽，\x01",
            "可以当成一次不错的训练。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2215")

    ChrTalk(    #94
        0x106,
        (
            "#053F的确如此\x01",
            "正好可以舒展一下筋骨……\x02\x03",

            "#051F好，那我们\x01",
            "就稍微绕点远路吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2276")

    label("loc_2215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2276")

    ChrTalk(    #95
        0x103,
        (
            "#021F呵呵，的确如此\x01",
            "正好可以舒展一下筋骨……\x02\x03",

            "#020F明白了，那我们\x01",
            "就稍微绕点远路吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2276")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22AE")

    ChrTalk(    #96
        0x104,
        "#031F嗯，那么走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x127,
        "#151F好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_22CA")

    label("loc_22AE")


    ChrTalk(    #98
        0x101,
        "#1006F嗯！　就这么办。\x02",
    )

    CloseMessageWindow()

    label("loc_22CA")

    Return()

    # Function_13_1DB6 end

    def Function_14_22CB(): pass

    label("Function_14_22CB")

    OP_62(0x127, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(400)
    OP_94(0x1, 0x127, 0x5A, 0x1F4, 0x3E8, 0x0)
    Sleep(800)
    OP_94(0x1, 0x127, 0x10E, 0x3E8, 0x3E8, 0x0)
    Sleep(200)
    OP_94(0x1, 0x127, 0x5A, 0x1F4, 0x3E8, 0x0)
    Sleep(400)
    OP_94(0x1, 0x127, 0xB4, 0x1F4, 0x3E8, 0x0)
    Sleep(800)
    OP_63(0x127)
    Return()

    # Function_14_22CB end

    def Function_15_2336(): pass

    label("Function_15_2336")

    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2365")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_2365")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2381")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_2381")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_239D")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_239D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23B9")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_23B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23D5")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_23D5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23F1")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_23F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_240D")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_240D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2429")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_2429")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2443")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_2443")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_245D")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_245D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2477")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_2477")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2491")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_2491")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24AB")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_24AB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24C5")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24DC")

    label("loc_24C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24DC")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24DC")

    Return()

    # Function_15_2336 end

    SaveToFile()

Try(main)
