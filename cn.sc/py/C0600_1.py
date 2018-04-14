from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0600_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C0600_1 ._SN',
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
        "Function_1_CBA",          # 01, 1
        "Function_2_E9B",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0xF7, -1300, 0, -6990, 0)
    SetChrPos(0xF8, -500, 0, -7670, 0)
    SetChrPos(0xF9, 950, 0, -6790, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F")
    SetChrPos(0xF9, -500, 0, -7670, 0)
    SetChrPos(0xF8, 750, 0, -6790, 0)

    label("loc_11F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E")
    SetChrPos(0xF9, -500, 0, -7670, 0)
    SetChrPos(0xF8, 750, 0, -6790, 0)

    label("loc_14E")

    OP_6D(1300, 0, -3480, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        (
            "#1011F#1P嗯……\x01",
            "还以为有什么……\x02\x03",

            "#1015F放眼望去都是垃圾嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E2():
        OP_90(0xFE, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E2)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22A")

    ChrTalk(    #1 op#A
        0x108,
        "#076F#8A艾丝蒂尔，等等！\x02",
    )

    Jump("loc_2A5")

    label("loc_22A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_258")

    ChrTalk(    #2 op#A
        0x106,
        "#054F#8A艾丝蒂尔，等等！\x02",
    )

    Jump("loc_2A5")

    label("loc_258")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_288")

    ChrTalk(    #3 op#A
        0x104,
        "#530F#8A艾丝蒂尔，等一下！\x02",
    )

    Jump("loc_2A5")

    label("loc_288")


    ChrTalk(    #4 op#A
        0x103,
        "#024F#8A艾丝蒂尔，等等！\x02",
    )


    label("loc_2A5")

    Sleep(500)
    OP_44(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)

    def lambda_2D0():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFE890, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D0)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 0, 0, 2200, 180)
    SetChrPos(0x9, 2200, 0, 2200, 180)
    SetChrPos(0xA, -2200, 0, 2200, 180)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_20(0x7D0)
    OP_22(0x26D, 0x0, 0x64)
    OP_82(0x80, 0x2)
    OP_79(0x0, 0x2)
    OP_7B()
    OP_77(0xE0, 0xE0, 0xE0, 0x0, 0x320)
    Sleep(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Sleep(1000)
    OP_22(0x26D, 0x0, 0x64)
    OP_82(0x80, 0x2)
    OP_79(0x0, 0x2)
    OP_7B()
    OP_77(0xC0, 0xC0, 0xC0, 0x0, 0x7D0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xA, 0x800)
    OP_22(0x28C, 0x0, 0x64)
    OP_43(0x8, 0x2, 0x1, 0x2)

    def lambda_402():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_402)
    Sleep(200)
    OP_43(0x9, 0x2, 0x1, 0x2)

    def lambda_420():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_420)
    Sleep(100)
    OP_43(0xA, 0x2, 0x1, 0x2)

    def lambda_43E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_43E)
    Sleep(2000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46C")
    SetChrChipByIndex(0x104, 4)

    label("loc_46C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47F")
    SetChrChipByIndex(0x105, 5)

    label("loc_47F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_492")
    SetChrChipByIndex(0x106, 6)

    label("loc_492")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A5")
    SetChrChipByIndex(0x107, 7)

    label("loc_4A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B8")
    SetChrChipByIndex(0x108, 8)

    label("loc_4B8")

    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    SetChrChipByIndex(0x101, 2)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0xA, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51A")
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #5
        0x107,
        "#065F啊……\x02",
    )

    CloseMessageWindow()

    label("loc_51A")


    ChrTalk(    #6
        0x101,
        "#1005F#1P这、这些家伙是什么啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#024F待会儿再问吧！\x02\x03",

            "必须先击退才行！\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_57B():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF060, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_57B)

    def lambda_599():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF060, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_599)

    def lambda_5B7():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF060, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5B7)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 0)
    SetChrChipByIndex(0xA, 0)
    Sleep(200)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0xCE4, 0x0, 0x0, 0x0, 0xFF)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_611"),
        (SWITCH_DEFAULT, "loc_614"),
    )


    label("loc_611")

    OP_B4(0x0)
    Return()

    label("loc_614")

    FadeToDark(0, 0, -1)
    OP_82(0x80, 0x0)
    EventBegin(0x0)
    OP_6D(1300, 0, -2480, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 0, -3000, 0)
    SetChrPos(0xF7, -1500, 0, -4190, 270)
    SetChrPos(0xF8, -500, 0, -5670, 180)
    SetChrPos(0xF9, 1150, 0, -4090, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D3")
    SetChrPos(0xF9, -500, 0, -5670, 180)
    SetChrPos(0xF8, 750, 0, -4790, 90)

    label("loc_6D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_702")
    SetChrPos(0xF9, -500, 0, -5670, 180)
    SetChrPos(0xF8, 750, 0, -4790, 90)

    label("loc_702")

    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x103, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71F")
    SetChrChipByIndex(0x104, 4)

    label("loc_71F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_732")
    SetChrChipByIndex(0x105, 5)

    label("loc_732")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_745")
    SetChrChipByIndex(0x106, 6)

    label("loc_745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_758")
    SetChrChipByIndex(0x107, 7)

    label("loc_758")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76B")
    SetChrChipByIndex(0x108, 8)

    label("loc_76B")

    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_79(0x0, 0x2)
    OP_7B()
    OP_77(0xC0, 0xC0, 0xC0, 0x0, 0x0)
    OP_6D(240, 0, -3900, 0)
    SetChrPos(0xB, 0, 0, -3900, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #8
        0x101,
        "#1002F呼…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FE")

    ChrTalk(    #9
        0x108,
        "#070F看来收拾了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_877")

    label("loc_7FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_826")

    ChrTalk(    #10
        0x106,
        "#050F看来解决了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_877")

    label("loc_826")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_850")

    ChrTalk(    #11
        0x104,
        "#030F看来收拾了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_877")

    label("loc_850")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_877")

    ChrTalk(    #12
        0x105,
        "#042F看来击退了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_877")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A3")

    ChrTalk(    #13
        0x107,
        "#561F……吓、吓死了～\x02",
    )

    CloseMessageWindow()
    Jump("loc_912")

    label("loc_8A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C9")

    ChrTalk(    #14
        0x105,
        "#042F……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_912")

    label("loc_8C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EF")

    ChrTalk(    #15
        0x104,
        "#031F……是吧⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_912")

    label("loc_8EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_912")

    ChrTalk(    #16
        0x106,
        "#051F……是吧。\x02",
    )

    CloseMessageWindow()

    label("loc_912")

    OP_22(0x86, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    Sleep(400)
    OP_82(0x80, 0x2)
    OP_79(0x0, 0x2)
    OP_7B()
    Sleep(800)
    OP_22(0x86, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)

    def lambda_9BB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9BB)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(200)
    SetChrChipByIndex(0x103, 65535)

    def lambda_9D8():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_9D8)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F8")
    SetChrChipByIndex(0x104, 65535)

    label("loc_9F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0B")
    SetChrChipByIndex(0x105, 65535)

    label("loc_A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1E")
    SetChrChipByIndex(0x106, 65535)

    label("loc_A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A31")
    SetChrChipByIndex(0x107, 65535)

    label("loc_A31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A44")
    SetChrChipByIndex(0x108, 65535)

    label("loc_A44")


    def lambda_A4A():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_A4A)

    def lambda_A58():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_A58)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x103, 0x3)
    WaitChrThread(0xF8, 0x3)
    WaitChrThread(0xF9, 0x3)

    ChrTalk(    #17
        0x101,
        (
            "#1007F呼～害我紧张了一下。\x02\x03",

            "那种东西突然\x01",
            "涌出来嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        (
            "#027F这一带\x01",
            "没见过的魔兽……\x02\x03",

            "……这算是怪盗绅士流\x01",
            "打招呼的方式吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4E")

    ChrTalk(    #19
        0x104,
        (
            "#030F唔，大概是吧……\x02\x03",

            "不过，看来这个\x01",
            "好像是最后的障碍了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C43")

    label("loc_B4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(    #20
        0x106,
        (
            "#050F啊啊，大概吧……\x02\x03",

            "不过，看来这个\x01",
            "好像是最后的障碍呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C43")

    label("loc_B9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF0")

    ChrTalk(    #21
        0x108,
        (
            "#070F啊啊，恐怕是……\x02\x03",

            "不过，看来这个\x01",
            "好像是最后的障碍哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C43")

    label("loc_BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C43")

    ChrTalk(    #22
        0x105,
        (
            "#047F嗯嗯，恐怕是……\x02\x03",

            "#040F不过，看来这个\x01",
            "好像是最后的障碍了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C43")


    ChrTalk(    #23
        0x103,
        (
            "#020F嗯嗯，接下来\x01",
            "只剩取回委任书了。\x02\x03",

            "找找看吧。\x01",
            "应该在这个房间里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F啊，\x01",
            "这可不能忘了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x77, 0x1, 0x4000)
    OP_65(0x2, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_CBA(): pass

    label("Function_1_CBA")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #25
        "\x07\x00得到了\x07\x02#16I矿山的委任书\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #26
        0x101,
        "#1018F好，回收完毕了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6D")

    ChrTalk(    #27
        0x107,
        (
            "#060F赶快还回去吧。\x02\x03",

            "叔叔……\x01",
            "一定等得很着急吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E55")

    label("loc_D6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBF")

    ChrTalk(    #28
        0x105,
        (
            "#040F那么，现在立刻\x01",
            "回去还给他吧。\x02\x03",

            "矿山长一定\x01",
            "也非常担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E55")

    label("loc_DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0D")

    ChrTalk(    #29
        0x104,
        (
            "#031F唔，那么赶快\x01",
            "送还回去吧。\x02\x03",

            "老大一定\x01",
            "十分的担心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E55")

    label("loc_E0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E55")

    ChrTalk(    #30
        0x106,
        (
            "#051F哦，那就早点还回去吧。\x02\x03",

            "大叔一定\x01",
            "也在担心了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E55")


    ChrTalk(    #31
        0x103,
        "#021F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #32
        0x101,
        "#1006F嗯！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0111   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_1_CBA end

    def Function_2_E9B(): pass

    label("Function_2_E9B")

    OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_2_E9B end

    SaveToFile()

Try(main)
