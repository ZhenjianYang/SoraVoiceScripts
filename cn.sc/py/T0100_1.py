from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0100_1 ._SN',
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
        "Function_1_59D",          # 01, 1
        "Function_2_60C",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 62320, 250, 19870, 239)
    SetChrPos(0xF7, 64480, 0, 19260, 270)
    SetChrPos(0xF8, 65420, 0, 20030, 270)
    SetChrPos(0xF9, 65940, 0, 18510, 269)
    OP_6D(62620, 250, 19470, 0)
    OP_67(0, 7170, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(300000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1011F这里是……\x01",
            "埃尔格先生的锻冶场吧。\x02\x03",

            "现在也没有生火，\x01",
            "摸起来冰凉凉的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#027F卡片中的\x01",
            "『八眼铁兽』……\x02\x03",

            "……你觉得是这里？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #2
        0x101,
        (
            "#1015F嗯……\x01",
            "虽说不是很有信心。\x02\x03",

            "#1000F那，保险起见还是调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x40)
    OP_8C(0x101, 239, 400)
    OP_8E(0x101, 0xF1C2, 0xFA, 0x4BB4, 0x3E8, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        (
            "\x07\x05调查炉中\x01",
            "发现了卡片和钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x101,
        "#1004F……有、有了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Fade(1000)
    SetChrChipByIndex(0x101, 38)
    OP_0D()

    ChrTalk(    #5
        0x101,
        "#1011F嗯……我看看……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)

    AnonymousTalk(    #6
        (
            "\x07\x05　　　　拿这个钥匙\x01",
            "　   打开『打不开的门』。\x01",
            "　　寻求的东西在地底深处。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(550)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\x35\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x235, 1)
    Sleep(400)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #8
        0x101,
        (
            "#1015F──就这样\x01",
            "钥匙是找到了……\x02\x03",

            "#1019F不过，这是哪里的钥匙啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#022F说是『打不开的门』\x01",
            "应该也是这市内的某处吧。\x02\x03",

            "所有的门都试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A1")

    ChrTalk(    #10
        0x107,
        (
            "#060F嗯……\x01",
            "也只能这样了吧，姐姐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_543")

    label("loc_4A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E6")

    ChrTalk(    #11
        0x106,
        (
            "#053F嗯，也只有这样了……\x02\x03",

            "#050F好，赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_543")

    label("loc_4E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_516")

    ChrTalk(    #12
        0x108,
        "#070F啊啊，也只有这样了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_543")

    label("loc_516")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_543")

    ChrTalk(    #13
        0x104,
        "#035F呼，也只有这样了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_543")


    ChrTalk(    #14
        0x101,
        (
            "#1007F呼，一定就差一步了。\x02\x03",

            "#1006F好，再加把劲吧。\x01",
            "继续找找看了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x77, 0x1, 0x40)
    OP_64(0x3, 0x1)
    ClearChrFlags(0x101, 0x40)
    EventEnd(0x4)
    Return()

    # Function_0_AA end

    def Function_1_59D(): pass

    label("Function_1_59D")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "进入地下水路\x01",      # 0
            "离开\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5F4"),
        (1, "loc_600"),
        (SWITCH_DEFAULT, "loc_600"),
    )


    label("loc_5F4")

    NewScene("ED6_DT21/C0500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_606")

    label("loc_600")

    TalkEnd(0xFF)
    Jump("loc_606")

    label("loc_606")

    Sleep(30)
    Return()

    # Function_1_59D end

    def Function_2_60C(): pass

    label("Function_2_60C")

    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(75350, 0, 18760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 75350, 0, 18760, 270)
    SetChrPos(0x1, 75350, 0, 18760, 270)
    SetChrPos(0x2, 75350, 0, 18760, 270)
    SetChrPos(0x3, 75350, 0, 18760, 270)
    OP_30(0x0)
    SetMapFlags(0x1)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_2_60C end

    SaveToFile()

Try(main)
