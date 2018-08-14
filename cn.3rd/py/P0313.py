from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P0313   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P0313.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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


    DeclEvent(
        X                   = -30,
        Y                   = -1000,
        Z                   = -7340,
        Range               = 3700,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFDC88,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_DE",           # 01, 1
        "Function_2_E8",           # 02, 2
        "Function_3_520",          # 03, 3
        "Function_4_574",          # 04, 4
        "Function_5_5A4",          # 05, 5
        "Function_6_5D4",          # 06, 6
        "Function_7_618",          # 07, 7
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_DD")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_DD")

    Return()

    # Function_0_CA end

    def Function_1_DE(): pass

    label("Function_1_DE")

    OP_B1("P0313_2")
    Return()

    # Function_1_DE end

    def Function_2_E8(): pass

    label("Function_2_E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -2290, 150, 8600, 180)
    SetChrPos(0x10F, -2290, 150, 8600, 180)
    SetChrPos(0x107, -2290, 150, 8600, 180)
    SetChrPos(0x10E, -2290, 150, 8600, 180)
    OP_6D(840, 0, 7550, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(3830, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x4)

    def lambda_19C():
        OP_6D(2370, 0, 440, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19C)

    def lambda_1B4():
        OP_67(0, 7090, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B4)

    def lambda_1CC():
        OP_6B(3830, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1CC)

    def lambda_1DC():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1DC)
    OP_43(0x10E, 0x0, 0x0, 0x3)
    Sleep(800)
    OP_43(0x109, 0x0, 0x0, 0x4)
    Sleep(1000)
    OP_43(0x10F, 0x0, 0x0, 0x5)
    Sleep(1000)
    OP_43(0x107, 0x0, 0x0, 0x6)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(840, 0, 4090, 0)
    OP_67(0, 5020, -10000, 0)
    OP_6B(3390, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x10E,
        "#178F#5P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_2A5():
        OP_6D(840, 0, 5090, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A5)
    OP_8C(0x10E, 0, 400)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x10E,
        (
            "#176F#6P……对不起。\x01",
            "花费了多余的时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x107,
        "#063F#5P尤莉亚小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        (
            "#1840F#5P哪里哪里……\x01",
            "别放在心上。\x02\x03",

            "站在尤莉亚小姐的立场上，\x01",
            "想亲眼确认也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10F,
        (
            "#1446F#5P……我们想办法来寻找\x01",
            "可以打开这局面的线索吧。\x02\x03",

            "#1448F这样的话，\x01",
            "应该也能确认部下们的安危。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10E,
        (
            "#176F#6P啊……没错。\x02\x03",

            "#170F……谢谢。\x01",
            "那就继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x261B)
    OP_28(0x2A, 0x1, 0x4)
    OP_6D(-150, 0, 4140, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -150, 0, 4140, 180)
    SetChrPos(0x1, -150, 0, 4140, 180)
    SetChrPos(0x2, -150, 0, 4140, 180)
    SetChrPos(0x3, -150, 0, 4140, 180)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_2_E8 end

    def Function_3_520(): pass

    label("Function_3_520")

    OP_8E(0xFE, 0xFFFFF813, 0x0, 0x1928, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFEDE, 0x0, 0x942, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_520 end

    def Function_4_574(): pass

    label("Function_4_574")

    OP_8E(0xFE, 0xFFFFF813, 0x0, 0x1928, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0xE6A, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_574 end

    def Function_5_5A4(): pass

    label("Function_5_5A4")

    OP_8E(0xFE, 0xFFFFF813, 0x0, 0x1928, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE6, 0x0, 0xF14, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_5A4 end

    def Function_6_5D4(): pass

    label("Function_6_5D4")

    OP_8E(0xFE, 0xFFFFF813, 0x0, 0x1928, 0x7D0, 0x0)
    OP_6F(0x4, 15)
    OP_70(0x4, 0x0)
    OP_71(0x1004, 0x0)
    ExitThread()
    OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0x1482, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_5D4 end

    def Function_7_618(): pass

    label("Function_7_618")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05门紧紧地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_7_618 end

    SaveToFile()

Try(main)
