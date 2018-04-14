from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5407   ._SN',
        MapName             = 'Other',
        Location            = 'C5407.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '歼灭天使玲',                           # 9
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


    AddCharChip(
        'ED6_DT27/CH03510 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT27/CH03510P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_EA",           # 01, 1
        "Function_2_109",          # 02, 2
        "Function_3_279",          # 03, 3
        "Function_4_2D5",          # 04, 4
        "Function_5_324",          # 05, 5
        "Function_6_467",          # 06, 6
        "Function_7_48D",          # 07, 7
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5")
    Event(0, 2)
    Jump("loc_E9")

    label("loc_E5")

    Event(0, 5)

    label("loc_E9")

    Return()

    # Function_0_D2 end

    def Function_1_EA(): pass

    label("Function_1_EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_108")

    Return()

    # Function_1_EA end

    def Function_2_109(): pass

    label("Function_2_109")

    EventBegin(0x0)
    OP_6D(1570, 0, 1270, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x12F, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x8, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x4)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x5A)
    Sleep(1000)
    SetMessageWindowPos(360, 60, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #0
        (
            "\x07\x05前往『圣堂』及『引擎室』\x01",
            "的通路已经设置了限制。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("声音")

    AnonymousTalk(    #1
        "\x07\x05请接受认证检查。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #2
        0x8,
        (
            "#263F#6PＮｏ．ⅩⅤ──\x01",
            "我是『歼灭天使』玲。\x02\x03",

            "现在要去『圣堂』。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    SetChrName("声音")

    AnonymousTalk(    #3
        "──认证完毕。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    Call(0, 6)
    Sleep(2000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/C5400   ._SN", 125, 0, 0)
    IdleLoop()
    Return()

    # Function_2_109 end

    def Function_3_279(): pass

    label("Function_3_279")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 340, 0, -1480, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A0)
    OP_8E(0xFE, 0x208, 0x0, 0xFFFFFFBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x672, 0x0, 0xFFFFFFBA, 0x7D0, 0x0)
    Return()

    # Function_3_279 end

    def Function_4_2D5(): pass

    label("Function_4_2D5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -200, 0, -1500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FC)
    OP_8E(0xFE, 0xFFFFFF38, 0x0, 0x2C6, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_2D5 end

    def Function_5_324(): pass

    label("Function_5_324")

    EventBegin(0x0)
    OP_6D(990, 0, 1420, 0)
    OP_67(0, 8620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1590, 0, -160, 90)
    SetChrPos(0x1, 830, 0, 1050, 90)
    SetChrPos(0x2, -790, 0, 1400, 90)
    SetChrPos(0x3, -580, 0, -150, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x390, 1)), scpexpr(EXPR_END)), "loc_3C8")
    Call(0, 7)
    NewScene("ED6_DT21/C5400   ._SN", 127, 0, 0)
    IdleLoop()
    Jump("loc_466")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x390, 2)), scpexpr(EXPR_END)), "loc_3DF")
    Call(0, 6)
    NewScene("ED6_DT21/C5402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_466")

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x390, 3)), scpexpr(EXPR_END)), "loc_3F6")
    Call(0, 7)
    NewScene("ED6_DT21/C5400   ._SN", 125, 0, 0)
    IdleLoop()
    Jump("loc_466")

    label("loc_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x390, 4)), scpexpr(EXPR_END)), "loc_40D")
    Call(0, 6)
    NewScene("ED6_DT21/C5400   ._SN", 124, 0, 0)
    IdleLoop()
    Jump("loc_466")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x390, 5)), scpexpr(EXPR_END)), "loc_424")
    Call(0, 7)
    NewScene("ED6_DT21/C5404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_466")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x390, 6)), scpexpr(EXPR_END)), "loc_43B")
    Call(0, 6)
    NewScene("ED6_DT21/C5403   ._SN", 147, 0, 0)
    IdleLoop()
    Jump("loc_466")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x390, 7)), scpexpr(EXPR_END)), "loc_452")
    Call(0, 7)
    NewScene("ED6_DT21/C5411   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_466")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x391, 0)), scpexpr(EXPR_END)), "loc_466")
    Call(0, 6)
    NewScene("ED6_DT21/C5404   ._SN", 153, 0, 0)
    IdleLoop()

    label("loc_466")

    Return()

    # Function_5_324 end

    def Function_6_467(): pass

    label("Function_6_467")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(990, -12000, 1420, 2000)
    Sleep(2000)
    Return()

    # Function_6_467 end

    def Function_7_48D(): pass

    label("Function_7_48D")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(990, 12000, 1420, 2000)
    Sleep(2000)
    Return()

    # Function_7_48D end

    SaveToFile()

Try(main)
