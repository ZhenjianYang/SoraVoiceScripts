from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C2400_1 ._SN',
        MapName             = 'Ruan',
        Location            = 'C2400.x',
        MapIndex            = 97,
        MapDefaultBGM       = "ed60125",
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
        "Function_1_A81",          # 01, 1
        "Function_2_A8A",          # 02, 2
        "Function_3_28B8",         # 03, 3
        "Function_4_4909",         # 04, 4
        "Function_5_49A5",         # 05, 5
        "Function_6_49FF",         # 06, 6
        "Function_7_4A13",         # 07, 7
        "Function_8_4A6F",         # 08, 8
        "Function_9_4ACB",         # 09, 9
        "Function_10_4B27",        # 0A, 10
        "Function_11_4B83",        # 0B, 11
        "Function_12_4BDA",        # 0C, 12
        "Function_13_4BF0",        # 0D, 13
        "Function_14_4C06",        # 0E, 14
        "Function_15_4C81",        # 0F, 15
        "Function_16_4D17",        # 10, 16
        "Function_17_4D2C",        # 11, 17
        "Function_18_4D41",        # 12, 18
        "Function_19_4D56",        # 13, 19
        "Function_20_4D6B",        # 14, 20
        "Function_21_4D80",        # 15, 21
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB")
    Call(1, 21)

    label("loc_BB")

    EventBegin(0x0)
    OP_6D(-170, 0, 490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -10, 0, 5410, 1)
    SetChrPos(0xF7, -10, 0, 5410, 1)
    SetChrPos(0x105, -10, 0, 5410, 1)
    SetChrPos(0x104, -10, 0, 5410, 1)
    SetChrPos(0x127, -10, 0, 5410, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, -320, 0, -8670, 7)
    FadeToDark(0, 0, -1)
    FadeToBright(2000, 0)

    def lambda_183():
        OP_8E(0x101, 0xFFFFFF56, 0x0, 0x1EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_183)
    Sleep(500)

    def lambda_1A3():
        OP_8E(0x105, 0xFFFFFF56, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A3)
    Sleep(500)

    def lambda_1C3():
        OP_8E(0xF7, 0xFFFFFF56, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1C3)

    def lambda_1DE():
        OP_8E(0x105, 0x2F8, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DE)
    Sleep(500)

    def lambda_1FE():
        OP_8E(0x104, 0xFFFFFF56, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FE)

    def lambda_219():
        OP_8E(0xF7, 0xFFFFFC2C, 0x0, 0x618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_219)
    Sleep(500)

    def lambda_239():
        OP_8E(0x127, 0xFFFFFF9C, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x127, 0, lambda_239)

    def lambda_254():
        OP_8E(0x104, 0x172, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_254)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_295():
        OP_6D(0, 0, -3920, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_295)

    def lambda_2AD():
        OP_67(0, 7000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AD)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #0
        0x101,
        "#1020F#4P咦……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_310")

    ChrTalk(    #1
        0x106,
        "#054F#7P切……这么快就来了吗！\x02",
    )

    CloseMessageWindow()
    Jump("loc_336")

    label("loc_310")


    ChrTalk(    #2
        0x103,
        "#523F#7P可恶……这么快就来了吗！\x02",
    )

    CloseMessageWindow()

    label("loc_336")

    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x104, 16)
    SetChrSubChip(0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_372")
    SetChrChipByIndex(0x106, 15)
    SetChrSubChip(0x106, 0)
    Jump("loc_37C")

    label("loc_372")

    SetChrChipByIndex(0x103, 14)
    SetChrSubChip(0x103, 0)

    label("loc_37C")

    OP_62(0x127, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_0D()
    OP_44(0x11, 0xFF)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 30)
    SetChrSubChip(0x11, 0)

    def lambda_3A8():
        OP_99(0xFE, 0x0, 0x1, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3A8)
    Sleep(500)

    def lambda_3BD():
        OP_99(0xFE, 0x1, 0x5, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3BD)

    def lambda_3CD():
        OP_8F(0xFE, 0xA, 0x0, 0xFFFFF7CC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3CD)

    def lambda_3E8():
        OP_6D(100, 0, -930, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E8)

    def lambda_400():
        OP_67(0, 6000, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_400)
    Sleep(500)
    OP_44(0x11, 0xFF)
    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    SetChrPos(0x101, -170, 0, 490, 180)
    SetChrPos(0x105, 760, 0, 700, 180)
    SetChrPos(0xF7, -980, 0, 1560, 180)
    SetChrPos(0x127, -100, 0, 3000, 180)
    SetChrPos(0x104, 370, 0, 1800, 180)
    SetChrFlags(0x11, 0x80)
    ClearMapFlags(0x1)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x127, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x127, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x127, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #3
        0x101,
        (
            "#1007F还、还真厉害呢。\x02\x03",

            "#1002F不过……\x01",
            "这里是地下遗迹？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        (
            "#042F是啊……\x01",
            "看来这是中世纪的地下建筑。\x02\x03",

            "想不到还有这种地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x104,
        (
            "#030F#5P呼，魔兽的气息\x01",
            "弥漫在四周呢。\x02\x03",

            "#035F总之，这地下遗迹\x01",
            "就是卡片上所写的『试炼』吧？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_620")
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    Jump("loc_62A")

    label("loc_620")

    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)

    label("loc_62A")

    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_755")

    ChrTalk(    #6
        0x106,
        (
            "#053F#6P带非战斗人员进去这种地方\x01",
            "毕竟还是很不妥的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_676():

        label("loc_676")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_676")

    QueueWorkItem2(0xF7, 1, lambda_676)
    Sleep(400)

    ChrTalk(    #7
        0x106,
        "#050F#6P喂，摄影师小姐。\x02",
    )

    CloseMessageWindow()

    def lambda_6AA():

        label("loc_6AA")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_6AA")

    QueueWorkItem2(0x101, 1, lambda_6AA)
    Sleep(100)

    def lambda_6C0():

        label("loc_6C0")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_6C0")

    QueueWorkItem2(0x105, 1, lambda_6C0)
    Sleep(100)

    def lambda_6D6():

        label("loc_6D6")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_6D6")

    QueueWorkItem2(0x104, 1, lambda_6D6)
    Sleep(100)
    TurnDirection(0x127, 0xF7, 400)

    ChrTalk(    #8
        0x127,
        "#153F嗯，什么事～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x106,
        (
            "#050F#6P你也听到了，\x01",
            "前面会相当危险。\x02\x03",

            "你就先在前面那个\x01",
            "房间里待命吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_874")

    label("loc_755")


    ChrTalk(    #10
        0x103,
        (
            "#026F#6P带非战斗人员进去这种地方\x01",
            "毕竟还是很危险呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_796():

        label("loc_796")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_796")

    QueueWorkItem2(0xF7, 1, lambda_796)
    Sleep(400)

    ChrTalk(    #11
        0x103,
        "#020F#6P我说，朵洛希小姐。\x02",
    )

    CloseMessageWindow()

    def lambda_7CC():

        label("loc_7CC")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_7CC")

    QueueWorkItem2(0x101, 1, lambda_7CC)
    Sleep(100)

    def lambda_7E2():

        label("loc_7E2")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_7E2")

    QueueWorkItem2(0x105, 1, lambda_7E2)
    Sleep(100)

    def lambda_7F8():

        label("loc_7F8")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_7F8")

    QueueWorkItem2(0x104, 1, lambda_7F8)
    Sleep(100)
    TurnDirection(0x127, 0xF7, 400)

    ChrTalk(    #12
        0x127,
        "#153F嗯，什么事～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        (
            "#020F#6P你也听到了，\x01",
            "前面会相当危险。\x02\x03",

            "你就先在前面那个\x01",
            "房间里待命吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_874")


    ChrTalk(    #14
        0x127,
        (
            "#154F啊～怎么这样啊。\x02\x03",

            "好不容易才有\x01",
            "拍摄幽灵的机会～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1006F好啦，我们发现什么的话\x01",
            "会回来叫你的。\x02\x03",

            "这样就没问题了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x127, 0x101, 400)

    ChrTalk(    #16
        0x127,
        (
            "#154F唔～没办法。\x02\x03",

            "那么大家\x01",
            "要小心啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x127, 0, 400)
    OP_8E(0x127, 0x0, 0x0, 0x1522, 0x7D0, 0x0)
    OP_9F(0x127, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x4, 0x8)
    RemoveParty(0x26, 0xFF)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_8C(0xF7, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9C1")

    ChrTalk(    #17
        0x106,
        (
            "#051F#1P那么……\x01",
            "我们前进吧。\x02\x03",

            "魔兽也相当不好对付。\x01",
            "要慎重地前进。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A09")

    label("loc_9C1")


    ChrTalk(    #18
        0x103,
        (
            "#022F#1P那么……\x01",
            "我们前进吧。\x02\x03",

            "魔兽也相当不好对付。\x01",
            "要慎重地前进。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A09")


    def lambda_A0F():
        TurnDirection(0xFE, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0F)

    def lambda_A1D():
        TurnDirection(0xFE, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A1D)

    def lambda_A2B():
        TurnDirection(0xFE, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2B)
    Sleep(500)

    ChrTalk(    #19
        0x101,
        "#1005F明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x105,
        "#042F明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        "#031F#5P呵呵，交给我吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x122A)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_A81(): pass

    label("Function_1_A81")

    Call(1, 2)
    Call(1, 3)
    Return()

    # Function_1_A81 end

    def Function_2_A8A(): pass

    label("Function_2_A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9B")
    Call(1, 21)

    label("loc_A9B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x1)
    SetChrPos(0x101, -262000, 0, 74000, 360)
    SetChrPos(0x105, -263500, 0, 73700, 360)
    SetChrPos(0xF7, -262000, 0, 72550, 360)
    SetChrPos(0x104, -264000, 0, 72550, 360)
    SetChrPos(0xF, -263000, 150, 90390, 9)
    OP_6D(-262870, 0, 73230, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    OP_20(0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0x101,
        "#1004F啊……！\x02",
    )

    CloseMessageWindow()
    OP_1D(0x6F)

    def lambda_B99():
        OP_6D(-262290, 0, 87050, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B99)

    def lambda_BB1():
        OP_67(0, 6810, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB1)

    def lambda_BC9():
        OP_6B(1810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BC9)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    SetChrPos(0x101, -262000, 0, 75500, 360)
    SetChrPos(0x105, -264000, 0, 75500, 360)
    SetChrPos(0xF7, -262000, 0, 74500, 360)
    SetChrPos(0x104, -264000, 0, 74500, 360)

    def lambda_C27():
        OP_8E(0xFE, 0xFFFBFE9C, 0x0, 0x14A14, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C27)
    Sleep(300)

    def lambda_C47():
        OP_8E(0xFE, 0xFFFBF8C0, 0x0, 0x14820, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C47)
    Sleep(150)

    def lambda_C67():
        OP_8E(0xFE, 0xFFFC0090, 0x0, 0x14438, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C67)
    Sleep(300)

    def lambda_C87():
        OP_8E(0xFE, 0xFFFBF8C0, 0x0, 0x142A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C87)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x104, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D0E")

    ChrTalk(    #23
        0x106,
        (
            "#057F#2P好像有影子，\x01",
            "不过，看上去不像是幽灵……\x02\x03",

            "你这家伙……是什么人！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D55")

    label("loc_D0E")


    ChrTalk(    #24
        0x103,
        (
            "#022F#2P好像有影子，\x01",
            "不过，看上去不像是幽灵……\x02\x03",

            "你到底是什么人？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D55")


    NpcTalk(    #25
        0xF,
        "神秘男子",
        "#5P呵呵呵……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 180, 400)

    NpcTalk(    #26
        0xF,
        "戴面具的男人",
        (
            "#230F欢迎来到我的临时居所。\x02\x03",

            "来接受我的款待吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1020F#2P面、面具……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        (
            "#042F#2P与艾丝蒂尔和波利的\x01",
            "目击情报一模一样呢……\x02\x03",

            "你就是在卢安各地引起骚动的\x01",
            "『影子』的真面目吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #29
        0xF,
        "戴面具的男人",
        (
            "#231F呵呵……\x01",
            "确实如此，科洛蒂娅公主。\x02\x03",

            "很荣幸见到您。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x101,
        (
            "#1005F#2P这、这家伙……\x01",
            "为什么知道科洛丝的真实身份！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #31
        0xF,
        "戴面具的男人",
        (
            "#231F呵呵……\x01",
            "世上没有我偷不到的秘密。\x02\x03",

            "郑重自我介绍一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x4B, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS114._CH")
    OP_C6(0x0, 0x0, 100000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("戴面具的男人")

    AnonymousTalk(    #32
        (
            "#230F执行者ＮＯ．Ⅹ。\x01",
            "『怪盗绅士』布卢布兰──\x02\x03",

            "『噬身之蛇』的一员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    Sleep(500)

    ChrTalk(    #33
        0x101,
        "#1020F#2P噬身之蛇！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_109B")

    ChrTalk(    #34
        0x106,
        "#057F#2P……切……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_10B5")

    label("loc_109B")


    ChrTalk(    #35
        0x103,
        "#523F#2P……唔……！\x02",
    )

    CloseMessageWindow()

    label("loc_10B5")


    def lambda_10BB():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10BB)
    Sleep(50)

    def lambda_10DB():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_10DB)
    Sleep(50)

    def lambda_10FB():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10FB)
    Sleep(50)

    def lambda_111B():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_111B)
    WaitChrThread(0x104, 0x1)
    Sleep(500)

    ChrTalk(    #36
        0xF,
        (
            "#231F呵呵……\x01",
            "不用那么杀气腾腾的。\x02\x03",

            "我只是在这里做一个\x01",
            "小小的实验而已。\x02\x03",

            "完全没有和诸位争斗的意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1002F#2P实、实验……？\x02",
    )

    CloseMessageWindow()

    def lambda_11C6():
        OP_6D(-262290, 0, 88050, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11C6)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    LoadEffect(0x0, "map\\\\mp044_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -263200, 1250, 92150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_83(0x0, 0x2)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x101,
        "#1020F#2P那、那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        (
            "#042F#2P理查德上校使用过的\x01",
            "漆黑色的导力器『福音』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x104,
        (
            "#032F#2P而且……\x01",
            "看来比那个还要大一圈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "#230F呵呵，和他的报告一样，\x01",
            "你们知道有这东西存在啊。\x02\x03",

            "这个『福音』\x01",
            "是为了实验而开发的新型号。\x02\x03",

            "在这次的实验中\x01",
            "起了很大的作用呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_138E")

    ChrTalk(    #42
        0x106,
        (
            "#057F#2P实验……\x01",
            "到底是什么实验？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B5")

    label("loc_138E")


    ChrTalk(    #43
        0x103,
        (
            "#022F#2P实验……\x01",
            "到底是什么实验？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B5")


    ChrTalk(    #44
        0xF,
        (
            "#231F呵呵呵……\x01",
            "百闻不如一见。\x02\x03",

            "请你们亲眼看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 400)
    OP_8F(0xF, 0xFFFBFF64, 0x96, 0x16616, 0x7D0, 0x0)
    OP_8C(0xF, 264, 400)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp088_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -263120, 80, 93290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    ClearChrFlags(0x10, 0x1)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -263000, 500, 89640, 180)
    OP_43(0x10, 0x1, 0x1, 0xC)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x101,
        "#1020F#2P幽、幽灵……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x104,
        (
            "#030F不是幽灵，是使用了导力装置\x01",
            "投射到空间之中的影像。\x02\x03",

            "我从未听说过这种技术已经被实现了，\x01",
            "看来是我孤陋寡闻了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 180, 400)

    ChrTalk(    #47
        0xF,
        (
            "#230F这是用我们的技术\x01",
            "制造出来的空间投影装置。\x02\x03",

            "原本靠单一装置的能力\x01",
            "只能实现把影像投射到眼前的距离……\x02\x03",

            "不过加上了『福音』的力量之后，\x01",
            "像这样的事情也可以办到了。\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp045_00.eff")
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -263200, 850, 92150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_16A9():
        OP_6D(-262290, 0, 85000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16A9)

    def lambda_16C1():
        OP_67(0, 6280, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16C1)
    Sleep(900)
    Fade(500)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, -263000, 500, 80000, 360)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)

    def lambda_1774():
        TurnDirection(0xFE, 0x10, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1774)

    def lambda_1782():
        TurnDirection(0xFE, 0x10, 600)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1782)

    def lambda_1790():
        TurnDirection(0xFE, 0x10, 600)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1790)

    def lambda_179E():
        TurnDirection(0xFE, 0x10, 600)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_179E)
    Sleep(600)

    ChrTalk(    #48
        0x105,
        "#044F#1P呀……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1020F#5P哇哇……\x02",
    )

    CloseMessageWindow()

    def lambda_17E0():

        label("loc_17E0")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_17E0")

    QueueWorkItem2(0x101, 1, lambda_17E0)

    def lambda_17F1():

        label("loc_17F1")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_17F1")

    QueueWorkItem2(0xF7, 1, lambda_17F1)

    def lambda_1802():

        label("loc_1802")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1802")

    QueueWorkItem2(0x105, 1, lambda_1802)

    def lambda_1813():

        label("loc_1813")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1813")

    QueueWorkItem2(0x104, 1, lambda_1813)
    SetChrChipByIndex(0x10, 22)
    SetChrSubChip(0x10, 0)
    OP_43(0x10, 0x1, 0x1, 0xC)
    OP_97(0x10, 0xFFFBFD20, 0x144B0, 0xFFF6D840, 0x1B58, 0x1)
    OP_97(0x10, 0xFFFBFD20, 0x144B0, 0xFFFC7D90, 0x1388, 0x1)
    TurnDirection(0x10, 0xF, 0)
    OP_8F(0x10, 0xFFFBFCA8, 0x96, 0x15E28, 0x7D0, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    SetChrChipByIndex(0x10, 23)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 180, 400)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0x90)
    Sleep(1000)
    Fade(1000)
    SetChrFlags(0x10, 0x80)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    SetChrSubChip(0xF, 0)
    OP_0D()
    Sleep(500)

    def lambda_18D9():
        OP_6D(-262290, 0, 87050, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18D9)

    def lambda_18F1():
        OP_67(0, 6810, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18F1)
    OP_8E(0xF, 0xFFFBFCA8, 0x96, 0x16116, 0x7D0, 0x0)
    OP_8C(0xF, 180, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #50
        0xF,
        (
            "#230F──嗯，就是这样。\x02\x03",

            "呵呵，卢安的各位市民\x01",
            "也一定很尽兴了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_19B1")

    ChrTalk(    #51
        0x106,
        (
            "#057F#2P切……\x02\x03",

            "也就是说这只是一场\x01",
            "单纯的恶作剧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E4")

    label("loc_19B1")


    ChrTalk(    #52
        0x103,
        (
            "#022F#2P无聊……\x02\x03",

            "总之就是\x01",
            "单纯的恶作剧罢了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E4")


    ChrTalk(    #53
        0xF,
        (
            "#231F说成是恶作剧，这种说法太难听了。\x02\x03",

            "这是奉献给沉醉于选举的市民们\x01",
            "一点点休闲和娱乐而已……\x02\x03",

            "希望你们能这么认为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1007F#2P你、你的机关我已经明白了……\x02\x03",

            "#1005F但你为什么\x01",
            "要这么做呢！？\x02\x03",

            "『噬身之蛇』……\x01",
            "到底有什么企图！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "#230F呵呵……\x01",
            "那就不是我应该说的了。\x02\x03",

            "我协助此次计划的\x01",
            "理由只有一个……\x02\x03",

            "就是想能和科洛蒂娅公主──\x01",
            "见上一面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x105,
        "#044F#2P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xF,
        (
            "#231F在逮捕市长时，您所展现出的\x01",
            "高尚美丽……\x02\x03",

            "为了将这样的美丽据为己有，\x01",
            "所以我才会协助这次的计划。\x02\x03",

            "在那之后的几个月──\x01",
            "我都在焦急地等待这个机会哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x105,
        "#043F#2P咦，这个，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1015F#2P……逮捕市长，\x01",
            "指的是戴尔蒙市长的事件吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x101,
        (
            "#1020F#2P为、为什么\x01",
            "你会知道那个时候的事啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xF,
        (
            "#230F呵呵，事件的过程中，\x01",
            "我都在暗地里观察着你们。\x02\x03",

            "比如说……用这样的方法。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1CF3():
        OP_6D(-262290, 0, 88050, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CF3)

    def lambda_1D0B():
        OP_6B(1700, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D0B)
    Sleep(500)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xF, 360, 2000)
    SetChrChipByIndex(0xF, 12)
    SetChrSubChip(0xF, 0)
    OP_8C(0xF, 270, 2000)
    OP_8C(0xF, 180, 2000)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    OP_AD(0x2400C1, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #62
        0x105,
        (
            "#043F#2P莫非你就是那时\x01",
            "戴尔蒙家的……！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇烛台失窃任务没有完成】\x01",      # 0
            "【◇烛台失窃任务完成了】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E73"),
        (1, "loc_1E7B"),
        (SWITCH_DEFAULT, "loc_1E83"),
    )


    label("loc_1E73")

    OP_28(0x57, 0x3, 0x10)
    Jump("loc_1E83")

    label("loc_1E7B")

    OP_28(0x57, 0x4, 0x10)
    Jump("loc_1E83")

    label("loc_1E83")

    FadeToBright(300, 0)

    label("loc_1E8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x57, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F72")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x101,
        (
            "#1005F#2P难道说……！\x02\x03",

            "那个时候从市长官邸\x01",
            "偷了烛台的『怪盗B』也是你！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        "#044F#2P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xF,
        (
            "#5P呵呵……\x01",
            "终于注意到了？\x02\x03",

            "我以为你们只要看了放在旧校舍的那些卡片\x01",
            "早就应该注意到了才对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F72")


    def lambda_1F78():
        OP_6D(-262290, 0, 87050, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F78)

    def lambda_1F90():
        OP_6B(1810, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F90)
    Sleep(500)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xF, 360, 2000)
    SetChrChipByIndex(0xF, 11)
    SetChrSubChip(0xF, 0)
    OP_8C(0xF, 270, 2000)
    OP_8C(0xF, 180, 2000)
    SetChrSubChip(0xF, 0)
    Sleep(500)

    ChrTalk(    #66
        0xF,
        (
            "#230F怪盗就是美的崇拜者。\x01",
            "注定会被高尚的东西所吸引。\x02\x03",

            "公主，您用您的高尚之美\x01",
            "偷走了我的心啊。\x02\x03",

            "竟然把怪盗的心盗走……\x02\x03",

            "#233F啊，这是多么甜美的屈辱！\x02\x03",

            "您打算要如何赎回\x01",
            "这样的罪孽呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x105,
        (
            "#043F#2P那、那个……\x01",
            "你这么说我也很为难。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x104, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2125")

    ChrTalk(    #68
        0x106,
        (
            "#552F#2P这种自我陶醉的语气……\x01",
            "和你这家伙简直没有什么两样！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_2125")


    ChrTalk(    #69
        0x103,
        (
            "#027F#2P这种陶醉的语气……\x01",
            "似乎和某个人简直一模一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2160")

    TurnDirection(0x104, 0xF7, 400)

    ChrTalk(    #70
        0x104,
        (
            "#6P#034F真失礼啊……\x01",
            "不要把我和他混为一谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1002F#2P『噬身之蛇』。\x01",
            "好像和我想象的有所不同……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #72
        0x101,
        (
            "#1005F#2P不过，你居然对科洛丝有所企图，\x01",
            "那就更不能不闻不问了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        "#542F#1P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_22D7")
    OP_8C(0x106, 360, 400)
    TurnDirection(0x104, 0xF, 400)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 15)
    SetChrSubChip(0x106, 0)
    OP_0D()

    ChrTalk(    #74
        0x106,
        (
            "#054F#2P按照协会规定，\x01",
            "我以非法入侵等嫌疑拘捕你。\x02\x03",

            "包括『福音』等等的详情\x01",
            "都要请你如实招来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235A")

    label("loc_22D7")

    OP_8C(0x103, 360, 400)
    TurnDirection(0x104, 0xF, 400)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 14)
    SetChrSubChip(0x103, 0)
    OP_0D()

    ChrTalk(    #75
        0x103,
        (
            "#024F#2P按照协会规定\x01",
            "我以非法侵入等嫌疑拘捕你。\x02\x03",

            "包括『福音』等等的详情\x01",
            "都要请你如实招来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235A")


    ChrTalk(    #76
        0xF,
        (
            "#231F受不了你们……\x01",
            "真是一些不解风情的人啊。\x02\x03",

            "要我来教训你们也无妨，\x01",
            "不过既然选了这个地方……\x02\x03",

            "就让『他』来对付你们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_23F9")

    ChrTalk(    #77
        0x106,
        "#052F#2P什么……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_23F9")


    ChrTalk(    #78
        0x103,
        "#023F#2P你说什么……？\x02",
    )

    CloseMessageWindow()

    label("loc_2415")

    Fade(250)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 32)
    SetChrSubChip(0xF, 0)
    OP_0D()
    Sleep(500)

    def lambda_2435():
        OP_6D(-262290, 0, 88050, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2435)

    def lambda_244D():
        OP_6B(1700, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_244D)
    WaitChrThread(0x101, 0x0)
    OP_99(0xF, 0x0, 0x2, 0x3E8)
    OP_22(0xBC, 0x0, 0x64)
    OP_20(0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-256350, 0, 81990, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(90000, 0)
    OP_6E(326, 0)
    OP_0D()
    OP_22(0x85, 0x0, 0x64)

    def lambda_24C2():

        label("loc_24C2")

        OP_7C(0x0, 0x64, 0x12C, 0x64)
        OP_48()
        Jump("loc_24C2")

    QueueWorkItem2(0xF, 3, lambda_24C2)
    OP_0D()
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -235000, 0, 82000, 270)
    OP_A1(0x12, 0x13)
    SetChrFlags(0x12, 0x1)
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    OP_7E(0xFE0C, 0xF830, 0x0, 0x50, 0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2561():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2561)

    def lambda_256F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_256F)

    def lambda_257D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_257D)

    def lambda_258B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_258B)
    Sleep(500)

    ChrTalk(    #79
        0x101,
        "#1020F#5P什、什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x104,
        (
            "#032F#2P唔……\x01",
            "我有一种不好～的预感。\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x14, 0)
    OP_70(0x14, 0xF0)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x14)
    OP_72(0x14, 0x8)
    OP_72(0x14, 0x20)
    OP_44(0xF, 0x3)
    OP_23(0x85)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    Sleep(1000)
    OP_1D(0x29)
    Sleep(1000)
    OP_43(0x12, 0x0, 0x1, 0x5)
    Sleep(3000)
    OP_43(0x12, 0x3, 0x1, 0x4)
    Sleep(1200)
    OP_44(0x12, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    OP_B0(0x13, 0x8)
    OP_22(0xEC, 0x0, 0x64)
    OP_6F(0x13, 21)
    OP_70(0x13, 0x28)
    Sleep(1500)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_73(0x13)
    Sleep(1000)
    OP_71(0x13, 0x20)
    OP_B0(0x13, 0x8)
    OP_6F(0x13, 1)
    OP_70(0x13, 0x10)
    Fade(500)
    OP_6D(-261589, 0, 84500, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(1860, 0)
    OP_6C(56000, 0)
    OP_6E(513, 0)
    OP_0D()

    ChrTalk(    #81
        0x101,
        "#1020F#5P那、那是什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x105,
        "#042F#6P盔甲人马兵！？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 11)
    SetChrSubChip(0xF, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #83
        0xF,
        (
            "#231F#5P呵呵，看来『他』好像是\x01",
            "这个遗迹的守护者。\x02\x03",

            "本来已经处于在半坏状况了……\x01",
            "不过，已经被我好心地修复好了。\x02\x03",

            "反正机会难得，\x01",
            "就让『他』来试一下你们的身手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1005F#5P开、开什么玩笑！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2822")

    ChrTalk(    #85
        0x106,
        "#054F#4P……来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_283A")

    label("loc_2822")


    ChrTalk(    #86
        0x103,
        "#024F#4P……来了！\x02",
    )

    CloseMessageWindow()

    label("loc_283A")

    Sleep(500)
    Fade(500)
    OP_44(0x12, 0x0)
    OP_72(0x13, 0x20)
    OP_0D()

    def lambda_2854():
        OP_6D(-258000, 0, 85500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2854)

    def lambda_286C():
        OP_6B(1960, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_286C)
    OP_6F(0x13, 81)
    OP_70(0x13, 0x61)
    OP_22(0xEC, 0x0, 0x64)
    OP_73(0x13)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x101, 0xFF)
    Battle(0x44C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_28B2"),
        (SWITCH_DEFAULT, "loc_28B7"),
    )


    label("loc_28B2")

    OP_B4(0x0)
    Jump("loc_28B7")

    label("loc_28B7")

    Return()

    # Function_2_A8A end

    def Function_3_28B8(): pass

    label("Function_3_28B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    ClearMapFlags(0x1)
    OP_6F(0x13, 160)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x12, -256500, 0, 81800, 236)
    OP_A1(0x12, 0x13)
    OP_6F(0x14, 240)
    SetChrPos(0x101, -263320, 0, 84630, 90)
    SetChrPos(0x105, -264530, 0, 82930, 90)
    SetChrPos(0xF7, -261260, 0, 83690, 90)
    SetChrPos(0x104, -262340, 0, 82220, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -262320, 150, 91670, 180)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x1)
    SetChrFlags(0xF, 0x40)
    OP_6D(-259000, 0, 84070, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(1810, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #87
        0x101,
        "#1025F#5P赢、赢了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A86")

    ChrTalk(    #88
        0x106,
        (
            "#053F#5P呼……\x01",
            "真不好对付。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29F5():
        OP_6D(-261290, 0, 88550, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29F5)

    def lambda_2A0D():
        OP_67(0, 6500, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A0D)
    TurnDirection(0x106, 0xF, 400)
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x105, 0xF, 400)
    TurnDirection(0xF7, 0xF, 400)
    TurnDirection(0x104, 0xF, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #89
        0x106,
        (
            "#054F#2P接下来就轮到你这家伙了……\x01",
            "做好准备了吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B4B")

    label("loc_2A86")


    ChrTalk(    #90
        0x103,
        (
            "#026F#5P呼……\x01",
            "真不好对付。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AAD():
        OP_6D(-261290, 0, 88550, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AAD)

    def lambda_2AC5():
        OP_67(0, 6500, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AC5)
    TurnDirection(0x103, 0xF, 400)
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x105, 0xF, 400)
    TurnDirection(0xF7, 0xF, 400)
    TurnDirection(0x104, 0xF, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #91
        0x103,
        (
            "#022F#2P那么……\x02\x03",

            "既然都到这个地步了，\x01",
            "看来，应该是有所觉悟了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B4B")


    ChrTalk(    #92
        0xF,
        (
            "#230F#5P受不了你们……\x01",
            "战斗的方式一点也没有优雅的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF, 24)
    SetChrSubChip(0xF, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #93
        0xF,
        (
            "#231F#5P没办法了……\x01",
            "我来示范给你们看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_99(0xF, 0x0, 0x5, 0x9C4)

    ChrTalk(    #94
        0xF,
        "#234F#5PＦｌａｍｍｅ！（火焰啊）！\x02",
    )

    CloseMessageWindow()

    def lambda_2C0D():
        OP_6D(-257000, 0, 86750, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C0D)

    def lambda_2C25():
        OP_67(0, 3910, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C25)

    def lambda_2C3D():
        OP_6B(2410, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C3D)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_22(0x86, 0x0, 0x64)
    Sleep(200)
    LoadEffect(0x1, "map\\\\mpfire5.eff")
    PlayEffect(0x1, 0x1, 0xFF, -256000, 2900, 86750, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, -256000, 2900, 77000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_C4(0x0, 0x2)
    OP_7E(0xFD44, 0xFEE8, 0xFEC0, 0x96, 0x7D0)
    OP_8C(0x101, 71, 400)
    OP_8C(0x105, 71, 400)
    OP_8C(0xF7, 71, 400)
    OP_8C(0x104, 71, 400)

    ChrTalk(    #95
        0x101,
        "#1004F#5P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x105,
        "#044F#5P篝火的火苗……！？\x02",
    )

    CloseMessageWindow()

    def lambda_2D4C():
        OP_6D(-261290, 0, 88550, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D4C)

    def lambda_2D64():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D64)

    def lambda_2D7C():
        OP_6B(1810, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D7C)
    SetChrSubChip(0xF, 0)
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x105, 0xF, 400)
    TurnDirection(0xF7, 0xF, 400)
    TurnDirection(0x104, 0xF, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #97
        0xF,
        "#234F#5PＡｉｇｕｉｌｌｅ！（针啊）！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 26)
    SetChrSubChip(0xF, 6)
    OP_0D()
    OP_7D(0x0, 0xF, 0x32, 0x1F4)

    def lambda_2DFE():
        OP_6D(-262290, 0, 87550, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DFE)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2E1B():
        OP_96(0xFE, 0xFFFBF046, 0x0, 0x15A72, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_2E1B)
    OP_43(0x15, 0x0, 0x1, 0x7)
    Sleep(100)
    OP_43(0x16, 0x0, 0x1, 0x8)
    Sleep(100)
    OP_43(0x17, 0x0, 0x1, 0x9)
    Sleep(100)
    OP_43(0x18, 0x0, 0x1, 0xA)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0xF, 0x1)
    OP_7D(0x1, 0xF, 0x0, 0x0)

    def lambda_2E76():

        label("loc_2E76")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_2E76")

    QueueWorkItem2(0x101, 1, lambda_2E76)

    def lambda_2E93():

        label("loc_2E93")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_2E93")

    QueueWorkItem2(0xF7, 1, lambda_2E93)

    def lambda_2EB0():

        label("loc_2EB0")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_2EB0")

    QueueWorkItem2(0x105, 1, lambda_2EB0)

    def lambda_2ECD():

        label("loc_2ECD")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_2ECD")

    QueueWorkItem2(0x104, 1, lambda_2ECD)

    ChrTalk(    #98
        0x101,
        "#1020F#2P啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        "#043F#2P呀……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x104,
        "#033F#2P啊……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F5C")

    ChrTalk(    #101
        0x106,
        (
            "#055F#2P这是……\x01",
            "『影缝』吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F81")

    label("loc_2F5C")


    ChrTalk(    #102
        0x103,
        (
            "#523F#2P莫非……\x01",
            "是『影缝』！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F81")

    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    SetChrSubChip(0xF, 7)
    Sleep(75)
    SetChrSubChip(0xF, 0)
    Sleep(75)
    SetChrChipByIndex(0xF, 26)
    SetChrSubChip(0xF, 0)
    Sleep(500)

    ChrTalk(    #103
        0xF,
        (
            "#231F#5P呵呵，动不了了吧。\x02\x03",

            "你们对戴尔蒙市长的\x01",
            "『宝杖』好像很吃惊吧……\x02\x03",

            "这种程度的技巧对我们执行者来说\x01",
            "根本不需要依靠什么古代遗物来实现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1020F#2P怎、怎么会……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3094")

    ChrTalk(    #105
        0x106,
        (
            "#057F#2P可恶……\x01",
            "太小看他了吗……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B4")

    label("loc_3094")


    ChrTalk(    #106
        0x103,
        "#522F#2P可恶，太大意了……\x02",
    )

    CloseMessageWindow()

    label("loc_30B4")

    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    OP_22(0x197, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_30E5():
        OP_6D(-262370, 0, 81630, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30E5)

    def lambda_30FD():
        OP_67(0, 7590, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_30FD)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    SetChrPos(0x13, -263400, 4000, 69400, 0)
    OP_43(0x13, 0x1, 0x1, 0xD)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_313C():
        OP_6D(-262000, 0, 87800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_313C)

    def lambda_3154():
        OP_67(0, 7590, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3154)

    def lambda_316C():
        OP_8E(0xFE, 0xFFFBF56E, 0x12C, 0x158E2, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_316C)
    Sleep(500)
    Sleep(300)
    OP_8C(0xF, 270, 0)
    SetChrSubChip(0xF, 6)
    OP_7D(0x0, 0xF, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_31AA():
        OP_96(0xF, 0xFFFBFE92, 0x0, 0x15C0C, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_31AA)
    Sleep(200)
    OP_43(0x19, 0x0, 0x1, 0xB)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0xF, 0x1)
    OP_7D(0x1, 0xF, 0x0, 0x0)
    WaitChrThread(0x13, 0x2)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0x13, 0)
    OP_44(0x13, 0x1)

    def lambda_31F9():

        label("loc_31F9")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_31F9")

    QueueWorkItem2(0x13, 1, lambda_31F9)
    WaitChrThread(0x19, 0x1)

    ChrTalk(    #107
        0x13,
        "#310F#4P啾！？\x02",
    )

    CloseMessageWindow()
    OP_44(0x13, 0x1)

    ChrTalk(    #108
        0x105,
        "#043F#2P基库！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 7)
    Sleep(75)
    SetChrSubChip(0xF, 0)
    Sleep(75)
    SetChrChipByIndex(0xF, 26)
    SetChrSubChip(0xF, 0)

    ChrTalk(    #109
        0xF,
        (
            "#231F#2P你出现了啊，小小的骑士。\x02\x03",

            "我要对你的骑士精神表示敬意，\x01",
            "不过请你先不要动。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0xF, 11)
    SetChrSubChip(0xF, 0)
    OP_0D()
    OP_8C(0xF, 225, 400)

    def lambda_32D5():
        OP_8E(0xFE, 0xFFFBF4D8, 0x0, 0x14B90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_32D5)
    Sleep(300)

    def lambda_32F5():
        OP_6D(-262900, 0, 84380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_32F5)

    def lambda_330D():
        OP_67(0, 6280, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_330D)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF, 0x1)
    OP_8C(0xF, 180, 400)

    ChrTalk(    #110
        0xF,
        (
            "#230F#1P科洛蒂娅公主。\x01",
            "现在，您就是我的俘虏了。\x02\x03",

            "呵呵，您的心情如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x105,
        (
            "#047F#6P……请不要小看我。\x02\x03",

            "#042F即便你能拘禁我的身躯，\x01",
            "但也无法囚禁我的心……\x02\x03",

            "只要我还活着，就一定不会屈服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xF,
        (
            "#231F#1P对，就是这眼神！\x02\x03",

            "高尚、纯洁，\x01",
            "绝不向任何人屈服的眼神！\x02\x03",

            "我要的就是这种充满希望的光芒！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1005F#5P别、别在那里\x01",
            "胡说八道了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3487():

        label("loc_3487")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_3487")

    QueueWorkItem2(0x101, 1, lambda_3487)
    TurnDirection(0x101, 0xF, 100)
    OP_44(0x101, 0x1)

    ChrTalk(    #114
        0x101,
        (
            "#1005F#5P你这个戴着面具的古怪家伙！\x01",
            "不许靠近科洛丝！\x02",
        )
    )


    def lambda_34E8():

        label("loc_34E8")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_34E8")

    QueueWorkItem2(0xF7, 1, lambda_34E8)
    TurnDirection(0xF7, 0xF, 100)
    OP_44(0xF7, 0x1)

    def lambda_3510():

        label("loc_3510")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_3510")

    QueueWorkItem2(0x104, 1, lambda_3510)
    OP_8C(0x104, 323, 100)
    OP_44(0x104, 0x1)
    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #115
        0xF,
        (
            "#230F#3P真受不了你，\x01",
            "竟然无法体会这面具的美……\x02\x03",

            "看来你还不了解\x01",
            "什么才是真正的美。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x104,
        "#035F#2P呵呵……\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xF, 135, 400)

    ChrTalk(    #117
        0xF,
        "#232F#1P嗯……？\x02",
    )

    CloseMessageWindow()

    def lambda_35E7():
        OP_6D(-262000, 0, 83690, 1500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_35E7)

    def lambda_35FF():
        OP_67(0, 6280, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_35FF)

    def lambda_3617():
        OP_6C(92000, 1500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3617)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)

    ChrTalk(    #118
        0x104,
        (
            "#031F#2P哈哈，看来我失礼了。\x02\x03",

            "#030F不，只是因为我发现你\x01",
            "犯了一个太过低级的错误。\x02\x03",

            "所以才不知不觉地流露出\x01",
            "没有恶意的微笑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xF,
        (
            "#232F#5P哦？……有意思。\x02\x03",

            "你是说我\x01",
            "想错问题了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x104,
        (
            "#030F#2P的确，我从不吝惜去赞美\x01",
            "公主殿下的美丽。\x02\x03",

            "但这不是能够用你那小家子气的美学\x01",
            "来加以衡量的。\x02\x03",

            "#035F回家温三年书再来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xF,
        (
            "#235F#5P啊，多么大言不惭！\x02\x03",

            "区区一个旅行演奏家，\x01",
            "有什么资格来贬低我的美学！？\x02\x03",

            "要是你回答不出来的话，看我怎么收拾你！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x104,
        (
            "#035F#2P呵呵，那么我来问你──\x02\x03",

            "#030F何谓美？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xF,
        (
            "#231F#5P我还以为是什么呢，愚蠢的问题……\x02\x03",

            "美是高尚！\x01",
            "是一种高高在上的光芒！\x02\x03",

            "除此以外\x01",
            "还有什么样的答案？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x104,
        "#035F#2P呵呵，可笑……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #125
        0x104,
        "#530F#2P#3S真正的美──那是爱！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #126
        0xF,
        "#233F#5P……什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x104,
        (
            "#035F#2P因为爱，人们才能感受美！\x02\x03",

            "无爱之美不过是镜花水月！\x02\x03",

            "#030F无论你是高贵还是卑微的人，\x01",
            "只要有了爱，就都是美丽的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xF,
        (
            "#235F#5P哼，跟我耍小聪明……\x02\x03",

            "#234F但是在我看来，\x01",
            "爱才是虚无的幻想！\x02\x03",

            "即便是不通过人的感悟，\x01",
            "美本身仍然可以成立！\x02\x03",

            "比如，就像高山顶上盛开的鲜花，\x01",
            "即便不为人所见，它也是美丽的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x104,
        "#032F#2P唔……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0xF7)
    OP_63(0x105)

    ChrTalk(    #130
        0x101,
        "#1019F#5P……那个。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3ADF")

    ChrTalk(    #131
        0x106,
        "#551F#2P多么搞笑的对话啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B03")

    label("loc_3ADF")


    ChrTalk(    #132
        0x103,
        "#025F#2P唉，一下子紧张感就……\x02",
    )

    CloseMessageWindow()

    label("loc_3B03")


    ChrTalk(    #133
        0x105,
        "#045F#4P真、真伤脑筋啊……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #134
        0xF,
        (
            "#230F#5P……想不到会在这种地方\x01",
            "遇到同样在寻求美的劲敌。\x02\x03",

            "演奏家──你的名字叫什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x104,
        (
            "#031F#2P奥利维尔·朗海姆。\x02\x03",

            "为爱彷徨的\x01",
            "漂泊诗人兼猎人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xF,
        (
            "#231F#5P呵呵……\x01",
            "我会记住你的名字的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -263660, 0, 73660, 339)
    OP_4A(0xE, 255)
    LoadEffect(0x0, "map\\\\mp032_00.eff")

    NpcTalk(    #137
        0xE,
        "女孩的声音",
        (
            "#1P啊～！\x01",
            "小艾，总算找到你们了～！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xF, 0xE, 400)

    def lambda_3CD9():
        OP_8E(0xFE, 0xFFFBF4BA, 0x0, 0x139C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3CD9)

    def lambda_3CF4():
        OP_6C(44000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_3CF4)

    def lambda_3D04():
        OP_6D(-263200, 0, 82600, 2000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3D04)

    def lambda_3D1C():
        OP_67(0, 6280, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_3D1C)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0xE, 0x3)

    ChrTalk(    #138
        0xE,
        (
            "#150F嘿嘿，实在是等不及了，\x01",
            "所以我就过来看看了⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1020F#5P朵、朵洛希！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x105,
        (
            "#042F#5P不好！\x01",
            "快跑！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xE,
        "#154F咦……？\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #142
        0xE,
        (
            "#153F啊！\x01",
            "带着面具的白色人影！\x02\x03",

            "你就是幽灵吧～！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xF,
        "#233F#5P不、不……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xE, 25)
    SetChrSubChip(0xE, 0)
    OP_0D()

    ChrTalk(    #144
        0xE,
        "#151F好，笑一个㈱\x02",
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xE, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    FadeToDark(100, 16777215, -1)
    OP_0D()
    OP_C4(0x1, 0x2)
    OP_7E(0xFD44, 0xFBB4, 0x64, 0x96, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x13, 0x1)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    FadeToBright(200, 16777215)

    ChrTalk(    #145
        0xF,
        "#235F#5P啊？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 10)
    SetChrSubChip(0xE, 0)
    SetChrFlags(0x13, 0x40)
    OP_43(0x13, 0x1, 0x1, 0xD)
    OP_22(0x8C, 0x0, 0x64)

    ChrTalk(    #146
        0x13,
        "#311F#3P啾⊙\x02",
    )

    CloseMessageWindow()
    OP_43(0x13, 0x1, 0x1, 0xF)
    OP_8C(0x101, 315, 400)
    Sleep(300)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #147
        0x101,
        "#1004F#5P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x105,
        "#542F#6P麻痹解除了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0xE, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3F9E")

    ChrTalk(    #149
        0x106,
        (
            "#051F#5P原来如此……\x01",
            "影子因为闪光灯消失了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FCF")

    label("loc_3F9E")


    ChrTalk(    #150
        0x103,
        (
            "#021F#5P原来如此……\x01",
            "影子因为闪光灯消失了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3FDE")
    SetChrChipByIndex(0x106, 15)
    Jump("loc_3FE3")

    label("loc_3FDE")

    SetChrChipByIndex(0x103, 14)

    label("loc_3FE3")

    SetChrChipByIndex(0x104, 16)
    OP_0D()
    WaitChrThread(0x101, 0x2)
    TurnDirection(0x104, 0xE, 400)

    ChrTalk(    #151
        0x104,
        "#031F#2P哟，真是个不得了的女孩啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x104, 400)

    ChrTalk(    #152
        0xE,
        (
            "#151F#6P嗯，交给我你就放心吧～\x02\x03",

            "虽然我也不知道\x01",
            "自己到底是哪里厉害～\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #153
        0xF,
        (
            "#231F哼哼哼……\x02\x03",

            "哈哈哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_409F():
        OP_6D(-262490, 0, 88500, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_409F)

    def lambda_40B7():
        OP_67(0, 6810, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_40B7)
    OP_7D(0x0, 0xF, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xF, 0xFFFBFCA8, 0x96, 0x16120, 0x1F4, 0x1388)
    OP_7D(0x1, 0xF, 0x0, 0x0)

    def lambda_40FB():
        TurnDirection(0x101, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40FB)

    def lambda_4109():
        TurnDirection(0xF7, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4109)

    def lambda_4117():
        TurnDirection(0x104, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4117)

    def lambda_4125():
        TurnDirection(0xE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4125)

    def lambda_4133():
        TurnDirection(0x105, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4133)
    WaitChrThread(0x101, 0x2)
    OP_8C(0xF, 225, 400)

    def lambda_414D():
        OP_8F(0xF, 0xFFFBFEC4, 0x96, 0x16648, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_414D)
    WaitChrThread(0xF, 0x1)
    OP_8C(0xF, 270, 400)
    OP_22(0x82, 0x0, 0x64)
    OP_71(0x15, 0x4)
    Sleep(500)

    ChrTalk(    #154
        0x101,
        "#1005F#2P啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x105,
        "#043F#2P他把『福音』！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x105, 0x20)
    OP_8C(0xF, 180, 400)

    ChrTalk(    #156
        0xF,
        (
            "#231F#6P好久没有过得\x01",
            "这么开心了。\x02\x03",

            "让我向你们致敬，诸位。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_422C")

    ChrTalk(    #157
        0x106,
        (
            "#057F#2P你这家伙……\x01",
            "还打算做什么吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4253")

    label("loc_422C")


    ChrTalk(    #158
        0x103,
        (
            "#022F#2P你……\x01",
            "还打算做什么吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4253")


    ChrTalk(    #159
        0xF,
        (
            "#230F#6P呵呵……\x01",
            "今晚就到此为止吧。\x02\x03",

            "不过对于诸位，\x01",
            "我似乎有必要重新认识一下。\x02\x03",

            "不愧为是有资格和\x01",
            "『漆黑之牙』并肩作战的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #160
        0x101,
        "#1020F#2P『漆黑之牙』……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x105,
        (
            "#043F#2P莫非……\x01",
            "是指约修亚！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xF,
        (
            "#231F#6P呵呵，我和他是旧交。\x02\x03",

            "我之所以会开始观察你们，\x01",
            "就是因为看到他的身影。\x02\x03",

            "他好像已经恢复了所有的记忆……\x01",
            "也不知他现在身在何处，在做些什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 24)
    SetChrSubChip(0xF, 0)
    OP_0D()
    OP_99(0xF, 0x0, 0x5, 0x9C4)
    LoadEffect(0x0, "map\\\\mp046_00.eff")
    PlayEffect(0x0, 0x0, 0xF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #163
        0x101,
        "#1020F#2P啊……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_447B")

    ChrTalk(    #164
        0x106,
        "#055F#2P什、什么……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4495")

    label("loc_447B")


    ChrTalk(    #165
        0x103,
        "#023F#2P莫非……！？\x02",
    )

    CloseMessageWindow()

    label("loc_4495")


    def lambda_449B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_449B)
    Sleep(1500)
    OP_82(0x0, 0x2)
    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("布卢布兰的声音")

    AnonymousTalk(    #166
        (
            "\x07\x05──再见了，诸位。\x02\x03",

            "计划才刚刚开始……\x01",
            "尽量不要大意了。\x02\x03",

            "我还打算以我自己的方式\x01",
            "向你们发出挑战呢。\x02\x03",

            "呵呵，敬请期待吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xF, 0x80)
    OP_20(0xBB8)
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x104, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0x13, 0)
    OP_43(0x13, 0x1, 0x1, 0xD)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_45F5():
        OP_8F(0x13, 0xFFFBF988, 0x708, 0x14370, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_45F5)
    OP_0D()
    Sleep(500)
    OP_43(0x101, 0x1, 0x1, 0x10)
    Sleep(200)
    OP_43(0x13, 0x2, 0x1, 0xE)

    def lambda_4629():
        OP_6D(-262500, 150, 91000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4629)

    def lambda_4641():
        OP_67(0, 6280, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4641)
    OP_43(0xF7, 0x1, 0x1, 0x11)
    OP_43(0x105, 0x1, 0x1, 0x12)
    Sleep(200)
    OP_43(0x104, 0x1, 0x1, 0x13)
    Sleep(100)
    OP_43(0xE, 0x1, 0x1, 0x14)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0xE, 0x3)

    ChrTalk(    #167
        0x101,
        "#1020F#5P消、消失了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        "#043F#6P难、难以置信……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xE,
        (
            "#153F哇～！\x01",
            "好像变魔术一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x104,
        (
            "#031F#6P哈哈哈。\x01",
            "挺厉害的嘛。\x02\x03",

            "看来，我也只好承认\x01",
            "他是我的劲敌了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #171
        0x101,
        (
            "#1005F#5P现在的问题不是这个！\x02\x03",

            "撇开他那古怪的样子不说……\x01",
            "那家伙可不是一般地强！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_47ED")

    ChrTalk(    #172
        0x106,
        "#053F#2P是啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 270, 400)
    OP_8C(0x105, 201, 400)

    ChrTalk(    #173
        0x106,
        (
            "#057F#2P『噬身之蛇』──\x01",
            "比想象的更加难以对付。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4846")

    label("loc_47ED")


    ChrTalk(    #174
        0x103,
        "#026F#2P是啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 270, 400)
    OP_8C(0x105, 201, 400)

    ChrTalk(    #175
        0x103,
        (
            "#022F#2P『噬身之蛇』──\x01",
            "比想象的更加难以对付。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4846")

    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #176
        (
            "\x07\x05就这样……\x01",
            "造成卢安各地骚动的幽灵事件落幕了。\x02\x03",

            "隔天早晨，回到城里的艾丝蒂尔一行人\x01",
            "和朵洛希暂时告别后，\x01",
            "前往协会报告这次事件的经过。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2120   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_3_28B8 end

    def Function_4_4909(): pass

    label("Function_4_4909")


    def lambda_490F():
        OP_96(0xFE, 0xFFFBEE98, 0x0, 0x13EC0, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_490F)
    Sleep(100)

    def lambda_4932():
        OP_96(0xFE, 0xFFFBF15E, 0x0, 0x14636, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4932)
    Sleep(100)

    def lambda_4955():
        OP_96(0xFE, 0xFFFBF69A, 0x0, 0x13E2A, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4955)
    Sleep(100)

    def lambda_4978():
        OP_96(0xFE, 0xFFFBF744, 0x0, 0x14410, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4978)
    SetChrChipByIndex(0x105, 17)
    SetChrChipByIndex(0x104, 16)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x104, 0)
    Return()

    # Function_4_4909 end

    def Function_5_49A5(): pass

    label("Function_5_49A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49FE")
    OP_24(0xEC, 0x32)
    OP_B0(0x13, 0xD)
    OP_6F(0x13, 251)
    OP_70(0x13, 0x10A)

    def lambda_49CA():
        OP_91(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_49CA)
    Sleep(500)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(200)
    OP_22(0xEC, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    OP_73(0x13)
    Jump("Function_5_49A5")

    label("loc_49FE")

    Return()

    # Function_5_49A5 end

    def Function_6_49FF(): pass

    label("Function_6_49FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A12")
    OP_6F(0x14, 240)
    Jump("Function_6_49FF")

    label("loc_4A12")

    Return()

    # Function_6_49FF end

    def Function_7_4A13(): pass

    label("Function_7_4A13")

    SetChrPos(0x15, -264690, 500, 90200, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_4A3E():
        OP_8F(0x15, 0xFFFBF47E, 0xFFFFFDA8, 0x14802, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4A3E)
    WaitChrThread(0x15, 0x1)
    SetChrPos(0x15, -265090, 0, 83870, 270)
    SetChrSubChip(0xFE, 2)
    Return()

    # Function_7_4A13 end

    def Function_8_4A6F(): pass

    label("Function_8_4A6F")

    SetChrPos(0x16, -264690, 500, 90200, 270)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_4A9A():
        OP_8F(0x16, 0xFFFBF096, 0xFFFFFDA8, 0x14262, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4A9A)
    WaitChrThread(0x16, 0x1)
    SetChrPos(0x16, -266090, 0, 82430, 270)
    SetChrSubChip(0xFE, 2)
    Return()

    # Function_8_4A6F end

    def Function_9_4ACB(): pass

    label("Function_9_4ACB")

    SetChrPos(0x17, -264690, 500, 90200, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_4AF6():
        OP_8F(0x17, 0xFFFBFE9C, 0xFFFFFDA8, 0x145C8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4AF6)
    WaitChrThread(0x17, 0x1)
    SetChrPos(0x17, -262500, 0, 83300, 270)
    SetChrSubChip(0xFE, 2)
    Return()

    # Function_9_4ACB end

    def Function_10_4B27(): pass

    label("Function_10_4B27")

    SetChrPos(0x18, -264690, 500, 90200, 270)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_4B52():
        OP_8F(0x18, 0xFFFBF8C0, 0xFFFFFDA8, 0x13F88, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B52)
    WaitChrThread(0x18, 0x1)
    SetChrPos(0x18, -264000, 0, 81700, 270)
    SetChrSubChip(0xFE, 2)
    Return()

    # Function_10_4B27 end

    def Function_11_4B83(): pass

    label("Function_11_4B83")

    SetChrPos(0x19, -263960, 500, 87940, 0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x4)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_4BA9():
        OP_8F(0x19, 0xFFFBEBDC, 0xFFFFFDA8, 0x153D8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4BA9)
    WaitChrThread(0x19, 0x1)
    SetChrPos(0x19, -267400, 0, 86950, 0)
    SetChrSubChip(0xFE, 1)
    Return()

    # Function_11_4B83 end

    def Function_12_4BDA(): pass

    label("Function_12_4BDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BEF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_12_4BDA")

    label("loc_4BEF")

    Return()

    # Function_12_4BDA end

    def Function_13_4BF0(): pass

    label("Function_13_4BF0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C05")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_13_4BF0")

    label("loc_4C05")

    Return()

    # Function_13_4BF0 end

    def Function_14_4C06(): pass

    label("Function_14_4C06")

    OP_8C(0x13, 332, 400)
    OP_97(0x13, 0xFFFBF6CC, 0x1575C, 0xFFFE0430, 0x1770, 0x1)
    OP_8F(0x13, 0xFFFC01BC, 0x708, 0x16C74, 0x7D0, 0x0)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0x13, 0)
    OP_8C(0x13, 270, 400)
    OP_8F(0x13, 0xFFFC01BC, 0x6C2, 0x16C74, 0x3E8, 0x0)
    OP_44(0x13, 0x1)
    Sleep(250)
    SetChrPos(0x13, -261700, 1780, 93300, 270)
    SetChrChipByIndex(0x13, 29)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Return()

    # Function_14_4C06 end

    def Function_15_4C81(): pass

    label("Function_15_4C81")

    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 0)
    OP_8F(0x13, 0xFFFBFCA8, 0x44C, 0x16120, 0xBB8, 0x0)
    OP_8C(0x13, 263, 400)

    def lambda_4CAC():
        OP_97(0x13, 0xFFFBF5E6, 0x151E4, 0xFFFC2F70, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_4CAC)
    WaitChrThread(0x13, 0x3)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 20)
    OP_8C(0x13, 0, 400)
    OP_8C(0x105, 90, 400)
    SetChrChipByIndex(0x105, 21)
    SetChrSubChip(0x105, 2)
    OP_8F(0x13, 0xFFFBF9EC, 0x64, 0x14438, 0x7D0, 0x0)
    Fade(500)
    OP_44(0x13, 0x1)
    SetChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x105, 21)
    SetChrSubChip(0x105, 0)
    OP_0D()
    Return()

    # Function_15_4C81 end

    def Function_16_4D17(): pass

    label("Function_16_4D17")

    OP_8E(0xFE, 0xFFFBFC62, 0x0, 0x15ED2, 0x7D0, 0x0)
    Return()

    # Function_16_4D17 end

    def Function_17_4D2C(): pass

    label("Function_17_4D2C")

    OP_8E(0xFE, 0xFFFBFEF6, 0x0, 0x15B9E, 0x7D0, 0x0)
    Return()

    # Function_17_4D2C end

    def Function_18_4D41(): pass

    label("Function_18_4D41")

    OP_8E(0xFE, 0xFFFBF62C, 0x0, 0x15D56, 0x7D0, 0x0)
    Return()

    # Function_18_4D41 end

    def Function_19_4D56(): pass

    label("Function_19_4D56")

    OP_8E(0xFE, 0xFFFBF79E, 0x0, 0x1570C, 0x7D0, 0x0)
    Return()

    # Function_19_4D56 end

    def Function_20_4D6B(): pass

    label("Function_20_4D6B")

    OP_8E(0xFE, 0xFFFBFBB8, 0x0, 0x153CE, 0x7D0, 0x0)
    Return()

    # Function_20_4D6B end

    def Function_21_4D80(): pass

    label("Function_21_4D80")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DFA"),
        (1, "loc_4E00"),
        (SWITCH_DEFAULT, "loc_4E06"),
    )


    label("loc_4DFA")

    OP_A2(0x1200)
    Jump("loc_4E06")

    label("loc_4E00")

    OP_A2(0x1201)
    Jump("loc_4E06")

    label("loc_4E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4E14")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4E18")

    label("loc_4E14")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4E18")

    Return()

    # Function_21_4D80 end

    SaveToFile()

Try(main)
