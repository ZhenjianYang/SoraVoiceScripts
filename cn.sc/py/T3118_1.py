from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3118_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3118_1 ._SN',
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
        "Function_1_30A",          # 01, 1
        "Function_2_30F",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x382), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_148")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_148")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    LoadEffect(0x0, "map\\\\mp108_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xF4240), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D")
    EventBegin(0x1)
    OP_4A(0x9, 1)
    TurnDirection(0x0, 0x9, 400)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    Call(1, 2)
    EventEnd(0x1)
    Jump("loc_303")

    label("loc_22D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4C4B40), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_27D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05这附近有反应！\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_303")

    label("loc_27D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x989680), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2C9")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05附近有反应\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_303")

    label("loc_2C9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "\x07\x05没有反应\x02",
    )

    OP_22(0xAB, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_303")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_30A(): pass

    label("Function_1_30A")

    Call(1, 2)
    Return()

    # Function_1_30A end

    def Function_2_30F(): pass

    label("Function_2_30F")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    Fade(1000)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, -5510, 0, -3140, 45)
    SetChrPos(0x101, -4640, 0, -2300, 225)
    SetChrPos(0xF7, -5400, 0, -1160, 180)
    SetChrPos(0xF8, -4170, 0, -1020, 225)
    SetChrPos(0xF9, -3520, 0, -2690, 270)
    OP_6D(-5020, 0, -2650, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x33\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x400)
    OP_64(0x0, 0x1)

    ChrTalk(    #4
        0x101,
        (
            "#1007F#5P真、真是的。\x02\x03",

            "没想到安东尼\x01",
            "居然拿着零件。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_45D")

    ChrTalk(    #5
        0x106,
        "#051F#1P差点就放过了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47B")

    label("loc_45D")


    ChrTalk(    #6
        0x103,
        "#020F#1P差点就放过了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_47B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F4")

    ChrTalk(    #7
        0x107,
        (
            "#560F#1P这么说来，埃里克先生\x01",
            "他说过和它一起玩过呢。\x02\x03",

            "它一定是那时候发现了零件\x01",
            "然后拿到这里来了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C5")

    label("loc_4F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55A")

    ChrTalk(    #8
        0x104,
        (
            "#030F这么说来，委托人也\x01",
            "说和它一起玩过吧。\x02\x03",

            "是那时候发现了零件\x01",
            "拿到这里来的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C5")

    label("loc_55A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C5")

    ChrTalk(    #9
        0x105,
        (
            "#040F这么说来，埃里克先生也\x01",
            "说和它一起玩过吧。\x02\x03",

            "是那时候发现了零件\x01",
            "然后拿到这里来了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C5")


    ChrTalk(    #10
        0x101,
        (
            "#1015F我想是吧……\x02\x03",

            "#1016F不过，没想到\x01",
            "会拿过来呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #11
        0xA,
        "喵呜？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65A")

    ChrTalk(    #12
        0x108,
        (
            "#071F哈哈，抱歉抱歉。\x02\x03",

            "把你的玩具拿走\x01",
            "你也很为难吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3")

    label("loc_65A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A3")

    ChrTalk(    #13
        0x105,
        (
            "#041F呵呵，对不起哦。\x02\x03",

            "难得有了件玩具\x01",
            "也被拿走了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3")

    label("loc_6A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F3")

    ChrTalk(    #14
        0x104,
        (
            "#031F呼，对不起啊小猫咪。\x02\x03",

            "虽然是你的玩具\x01",
            "就暂且借用一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F3")


    ChrTalk(    #15
        0x101,
        (
            "#1006F嗯，这个补偿\x01",
            "就让埃里克先生来做吧。\x02\x03",

            "那再见哦，安东尼。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #16
        0xA,
        "喵～呜。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Return()

    # Function_2_30F end

    SaveToFile()

Try(main)
