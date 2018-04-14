from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C1102_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C1102_1 ._SN',
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        "Function_1_FB",           # 01, 1
        "Function_2_446",          # 02, 2
        "Function_3_462",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x2)
    OP_28(0x7D, 0x1, 0x8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x05打倒了所有的魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    EventEnd(0x3)
    Return()

    # Function_0_AA end

    def Function_1_FB(): pass

    label("Function_1_FB")

    EventBegin(0x2)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 75710, -500, 187310, 180)
    SetChrPos(0x8, 76850, -500, 177570, 0)
    SetChrPos(0x9, 74990, -500, 176460, 0)
    OP_6D(75660, -350, 200280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_1D(0x51)

    def lambda_199():
        OP_6D(75710, -500, 187310, 8500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_199)
    OP_0D()
    WaitChrThread(0x8, 0x0)
    Sleep(1000)

    NpcTalk(    #1
        0x8,
        "男人的声音",
        (
            "#2P真是的……\x01",
            "被彻底打败。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_1E8():
        OP_6D(75710, -500, 185000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1E8)
    Sleep(2500)

    def lambda_205():
        OP_8E(0x8, 0x12C32, 0xFFFFFE0C, 0x2D456, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_205)
    Sleep(500)

    def lambda_225():
        OP_8E(0x9, 0x124EE, 0xFFFFFE0C, 0x2D0D2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_225)
    WaitChrThread(0x8, 0x0)
    OP_6D(75710, -500, 187310, 4500)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 315, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #2
        0x8,
        (
            "想不到那些游击士\x01",
            "居然会闯进来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "虽然全力以赴，\x01",
            "不过，最后还是被击败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        "嗯，真是的──\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "那帮家伙\x01",
            "总是妨碍我……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #6
        0x8,
        "哟，你认识他们？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #7
        0x9,
        (
            "别问了──\x01",
            "先不管这些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "赶快把残骸收拾掉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "是啊……\x01",
            "尽快撤退吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "以巡逻型人形兵器的测试来说，\x01",
            "这次的成果也非常足够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    OP_43(0x8, 0x1, 0x1, 0x2)
    OP_8C(0x9, 0, 400)

    def lambda_3B0():
        OP_69(0x9, 0xDAC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3B0)

    def lambda_3BE():
        OP_6B(2600, 3500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3BE)
    Sleep(1000)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #11
        0x9,
        (
            "哼，不过……\x01",
            "想不到他们对付巡逻型也这么棘手。\x02\x03",

            "那帮家伙的小命──\x01",
            "估计也不会太长了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/R1502   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_1_FB end

    def Function_2_446(): pass

    label("Function_2_446")

    OP_8E(0x8, 0x12B9C, 0xFFFFFE0C, 0x2DBAE, 0x5DC, 0x0)
    OP_8C(0x8, 270, 400)
    Return()

    # Function_2_446 end

    def Function_3_462(): pass

    label("Function_3_462")

    OP_8E(0x9, 0x124EE, 0xFFFFFE0C, 0x2D730, 0x7D0, 0x0)
    OP_8C(0x9, 45, 400)
    Return()

    # Function_3_462 end

    SaveToFile()

Try(main)
