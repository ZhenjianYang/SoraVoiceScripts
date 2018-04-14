from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0122_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0122   ._SN',
            'ED6_DT21/T0122_1 ._SN',
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
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_8C(0xFE, 180, 0)
    Fade(1000)
    SetChrPos(0x101, -40360, 0, -4070, 270)
    SetChrPos(0x103, -39740, 0, -4770, 270)
    SetChrPos(0xF8, -38890, 0, -3380, 270)
    SetChrPos(0xF9, -38350, 0, -4310, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    SetChrPos(0xF9, -38890, 0, -3380, 270)
    SetChrPos(0xF8, -38350, 0, -4310, 270)

    label("loc_12B")

    OP_6D(-39690, 0, -3410, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #0
        0xFE,
        "哼哼哼哼～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "嘿嘿，偶尔好好\x01",
            "买些东西也不坏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000F#1P对不起，我能问个问题吗？\x02\x03",

            "你是定期船的操舵手\x01",
            "库因特先生吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        (
            "咦？\x01",
            "嗯，是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "……有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1002F#1P嗯，有点事想要问你。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05向他说明了正在寻找\x01",
            "褐色猫的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #7
        0xFE,
        (
            "哟，你们在找迷路猫啊？\x01",
            "在雾起得这么厉害的夜晚，真不容易。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "不过很遗憾……\x01",
            "我没看见过那只猫。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x101,
        "#1004F#1P啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        "#023F#4P……你没看见？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "嗯，我向空之女神发誓\x01",
            "我没看见过猫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "我只是从别人\x01",
            "那里听说的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B1")

    ChrTalk(    #13
        0x106,
        "#052F是从谁那里听说的？\x02",
    )

    CloseMessageWindow()
    Jump("loc_449")

    label("loc_3B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E3")

    ChrTalk(    #14
        0x108,
        "#073F哦？是从谁那里听说的？\x02",
    )

    CloseMessageWindow()
    Jump("loc_449")

    label("loc_3E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_415")

    ChrTalk(    #15
        0x104,
        "#033F哦？是从谁那里听说的？\x02",
    )

    CloseMessageWindow()
    Jump("loc_449")

    label("loc_415")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_449")

    ChrTalk(    #16
        0x105,
        (
            "#040F那个……\x01",
            "是从谁那里听说的？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_449")


    ChrTalk(    #17
        0xFE,
        "是一同乘船的索斯摩夫。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "记得他说是在\x01",
            "飞船坪工作时看到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "详细情况你们去问他本人吧。\x01",
            "他应该还在飞船坪工作着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1015F#1P飞船坪的索斯摩夫先生吗。\x02\x03",

            "#1007F哈哈……\x01",
            "结果又绕回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#025F反正就在附近。\x01",
            "与其发牢骚还不如赶快去。\x02\x03",

            "#020F好了，我们回飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_586")

    ChrTalk(    #22
        0x107,
        "#060F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_609")

    label("loc_586")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B4")

    ChrTalk(    #23
        0x105,
        "#040F嗯，那我们就走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_609")

    label("loc_5B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DE")

    ChrTalk(    #24
        0x104,
        "#030F呼，那就走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_609")

    label("loc_5DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_609")

    ChrTalk(    #25
        0x108,
        "#070F好，那我们就走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_609")

    OP_28(0x74, 0x1, 0x40)
    OP_28(0x74, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
