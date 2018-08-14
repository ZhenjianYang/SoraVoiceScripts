from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4200.x',
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
        "Function_1_C0",           # 01, 1
        "Function_2_F8",           # 02, 2
        "Function_3_367",          # 03, 3
        "Function_4_3E8",          # 04, 4
        "Function_5_46E",          # 05, 5
        "Function_6_537",          # 06, 6
        "Function_7_538",          # 07, 7
        "Function_8_539",          # 08, 8
        "Function_9_53A",          # 09, 9
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_BF")

    Return()

    # Function_0_AA end

    def Function_1_C0(): pass

    label("Function_1_C0")

    OP_64(0x3, 0x1)
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    OP_22(0x1CD, 0x1, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6")
    OP_A2(0x2F4F)

    label("loc_E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 7)), scpexpr(EXPR_END)), "loc_F2")
    OP_1B(0xD, 0x0, 0x5)

    label("loc_F2")

    OP_1B(0xF, 0x0, 0x2)

    label("loc_F7")

    Return()

    # Function_1_C0 end

    def Function_2_F8(): pass

    label("Function_2_F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_20(0x7D0)
    Sleep(2000)
    OP_6D(46500, 0, -7000, 0)
    OP_67(0, 8020, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 49340, -2000, -7440, 270)
    SetChrFlags(0x151, 0x40)
    SetChrPos(0x151, 49340, -2000, -7440, 270)
    OP_43(0x103, 0x3, 0x0, 0x3)
    OP_43(0x151, 0x3, 0x0, 0x4)

    def lambda_18B():
        OP_6D(50200, 0, -12660, 7000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_18B)

    def lambda_1A3():
        OP_67(0, 6900, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_1A3)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x103, 0x3)
    WaitChrThread(0x151, 0x3)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x151,
        "#1652F门上了锁呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#1646F#12P……我知道。\x02\x03",

            "#1642F你别出声。\x01",
            "会分心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x151,
        "#1653F啊，是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x103,
        "#1648F#12P………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05雪拉扎德取出一根针，\x01",
            "插入钥匙孔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_22(0x73, 0x0, 0x64)
    Sleep(120)
    OP_22(0x73, 0x0, 0x64)
    Sleep(250)
    OP_22(0x73, 0x0, 0x64)
    Sleep(400)
    OP_70(0x3, 0x50)
    OP_22(0x6E, 0x0, 0x64)
    OP_73(0x3)
    Sleep(300)

    def lambda_315():
        OP_8E(0xFE, 0xC92C, 0x0, 0xFFFFCC98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_315)
    Sleep(500)

    def lambda_335():
        OP_8E(0xFE, 0xC92C, 0x0, 0xFFFFCD9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_335)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4102   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_F8 end

    def Function_3_367(): pass

    label("Function_3_367")


    def lambda_36D():
        OP_8E(0xFE, 0xAFC8, 0x0, 0xFFFFE2F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_36D)
    WaitChrThread(0x103, 0x1)

    def lambda_38D():
        OP_8E(0xFE, 0xAFC8, 0x0, 0xFFFFD3DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_38D)
    WaitChrThread(0x103, 0x1)

    def lambda_3AD():
        OP_8E(0xFE, 0xB70C, 0x0, 0xFFFFCC98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AD)
    WaitChrThread(0x103, 0x1)

    def lambda_3CD():
        OP_8E(0xFE, 0xBEDC, 0x0, 0xFFFFCC98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3CD)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_3_367 end

    def Function_4_3E8(): pass

    label("Function_4_3E8")

    Sleep(700)

    def lambda_3F3():
        OP_8E(0xFE, 0xAFC8, 0x0, 0xFFFFE2F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3F3)
    WaitChrThread(0x151, 0x1)

    def lambda_413():
        OP_8E(0xFE, 0xAFC8, 0x0, 0xFFFFD3DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_413)
    WaitChrThread(0x151, 0x1)

    def lambda_433():
        OP_8E(0xFE, 0xB608, 0x0, 0xFFFFCD9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_433)
    WaitChrThread(0x151, 0x1)

    def lambda_453():
        OP_8E(0xFE, 0xB950, 0x0, 0xFFFFCD9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_453)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_4_3E8 end

    def Function_5_46E(): pass

    label("Function_5_46E")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4C4")
    OP_8C(0x103, 270, 500)
    Sleep(200)

    ChrTalk(    #5
        0x103,
        (
            "#1646F……回头很危险。\x02\x03",

            "#1642F赶快前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_520")

    label("loc_4C4")

    OP_8C(0x103, 270, 500)
    Sleep(200)

    ChrTalk(    #6
        0x103,
        (
            "#1646F入口处的门\x01",
            "差不多该被突破了……\x02\x03",

            "#1642F赶快前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_520")

    OP_90(0xEE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_5_46E end

    def Function_6_537(): pass

    label("Function_6_537")

    Return()

    # Function_6_537 end

    def Function_7_538(): pass

    label("Function_7_538")

    Return()

    # Function_7_538 end

    def Function_8_539(): pass

    label("Function_8_539")

    Return()

    # Function_8_539 end

    def Function_9_53A(): pass

    label("Function_9_53A")

    EventBegin(0x1)

    ChrTalk(    #7
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_568():
        OP_6D(-12420, 0, 1330, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_568)

    def lambda_580():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_580)

    def lambda_598():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_598)

    def lambda_5A8():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_5A8)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    Jump("loc_5D6")

    label("loc_5D6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    Jump("loc_5FE")

    label("loc_5FE")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649")
    OP_C0(0xE, 0x2A, 0xFFFFD1B6, 0x0, 0x1194, 0xB4, 0xFFFFCC48, 0x0, 0xFFFFFE2A)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_658")

    label("loc_649")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_658")
    EventEnd(0x1)

    label("loc_658")

    Return()

    # Function_9_53A end

    SaveToFile()

Try(main)
