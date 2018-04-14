from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0707   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0707.x',
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
        '@FileName',                            # 8
        '怪盗布卢布兰',                         # 9
        '福音',                                 # 10
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
        'ED6_DT27/CH03530 ._CH',             # 00
        'ED6_DT27/CH04530 ._CH',             # 01
        'ED6_DT27/CH04000 ._CH',             # 02
        'ED6_DT27/CH04001 ._CH',             # 03
        'ED6_DT27/CH04010 ._CH',             # 04
        'ED6_DT27/CH04011 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT27/CH03530P._CP',             # 00
        'ED6_DT27/CH04530P._CP',             # 01
        'ED6_DT27/CH04000P._CP',             # 02
        'ED6_DT27/CH04001P._CP',             # 03
        'ED6_DT27/CH04010P._CP',             # 04
        'ED6_DT27/CH04011P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458758,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_13F",          # 01, 1
        "Function_2_140",          # 02, 2
        "Function_3_FC3",          # 03, 3
        "Function_4_FD8",          # 04, 4
        "Function_5_FED",          # 05, 5
        "Function_6_1035",         # 06, 6
        "Function_7_10BC",         # 07, 7
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_13E")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_13E")

    Return()

    # Function_0_122 end

    def Function_1_13F(): pass

    label("Function_1_13F")

    Return()

    # Function_1_13F end

    def Function_2_140(): pass

    label("Function_2_140")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157")
    Call(0, 6)
    Call(0, 7)

    label("loc_157")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_178"),
        (5, "loc_18F"),
        (4, "loc_1A6"),
        (6, "loc_1BD"),
        (7, "loc_1D4"),
        (8, "loc_1EB"),
        (SWITCH_DEFAULT, "loc_202"),
    )


    label("loc_178")

    OP_D2(0x701D0, 0x701DC, 0x7)
    OP_D2(0x701D1, 0x701DD, 0x8)
    Jump("loc_202")

    label("loc_18F")

    OP_D2(0x70218, 0x70224, 0x7)
    OP_D2(0x70219, 0x70225, 0x8)
    Jump("loc_202")

    label("loc_1A6")

    OP_D2(0x70200, 0x7020C, 0x7)
    OP_D2(0x70201, 0x7020D, 0x8)
    Jump("loc_202")

    label("loc_1BD")

    OP_D2(0x70230, 0x7023C, 0x7)
    OP_D2(0x70231, 0x7023D, 0x8)
    Jump("loc_202")

    label("loc_1D4")

    OP_D2(0x70248, 0x70254, 0x7)
    OP_D2(0x70249, 0x70255, 0x8)
    Jump("loc_202")

    label("loc_1EB")

    OP_D2(0x270080, 0x270084, 0x7)
    OP_D2(0x270081, 0x270085, 0x8)
    Jump("loc_202")

    label("loc_202")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_223"),
        (5, "loc_23A"),
        (4, "loc_251"),
        (6, "loc_268"),
        (7, "loc_27F"),
        (8, "loc_296"),
        (SWITCH_DEFAULT, "loc_2AD"),
    )


    label("loc_223")

    OP_D2(0x701D0, 0x701DC, 0x9)
    OP_D2(0x701D1, 0x701DD, 0xA)
    Jump("loc_2AD")

    label("loc_23A")

    OP_D2(0x70218, 0x70224, 0x9)
    OP_D2(0x70219, 0x70225, 0xA)
    Jump("loc_2AD")

    label("loc_251")

    OP_D2(0x70200, 0x7020C, 0x9)
    OP_D2(0x70201, 0x7020D, 0xA)
    Jump("loc_2AD")

    label("loc_268")

    OP_D2(0x70230, 0x7023C, 0x9)
    OP_D2(0x70231, 0x7023D, 0xA)
    Jump("loc_2AD")

    label("loc_27F")

    OP_D2(0x70248, 0x70254, 0x9)
    OP_D2(0x70249, 0x70255, 0xA)
    Jump("loc_2AD")

    label("loc_296")

    OP_D2(0x270080, 0x270084, 0x9)
    OP_D2(0x270081, 0x270085, 0xA)
    Jump("loc_2AD")

    label("loc_2AD")

    OP_D2(0x27026E, 0x270278, 0xB)
    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, 700, 950, 12150, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 4)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 7)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 9)
    SetChrPos(0x101, -700, 0, 4650, 90)
    SetChrPos(0x102, 700, 0, 4520, 90)
    SetChrPos(0xF8, -800, 0, 2930, 90)
    SetChrPos(0xF9, 800, 0, 2800, 90)
    LoadEffect(0x0, "map\\\\mp046_00.eff")
    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    OP_72(0x6, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    FadeToBright(1000, 0)

    def lambda_3E1():
        OP_6D(1840, 0, 7670, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E1)

    def lambda_3F9():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F9)

    def lambda_411():
        OP_6B(4800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_411)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1025F#6P啊……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_470")

    ChrTalk(    #1
        0x109,
        "#1062F#6P恢复原状了吗……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_539")

    label("loc_470")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A5")

    ChrTalk(    #2
        0x105,
        "#542F#6P恢、恢复原状了……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_539")

    label("loc_4A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D8")

    ChrTalk(    #3
        0x103,
        "#027F#6P恢复原状了吗……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_539")

    label("loc_4D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_509")

    ChrTalk(    #4
        0x108,
        "#070F#6P恢复原状了吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_539")

    label("loc_509")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_539")

    ChrTalk(    #5
        0x106,
        "#051F#6P恢复原状了吗……！？\x02",
    )

    CloseMessageWindow()

    label("loc_539")


    ChrTalk(    #6
        0x8,
        (
            "#230F#6P唔，看来任务\x01",
            "到此结束了啊。\x02\x03",

            "……没办法了。\x01",
            "撤退吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    def lambda_588():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_588)
    Sleep(50)

    def lambda_59B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_59B)
    Sleep(50)

    def lambda_5AE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5AE)
    Sleep(50)

    ChrTalk(    #7
        0x101,
        "#1004F#6P什么……\x02",
    )

    CloseMessageWindow()

    def lambda_5D8():
        OP_6D(1500, 0, 9790, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5D8)

    def lambda_5F0():
        OP_67(0, 5000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F0)

    def lambda_608():
        OP_6B(4220, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_608)
    OP_8C(0x8, 180, 400)
    Sleep(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 11)
    OP_99(0x8, 0x0, 0x5, 0x7D0)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D4")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_712")

    label("loc_6D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FB")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_712")

    label("loc_6FB")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_712")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_77C")

    label("loc_73E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_765")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_77C")

    label("loc_765")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_77C")

    Sleep(1000)

    ChrTalk(    #8
        0x101,
        "#1005F#6P慢、慢着！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C7")

    ChrTalk(    #9
        0x105,
        "#043F#4P等、等一下！\x02",
    )

    CloseMessageWindow()
    Jump("loc_878")

    label("loc_7C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FB")

    ChrTalk(    #10
        0x106,
        (
            "#054F#4P你小子……\x01",
            "想逃吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_878")

    label("loc_7FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_829")

    ChrTalk(    #11
        0x109,
        "#1069F#4P喂，想逃吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_878")

    label("loc_829")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_852")

    ChrTalk(    #12
        0x103,
        "#024F#4P想逃吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_878")

    label("loc_852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_878")

    ChrTalk(    #13
        0x108,
        "#076F#4P想逃吗！？\x02",
    )

    CloseMessageWindow()

    label("loc_878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_913")

    ChrTalk(    #14
        0x8,
        (
            "#231F#5P哈哈，殿下自不必说\x01",
            "诸位游击士作战的模样\x01",
            "真让我感动啊。\x02\x03",

            "至于这是否真实，\x01",
            "就留待下次见面时再确认吧。\x02\x03",

            "#230F那么诸位，失陪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A2")

    label("loc_913")


    ChrTalk(    #15
        0x8,
        (
            "#231F#5P哈哈，『漆黑之牙』自不必说，\x01",
            "诸位游击士也相当有本事嘛。\x02\x03",

            "至于那个光辉是否真实，\x01",
            "等下次有机会我再确认吧。\x02\x03",

            "#230F那么诸位，失陪了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A2")

    OP_99(0x8, 0x5, 0xE, 0x7D0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    SetChrFlags(0x8, 0x80)
    OP_82(0x0, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x5)
    Sleep(3500)

    ChrTalk(    #16
        0x101,
        "#1019F#6P逃、逃掉了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#1042F#4P……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()

    def lambda_A31():
        OP_8E(0xFE, 0xDC, 0x3B6, 0x2F58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A31)

    def lambda_A4C():
        OP_6D(0, 950, 13850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A4C)

    def lambda_A64():
        OP_67(0, 6500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A64)

    def lambda_A7C():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A7C)

    def lambda_A8C():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A8C)

    def lambda_A9C():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A9C)
    Sleep(200)

    def lambda_AB1():
        OP_8E(0xFE, 0xFFFFFBA0, 0x3B6, 0x2EF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB1)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x4)
    Sleep(200)
    OP_43(0xF8, 0x1, 0x0, 0x3)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #18
        0x102,
        (
            "#1043F#4P这就是『β』……\x01",
            "结社制作的『福音』的最终形态吗。\x02\x03",

            "比至今为止的新型号\x01",
            "好像还大一圈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1002F#6P塔顶上\x01",
            "恢复了原状是不错，不过……\x02\x03",

            "问题是他们到底想\x01",
            "使用这个来做什么。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF3")

    ChrTalk(    #20
        0x108,
        (
            "#072F#4P之前启动的装置\x01",
            "好像也再度停了。\x02\x03",

            "#572F……糟糕透了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D60")

    label("loc_BF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C48")

    ChrTalk(    #21
        0x106,
        (
            "#552F#4P之前启动的装置\x01",
            "好像也再度停止了。\x02\x03",

            "#053F……真是糟糕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D60")

    label("loc_C48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA7")

    ChrTalk(    #22
        0x109,
        (
            "#1063F#4P之前启动的装置\x01",
            "好像也再度停止了。\x02\x03",

            "#1068F总觉得有不好～的预感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D60")

    label("loc_CA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(    #23
        0x103,
        (
            "#022F#4P之前启动的装置\x01",
            "也再度停止了。\x02\x03",

            "#522F……总觉得有一种不祥的预感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D60")

    label("loc_D06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D60")

    ChrTalk(    #24
        0x107,
        (
            "#561F#4P之前启动的装置\x01",
            "好像也再度停了……\x02\x03",

            "#063F总觉得有不好的预感……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB0")

    ChrTalk(    #25
        0x105,
        (
            "#043F#4P而且，刚才\x01",
            "笼罩着塔顶的结界……\x02\x03",

            "那到底是什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED")

    label("loc_DB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E00")

    ChrTalk(    #26
        0x107,
        (
            "#065F#4P而、而且……\x02\x03",

            "刚才笼罩着塔顶的\x01",
            "结界到底是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED")

    label("loc_E00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E4D")

    ChrTalk(    #27
        0x103,
        (
            "#522F而且，刚才\x01",
            "笼罩着塔顶的结界……\x02\x03",

            "那到底是什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED")

    label("loc_E4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9B")

    ChrTalk(    #28
        0x109,
        (
            "#1067F而且，刚才\x01",
            "笼罩着塔顶的结界……\x02\x03",

            "那到底是什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED")

    label("loc_E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EED")

    ChrTalk(    #29
        0x106,
        (
            "#555F而且，刚才笼罩着\x01",
            "塔顶的结界也让人很在意。\x02\x03",

            "那到底是什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EED")


    ChrTalk(    #30
        0x102,
        "#1043F#4P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #31
        0x102,
        (
            "#1040F#2P总之这样一来，\x01",
            "这座塔应该就恢复原状了。\x02\x03",

            "暂且先返回『埃尔赛尤』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #32
        0x101,
        (
            "#1025F#6P嗯……\x01",
            "得回去向博士报告才行。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_140 end

    def Function_3_FC3(): pass

    label("Function_3_FC3")

    OP_8E(0xFE, 0xFFFFFBB4, 0xFA, 0x2B48, 0xBB8, 0x0)
    Return()

    # Function_3_FC3 end

    def Function_4_FD8(): pass

    label("Function_4_FD8")

    OP_8E(0xFE, 0x17C, 0x1F4, 0x2B8E, 0xBB8, 0x0)
    Return()

    # Function_4_FD8 end

    def Function_5_FED(): pass

    label("Function_5_FED")

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
    Return()

    # Function_5_FED end

    def Function_6_1035(): pass

    label("Function_6_1035")

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
        (0, "loc_10AF"),
        (1, "loc_10B5"),
        (SWITCH_DEFAULT, "loc_10BB"),
    )


    label("loc_10AF")

    OP_A2(0x1200)
    Jump("loc_10BB")

    label("loc_10B5")

    OP_A2(0x1201)
    Jump("loc_10BB")

    label("loc_10BB")

    Return()

    # Function_6_1035 end

    def Function_7_10BC(): pass

    label("Function_7_10BC")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_7_10BC end

    SaveToFile()

Try(main)
